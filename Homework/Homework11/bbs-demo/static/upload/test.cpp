#include <float.h>
#include "hip/hip_runtime.h"

#define INF FLT_MAX

// Block单个方向上的线程数
#define THREAD_NUM 32
// 每个Block开启1024个线程
#define THREAD_NUM_TOTAL (THREAD_NUM * THREAD_NUM)

// shared memory
#define POS1(x, y) (x * THREAD_NUM + y)
// global memory
#define POS2(x, y) (x * num_node + y)

/**
* num_node 节点数量
* n 主分块的编号，从0开始计数
*/
__global__ void phase1(float *dis, uint16_t *path, int num_node, int n) {
	__shared__ float main_block[THREAD_NUM_TOTAL];  // size = 4KB
	
	// 常量可能会得到进一步的缓存优化
	const int smj = threadIdx.x;  // shared memory j
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	const int gmj = n * THREAD_NUM + smj; // global memory j
	const int gmi = n * THREAD_NUM + smi;
	const int gIdx = POS2(gmi, gmj);
	
	// 将全局内存中的第n个主分块复制到共享内存
	uint16_t tmp_path;
	if (gmi < num_node && gmj < num_node) {
		main_block[sIdx] = dis[gIdx];
		tmp_path = path[gIdx];
	} else {
		// 填充无关数据，避免进一步的判断
		main_block[sIdx] = INF;
	}
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	float tmp;  // 用私有内存访问替换共享内存访问
	const int base = smi * num_node;
	const uint16_t path_base = n * THREAD_NUM  + 1;
	for (int k = 0; k < THREAD_NUM; k++) {
		tmp = main_block[base + k] + main_block[POS1(k, smj)];
		
		// 第k行和第k列在本轮更新中值不会改变
		if (main_block[sIdx] > tmp) {
			main_block[sIdx] = tmp;
			tmp_path = path_base + k;
		}
		
		// 每个线程都完成本轮更新才能进行下一轮
		__syncthreads();
	}
	
	// 将更新后的数据复制回全局内存
	if (gmi < num_node && gmj < num_node) {
		dis[gIdx] = main_block[sIdx];
		path[gIdx] = tmp_path;
	}
}

__global__ void phase2(float *dis, uint16_t *path, int num_node, int n) {
	if (blockIdx.x == n)  // 与主分块重叠
		return;
	
	// 主分块数据
	__shared__ float main_block[THREAD_NUM_TOTAL];  // size = 4KB
	// 与主分块同行或同列的分块数据
	__shared__ float side_block[THREAD_NUM_TOTAL];  // size = 4KB
	
	const int smj = threadIdx.x;
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	// 主分块
	int gmj = n * THREAD_NUM + smj;
	int gmi = n * THREAD_NUM + smi;
	
	if (gmi < num_node && gmj < num_node) {
		main_block[sIdx] = dis[POS2(gmi, gmj)];
	} else {
		main_block[sIdx] = INF;
	}
	
	// 该核函数对应的Grid有两行Block
	// 第一行Block(blockIdx.y == 0)负责与主分块同行的分块更新
	// 第二行Block(blockIdx.y == 1)负责与主分块同列的分块更新
	if (blockIdx.y == 0)
		gmj = blockIdx.x * THREAD_NUM + smj;
	else
		gmi = blockIdx.x * THREAD_NUM + smi;
	const int gIdx = POS2(gmi, gmj);  // 减少重复运算
	
	// 复制与主分块同行、同列分块的数据
	uint16_t tmp_path;
	if (gmi < num_node && gmj < num_node) {
		side_block[sIdx] = dis[gIdx];
		tmp_path = path[gIdx];
	} else {
		side_block[sIdx] = INF;
	}
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	const int base = smi * num_node;  // 减少重复运算
	const uint16_t path_base = n * THREAD_NUM + 1;
	float tmp;
	if (blockIdx.y == 0) {  // 同行
		for (int k = 0; k < THREAD_NUM; k++) {
			tmp = main_block[base + k] + side_block[POS1(k, smj)];
			if (side_block[sIdx] > tmp) {
				side_block[sIdx] = tmp;
				tmp_path = path_base + k;
			}
			
			__syncthreads();
		}
	} else {  // 同列
		for (int k = 0; k < THREAD_NUM; k++) {
			tmp = side_block[base + k] + main_block[POS1(k, smj)];
			if (side_block[sIdx] > tmp) {
				side_block[sIdx] = tmp;
				tmp_path = path_base + k;
			}
			
			__syncthreads();
		}
	}
	
	if (gmi < num_node && gmj < num_node) {
		dis[gIdx] = side_block[sIdx];
		path[gIdx] = tmp_path;
	}
}

