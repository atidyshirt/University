drop table bookcopy;
drop table member;
drop table branch;
drop table author_of;
drop table book;
drop table author;
drop table publisher;
drop table student;


create table PUBLISHER
(Code char(2) not null,
Name varchar(30) not null,
City varchar(15) not null,
constraint pk_publisher primary key (Code));

create table AUTHOR
(AuthorId integer not null check (AuthorId > 0),
Lname varchar(20) not null,
Fname varchar(15) not null,
constraint pk_author primary key (AuthorId));

create table BOOK
(Book_id char(4) not null,
Title varchar(60) not null,
Publisher char(2),
constraint pk_item primary key (Book_Id),
constraint fk_item foreign key (publisher) references PUBLISHER);

create table AUTHOR_OF
(Book char(4) not null,
Author integer not null,
Sequence integer check (sequence > 0),
constraint pk_AuthorOf primary key (book,author),
constraint fk2_AuthorFor foreign key (book) references BOOK, constraint fk_writtenBy foreign key (author) references AUTHOR);

create table BRANCH
(BranchId char(3) not null,
Bname varchar(12) not null,
Address varchar(25),
constraint pk_branch primary key (BranchId));

create table STUDENT
(Lib_Id char(9) not null,
FName varchar(20) not null,
Lname varchar(20) not null,
constraint pk_student primary key (Lib_Id));

create table BookCopy
(Book char(4) not null,
Copy_Id integer not null check (Copy_Id>0),
Branch char(3) not null,
student char(9),
Due date,
constraint pk_bookcopy primary key (book,Copy_Id),
constraint fk1_bookcopy foreign key (book) references Book,
constraint fk2_bookcopy foreign key (Branch) references Branch,
constraint fk3_bookcopy foreign key (student) references student);


/* Adding data into the PUBLISHER table */
insert into PUBLISHER values('AH','Arkham House','Sauk City WI');
insert into PUBLISHER values('AP','Arcade Publishing','New York');
insert into PUBLISHER values('BA','Basic Books','Boulder CO');
insert into PUBLISHER values('BP','Berkley Publishing','Boston');
insert into PUBLISHER values('BY','Back Bay Books','New York');
insert into PUBLISHER values('CT','Course Technology','Boston');
insert into PUBLISHER values('FA','Fawcett Books','New York');
insert into PUBLISHER values('FS','Farrar Straus Giroux','New York');
insert into PUBLISHER values('HC','HarperCollins Publishers','New York');
insert into PUBLISHER values('JP','Jove Publications','New York');
insert into PUBLISHER values('JT','Jeremy P. Tarcher','Los Angeles');
insert into PUBLISHER values('LB','Lb Books','New York');
insert into PUBLISHER values('MP','McPherson and Co.','Kingston');
insert into PUBLISHER values('PE','Penguin USA','New York');
insert into PUBLISHER values('PL','Plume','New York');
insert into PUBLISHER values('PU','Putnam Publishing Group','New York');
insert into PUBLISHER values('RH','Random House','New York');
insert into PUBLISHER values('SB','Schoken Books','New York');
insert into PUBLISHER values('SC','Scribner','New York');
insert into PUBLISHER values('SS','Simon Schuster','New York');
insert into PUBLISHER values('ST','Scholastic Trade','New York');
insert into PUBLISHER values('TA','Taunton Press','Newtown CT');
insert into PUBLISHER values('TB','Tor Books','New York');
insert into PUBLISHER values('TH','Thames and Hudson','New York');
insert into PUBLISHER values('TO','Touchstone Books','Westport CT');
insert into PUBLISHER values('VB','Vintage Books','New York');
insert into PUBLISHER values('WN','W.W.Norton','New York');
insert into PUBLISHER values('WP','Westview Press','Boulder CO');

