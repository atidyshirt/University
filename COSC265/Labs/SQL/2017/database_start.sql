--------------------------------------------------------------------
-- COSC265 S2 2017, Lab Test
-- Achievement Script
--------------------------------------------------------------------
drop table Town;
drop table Creature;
drop table Skill;
drop table Achievement;
drop table JobSkill;

-- Town (City) table
create table Town
(T_id        varchar(2)       ,
  T_name      varchar(20)      not null,
  primary key (T_id)
);

-- Creature table
create table Creature
(C_id             smallint    ,
  C_name           varchar(15) not null,
  C_type           varchar(10) not null,
  reside_t_id      varchar(2),
  primary key (C_id),
  constraint fk_cr_to foreign key (reside_t_id) references Town(T_id) on delete set null
);

-- Skill table
create table Skill
(S_code       char            ,
  S_desc       varchar(15)     not null,
  S_weight     number          ,
  primary key (S_code)
);

-- Achievement table
create table Achievement
(C_id         smallint        references Creature(C_id),
S_code       char            references Skill(S_code),
score        smallint        not null,
test_t_id    varchar(2)      references Town(T_id),
primary key (C_id, S_code),
constraint fk_ac_cr foreign key (C_id) references Creature (C_id) on delete set null,
constraint fk_ac_sk foreign key (S_code) references Skill (S_code) on delete set null,
constraint fk_ac_to foreign key (test_t_id) references Town (T_id) on delete set null
);

  -- Job Skill table
create table JobSkill
(
job_name varchar(20) not null,
skill_code char(1) not null references skill(S_Code),
rank_value smallint not null,
constraint pk_jobskill primary key (job_name, skill_code)
);

--Question 1(b)
INSERT INTO JobSkill VALUES ('SWDeveloper', 'C', 2);
INSERT INTO JobSkill VALUES ('SWDeveloper', 'D', 3);
INSERT INTO JobSkill VALUES ('SWDeveloper', 'T', 1);
INSERT INTO JobSkill VALUES ('Lifeguard', 'F', 2);
INSERT INTO JobSkill VALUES ('Lifeguard', 'S', 1);

--------------------------------------------------------------------
-- COSC265 S2 2017, Lab Test
-- Achievement Instances Script
--------------------------------------------------------------------

-- Town records
insert
into Town (T_id, T_Name)
values    ('Au', 'Auckland');

insert
into Town (T_id, T_name)
values    ('Ch', 'Christchurch');

insert
into Town (T_id, T_name)
values    ('We', 'Wellington');


-- Creature records
insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (1, 'Bannon', 'Person', 'Ch');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (2, 'Myers', 'Person', 'Au');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (3, 'Neff', 'Person', 'We');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (4, 'Neff', 'Person', 'Ch');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (5, 'Mieska', 'Person', 'Ch');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (6, 'Carlis', 'Person', 'We');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (7, 'Gollum', 'Hobbit', 'We');

insert
into Creature (C_id, C_name, C_type, reside_T_id)
values        (8, 'Smaug', 'Dragon', null);


-- Skill records
insert
into Skill (S_code, S_desc, S_weight)
values     ('B', 'Breathe fire', 0.9);

insert
into Skill (S_code, S_desc, S_weight)
values     ('C', 'Code', 0.6);

insert
into Skill (S_code, S_desc, S_weight)
values     ('D', 'Design', 0.7);

insert
into Skill (S_code, S_desc, S_weight)
values     ('F', 'Float', 0.5);

insert
into Skill (S_code, S_desc, S_weight)
values     ('R', 'Riddle', 0.2);

insert
into Skill (S_code, S_desc, S_weight)
values     ('S', 'Swim', 0.7);

insert
into Skill (S_code, S_desc, S_weight)
values     ('T', 'Test', 0.8);

insert
into Skill (S_code, S_desc, S_weight)
values     ('W', 'Walk', 0.4);


-- Achievement records
insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (1, 'S', 1, 'Au');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (1, 'F', 3, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (1, 'C', 3, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (2, 'S', 3, 'Au');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (3, 'S', 2, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (3, 'D', 1, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (4, 'S', 2, 'We');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (4, 'F', 2, 'We');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (5, 'C', 3, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (5, 'T', 2, 'We');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (5, 'D', 1, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (7, 'F', 1, 'Ch');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (7, 'R', 2, 'We');

insert
into Achievement (C_id, S_Code, score, test_T_id)
values    (8, 'B', 1, null);

