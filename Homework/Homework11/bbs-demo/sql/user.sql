CREATE TABLE IF NOT EXISTS `user` (
	`user_id` INT AUTO_INCREMENT,  -- 用户唯一id
    `username` VARCHAR(50) NOT NULL,  -- 用户登录时输入账号
    `nickname` VARCHAR(50) NOT NULL,  --	用户昵称
    `password` CHAR(32), -- MD5加密字符 用户登录密码
    `avatar` VARCHAR(50) NOT NULL DEFAULT 'default.png',  -- 有默认头像 头像文件名称
    `email` VARCHAR(50),  -- 用户安全邮箱
    `role` VARCHAR(10) NOT NULL DEFAULT 'user',  -- admin为管理员 user为普通用户 用户身份
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 格式YYYY-MM-DD hh:mm:ss 记录创建时间
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- 记录修改时间
	 PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