/* Adding data into the PUBLISHER table */
insert into AUTHOR values(1,'Morisson','Toni');
insert into AUTHOR values(2,'Solotaroff','Paul');
insert into AUTHOR values(3,'Vintage','Vernor');
insert into AUTHOR values(4,'Francis','Dick');
insert into AUTHOR values(5,'Straub','Peter');
insert into AUTHOR values(6,'King','Stephen');
insert into AUTHOR values(7,'Pratt','Phillip');
insert into AUTHOR values(8,'Chase','Truddi');
insert into AUTHOR values(9,'Collins','Bradley');
insert into AUTHOR values(10,'Heller','Joseph');
insert into AUTHOR values(11,'Wills','Gary');
insert into AUTHOR values(12,'Hofstadter','Douglas R.');
insert into AUTHOR values(13,'Lee','Harper');
insert into AUTHOR values(14,'Ambrose','Stephen E.');
insert into AUTHOR values(15,'Rowling','J.K.');
insert into AUTHOR values(16,'Salinger','J.D.');
insert into AUTHOR values(17,'Heaney','Seamus');
insert into AUTHOR values(18,'Camus','Albert');
insert into AUTHOR values(19,'Collins Jr.','Bradley');
insert into AUTHOR values(20,'Steinbeck','John');
insert into AUTHOR values(21,'Castelman','Riva');
insert into AUTHOR values(22,'Owen','Barbara');
insert into AUTHOR values(23,'O''Rourke','Randy');
insert into AUTHOR values(24,'Kidder','Tracy');
insert into AUTHOR values(25,'Schleining','Lon');

/* Adding data into the BOOK table */
insert into BOOK values('0180','A Deepness in the Sky','TB');
insert into BOOK values('0189','Magic Terror','FA');
insert into BOOK values('0200','The Stranger','VB');
insert into BOOK values('0378','Venice','SS');
insert into BOOK values('0797','Second Wind','PU');
insert into BOOK values('0808','The Edge','JP');
insert into BOOK values('1351','Dreamcatcher','SC');
insert into BOOK values('1382','Treasure Chests','TA');
insert into BOOK values('1387','Beloved','PL');
insert into BOOK values('2226','Harry Potter and the Prisoner of Azkaban','ST');
insert into BOOK values('2225','Harry Potter and the Prisoner of Azkaban','ST');
insert into BOOK values('2281','Van Gogh and Gauguin','WP');
insert into BOOK values('2766','Of Mice and Men','PE');
insert into BOOK values('2908','Electric Light','FS');
insert into BOOK values('3350','Group: Six People in Search of a Life','BP');
insert into BOOK values('3683','The Catcher in the Rye','RH');
insert into BOOK values('3743','Nine Stories','LB');
insert into BOOK values('3906','The Soul of a New Machine','BY');
insert into BOOK values('5163','Travels with Charley','PE');
insert into BOOK values('5790','Catch-22','SC');
insert into BOOK values('6128','Jazz','PL');
insert into BOOK values('6328','Band of Brothers','TO');
insert into BOOK values('6697','A Guide to SQL','CT');
insert into BOOK values('6908','Franny and Zooey','LB');
insert into BOOK values('7405','East of Eden','PE');
insert into BOOK values('7443','Harry Potter and the Goblet of Fire','ST');
insert into BOOK values('7559','The Fall','VB');
insert into BOOK values('8720','When Rabbit Howls','JP');
insert into BOOK values('9611','Black House','RH');
insert into BOOK values('9627','Song of Solomon','PL');
insert into BOOK values('9701','The Grapes of Wrath','PE');
insert into BOOK values('9882','Slay Ride','JP');
insert into BOOK values('9883','The Catcher in the Rye','LB');
insert into BOOK values('9931','To Kill a Mockingbird','HC');
insert into BOOK values('8092','Godel Escher Bach','BA');
insert into BOOK values('9991','Harry Potter and the Order of Phoenix','ST');


/* Adding data into the AUTHOR_OF table */
insert into AUTHOR_OF values('0180',3,1);
insert into AUTHOR_OF values('0189',5,1);
insert into AUTHOR_OF values('0200',18,1);
insert into AUTHOR_OF values('0378',11,1);
insert into AUTHOR_OF values('0797',4,1);
insert into AUTHOR_OF values('0808',4,1);
insert into AUTHOR_OF values('1351',6,1);
insert into AUTHOR_OF values('1382',23,2);
insert into AUTHOR_OF values('1382',25,1);
insert into AUTHOR_OF values('1387',1,1);
insert into AUTHOR_OF values('2226',15,1);
insert into AUTHOR_OF values('2281',9,2);
insert into AUTHOR_OF values('2281',19,1);
insert into AUTHOR_OF values('2766',20,1);
insert into AUTHOR_OF values('2908',17,1);
insert into AUTHOR_OF values('3350',2,1);
insert into AUTHOR_OF values('3683',16,1);
insert into AUTHOR_OF values('3743',16,1);
insert into AUTHOR_OF values('3906',24,1);
insert into AUTHOR_OF values('5163',20,1);
insert into AUTHOR_OF values('5790',10,1);
insert into AUTHOR_OF values('6128',1,1);
insert into AUTHOR_OF values('6328',14,1);
insert into AUTHOR_OF values('6697',7,1);
insert into AUTHOR_OF values('6908',16,1);
insert into AUTHOR_OF values('7405',20,1);
insert into AUTHOR_OF values('7443',15,1);
insert into AUTHOR_OF values('7559',18,1);
insert into AUTHOR_OF values('8092',12,1);
insert into AUTHOR_OF values('8720',8,1);
insert into AUTHOR_OF values('9611',6,1);
insert into AUTHOR_OF values('9627',1,1);
insert into AUTHOR_OF values('9701',20,1);
insert into AUTHOR_OF values('9882',4,1);
insert into AUTHOR_OF values('9883',16,1);
insert into AUTHOR_OF values('9931',13,1);


