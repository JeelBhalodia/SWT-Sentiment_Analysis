# SWT-Twitter_Sentiment_Analysis
Advanced Software Engineering Exercises

## TASK - 1
For the pet project, I have used Python language and the code is relatively small. However, if time permits I would also like to do the same thing using NLP.

Here, I have used Tweepy module to stream live tweets directly from Twitter in real-time. The tweets are visualized and then the TextBlob module is used to do sentiment analysis on the tweets. Based on certain keywords, tweets are refined and then are given a sentiment score of -1(negative sentiment), 0(neutral), 1(positive).


## TASK - 2

### 1. UML Diagrams (Atleast 3)

Here, I have attached 
+ [Class Diagram](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/UML/class_diagram.PNG)
+ [Activity Diagram](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/UML/Activity%20Diagram.png)
+ [Use-case Diagram](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/UML/Usecase_diagram.png)

I have used lucidchart and GitUML (class diagram) for the this task.

### 2. Metrics

I have used both Sonarcube and Codacy for the task.

Sonarcloud Code Qulity Badge
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=JeelBhalodia_SWT-Sentiment_Analysis2&metric=alert_status)](https://sonarcloud.io/dashboard?id=JeelBhalodia_SWT-Sentiment_Analysis2)

Codacy Code quality badge 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8d028e61c35449acad16a139efa656a3)](https://www.codacy.com/manual/JeelBhalodia/SWT-Sentiment_Analysis?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JeelBhalodia/SWT-Sentiment_Analysis&amp;utm_campaign=Badge_Grade)

### 3. Clean Code Development

I have maintained the PEP8 coding standards while developing my Project. Some of the examples are mentioned below:

+ [Naming conventions](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/screenshots/naming_conventions.PNG) for the functions: lowercase with words separated by underscore to improve readability.
+ Each [imports](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/screenshots/imports.PNG) are on the top of the file and clearly readable.
+ Keeping the functions short and simple. No more than [3 arguments](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/screenshots/less_no_of_arguments.PNG) if possible.
+ Using [exceptions](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/screenshots/exception_handling.PNG) instead of returning error codes.
+ [Tests](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/screenshots/tests.PNG) should be fast and independent.

However, these are just few examples to demonstrate. 

+ One of the [cheatsheet](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)(more like a summary) which I found helpful.

+ [Cheatsheet2](https://www.planetgeek.ch/wp-content/uploads/2011/02/Clean-Code-Cheat-Sheet-V1.3.pdf)

### 4. Build Management

I have used Github Actions for the Build Management.
Here is the [build file](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/.github/workflows/pythonapp.yml).

![Python application](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/workflows/Python%20application/badge.svg?branch=master)

### 5. Unit tests

I have created some [unit tests](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/test/test_sentiment.py) and integrated it in my project.

### 6. Continuous Delivery

I have used CircleCI tool for the continuous delivery. [![CircleCI](https://circleci.com/gh/JeelBhalodia/SWT-Sentiment_Analysis.svg?style=svg)](https://circleci.com/gh/JeelBhalodia/SWT-Sentiment_Analysis)

You can find the config.yml file [here](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/.circleci/config.yml).

The pipelines can be found [here](https://app.circleci.com/github/JeelBhalodia/SWT-Sentiment_Analysis/pipelines).
Here are all the [jobs](https://circleci.com/gh/JeelBhalodia).

### 7. IDE

I have used PyCharm Community Edition as my IDE.
Some of my favourite shortcuts are 
+ shift+ctrl+/  to  comment code with block comments or
+ ctrl+/  to  comment current line or selected block with line comments
+ shift+TAB  to  unindent selection
+ ctrl+E  to  show the list of recently viewed files
+ alt+RIGHT  to  activate the next tab

And ofc it's 'Darcula' color scheme

The only drawback (not so serious) which I faced was that it doesn't generate class diagrams unlike Professional Edition.
Also there's a [cheat sheet](https://www.shortcutfoo.com/app/dojos/pycharm-win/cheatsheet) which can be handy.

### 8. DSL

I have written a simple dsl which doesn't contribute to my project, but it's generic in nature that uses other Python source files to do some work.
+ 'src1.dsl' is the DSL source file that users write. This is not Python code but contains code written in custom DSL.
+ 'dsl1.py' is the Python source file that contains the implementation of domain specific language.
+ 'module1.py' contains the Python code that users can call and execute indirectly via DSL.

[DSL-Part 1](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/DSL/dsl1.py)

Importing a Python module dynamically at runtime using the importlib module from the standard library.

[DSL-Part 2](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/DSL/dsl2.py)

Bit more general and flexible. Instead of hardcoding the arguments, users pass any number of arguments. 

### 9. Functional Programming

+ [Final data structures](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/func_programming/data_structure.PNG)

	A persistent data structure is one in which no operations result in permanent changes to the underlying structure. It's called “persistent” because as the structure goes through successive operations, all versions of the structure persist over time.

	I have used dataframes here so that we can have a little flexibilty, unlike tuples but however the structure doesn't change.
+ [Side effect free functions](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/func_programming/pure_function.PNG)

	Pure functions do not have side effects, that is, they do not change the state of the program. Given the same input, a pure function will always produce the same output. If we like functions to be pure, then we should not change the value of the input or any data that exists outside the function's scope.

+ [Higher order functions](https://github.com/JeelBhalodia/SWT-Sentiment_Analysis/blob/master/func_programming/higher_order_function.PNG)

	Higher Order Functions either accept a function as an argument or return a function for further processing. Higher Order Functions give our code flexibility. By abstracting what functions are applied or returned, we gain more control of our program's behavior.
____________________

If the length of the code seems a bit small and my grades might affect, please click [here](https://github.com/JeelBhalodia/SWT-1920).