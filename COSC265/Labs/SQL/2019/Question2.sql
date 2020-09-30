--  Query for part (a)
SELECT title, COUNT(Book_id) AS number_of_copies
FROM Book
GROUP BY title;

--  Query for part (b)
SELECT BRANCH.Bname, COUNT(*) - count(BOOKCOPY.student) AS Loaned, COUNT(BOOKCOPY.student) AS Availible
FROM BRANCH
JOIN BOOKCOPY ON (BRANCH.BranchId = BOOKCOPY.Branch)
GROUP BY BRANCH.Bname;

-- Correct Query for part (b) *STILL BROKEN*
select bname, count(student) as OnLoan, count(*)-count(student) as Avail
from branch join bookcopy on branch=branchid
group by bname;

select student.fname, student.lname, bookcopy.branch, count(*)
from bookcopy inner left join student on (student = lib_id)
group by bookcopy.student, bookcopy.branch, student.fname, student.lname
order by bookcopy.branch ASC;

select Copy_id, book, branch
from BookCopy join Book on bookcopy.book = book.book_id
where (bookcopy.student is NULL AND book.title = 'The Catcher in the Rye')
order by book.book_id;