/* Adding data into the BRANCH table */
insert into BRANCH values('CEN','Central','Library Tower');
insert into BRANCH values('ENG','Engineering','Engineering Building');
insert into BRANCH values('SCI','Science','Science Block');

/* Adding data into the Bookcopy table */
insert into Bookcopy values('0180',1,'CEN','111564812','18-Oct-19');
insert into Bookcopy values('0180',2,'SCI','112348546','28-Nov-19');
insert into Bookcopy values('0180',3,'ENG',null,null);
insert into Bookcopy values('0180',4,'CEN',null,null);
insert into Bookcopy values('0189',1,'CEN','348121549','21-Nov-19');
insert into Bookcopy values('0200',1,'CEN',null,null);
insert into Bookcopy values('0200',2,'SCI',null,null);
insert into Bookcopy values('0200',3,'ENG',null,null);
insert into Bookcopy values('0378',1,'CEN',null,null);
insert into Bookcopy values('0797',1,'CEN',null,null);
insert into Bookcopy values('0808',1,'SCI',null,null);
insert into Bookcopy values('1351',1,'CEN','348121549','13-Oct-19');
insert into Bookcopy values('1351',2,'SCI',null,null);
insert into Bookcopy values('1351',3,'ENG','111564812','12-Dec-19');
insert into Bookcopy values('1382',1,'ENG',null,null);
insert into Bookcopy values('1387',1,'SCI',null,null);
insert into Bookcopy values('1387',2,'CEN','125487874','09-Jan-20');
insert into Bookcopy values('2226',1,'SCI','489456522','29-Nov-19');
insert into Bookcopy values('2281',1,'CEN',null,null);
insert into Bookcopy values('2766',1,'CEN','348121549','18-Nov-19');
insert into Bookcopy values('2908',1,'CEN',null,null);
insert into Bookcopy values('3350',1,'ENG',null,null);
insert into Bookcopy values('3683',1,'SCI','242518965','18-Oct-19');
insert into Bookcopy values('3683',2,'ENG',null,null);
insert into Bookcopy values('3683',3,'ENG','619023588','15-Oct-19');
insert into Bookcopy values('3683',4,'SCI',null,null);
insert into Bookcopy values('3683',5,'CEN',null,null);
insert into Bookcopy values('3683',6,'CEN',null,null);
insert into Bookcopy values('3683',7,'SCI',null,null);
insert into Bookcopy values('3743',1,'CEN','291795563','18-Nov-19');
insert into Bookcopy values('3906',1,'ENG','348121549','30-Nov-19');
insert into Bookcopy values('5163',1,'SCI',null,null);
insert into Bookcopy values('5790',1,'SCI',null,null);
insert into Bookcopy values('6128',1,'CEN','111564812','28-Oct-19');
insert into Bookcopy values('6328',1,'CEN',null,null);
insert into Bookcopy values('6697',1,'CEN','619023588','8-Dec-19');
insert into Bookcopy values('6697',2,'ENG',null,null);
insert into Bookcopy values('6908',1,'SCI','125487874','05-Dec-19');
insert into Bookcopy values('7405',1,'CEN',null,null);
insert into Bookcopy values('7443',1,'SCI',null,null);
insert into Bookcopy values('7559',1,'SCI','619023588','20-Jan-20');
insert into Bookcopy values('8720',1,'SCI','619023588','22-Jan-20');
insert into Bookcopy values('9611',1,'SCI',null,null);
insert into Bookcopy values('9611',2,'CEN','348121549','2-Feb-20');
insert into Bookcopy values('9627',1,'CEN',null,null);
insert into Bookcopy values('9701',1,'SCI',null,null);
insert into Bookcopy values('9701',2,'CEN',null,null);
insert into Bookcopy values('9701',3,'ENG','125487874','10-Jan-20');
insert into Bookcopy values('9882',1,'ENG',null,null);
insert into Bookcopy values('9883',1,'CEN','619023588','08-Jan-20');
insert into Bookcopy values('9931',1,'CEN',null,null);
insert into Bookcopy values('8092',1,'CEN',null,null);
insert into Bookcopy values('9991',1,'CEN','489456522','17-Nov-19');

