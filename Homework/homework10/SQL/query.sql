-- 1. 查询所有男生的姓名，年龄，所在班级名称
-- INNER JOIN 忽略了未保存在classes表中的cls_id
SELECT s.name, s.age, c.name FROM students AS s JOIN classes AS c ON s.cls_id = c.id WHERE gender = '男';

-- 2. 查询所有编号小于4或没被删除的学生
SELECT * FROM students WHERE id < 4 OR is_delete = b'0';

-- 3. 查询姓黄并且“名”是一个字的学生
SELECT * FROM students WHERE name LIKE '黄_';

-- 4. 查询编号是1或3或8的学生
SELECT * FROM students WHERE id IN (1, 3, 8);

-- 5. 查询编号为3至8的学生
SELECT * FROM students WHERE id BETWEEN 3 AND 8;

-- 6. 查询未删除男生信息，按年龄降序
SELECT * FROM students WHERE (gender = '男' AND is_delete = b'0') ORDER BY age DESC;

-- 7. 查询女生的总数
SELECT COUNT(*) FROM students WHERE gender = '女';

-- 8. 查询学生的平均年龄
SELECT AVG(age) AS `Average Age` FROM students;

-- 9. 分别统计性别为男/女的人年龄平均值
SELECT gender, AVG(age) AS `Average Age` FROM students WHERE gender IN ('男', '女') GROUP BY gender;

-- 10. 按照性别来进行人员分组（group by + group_concat()）
SELECT gender, GROUP_CONCAT(name) AS NAME FROM students GROUP BY gender;