__global__ void phase3(float *dis, uint16_t *path, int num_node, int n) {
	if (blockIdx.x == n || blockIdx.y == n) // 与阶段1和2的分块重叠
		return;

	// 分块数据（同列分块、同行分块）
	__shared__ float ver_block[THREAD_NUM_TOTAL];
	__shared__ float hor_block[THREAD_NUM_TOTAL];
	
	const int smj = threadIdx.x;
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	// 同列分块
	int gmj = blockIdx.x * THREAD_NUM + smj;
	int gmi = n * THREAD_NUM + smi;
	if (gmi < num_node && gmj < num_node) {
		ver_block[sIdx] = dis[POS2(gmi, gmj)];
	} else {
		ver_block[sIdx] = INF;
	}
	
	
	// 同行分块
	gmj = n * THREAD_NUM + smj;
	gmi = blockIdx.y * THREAD_NUM + smi;
	if (gmi < num_node && gmj < num_node) {
		hor_block[sIdx] = dis[POS2(gmi, gmj)];
	} else {
		hor_block[sIdx] = INF;
	}
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	
	// 本分块
	gmj = blockIdx.x * THREAD_NUM + smj;
	if (gmi < num_node && gmj < num_node) {
		const int gIdx = POS2(gmi, gmj);  // 根据需要使用变量gIdx的值，加快访问速度
		const int base = smi * num_node;
		const uint16_t path_base = n * THREAD_NUM + 1;
		
		float tmp;
		float tmp_dis = dis[gIdx];
		uint16_t tmp_path = path[gIdx];
		for (int k = 0; k < THREAD_NUM; k++) {
			tmp = hor_block[base + k] + ver_block[POS1(k, smj)];
			if (tmp_dis > tmp) {
				tmp_dis = tmp;
				tmp_path = path_base + k;
			}
		}
	
		// 将更新后的数据复制回全局内存
		dis[gIdx] = tmp_dis;
		path[gIdx] = tmp_path;
	}
}

__global__ void path_init(float *dis, uint16_t *path, int num_node) {
	const int gmj = blockIdx.x * THREAD_NUM + threadIdx.x;
	const int gmi = blockIdx.y * THREAD_NUM + threadIdx.y;
	
	if (gmi < num_node && gmj < num_node) {
		if (dis[POS2(gmi, gmj)] < INF) {
			path[POS2(gmi, gmj)] = gmj + 1;
		} else {
			path[POS2(gmi, gmj)] = 0;
		}
	}
}

__global__ void fast_phase1(float *dis, uint16_t *path, int num_node, int n) {
	__shared__ float main_block[THREAD_NUM_TOTAL];  // size = 4KB
	
	// 常量可能会得到进一步的缓存优化
	const int smj = threadIdx.x;  // shared memory j
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	const int gIdx = POS2((n * THREAD_NUM + smi), (n * THREAD_NUM + smj));
	
	// 将全局内存中的第n个主分块复制到共享内存
	main_block[sIdx] = dis[gIdx];
	uint16_t tmp_path = path[gIdx];
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	float tmp;  // 用私有内存访问替换共享内存访问
	const int base = smi * THREAD_NUM;
	const uint16_t path_base = n * THREAD_NUM + 1;
	for (int k = 0; k < THREAD_NUM; k++) {
		tmp = main_block[base + k] + main_block[POS1(k, smj)];
		
		// 第k行和第k列在本轮更新中值不会改变
		if (main_block[sIdx] > tmp) {
			main_block[sIdx] = tmp;
			tmp_path = path_base + k;
		}
		
		// 每个线程都完成本轮更新才能进行下一轮
		__syncthreads();
	}
	
	// 将更新后的数据复制回全局内存
	dis[gIdx] = main_block[sIdx];
	path[gIdx] = tmp_path;
}

