---
title: "ENCE360: Operating Systems"
author: [Jordan Pyott]
date: "2021-05-06 16:57"
subject: "ENCE360"
subtitle: ""
lang: "en"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
---

\newpage

# Operating Systems

## Course Information

The course covers core topics.

- Introduction to operating systems
- Processes and Threads
- Pipes
- Sockets
- Deadlocks
- Files and Directories
- Input/output
- Memory management - Caches
- Memory management - Virtual memory
- Virtualisation

**Grade structure**

Standard Computer science policy applies

- Average 50% over all assessment items
- Average at least 45% on all invigilated assessment items

Grading structure for course

- Lab Test (20%)
- Assignment (20%)
- Lab quizzes (10%)
  * Weekly Quiz Assessments
- Final Exam (50%)
  * Closed book and no calculator
  * Cheat sheet Double sided A4

### Textbooks / Resources

- Modern Operating systems - Andrew Tanenbaum
- Xv6 - Online shorter method, lots of examples

> For information on these resources see the first lecture slides

## Readings

## Lectures

### Lecture One - Introduction to Operating Systems

**The beginning of computing**

- Called the Analytical engine
- Charles Babbage 1972-1871
- Digital, programmable, *Turing complete*
- Punch card IO
- Unable to be engineered
- Would be very slow
- Ada Lovelace - worlds first programmer

**1st Generation computers**

In 1945 we moved on to hard-wired machines. These were just a plugged set
of wires.

**2nd Generation computers**

Operating systems started to appear when systems were designed to be programmable,
this came with programmed batch systems, they operated with one job at a time and
had storage, this is the initial life of an operating system.

**3rd Generation computers**

- Multiprogramming
  * the ability to run multiple jobs at once
- First real operating systems
  * MULTICS/Unix/Linux, VMS and others

This bought the first initial need for security and segregation between
users on the same machine.

**4th Generation computers**

This is the first view of **personal computers**, bringing the `BASIC` interpreter
using Machine code, complexity hidden from the user, one program could be held
in memory.

Usually had ~8 kb of memory to run the entire operating system. 

Eventually got a GUI, use of mouse and the initial real world of what we call
computers, could also store multiple applications in memory at once.

Then finally, we have modern day computers

- Personal
- Multiple applications at once
- Modern OS, *(Linux, MacOS and Windows)*

**5th Generation computers**

Wearable devices, quantum computing and further AI development, we are
not there yet!

**What is in a computer?**

- CPU
- Memory
- Video Controller
- Keyboard Controller
- Optical disk controller
- Hard disk controller

This is even a simplistic model, a computer really looks like this:

![Computer Model](./Diagrams/computer-model.png)

It is extremely difficult to have to write to all sectors of this without knowing
its exact structure and expected input. This means that we need some interface to
handle this for us. Hence, **operating systems**.

**Storage hierarchy**

![Storage hierarchy](./Diagrams/storage-hierarchy.png)

In order for the operating system to work, it needs to have some method of
handling storage, and knowing where we are allowed to write to, and have some
method of creating an interface or abstraction to solve writing issues.

**What is the main purpose of an operating system?**

- Virtualization (sharing users)
  - Time (CPU)
  - Space (memory)
- Concurrency
- Persistence (I/O)
- Protection
- Hides complex details
- Protects the machine from malicious code

**Core OS concepts**

These will be expanded throughout the lectures

- Processes
- System calls and kernel mode
- Address spaces
- Files and IO
- The shell

**Typical process model**

- Processes are normal, sequencial code
- The schedular decides what runs and when
- Alternative cooperative models exists

**OS API: System calls**

![System Calls](./Diagrams/system-calls.png)

These really work because the user has no direct access to the low level routines

- OS runs in kernel mode with higher privileges
- User mode system calls execute TRAP instructions
- Hardware looks up the **Trap table** to find address

**Address spaces**

Modern operating systems have **Virtual Memory**

- Multiple programs in memory at once
- Idle memory can be paged and swapped to disk
- Give an illusion of unlimited memory (*at a price*)

**Sample exam question**

Which of the following is NOT an operating system?

- Linux
- Windows
- Android - NOT
  * Is using Linux kernel
- ROS - NOT
  * Is using Linux kernel
  * Is a set of libraries to use with an OS to make system calls
- MacOS
- DOS
- iOS
- Arduino - NOT
  * Is a package