/* Adding data into the STUDENT table */
insert into STUDENT values('111564812','John','Williams');
insert into STUDENT values('125487874','Gene','Edwards');
insert into STUDENT values('135645489','Daniel','Evans');
insert into STUDENT values('151135593','Maria','White');
insert into STUDENT values('154879887','Dorthy','Lewis');
insert into STUDENT values('160839453','Charles','Harris');
insert into STUDENT values('174454898','Scott','Bell');
insert into STUDENT values('190873519','Elizabeth','Taylor');
insert into STUDENT values('198784544','Eric','Collins');
insert into STUDENT values('112348546','Joseph','Thompson');
insert into STUDENT values('115987938','Christopher','Garcia');
insert into STUDENT values('128778823','William','Ward');
insert into STUDENT values('132977562','Angela','Martinez');
insert into STUDENT values('141582651','Mary','Johnson');
insert into STUDENT values('141582657','Stanley','Browne');
insert into STUDENT values('142519864','Susan','Martin');
insert into STUDENT values('156465461','Eric','Cooper');
insert into STUDENT values('156489494','Gil','Richardson');
insert into STUDENT values('159542516','Matt','Nelson');
insert into STUDENT values('178949844','Chad','Stewart');
insert into STUDENT values('179887494','Dorthy','Howard');
insert into STUDENT values('242518965','James','Smith');
insert into STUDENT values('248965255','Barbara','Wilson');
insert into STUDENT values('254099823','Patricia','Jones');
insert into STUDENT values('254898318','Gim','Rogers');
insert into STUDENT values('267894232','Paul','Hall');
insert into STUDENT values('269734834','Rick','Carter');
insert into STUDENT values('274878974','Harry','Watson');
insert into STUDENT values('280158572','Margaret','Clark');
insert into STUDENT values('287321212','Michael','Miller');
insert into STUDENT values('289562686','Thomas','Robinson');
insert into STUDENT values('291795563','Haywood','Kelly');
insert into STUDENT values('298489484','Lisa','Gray');
insert into STUDENT values('301221823','Juan','Rodriguez');
insert into STUDENT values('310454876','Milo','Brooks');
insert into STUDENT values('318548912','Ann','Mitchell');
insert into STUDENT values('320874981','Daniel','Lee');
insert into STUDENT values('322654189','Lisa','Walker');
insert into STUDENT values('334568786','William','Moore');
insert into STUDENT values('348121549','Trey','Phillips');
insert into STUDENT values('351565322','Nancy','Allen');
insert into STUDENT values('355548984','Tom','Murphy');
insert into STUDENT values('356187925','Robert','Brown');
insert into STUDENT values('390487451','Mark','Coleman');
insert into STUDENT values('451519864','Mark','Young');
insert into STUDENT values('454565232','Louis','Jenkins');
insert into STUDENT values('455798411','Luis','Hernandez');
insert into STUDENT values('486512566','David','Anderson');
insert into STUDENT values('489221823','Richard','Jackson');
insert into STUDENT values('489456522','Linda','Davis');
insert into STUDENT values('548977562','Donald','King');
insert into STUDENT values('550156548','George','Wright');
insert into STUDENT values('552455318','Ana','Lopez');
insert into STUDENT values('556784565','Kenneth','Hill');
insert into STUDENT values('567354612','Karen','Scott');
insert into STUDENT values('573284890','Steven','Green');
insert into STUDENT values('574489456','Betty','Adams');
insert into STUDENT values('578875478','Edward','Baker');
insert into STUDENT values('619023588','Jennifer','Thomas');


