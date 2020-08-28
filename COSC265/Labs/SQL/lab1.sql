drop table registration;
drop table color;
drop table owns;
drop table vehicle;

create table VEHICLE
(plates varchar(6) not null primary key,
year char(4) check (year between '1900' and '2019'),
eng_no varchar(9) not null unique,
ch_no varchar(7) not null unique,
type char(1) check (type in ('p','m','t','r','l')),
make varchar(10),
model varchar(10),
foreign key (make,model) references vehicle_type);

create table OWNS
(plates /* Owner's plates number */ varchar(6) not null references vehicle,
ownerid /* Owner's id number */ char(8) not null references owner,
purchase_date /* The date of purchase */ date,
drr /* The mileage */ char(6),
DateSold /* The date the vehicle was sold */ date default null,
primary key (plates,ownerid));

create table COLOR
(plates /* The plate number */ varchar(6) not null references vehicle,
color /* Color of the vehicle */ varchar(10) not null,
primary key (plates,color));

create table REGISTRATION
(plates /* Plates */ varchar(6) not null references vehicle,
emp /* IRD of the employee who registered the vehicle */ varchar(10) not null references employee,
reg_org /* Organization number */ varchar(10) not null references reg_org,
reg_date /* Registration date */ date not null,
country /* The country */ varchar(10),
drr /* mileage */ char(6),
amount /* the price */ number,
primary key (plates,emp,reg_org,reg_date));



/*Data for the VEHICLE table */
insert into vehicle values('QJD123',2003,1686617,655239,'p','ford','telstar');
insert into vehicle values('JS2938',1975,3857364,36333,'p','ford','telstar');
insert into vehicle values('JJ3847',1985,3847523,82736,'t','VW','golf');
insert into vehicle values('OZ8347',1991,2948573,84723,'p','mazda',323);
insert into vehicle values('PP3958',1995,9385734,82222,'p','mazda',121);
insert into vehicle values('PA9485',1994,1928434,29384,'p','daihatsu','charade');
insert into vehicle values('TX9283',1993,9287323,44735,'p','ford','telstar');
insert into vehicle values('DBA256',2012,7918189,11122,'p','honda','jazz');
insert into vehicle values('JAL264',2006,8928382,22322,'p','honda','civic');
insert into vehicle values('GRW858',2017,9928456,33434,'t','honda','accord');

/*Data for the OWNS table */
insert into owns values('QJD123','BA789256','15-mar-2003',20,'15-jul-2011');
insert into owns values('JS2938','HD293847','02-mar-75',100,'15-apr-2003');
insert into owns values('JJ3847','HD543235','17-may-85',1573,'17-may-97');
insert into owns values('OZ8347','FF849583','15-sep-91',294,null);
insert into owns values('PP3958','HA385767','08-aug-95',903,'19-sep-2009');
insert into owns values('PA9485','UJ203954','31-mar-96',45,'13-mar-99');
insert into owns values('TX9283','HD543235','14-nov-95',28721,'15-feb-2003');
insert into owns values('TX9283','HD293847','15-feb-2003',92870,null);
insert into owns values('PA9485','GG847264','13-mar-99',11920,'27-nov-2006');
insert into owns values('JJ3847','HA928375','17-may-97',45736,'27-aug-2008');
insert into owns values('JS2938','IA192837','15-apr-2003',55612,null);
insert into owns values('JJ3847','BA789256','27-aug-2008',155736,null);
insert into owns values('PP3958','FF849583','19-sep-2009',195503,null);
insert into owns values('QJD123','HD543235','15-jul-2011',65499,null);
insert into owns values('PA9485','IA192837','27-nov-2006',12920,null);
insert into owns values('DBA256','GR153856','14-aug-2017',31350,null);
insert into owns values('JAL264','DB125699','5-mar-2019',2018,null);
insert into owns values('GRW858','JA264818','27-feb-2018',81456,null);


/*Data for the COLOR table */
insert into color values('QJD123','black');
insert into color values('JS2938','red');
insert into color values('JJ3847','blue');
insert into color values('OZ8347','green');
insert into color values('PP3958','white');
insert into color values('PP3958','blue');
insert into color values('PA9485','yellow');
insert into color values('TX9283','red');
insert into color values('DBA256','white');
insert into color values('JAL264','navy');
insert into color values('GRW858','violet');


