<center>

# COSC264 Notes

</center>

> [TOC]

### General Info About Course

Note that although a number of assessments are closed-book, we will be permitted to bring an A4 hand written sheet of paper, this can be double sided but must be *hand written*.

#### Grading
- Lab quizzes (16%)
    - Four in first term (2% each)
    - Four in second term (2% each)
- Super quiz on packet processing (7%)
    - Open during week 3
- Socket programming assignment (10%)
    - Due: Sunday, August 16, 2020, 11:59pm
- Mid-term test (25%)
  - 90 minutes
  - Closed-book, mostly electronic
  - Covers all first term content
  - Friday September 11, 2020 7:00 - 8:00pm
- Lab test(17%)
    - 60 minutes
    - closed-book
    - Friday, October 9, 7:00pm
    - Held in Jack Erskine Labs (TBC)
    - Covers material from labs in second term
- Final exam (25%)
    - 90 minutes
    - closed-book
    - time and place to be determined

> In order to pass this course, you must meet the following criteria, an average of 50%
> across all assessments, and an average mark of at least 45% on invigilate assessments 
> (mid-term, lab test and final exam).

#### Resources
- [Lecture Notes](https://learn.canterbury.ac.nz/course/view.php?id=9047&section=1)
- [Problem Sheets](https://learn.canterbury.ac.nz/course/view.php?id=9047&section=2)
- Principles of Digital Transmission – With Wireless Applications
    - Sergio Benedetto and Ezio Biglieri
- Principles of Digital Communication
    -  Robert G. Gallager
- Data and Computer Communications
    - William Stallings
- Computer Networks.
    - Andrew S. Tanenbaum and David J. Wetherall

### Introduction to Networking

#### Terminology
| Term         | Description                                                                                                       |
| ------       | -----------                                                                                                       |
| End Stations | These are the items connecting to a user ie a computer, servers etc. these are always connected to other stations |
| Network      | A loose term used in many ways, but essentially is a path for information flow                                    |
| Router       | Connects networks together so data can flow from one network to another                                           |

#### First look at the internet

**Where do routers send traffic?** 
> Routers do not normally generate any traffic of their own, they are there to connect
> networks from point to point, they make routing decisions in order to indicate where
> to send the traffic to.

**How can I connect overseas then?**
> Parts of the internet are owned by service providers. These companies own large cables 
> that go overseas to allow companies to connect their networks to the world, service
> providers sell connectivity for a price, your local internet providers will purchase
> access from the largest providers, the top level service providers tend to provide to
> each other, however this tends to not be paid for as it is a mutual benefit for both
> companies to be more connected.

### Bitwise operations

**Bitwise `AND` Operation**

The `AND` operation works by multiplying each bit in the first string to the bits in the
second string, in the python interpreter, the symbol `~` denotes the bitwise `AND`. The 
following example will multiple two binary numbers.

```python
# Here is a python example of a bitwise AND operation
binary_first = 0b0110110110
binary_second = 0b1100011101

bitwise_first_AND_second = binary_first & binary_second
print(bitwise_first_AND_second)
```
> Result: 01 0001 0100

**Bitwise `OR` Operation**

The `OR` operation works by checking if the bit is equal to *1*, if it is equal to 1 then
put 1, else put 0.

```python
# This is how to preform the bitwise function manually
output = ""
if see == 1:
    output.append(1)
else:
    output.append(0)
print(reversed(output))
```

To actually preform this in python, you would use the `|` operand to denote the `OR` bitwise
function. The following is how to preform this in python.

```python
# Here is a python example of a bitwise OR operation
binary_first = 0b0110110110
binary_second = 0b1100011101

bitwise_first_OR_second = binary_first | binary_second
print(bitwise_first_OR_second)
```
