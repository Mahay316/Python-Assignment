CREATE TABLE IF NOT EXISTS `comment` (
	`comment_id`	INT	AUTO_INCREMENT,  -- 评论唯一id
	`user_id` INT,  -- 发表回复的用户id
	`message_id` INT,  -- 回复的留言id
	`content` TEXT,  -- 最多65536个字符 评论内容
	`reply_to` INT NOT NULL,  -- 留言的原始评论为0 评论的回复该字段为对应的commentid回复针对的内容
	`reply_to_id` INT,  -- 回复给id为reply_to_id的用户
	`hidden` BIT(1)	NOT NULL DEFAULT b'0',  -- 非空、默认为0 是否隐藏
	`create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 格式YYYY-MM-DD hh:mm:ss 记录创建时间
	`update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- 记录修改时间

	PRIMARY KEY (`comment_id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
	FOREIGN KEY (`message_id`) REFERENCES `message`(`message_id`),
	FOREIGN KEY (`reply_to_id`) REFERENCES `user`(`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