/*Data for the REGISTRATION table */
insert into registration values('JJ3847',21321322,1352,'17-may-85','Japan',15736,84.25);
insert into registration values('JAL264',21321322,1352,'5-sep-2013',null,79256,165.35);
insert into registration values('JAL264',91837243,1303,'5-sep-2014',null,90018,150.35);
insert into registration values('GRW858',91837243,1303,'15-apr-2018',null,99560,292.70);
insert into registration values('PA9485',38473342,1352,'31-mar-94','NZ',1920,184.90);
insert into registration values('QJD123',21321322,1352,'15-mar-2003','NZ',20,175.95);
insert into registration values('JAL264',91837243,1303,'5-sep-2018',null,169018,350.35);
insert into registration values('TX9283',38473342,1352,'17-nov-95','NZ',28943,150.55);
insert into registration values('PP3958',21321322,1352,'08-aug-95','NZ',903,303.15);
insert into registration values('JAL264',91837243,1303,'5-sep-2009',null,42180,150.35);
insert into registration values('JS2938',91382743,1303,'15-apr-83','Japan',55612,101.15);
insert into registration values('OZ8347',91837243,1303,'25-sep-91','Japan',2948,211.35);
insert into registration values('JJ3847',91382743,1303,'29-nov-94',null,25253,224.70);
insert into registration values('JJ3847',91382743,1303,'29-nov-93',null,17253,284.70);
insert into registration values('QJD123',21321322,1352,'13-mar-2004',null,3150,185.95);
insert into registration values('JJ3847',91382743,1303,'30-nov-96',null,75253,284.70);
insert into registration values('JJ3847',91382743,1303,'29-nov-95',null,56253,184.70);
insert into registration values('QJD123',21321322,1352,'03-mar-2005',null,6150,195.95);
insert into registration values('PA9485',38473342,1352,'31-mar-95',null,31920,154.90);
insert into registration values('QJD123',21321322,1352,'11-mar-2006',null,16150,195.95);
insert into registration values('JAL264',21321322,1352,'5-sep-2006',null,2018,150.35);
insert into registration values('PA9485',21321322,1352,'31-mar-96',null,43920,124.35);
insert into registration values('QJD123',21321322,1352,'09-mar-2007',null,26150,195.95);
insert into registration values('PA9485',38473342,1352,'13-apr-97',null,51920,231.30);
insert into registration values('QJD123',21321322,1352,'09-mar-2008',null,26150,195.95);
insert into registration values('TX9283',21321322,1352,'15-feb-97',null,2870,250.00);
insert into registration values('QJD123',21321322,1352,'09-mar-2009',null,29150,195.95);
insert into registration values('JAL264',21321322,1352,'2-sep-2008',null,25018,192.50);
insert into registration values('JS2938',91837243,1303,'02-mar-95',null,150101,121.05);
insert into registration values('QJD123',21321322,1352,'10-mar-2010',null,49150,185.95);
insert into registration values('JS2938',91837243,1303,'02-mar-96',null,169113,114.05);
insert into registration values('JS2938',91837243,1303,'15-feb-97',null,180101,121.05);
insert into registration values('OZ8347',38473342,1352,'15-feb-97',null,2948,203.35);
insert into registration values('QJD123',21321322,1352,'15-jul-2011',null,65499,165.95);
insert into registration values('QJD123',21321322,1352,'14-jul-2012',null,71499,165.95);
insert into registration values('GRW858',21321322,1352,'15-apr-2019',null,120120,340.6);
insert into registration values('DBA256',91382743,1352,'14-aug-2017',null,31350,105.90);
insert into registration values('QJD123',21321322,1352,'13-jul-2014',null,91036,165.95);
insert into registration values('JAL264',21321322,1352,'25-aug-2017',null,144256,265.35);
insert into registration values('DBA256',91382743,1352,'14-aug-2018',null,55480,155.90);
insert into registration values('QJD123',21321322,1352,'15-jul-2014',null,91580,186.30);
insert into registration values('JAL264',21321322,1352,'5-sep-2007',null,19256,165.35);
insert into registration values('QJD123',58743344,1352,'16-jul-2015',null,102300,186.30);
insert into registration values('QJD123',21321322,1352,'14-jul-2016',null,129232,202.95);
insert into registration values('DBA256',91382743,1352,'1-aug-2019',null,55480,162.50);
insert into registration values('QJD123',91382743,1352,'13-jul-2017',null,145678,202.95);
insert into registration values('QJD123',21321322,1352,'10-jul-2018',null,152888,255.95);
insert into registration values('JAL264',21321322,1352,'25-aug-2010',null,49256,165.35);
insert into registration values('JAL264',91382743,1303,'29-aug-2011',null,55018,192.50);
insert into registration values('JAL264',21321322,1352,'5-sep-2012',null,62018,150.35);
insert into registration values('GRW858',21321322,1352,'15-apr-2017',null,81456,240.70);
insert into registration values('JAL264',21321322,1352,'25-aug-2015',null,109256,210.30);
insert into registration values('JAL264',91837243,1303,'5-sep-2016',null,123018,240.80);