__global__ void fast_phase2(float *dis, uint16_t *path, int num_node, int n) {
	if (blockIdx.x == n)  // 与主分块重叠
		return;
	
	// 主分块数据
	__shared__ float main_block[THREAD_NUM_TOTAL];  // size = 4KB
	// 与主分块同行或同列的分块数据
	__shared__ float side_block[THREAD_NUM_TOTAL];  // size = 4KB
	
	const int smj = threadIdx.x;
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	// 主分块
	int gmj = n * THREAD_NUM + smj;
	int gmi = n * THREAD_NUM + smi;
	
	main_block[sIdx] = dis[POS2(gmi, gmj)];
	
	// 该核函数对应的Grid有两行Block
	// 第一行Block(blockIdx.y == 0)负责与主分块同行的分块更新
	// 第二行Block(blockIdx.y == 1)负责与主分块同列的分块更新
	if (blockIdx.y == 0)
		gmj = blockIdx.x * THREAD_NUM + smj;
	else
		gmi = blockIdx.x * THREAD_NUM + smi;
	const int gIdx = POS2(gmi, gmj);  // 减少重复运算
	
	// 复制与主分块同行、同列分块的数据
	side_block[sIdx] = dis[gIdx];
	uint16_t tmp_path = path[gIdx];
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	const int base = smi * THREAD_NUM;  // 减少重复运算
	const uint16_t path_base = n * THREAD_NUM + 1;
	float tmp;
	if (blockIdx.y == 0) {  // 同行
		for (int k = 0; k < THREAD_NUM; k++) {
			tmp = main_block[base + k] + side_block[POS1(k, smj)];
			if (side_block[sIdx] > tmp) {
				side_block[sIdx] = tmp;
				tmp_path = path_base + k;
			}
			
			__syncthreads();
		}
	} else {  // 同列
		for (int k = 0; k < THREAD_NUM; k++) {
			tmp = side_block[base + k] + main_block[POS1(k, smj)];
			if (side_block[sIdx] > tmp) {
				side_block[sIdx] = tmp;
				tmp_path = path_base + k;
			}
			
			__syncthreads();
		}
	}
	
	dis[gIdx] = side_block[sIdx];
	path[gIdx] = tmp_path;
}

__global__ void fast_phase3(float *dis, uint16_t *path, int num_node, int n) {
	if (blockIdx.x == n || blockIdx.y == n) // 与阶段1和2的分块重叠
		return;

	// 分块数据（同列分块、同行分块）
	__shared__ float ver_block[THREAD_NUM_TOTAL];
	__shared__ float hor_block[THREAD_NUM_TOTAL];
	
	const int smj = threadIdx.x;
	const int smi = threadIdx.y;
	const int sIdx = POS1(smi, smj);
	
	// 同列分块
	int gmj = blockIdx.x * THREAD_NUM + smj;
	int gmi = n * THREAD_NUM + smi;
	ver_block[sIdx] = dis[POS2(gmi, gmj)];
	
	
	// 同行分块
	gmj = n * THREAD_NUM + smj;
	gmi = blockIdx.y * THREAD_NUM + smi;
	hor_block[sIdx] = dis[POS2(gmi, gmj)];
	// 保证所需数据全部复制到了共享内存
	__syncthreads();
	
	
	// 本分块
	gmj = blockIdx.x * THREAD_NUM + smj;
	const int gIdx = POS2(gmi, gmj);  // 根据需要使用变量gIdx的值，加快访问速度
	const int base = smi * THREAD_NUM;
	const uint16_t path_base = n * THREAD_NUM + 1;
		
	float tmp;
	float tmp_dis = dis[gIdx];
	uint16_t tmp_path = path[gIdx];
	for (int k = 0; k < THREAD_NUM; k++) {
		tmp = hor_block[base + k] + ver_block[POS1(k, smj)];
		if (tmp_dis > tmp) {
			tmp_dis = tmp;
			tmp_path = path_base + k;
		}
	}
	
	// 将更新后的数据复制回全局内存
	dis[gIdx] = tmp_dis;
	path[gIdx] = tmp_path;
}

