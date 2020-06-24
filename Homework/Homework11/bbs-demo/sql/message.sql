CREATE TABLE IF NOT EXISTS `message` (
	`message_id` INT AUTO_INCREMENT,  -- 留言唯一id
	`user_id` INT,  -- 发布留言的用户id
	`type` TINYINT NOT NULL,  -- 留言类型
	`headline` VARCHAR(100)	NOT NULL,  -- 留言标题
	`content` MEDIUMTEXT,  -- 留言内容
	`read_count` INT NOT NULL DEFAULT 0,  -- 阅读次数
	`reply_count` INT NOT NULL DEFAULT 0,  -- 回复数量（包括留言评论和评论的回复）
	`hidden` BIT(1)	NOT NULL DEFAULT b'0',  -- 是否隐藏（临时删除）
	`drafted` BIT(1) NOT NULL,  -- 是否为草稿
	`recommended` BIT(1) NOT NULL DEFAULT b'0',  -- 管理员是否置顶
	`create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 格式YYYY-MM-DD hh:mm:ss 记录创建时间
	`update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- 记录修改时间

	PRIMARY KEY (`message_id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
