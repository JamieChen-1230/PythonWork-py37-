-- select * from sc where cid='01';
-- select * from sc where cid='02';
-- select * from 
-- 	(select * from sc where cid='01') as t01, 
-- 	(select * from sc where cid='02') as t02
-- 	where t01.sid=t02.sid and t01.score>t02.score;
-- select * from student inner join
-- 	(select t01.sid, t01.score as 01score, t02.score as 02score from 
-- 		(select * from sc where cid='01') as t01, 
-- 		(select * from sc where cid='02') as t02
-- 		where t01.sid=t02.sid and t01.score>t02.score) as t
-- 	on student.sid=t.sid;

-- select t01.sid, t01.score as 01score, t02.score as 02score from 
--             (select * from sc where cid='01') as t01 left join (select * from sc where cid='02') as t02
--             on t01.sid=t02.sid;

-- select student.*, mean from student inner join 
--         (select sid, avg(score) as mean from sc group by sid Having avg(score)>60) as t
--         on student.sid=t.sid;

-- select * from student where sid in (select distinct sid from sc);
-- select * from student where not exists (select * from sc where sc.sid=student.sid);

-- select count(*) from teacher where tname like '李%';

-- select * from student where student.sid in 
--         (select sid from sc where sc.cid in 
--             (select cid from course where tid=(select tid from teacher where tname='张三')));


-- select *
--             from teacher, course, student, sc
--             where teacher.Tname='张三'
--                 and teacher.TId=course.TId
--                 and course.CId=sc.CId
--                 and sc.SId=student.SId;

-- select *, count(*) from sc group by sid Having count(cid)=(select count(*) from course);

-- select * from student where sid not in (
--             select sid from sc group by sid Having count(cid)=(
--                 select count(*) from course
--                 )
--             );

-- select * from student where sid in (
--         select distinct sid from sc where cid in (select cid from sc where sid='01') and sid!='01'
--         );

-- select *, GROUP_CONCAT(cid) as all_cid from sc group by sid Having all_cid=(
--         select GROUP_CONCAT(cid) as all_cid from sc where sid='01'
--     );

-- select * from student where sid not in(
--         select distinct sid from sc where cid in (
--             select cid from course where tid=(select tid from teacher where tname='张三')
--         )
--     );

-- select * from sc inner join 
--         (select sid, count(*) from sc where score<60 group by sid Having count(*)>=2) as t
--     on sc.sid=t.sid; 
    
-- select student.*, t2.avgscore from 
--         student inner join (
--             select sc.sid as id, avg(score) as avgscore from sc inner join (
--                 select sid, count(*) from sc where score<60 group by sid Having count(*)>=2
--             ) as t on sc.sid=t.sid group by sc.sid
--         ) as t2 on student.sid=t2.id;

-- select student.*, t.score from student inner join (
--         select sid, score from sc where cid='01' and score<60) as t
--         on student.sid=t.sid order by t.score;

-- select sid, group_concat(score), avg(score) as avgscore from sc group by sid order by avgscore desc;

-- select sc.cid as 課程ID, course.cname as 課程名, max(score) as 最高分, min(score) as 最低分, avg(score) as 平均分, count(*) as 選課人數,
--      sum(case when sc.score>=60 then 1 else 0 end)/count(*) as 及格率,
--      sum(case when sc.score>=70 and sc.score<80 then 1 else 0 end )/count(*) as 中等率,
--      sum(case when sc.score>=80 and sc.score<90 then 1 else 0 end )/count(*) as 優良率,
--      sum(case when sc.score>=90 then 1 else 0 end)/count(*) as 優秀率 
--      from sc inner join course on sc.cid=course.cid
--      group by sc.cid
--      order by 選課人數 desc, 課程ID asc;


-- select sc.SId, sc.CId,
--         case 
--             when @pre_parent_code=sc.CId then @curRank:=@curRank+1
--             -- 當換至另一門課程時，重置排名
--             when @pre_parent_code:=sc.CId then @curRank:=1  
--         end as 排名, sc.score
--         -- 使用變數必須宣告初始值(變數前面需加@)
--         from (select @curRank:=0,@pre_parent_code:='') as t, sc
--         ORDER by sc.CId, sc.score desc;


