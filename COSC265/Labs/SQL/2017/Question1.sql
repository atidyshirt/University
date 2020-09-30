create table JobSkill
(
 job_name varchar(20) not null,
 skill_code char(1) not null references skill(S_Code),
 rank_value smallint not null,
 primary key(job_name, skill_code)
);


