---
title: "Data and Network Security"
author: [Jordan Pyott]
date: "2021-05-06 17:02"
subject: "COSC362"
lang: "en"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
---

\newpage

## Course Information

**Lecturers Details**

- Lecturer: Dr. Clementine Gritti
  * Office: Erskine 304
  * Email: clementine.gritti@canterbury.ac.nz
- Tutor: Ryan Beaumont
  * Email: rbe72@uclive.ac.nz

**Other Information**

- Labs and Quiz's will be available on learn
- Textbooks
  * Cryptography and network security : principles and practice, William Stallings, 5th edition
    + This course is inspired from this book as the bulk of the course
      is founded in cryptography.
    + The exam will only be on content in the slides not from the book
  * Computer security : principles and practice, William Stallings and Lawrie Brown, 3rd edition

![Timetable](./Diagrams/timetable.png)

### Assessment

1. Labs (10%) - attendance and participation:
  * Labs are done individually but you are encouraged to discuss and share with your peers (you are allowed to see each other during labs).
  * Attending one lab each week over the semester automatically gives you full mark: – The tutor will assess your attendance.
  * If you cannot attend one lab session, then a report (along with a justification of student absence) will be required and assessed: 
    - The report needs to be submitted by one week after the missed session.
    - Example: if you miss Tuesday lab on Week X then you are asked to submit a report by Tuesday of Week X+1. 
    - The report needs to be sent to *both* the lecturer and the tutor.
2. Weekly quizzes (20%):
  * They can be found and done on LEARN.
  * 9 quizzes in total.
  * Each quiz contains 10 questions. Each question contains 4 choices such that only one choice is correct.
  * 2 attempts per quiz, such that the highest grade is taken into account.
  * A quiz is given on Friday of Week X, and should be done before Friday of Week X+1 (except for the one released just before the break):
3. Assignment (20%):
  * *Deadline*: 17 September 2021.
  * Small exercises on what has been covered so far.
  * The assignment will be released on LEARN on 20 August 2021. 
  * Your report should be uploaded to LEARN.
4. Final exam (50%)
  * 3-hours duration
  * 25 multiple-choice questions
  * 5 open questions, such that if additional information is needed to solve the problem then it will be provided.
  * Covers all content from all lectures study *definitions, mechanisms, processes*
    * Not expected to remember the code of each standard (e.g. RFC1234)

## Lectures

### Lecture One - Course Introduction

- All materials will be found on learn, including lectures, labs, quizzes
and assignments.
- Course outline available
- Labs must be done in person or a report *will not get full marks if do not attend*
- Labs start next week
- Weekly quizzes go over two lectures each *multi-choice*
- Midterm and final will all be entirely open questions

**Why do we need cyber security**

- Privacy
- Security
- Risk management

**Famous recent attacks**

- Dark hotel attack
  * Targeted phishing attacks using spy-ware
  * Infiltrating guests computers through WIFI networks at hotels
  * Loss of confidentiality
- POODLE attack
  * man in the middle exploit
  * Communications can be decryped and exploited
- EncroChat
  * A communications network and service provider
  * Infiltrated by police in 2020
- WannaCry
  * Loss of availability
  * stolen government hacking tools
  * Worm encrypting files on computers hard drive
    + Was a form of ransom-ware
- Botnet
  * Botnet attacking IoT devices with default admin credentials
  * DDos
  * Loss of availability

Because of these attacks, some users have lost confidence in the service
provided not storing/selling data.

**Course Focus**

- Cryptography as a foundation for information security
- Applications of cryptography
- History of cryptography
- Modern cryptography
  * Block ciphers, stream ciphers
  * public key crypto
  * Hashing and MAC
- Some mathematics
  * Modular arithmetic
  * Number theory
  * Elliptic curves
- Using all of the cryptography
  * Public key infrastructure
  * Secure email
  * TLS (HTTPS)
