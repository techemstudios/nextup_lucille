# Intro to Computer Science: Game Design - NextUp  

### Introductions

* Name
* Age
* Grade
* Experience
  - Any programming/coding experience?

### Objectives
##### What We'll Learn

#### Core Computer Science Concepts

* Computational Thinking
  * Decomposition
    - Decompose: break down: divide & conquer
    - Break down a problem into smaller problems
  * Generalize
    - Be able to see the big picture
    - See how the smaller tasks make up the larger task
  * Recognize Patterns
    - Look for familiar things
    - Be able to see parts that repeat
    - Don't Repeat Yourself --> **DRY**
  * Algorithm Design
    - Make a plan to tackle the problem
    - Carry out the plan


* Abstraction
  * Mental model, or way to think about something
    - Focus on what needs to be done in the moment
    - Leave only the information we need, to complete our goal


* Object Oriented Programming
  * OOP or OOD
    - Everything is an object having its own, or similar properties to other objects
    - Each object belongs to a *class*


* Development Process
**Write Simple Programs**
  * Take a systematic approach to create useful programs
    1. Analysis
    2. Specifications/guidelines
    3. Design it
    4. Implement it
    5. Test/debug it
    6. Maintain it

### How to Think
#### Like a Computer Scientist
*10 min*

Take a problem that at first, may seem overwhelming, or not "attackable" with a program, then break the problem into smaller manageable problems where we can use computation to solve. See how the smaller problems together make up the larger one. Think about computational thinking as useful ways to approach and solve problems using these steps: decomposition, generalization, recognize patterns, make plan (or algorithm) and carry it out.

Example, Clean the Whole House problem.

### What is Computer Science

Not just the study of computers. Really, it is the study of what can be computed. A major part of computer science is to design a solution, or step-by-step process for reaching a goal, design an algorithm, much like designing a recipe. And more...

### What are Computers?

Computers today, are devices that store and manipulate information and can do this because of programs. When we put info into a computer, it transforms the info into new, useful forms. Computer can then output or display the information we put into it.

### Quick Computer History

*10 min*

How far we've come. Early computers were tools (or mechanical devices) people used to help them calculate math problems. A modern computer is a device that can be programmed to perform a task. From Talley Sticks, to the Babbage Machine --end with Ada Lovelace, recognized as the first computer programmer.

Difference between hardware and software.

### What is a Computer Program?

*5 min*

Simply a set of instructions written by humans that causes the computer to perform some action. Coding and programming are synonymous.

Discuss difference between Hardware and Software.

### Out-of-Seat Programming Exercise

*5 - 10 min*

Pick four volunteers to form two groups. Each group has a designated programmer and robot. Have each group stand in same area of the classroom. Point out a place in the room to be a destination. Explain that the programmer needs to give their robot step-by-step to get to the destination by telling the robot to walk forward (x amount of steps) or turn (90 degrees, left or right). The robot can only follow the directions given by their programmer.

                  Go Forward 3 steps
                  Turn left 90 degrees
                  Go forward 5 steps
                  etc.

Ask the class, which group was more efficient (the least amount of steps).

***

## Code

*5 min*

Code lets you communicate! In general, *code* is a system for transferring information. People use code to communicate with another, and between a person and a machine. Examples:

* Morse
  - light (flashlights, sun & mirrors, etc.)
  - sound
  - dots & dashes (telegraph machines)
* Braille
* Human Languages
  - sign
  - speech
  - written
  - shorthand (stenography)
* Computer languages


### How Computers Manage Information

*10 min*

Computers *speak* using binary; where only the digits 0 and 1 are used. Zero is "coded" to mean OFF, one is "coded" to mean ON. Relate to a light switch.

Use the whiteboard to explain how computers translate numbers we use, decimal number system into the binary number system --by explaining the difference between the two by focusing on the place values.

Decimal numbers use a **Base 10** system, meaning it uses a total of ten digits:

                    0 1 2 3 4 5 6 7 8 9