__global__ void fast_path_init(float *dis, uint16_t *path, int num_node) {
	const int gmj = blockIdx.x * THREAD_NUM + threadIdx.x;
	const int gmi = blockIdx.y * THREAD_NUM + threadIdx.y;
	
	if (dis[POS2(gmi, gmj)] < INF) {
		path[POS2(gmi, gmj)] = gmj + 1;
	} else {
		path[POS2(gmi, gmj)] = 0;
	}
}

__global__ void convert(uint16_t *path, int *path_tmp, int num_node) {
	const int gmj = blockIdx.x * THREAD_NUM + threadIdx.x;
	const int gmi = blockIdx.y * THREAD_NUM + threadIdx.y;
	
	if (gmi < num_node && gmj < num_node)
		path_tmp[POS2(gmi, gmj)] = int(path[POS2(gmi, gmj)]);
}

/**
* 输入：
* 	num_node 结点数 [70, 50000]
* 	arc 邻接矩阵
* 输出：
* 	path_node 任意两节点之间最短路径经过的节点
*	shortLenTable 任意两节点之间最短路径的长度
*/
void shortestPath_floyd(int num_node, float *arc, int *path_node, float *shortLenTable) {
	float *d_dis;
	uint16_t *d_path;
	int *d_path_tmp;  // 用于将uint16_t转成int
	
	// 距离矩阵 size <= 9.31GB
	hipMalloc((void **) &d_dis, num_node * num_node * sizeof(float));
	// 路径矩阵，由于最多仅有50000个节点，则编号可用uint16_t存储 size <= 4.65GB
	hipMalloc((void **) &d_path, num_node * num_node * sizeof(uint16_t));
	
	// 复制邻接矩阵到显存中的距离矩阵
	hipMemcpy(d_dis, arc, num_node * num_node * sizeof(float), hipMemcpyHostToDevice);
	
	// 将矩阵分割成n * n个分块
	int n = (num_node - 1) / THREAD_NUM + 1;
	if (num_node % THREAD_NUM == 0) {
		// 初始化路径矩阵
		hipLaunchKernelGGL(fast_path_init, dim3(n, n), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node);
		for (int i = 0; i < n; i++) {
			hipLaunchKernelGGL(fast_phase1, 1, dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
			hipLaunchKernelGGL(fast_phase2, dim3(n, 2), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
			hipLaunchKernelGGL(fast_phase3, dim3(n, n), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
		
			//printf("%dst round\n", i + 1);
		}
	} else {
		hipLaunchKernelGGL(path_init, dim3(n, n), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node);	
		for (int i = 0; i < n; i++) {
			hipLaunchKernelGGL(phase1, 1, dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
			hipLaunchKernelGGL(phase2, dim3(n, 2), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
			hipLaunchKernelGGL(phase3, dim3(n, n), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_dis, d_path, num_node, i);
		
			//printf("%dst round\n", i + 1);
		}
	}
	
	// 将结果输出，释放内存供d_path_tmp使用
	hipMemcpy(shortLenTable, d_dis, num_node * num_node * sizeof(float), hipMemcpyDeviceToHost);
	hipFree(d_dis);
	
	// size <= 9.31GB
	hipMalloc((void **) &d_path_tmp, num_node * num_node * sizeof(int));
	// uint16_t -> int
	hipLaunchKernelGGL(convert, dim3(n, n), dim3(THREAD_NUM, THREAD_NUM), 0, 0, d_path, d_path_tmp, num_node);
	// 将结果输出
	hipMemcpy(path_node, d_path_tmp, num_node * num_node * sizeof(int), hipMemcpyDeviceToHost);
	
	// 释放内存
	hipFree(d_path);
	hipFree(d_path_tmp);
}
