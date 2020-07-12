-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: bbs
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `message_id` int DEFAULT NULL,
  `content` text,
  `reply_to` int NOT NULL,
  `reply_to_id` int DEFAULT NULL,
  `hidden` bit(1) NOT NULL DEFAULT b'0',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `message_id` (`message_id`),
  KEY `reply_to_id` (`reply_to_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`message_id`) REFERENCES `message` (`message_id`),
  CONSTRAINT `comment_ibfk_3` FOREIGN KEY (`reply_to_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (6,6,12,'comment 测试',0,6,_binary '\0','2020-06-27 21:56:02','2020-06-27 21:56:02'),(7,6,12,'reply 测试',6,6,_binary '\0','2020-06-27 21:56:43','2020-06-27 21:56:43'),(8,6,12,'reply 测试',6,6,_binary '\0','2020-06-27 21:56:46','2020-06-27 21:56:46'),(9,6,12,'长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试',6,6,_binary '\0','2020-06-27 21:57:01','2020-06-27 21:57:01'),(10,6,12,'长回复测试长回复测试长回复测试长回复测试长回复测试长回复测长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试长回复测试试长回复测试长回复测试',6,6,_binary '\0','2020-06-27 21:57:06','2020-06-28 15:30:20'),(11,6,12,'长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试',0,6,_binary '\0','2020-06-27 21:57:37','2020-06-27 21:57:37'),(12,6,12,'评论测试',0,6,_binary '\0','2020-06-28 11:29:11','2020-06-28 11:29:11'),(13,6,12,'回复测试',12,6,_binary '\0','2020-06-28 11:29:19','2020-06-28 11:29:19'),(14,6,12,'清空测试',0,6,_binary '\0','2020-06-28 11:29:49','2020-06-28 11:29:49'),(15,6,12,'清空测试',0,6,_binary '\0','2020-06-28 11:30:04','2020-06-28 11:30:04'),(16,6,12,'长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试长评论测试',0,6,_binary '\0','2020-06-28 11:30:37','2020-06-28 15:30:20'),(17,6,7,'评论测试评论测试评论测试评论测试评论测试',0,6,_binary '\0','2020-06-28 11:30:59','2020-06-30 10:44:34'),(18,6,7,'顶',0,6,_binary '\0','2020-06-28 11:37:25','2020-06-28 11:37:25'),(19,3,12,'用户评论测试',0,6,_binary '\0','2020-06-28 11:39:57','2020-06-28 11:39:57'),(20,3,12,'用户回复测试',16,6,_binary '\0','2020-06-28 11:40:08','2020-06-28 11:40:08'),(21,6,24,'顶！',0,6,_binary '\0','2020-06-28 14:09:27','2020-06-28 14:09:27'),(22,6,24,'√',21,6,_binary '\0','2020-06-28 14:09:35','2020-06-28 14:09:35'),(23,6,12,'666',19,3,_binary '\0','2020-06-28 14:12:51','2020-06-28 15:30:20'),(25,6,12,'评论分页测试',0,6,_binary '\0','2020-06-28 14:43:28','2020-06-28 14:43:28'),(26,6,12,'评论分页测试',0,6,_binary '\0','2020-06-28 14:43:37','2020-06-28 14:43:37'),(27,6,12,'评论分页测试',0,6,_binary '\0','2020-06-28 14:43:39','2020-06-28 15:30:20'),(29,6,12,'评论分页测试',0,6,_binary '\0','2020-06-28 14:52:00','2020-06-28 15:31:03'),(30,6,12,'分页评论测试',0,6,_binary '\0','2020-06-28 14:52:12','2020-06-28 15:31:03'),(31,6,12,'分页回复测试',11,6,_binary '\0','2020-06-28 14:52:28','2020-06-28 14:52:28'),(32,6,15,'hello',0,6,_binary '\0','2020-06-29 18:28:26','2020-06-30 10:44:20'),(33,6,15,'hi',32,6,_binary '\0','2020-06-29 18:28:33','2020-06-29 18:28:33'),(34,6,26,'欢迎欢迎',0,7,_binary '\0','2020-06-29 22:38:58','2020-06-29 22:38:58'),(35,6,26,'哈哈哈',34,6,_binary '\0','2020-06-29 22:39:09','2020-06-30 10:42:49'),(36,7,24,'Hello',0,6,_binary '\0','2020-06-29 23:18:36','2020-06-29 23:18:36'),(37,8,20,'这是一条为展示评论功能的评论',0,6,_binary '\0','2020-07-01 11:00:34','2020-07-01 11:00:34'),(38,8,20,'展示回复功能',37,8,_binary '','2020-07-01 11:05:40','2020-07-01 12:56:48'),(39,6,29,'这个留言板的功能实在是太丰富了',0,8,_binary '\0','2020-07-01 11:31:08','2020-07-01 11:31:08'),(40,3,29,'太棒了太棒了',0,8,_binary '\0','2020-07-01 11:31:45','2020-07-01 11:31:45');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `type` smallint DEFAULT NULL,
  `headline` varchar(100) NOT NULL,
  `content` text,
  `read_count` int NOT NULL DEFAULT '0',
  `reply_count` int NOT NULL DEFAULT '0',
  `hidden` bit(1) NOT NULL DEFAULT b'0',
  `drafted` bit(1) NOT NULL,
  `recommended` bit(1) NOT NULL DEFAULT b'0',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`message_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (7,6,0,'留言富文本测试','<p>中文</p><p>English</p><p><strong>加粗文本</strong></p><p><em>斜体文本</em></p><p><strong><em>斜体加粗文本</em></strong></p>',38,2,_binary '\0',_binary '',_binary '\0','2020-06-25 21:53:20','2020-06-28 11:37:26'),(8,6,0,'是发送到发送到发','<p>是发送方士大夫水电费水电费双丰收地方</p>',13,0,_binary '\0',_binary '',_binary '\0','2020-06-25 21:56:30','2020-06-27 21:21:34'),(9,6,1,'测试测试','<p>似懂非懂算法都是发送到发顺丰算法</p>',1,0,_binary '\0',_binary '\0',_binary '\0','2020-06-25 21:58:33','2020-06-26 09:29:00'),(11,6,1,'留言列表测试','<p>留言列表测试</p><p><strong>留言列表测试</strong></p><p>留言列表测试</p><p>图片测试<img src=\"/static/upload/user6_reactivity.png\" title=\"user6_reactivity.png\" alt=\"user6_reactivity.png\"/></p>',1,0,_binary '',_binary '',_binary '\0','2020-06-26 09:38:24','2020-06-29 18:11:56'),(12,6,1,'侧边栏隐藏测试','<p>测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试</p>',176,21,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:39:07','2020-06-30 19:02:30'),(13,6,1,'侧边栏隐藏测试','<p>侧边栏隐藏测试侧边栏隐藏测试侧边栏隐藏测试侧边栏隐藏测试侧边栏隐藏测试侧边栏隐藏测试</p>',1,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:39:39','2020-06-26 09:39:39'),(14,6,1,'分页测试','<p>分页测试分页测试分<sup>页测试分页</sup>测试<sub>分页</sub>测试</p><p>文章修改测试</p>',2,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:43:16','2020-06-30 09:57:22'),(15,6,1,'分页测试','<p>分页测试分页测试分页测试分页测试分页测试分页测试分页测试<img src=\"http://img.baidu.com/hi/jx2/j_0025.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0060.gif\"/></p>',7,2,_binary '',_binary '',_binary '\0','2020-06-26 09:44:59','2020-06-30 10:46:37'),(16,6,1,'分页测试','<p>分页测试分页测试分页测试分页测试分页测试分页测试分页测试分页测试分页测试分页测试</p>',1,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:45:38','2020-06-26 09:45:39'),(17,6,1,'分页测试','<p>分页测试分页测试<img src=\"http://img.baidu.com/hi/jx2/j_0003.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0057.gif\"/>分页测试分页测分页测试分页测分页测试分页测分页测试分页测</p>',1,0,_binary '',_binary '\0',_binary '\0','2020-06-26 09:46:20','2020-06-29 18:07:33'),(18,6,1,'分页测试','<pre class=\"brush:cpp;toolbar:false\">#include&nbsp;&lt;stdio.h&gt;\n\nvoid&nbsp;main()&nbsp;{\n&nbsp;&nbsp;&nbsp;&nbsp;printf(&quot;Hello&nbsp;World\\n&quot;);\n&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;0;\n}</pre><p><br/></p>',2,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:47:10','2020-06-26 13:05:05'),(19,6,1,'分页测试10','<p>分页测试10分页测试10分页测试10分页测试10分页测试10</p>',3,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:47:27','2020-06-26 13:05:56'),(20,6,1,'分页测试11','<p>分页测试11分页测试11分页测试11分页测试11分页测试11分页测试11<img src=\"http://img.baidu.com/hi/jx2/j_0024.gif\"/></p>',3,2,_binary '\0',_binary '\0',_binary '\0','2020-06-26 09:47:44','2020-07-01 11:05:40'),(21,3,1,'头像测试','<p><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/>头像测试头像测试头像测试头像测试头像测试头像测试头像测试头像测试头像测试头像测试头像测试</p>',3,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 10:13:25','2020-06-27 21:59:04'),(22,6,1,'intro文本截取测试','<p>文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试文本截取测试</p><p>文本截取测试文本截取测试文本截取测试</p><p>文本截取测试文本截取测试</p>',40,0,_binary '\0',_binary '\0',_binary '\0','2020-06-26 13:07:25','2020-06-27 16:04:36'),(24,6,0,'编程语言','<p>编程语言编程语言编程语言编程语言编程语言编程语言编程语言编程语言编程语言</p>',20,3,_binary '\0',_binary '\0',_binary '\0','2020-06-28 14:00:59','2020-06-30 19:02:37'),(25,6,0,'表情测试','<p><img src=\"http://img.baidu.com/hi/jx2/j_0007.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0011.gif\"/></p><p>Хорошо!&nbsp; &nbsp;&nbsp;</p>',2,1,_binary '',_binary '\0',_binary '\0','2020-06-28 14:14:15','2020-06-30 10:18:39'),(26,7,0,'新用户！！','<p>大家好，我是新用户！<img src=\"http://img.baidu.com/hi/jx2/j_0011.gif\"/></p>',8,2,_binary '\0',_binary '\0',_binary '\0','2020-06-29 17:00:53','2020-06-29 23:30:57'),(27,6,5,'新发布留言','<p>新发布留言新发布留言新发布留言新发布留言新发布留言<img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>',2,0,_binary '\0',_binary '',_binary '\0','2020-06-30 09:32:14','2020-06-30 10:22:00'),(28,6,0,'搜索分页测试','<p>搜索分页测试搜索分页测试搜索分页测试搜索分页测试搜索分页测试搜索分页测试搜索分页测试搜索分页测试搜索分页测试<img src=\"http://img.baidu.com/hi/jx2/j_0003.gif\"/></p>',2,0,_binary '\0',_binary '\0',_binary '\0','2020-06-30 19:07:07','2020-07-01 09:36:07'),(29,8,5,'留言发布功能介绍','<p>留言内容不只支持纯文本，还支持格式化文本，如：<strong>加粗</strong>、<em>斜体</em>、<span style=\"text-decoration: underline;\">下划线</span>、<span style=\"text-decoration: line-through;\">删除线</span>、上<sup>标</sup>、下<sub>标</sub>等。</p><p>同时支持动态表情的插入：<img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0019.gif\"/></p><p>支持图片上传功能：<img src=\"/static/upload/user8_dinosaur.jpg\" title=\"user8_dinosaur.jpg\" alt=\"user8_dinosaur.jpg\" width=\"150\" height=\"150\"/></p><p><span style=\"font-size: 18px;\"><strong>还支持代码语言、修改字体、表格等多种功能！！！</strong></span></p>',7,2,_binary '\0',_binary '\0',_binary '\0','2020-07-01 10:21:46','2020-07-01 12:59:12'),(30,8,5,'这是我发布的第二条留言！！','<p><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/></p><p>第二条留言！！欢迎评论&amp;回复！！！！</p>',1,0,_binary '',_binary '\0',_binary '\0','2020-07-01 11:34:07','2020-07-01 12:52:54'),(31,8,2,'这是一篇草稿','<p>这是一篇草稿，目前还不准备发布，待修改到满意再说。</p>',1,0,_binary '',_binary '',_binary '\0','2020-07-01 11:37:12','2020-07-01 12:52:55');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `password` char(32) DEFAULT NULL,
  `avatar` varchar(50) NOT NULL DEFAULT 'default.jpg',
  `email` varchar(50) DEFAULT NULL,
  `role` varchar(10) NOT NULL DEFAULT 'user',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'zpf1','Peter','e10adc3949ba59abbe56e057f20f883e','default.jpg',NULL,'user','2020-06-24 23:56:30','2020-06-26 00:10:47'),(6,'a1422411405','Mahay','e10adc3949ba59abbe56e057f20f883e','user6_dinosaur.jpg','test@qq.com','user','2020-06-25 15:28:25','2020-06-30 22:12:47'),(7,'abc123','Megie','4297f44b13955235245b2497399d7a93','default.jpg',NULL,'user','2020-06-29 16:57:22','2020-06-29 16:58:04'),(8,'test1','Donald','e10adc3949ba59abbe56e057f20f883e','user8_dinosaur.jpg',NULL,'user','2020-07-01 09:48:03','2020-07-01 11:27:55');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-01 13:17:01
