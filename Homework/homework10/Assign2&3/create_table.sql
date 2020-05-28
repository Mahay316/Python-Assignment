-- 创建存储留言板数据的表
-- ID，留言内容，留言人，留言时间，是否删除
DROP TABLE IF EXISTS `bbs`;
CREATE TABLE `bbs` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `content` text,
    `username` varchar(255) DEFAULT NULL,
    `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `is_delete` bit DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
