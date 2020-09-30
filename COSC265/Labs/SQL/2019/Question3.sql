-- Part (a)
create view Availible_Books
AS select *
from bookcopy
where student is null;

-- Part (b)
update bookcopy
set student = (select lib_id from student where lname='White' AND fname='Maria'),
due = add_Months(sysdate,2)
where copy_id=1 and student is null and book=(select book_id from book where title='Catch-22') and student is null;

-- Part (c) *Triggers (complex af)