-- select *, DENSE_RANK()over(PARTITION BY cid order by score desc)排名 from SC;

-- select sc.SId, sc.CId, 
--             CASE 
--                 when @pre_parent_code=sc.CId then (
--                     CASE 
--                         when @prefontscore=sc.score then @curRank 
--                         when @prefontscore:=sc.score then @curRank:=@curRank+1 
--                     END) 
--                 when @pre_parent_code:=sc.CId then @prefontscore:=sc.score and @curRank:=1
--             END as 排名 , sc.score
--             from (select @curRank:=0, @pre_parent_code:='', @prefontscore:=null) as t, sc
--             ORDER by sc.CId, sc.score desc;

-- select t.*, (@curRank:=@curRank+1) as 排名 from (
--             select sid, sum(score) as sumscore from sc group by sc.sid order by sum(score) desc
--         ) as t, (select @curRank:=0) as val;

-- select t.*, DENSE_RANK()over(order by sumscore desc) as 排名 from(
--             select sid, sum(score) as sumscore from sc group by sid) as t;

-- select cname as 課程名稱, t.* from course inner join (
--         select cid as 課程編號,
--         sum(CASE WHEN score<=100 and score>85 THEN 1 ELSE 0 END) as '[100-85]',
--         sum(CASE WHEN score<=100 and score>85 THEN 1 ELSE 0 END)/count(*) as '[100-85]%',
--         sum(CASE WHEN score<=85 and score>70 THEN 1 ELSE 0 END) as '[85-70]',
--         sum(CASE WHEN score<=70 and score>60 THEN 1 ELSE 0 END) as '[70-60]',
--         sum(CASE WHEN score<=60 THEN 1 ELSE 0 END) as '[60-0]'
--         from sc group by cid
--     ) as t on course.cid=t.課程編號;

-- select * from (
--         select *, RANK()over(PARTITION by cid order by score desc) as ranks from sc
--         ) as t where t.ranks<=3;

-- select cid, count(*) from sc group by cid;

-- select sid, sname from student where sid in (
--         select sid from sc group by sid Having count(cid)=2);

-- select ssex, count(*) from student group by ssex;

-- select sname, count(*) as 同名人數 from student as stu1 where exists (select * from student as stu2 where stu1.sid!=stu2.sid and stu1.sname=stu2.sname);

-- select * from student where YEAR(sage)=1990;

-- select cid, avg(score) as avgscore from sc group by cid order by avgscore desc, cid asc;

-- select student.*, t.avgscore from student inner join (
--         select sid, avg(score) as avgscore from sc group by sid Having avgscore>85
--         ) as t on student.sid=t.sid;

-- select * from student inner join (
--         select sid from sc where cid=(select cid from course where cname='数学') and score<60
--     ) as t on student.sid=t.sid;

-- select * from student left join sc on student.sid=sc.sid;

-- select student.sname, course.cname, t.score from student, course, (select sid, cid, score from sc where score>70) as t 
--     where student.sid=t.sid and t.cid=course.cid;

-- select * from course where cid in (select cid from sc where score<60);

-- select * from student where sid in (select sid from sc where cid='01' and score>=80);

-- select * from sc where cid in (
--         select cid from course where tid=(select tid from teacher where tname='张三')
--         ) ;

-- select student.*, t.score from student inner join (
--         select sid, score from sc where cid in (
--             select cid from course where tid=(select tid from teacher where tname='张三')
--         ) order by score desc limit 1
--     ) as t on student.sid=t.sid;

-- select student.* from student inner join (
--         select *, RANK()over(order by score desc) as ranks from sc where cid in (
--             select cid from course where tid=(select tid from teacher where tname='李四'))
--     ) as t on student.sid=t.sid where t.ranks=1;

 select * from sc where (select * from sc as sc2 where sc.cid!=sc2.cid and sc.score=sc2.score);