Binary numbers use a Base 2 system, two digits:

                    0 1

### Binary Flashcards

*10 min*

An all class activity to visually see how the binary number system operates by practicing a method that converts decimal numbers to binary. Ask for five volunteers. Give each volunteer a big binary flashcard (dark side of cards facing the class). Arrange the students to be in correct place value order. Write the number one on the board, use the cards and input from the class to have each volunteer flip the correct cards (turn "ON") to collectively show the number, one in binary. Do this for the numbers, 2 - 10. The class should progressively get quicker.

### Python

There are tons of different programming languages out there. We will learn how to write code in the Python programming language, an easy to read, understand and write language.

| Py Concepts  |
|--------------|
| Data Types   |
| Variables    |
| Expressions  |
| Statements   |
| Functions    |
| Loops        |
| Conditions   |
| Objects      |
| Classes      |

***

### Getting Started with Chromebooks (trusty)

```bash
mkdir your_name
geany helloworld.py
```

#### HelloWorld.py

Go over data types: strings, integers (INT), floats (FLOAT), boolean (BOOL). *see notes.py*  

### Simple Calculator  

Finish creating a simple calculator in Python. Walking through step-by-step, starting with first variables with input:  

```python  
number1 = int(raw_input("Give me a number"))
number2 = int(raw_input("Give me another number"))

```  

### Random Number Game  

Go through a simple interactive random number game, starting with what is needed for this type of program, i.e. computer chooses from a range of numbers, place that random number into a variable, user-computer interaction (input), get the computer to check the user input to the random number chosen, keep the game alive with a simple while loop.  

### Pygame: Getting Started  

Creating a whole game using pygame can be daunting. First walkthrough creating a simple game from scratch, touching on the *bone structure* (or skeleton) to get a python program using pygame up and running. A first example can be execution of a simple pygame window, modify the background, display a picture object, have the picture object "bounce" around, then onto controlling the object with keystrokes. Reference the Development Process of the Intro to Computer Science Readme, found in this repo. The process can easily be tweaked to fit the initial specs for designing a simple pygame.  

### Pygame Walkthroughs  

Already-made games using pygame; however, with missing key points of code.  

### Computer System Layers
#### Abstraction

[Layers of Computer System Activity](https://github.com/techemstudios/nextup_lucille/blob/master/mini_lessons/computer_system_layers.pdf)

*15 - 20 min*

When we are working in one layer, we do not need to concern ourselves with the information in the surrounding layers. This way, we can just focus on what needs to be done in the moment. Think of abstraction as a mental model; a way to think about something. Have the unnecessary details hidden, so we can leave only the information we need to complete our goal.

Abstraction Examples:

* A Person Driving a Car
  - The only thing they need to focus on is the road ahead.
  - It is unnecessary to worry about details of how the engine or electronics of the car work.

* Fast Food Restaurant
  - At many restaurants, the names of meals have corresponding numbers.
  - The food prep has been trained to recognize the meal number, not worry about the full name.

### Object Oriented Programming

As we talked about decomposing (divide and conquer) and generalization (seeing the big picture) in computational thinking, object oriented in a nutshell is to look at the interaction of simple *objects*, as being part of a complex system. Each object does something, it has its own set of properties and attributes (things it can do) and belongs to a *Class*. Let's look at an example of a dog named, Scrappy. We can say, Scrappy is a specific individual in a larger class, Dogs. In Object Oriented terms, Scrappy is a particular *instance* of the dog class. Since Scrappy is part of the dog class, we can assume certain things about him. Scrappy most likely has four legs, a tail, a wet nose, an age, and can bark. Now take a dog named, Lassy. She will have similar characteristics, but may only differ in behavior, size, or color. So, every object is an instance of some class. The class describes the general characteristics (or properties) an instance will have. The instance of the class will hold more specific properties and attributes.
