# Sorting Hat Quiz



**Author(s)**: Cody Bandy

**Google Doc Link**: https://docs.google.com/document/d/1hUkpndO_Y33dohdYFrD94r5aF0yBLR0EfFUOT2MJWuI/edit?usp=sharing

---

## References 

https://chatgpt.com/share/67512164-0ef0-8007-a5cc-2f10620b990f - AI assistance in helping set up the test suite.
---

## Milestone 1: Setup, Planning, Design

**Title**: `Sorting Hat Quiz`

**Purpose**: `Ask the user multiple choice questions to determine a result, then use turtle drawing to display which house they belong to.`

**Source Assignment(s)**: `T01 (conditionals), T02/03 (turtles), T10 (classes), T12 (GUI)`

**CRC Card(s)**:
  
![CRC of class one.](image/crc1.png)
![CRC of class two.](image/crc2.png)
![CRC of class three.](image/crc3.png)
![CRC of class four.](image/crc4.png)

**Branches**:

```
    Branch 1 name: bandyc
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    I would say I am about 50% done with the project overall. I feel I am on track to complete the project on time.
    I have a clear idea of where I need to do. I have most of the logic figured out, but I still need to figure
    out the specifics of the GUI to get it looking the way I want it to.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `90%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    I am feeling very confident. My code is almost completely finished besides going in and making the GUI look
    more visually appealing and adding some more questions for the quiz. I had some trouble figuring out how to
    do the test suite without relying on user input, which I had to defer to ChatGPT for help with. As for
    strategies, I just need to make sure to finish these touch ups and go over everything some more and look
    for flaws in the program, even if they aren't caught by tests.
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions
Read the question presented and pick from the four answers displayed that which most aligns with you. Click the bubble
next to your chosen answer and then click the green next button. Continue to do this until you have answered 10 questions.
Then, a new window will appear and a turtle drawing will show you your result.

### Reflection
I selected this project because I thought it would be a fun project that isn't terribly complicated but still required a
rounded knowledge of many of the aspects of the course. I also wanted it to be themed after something that holds a
special place in my childhood and which I have a great nostalgia for, which is Harry Potter. Putting those two ideas
together, I settled on something that addresses one of the most iconic aspects of the franchise, the sorting quiz. Most
people who know of Harry Potter know what the sorting quiz is, and have most likely taken one themselves online in the past.
I wanted to take my own shot at that, and so this project idea was born.

The general design ideas are more or less intact from the beginning of the project to the end. After all, it is a
multiple choice quiz, there aren't many ways to reinvent the wheel when it comes to something like this. The parts that
did change were the more specific details, mostly relating to the GUI side of things. The initial design of the GUI was
barebones, just enough to get the info on the screen and spit out a result in a turtle screen. However, after some
revamping and tinkering with formatting throughout the quiz and the final results window, it now looks quite a bit better
with larger fonts, more colors, and a more uniform format throughout. The final results window had the biggest changes,
but I was not able to use copyrighted images which limited my original vision for this area.

I learned a lot from this project. I learned that getting things to look the same way on the screen that you imagine
them as in your head is difficult. For example, getting all the words in the turtle window to fit within the confines of
the borders without altering the sizes took some trial and error. I learned that planning things out in steps with a
general roadmap helps maintain focus and makes design easier. I learned that making proper use of classes is immensely
helpful in terms of organization and reuse of code. As for the hardest part of this project, it was probably the test
suite. My project relies on user input, and I could not figure out how to simulate that in unit tests or make a test suite
built around it. I eventually deferred to AI resources for this portion of the project (which was credited) but I am also
now realizing that the test suite should probably have been updated to account for the revamp in format/questions,
but I will leave that as a "wanted to do but didn't have time" and note it in the appropriate issue queue entry.

If I were to do something differently next time, knowing what I do now, I would try to spread out the process of this
project more evenly. As it stands, I did most of the work in several long sittings rather than making incremental steady
progress over time. I would also probably choose a topic that is a bit more exciting to work on. While I enjoyed the idea
of a Harry Potter sorting quiz, and I liked the process of creating the questions and the quiz logic, I did not enjoy
the GUI related processes and formatting work as much. But all in all, I still had fun working on this project and I am
satisfied with how it turned out. It may not be the most complex program, but it functions and it looks decent enough 
doing it, and that's all I can really ask for right now.