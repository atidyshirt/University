---
title: "COSC368: Humans and Computers"
author: [Jordan Pyott]
date: "2021-05-06 16:57"
subject: "COSC368"
subtitle: "The course provides an introduction to Human-Computer Interaction (HCI). HCI is concerned with understanding, designing, implementing and evaluating user-interfaces so that they better support users in carrying out their tasks. On completing the course you will have knowledge of the theoretical foundations of designing for interaction between humans and computers. You will also have practical experience in implementing and evaluating graphical user interfaces."
lang: "en"
titlepage: true
titlepage-color: "3C9F53"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
---

\newpage

# Humans and Computers

## Course Information

### Lecturers Details

- Lecturer: Andy Cockburn 
  * Email: andy.cockburn@canterbury.ac.nz
- Tutors: 
  * Katia De Lu: 
    + Email: katia.delu@canterbury.ac.nz
  * Stewart Dowding: 
    + Email: stewart.dowding@canterbury.ac.nz
- Team alias: team368@cosc.canterbury.ac.nz

### Schedule

**Topics**

- Introduction
- Models of interaction and interface technology
- The human
- Interface design
- Evaluation
- UI intellectual property

![Course Schedule](./Diagrams/schedule.png)

### Assessment Structure

- Labs (9%)
  * 1% per lab
  * Binary marking scheme - go to the lab, get full marks
- Usability analysis and storyboard (25%)
  * Wed 22nd September 5:00 pm
  * Teams of ~six, forming own groups
- Design Specification and Rationale (15%)
  * Wed 20th October 5:00 pm
- Exam (51%)
  * TBA

### Textbooks/Resources

- Designing with the Mind in Mind 
  * Based on COSC368, Old lecturers thoughts
  * Author: Jeff Johnson, Morgan-Kaufmann
- Papers on ACM Digital Library
- Other materials on Learn

## Lectures

### Lecture One - Introduction

**Technologies in this course**

- TKinter
  * Lab one - Refresher
  * Lab two - Keyboard GUI
  * Canvas & fitts law GUI
- Python

> NOTE: Labs will be used as the basis for analysis in assessments, so we need to build them

**What is HCI?**

Human computer interaction (HCI) is a discipline concerned with the design evaluation and implementation of interactive computing systems for human
use, and with the study of major phenomena surrounding them.

**What is HCI Responsible for?**

1. Learnability
2. Efficiency
3. Subjective satisfaction
4. *Memorability*
  * Mostly encapsulated in Learnability
5. *Errors*
  * Opposite of Efficiency

### Lecture Two - Goals of HCI

**Knowing the user: Preliminary Factors**

- safety considerations
- need for throughput
- Frequency of use
- Physical space, lighting, noise, pollution
- Social context
- Cognitive factors: age, fatigue, stress, focus

**Managing complexity**

- Poorly designed interfaces amplify complexity
- Well designed UI's make interfaces as simple as possible, but no simpler
- Sometimes it may be appropriate to over-simplify *cater to an audience*

**Models of Interaction**

- A model is a simplification of reality
- They are useful when they help us understand a complex artifact

**Don Norman's Model of Interaction**

- Helps understand the designer's role in creating a system that is used by a thinking person
- Generally designers have a design model that is incomplete
- Then we get a system image, that is working, but in high incite, we would have
  built it differently
- The user has a model, that is weak, we need to try to map the designers model
  with the user model to create a mapping of the system image.

### Lecture Three - The Human

**Don Norman's Execute-Evaluate Cycle**

- Execute:
  * Goal > Intention > Actions > Exeution
  * Gulf of Execution: Problem arrives when executing intention/action
- Evaluate:
  * Perceive > Interpret > Evaluate
  * Gulf of Evaluation: Problem assessing state, determining effect, etc.
**UISO Interaction Framework**

- Emphasises translations during interaction - This is a cycle
  1. Articulation: user's task language to input language
  2. Performance: callbacks, etc.
  3. Presentation: show new state
  4. Observation: interpretation
  5. Back to step one

**Mappings**

- Good mappings (relationships) between User and I/O, increasing Usability.
- We can try to allocate real world relationships by using mappings to real world items
  * We can also use spacing and different design to make things more intuative

**Affordance**

- Objects afford particular actions to users
  * Buttons afford pushing, chairs for sittings, sliders for sliding, dials for turning, handles for pulling.
  * Poor affordance encourages incorrect actions
  * Strong affordance may stifle efficiency

**Over and Under-Determined Dialogues**

- Ideally dialogue is well-determined, natural translation from task to input language
- **Under-determined** - User knows what they want to do, but not how to do it
- **Over-determined** - User forced through unnecessary or unnatural steps

**Direct Manipulation**

- Visibility of object
- Direct, rapid, incremental, reversible actions
  * This allows users to learn the interface and experiment without loss of data or risk
  * Unix's `sudo rm -rf / --no-preserve-root` is **NOT** an example of this as it is not reversible
- Rapid feedback
- Syntactic correctness
  * Disable illegal actions
- Replace language with action

- Advantages:
  * Easy to learn
  * Low memory
  * Easy to undo
  * Immediate feedback to user actions
  * Enables user to use spatial cues
- Disadvantages:
  * Consumes screen real estate
  * High graphical system requirements
  * May trap user in *beginner mode*

### Lecture Four - 

