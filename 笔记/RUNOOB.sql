/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Version : 50621
 Source Host           : localhost
 Source Database       : RUNOOB

 Target Server Version : 50621
 File Encoding         : utf-8

 Date: 03/03/2016 15:36:16 PM
*/


SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for test1
-- ----------------------------
DROP TABLE IF EXISTS test1;
CREATE TABLE test1 (
  test1_id int(11) NOT NULL,
  title varchar(255) DEFAULT NULL,
  name varchar(255) DEFAULT NULL ,
  date date DEFAULT NULL,
  PRIMARY KEY (test1_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of test1
-- ----------------------------
BEGIN;
INSERT INTO test1 VALUES 
(1, 'Learn PHP', 'a', '2007-05-24'), 
(2, 'Learn MySQL', 'b', '2007-05-24'), 
(6, 'Learn MySQL', 'b', '2007-05-24'), 
(3, 'Learn MySQL', 'c', '2007-05-24'), 
(5, 'Learn MySQL', 'jk', '2007-05-24'), 
(4, 'JAVA Tutorial', 'd', '2007-05-06');
COMMIT;

-- ----------------------------
--  Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS test2 ;
CREATE TABLE test2  (
	name1 char(20) not null,
	name2 char(20) not null,
	sex char(10),
	test2_id int not null,
	primary key (test2_id),
	test1_id int,
	foreign key (test1_id) references test1(test1_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of test
-- ----------------------------
BEGIN;

insert INTO test2
 VALUES 
('a','a1fdf','m', 1, 1),
('a','bcv1','f',34 , 2),
('b','b1df','f',564 ,3),
('c','c1dsf','m',8,4),
('c1','c1','m',657, 5),
('d','d2','f',23, 6),
('d','d1df','f',34234, 7),
('e','e1','m',45, 8),
('e','eee','m',464, 9),
('f','f1df','f', 4, 10);
COMMIT;



SET FOREIGN_KEY_CHECKS = 1;
