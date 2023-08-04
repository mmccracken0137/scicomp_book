#!/usr/bin/env python
# coding: utf-8

# # Basic syntax, variables, functions

# ## Introduction
# 
# In PHY 220 we'll be investigating some of the foundational principles of computer programming, specifically those which are useful in the physical sciences.  Now, you may ask yourself, "Why?"  I have a pretty good, two-fold answer for this...
# 
# 1. The study of science (as a student) and pursuit of scientific research are often characterized by doing long, difficult, or tedious calculations.  While much insight can be acheived by doing such things by hand (and we'll definitely make you do them by hand at some point), modern computation has allowed physicists, mathematicians, biologists, chemists, social scientists, and researchers in many other fields to do things that they previously thought impossibly or prohibitively time-consuming.  [There are entire fields of physics, chemistry, and biology that are possible *only* with the use of computers. (See Lattice Gauge Theory, Computational Biophysics, Genomics/Bioinformatics, etc.).]
# 1. Physics experiments are often expensive... REALLY expensive.  [*E.g.*, the Large Hadron Collider at CERN cost more than 13 gigadollars to construct and has an annual operating budget of about 1 gigadollars!]  Physics experiments often take a long time to build and perform.  [*E.g.*, planning for the next generation of high-energy accelerators began over twenty years ago and the experiments wouldn't be built (if at all) for another 20 years.]  Before investing massive amounts of capital and effort (and energy!), scientists rely on simulations of their experiments to suggest whether they are feasible and will give the desired precision or scope.  This is hard, but it's a heck of a lot cheaper (and more responsible) than dropping gigadollars on a project that *might not* work.
# 1. Science is (loosely) concerned with drawing conclusions about the Universe by considering measurements of the Universe.  We now live in an era of **BIG DATA**, volumes of information too vast for humans to process in any useful amount of time.  The only way to turn these data into knowledge and wisdom is with computers.
# 
# As such, programming is a vital part of almost all fields of scholarly scientific research and industry. 
# 
# Here's a motivational example: John A. Swanson, W&J's cool-guy benefactor, made his fortune by developing a computational suite (ANSYS) that allows designers to, among many other things, simulate and test structural properties of materials and components before they are physically prototyped.  ANSYS was a gamechanger in the world of engineering and industrial design.  Maybe you'll make something similar!
# 
# Because it is essential to modern research and industry, we have built several stages of computing education into the Physics Major.  In this course, you'll study the basics using Python, a general-purpose language.  Hopefully you'll gain an appreciation of what computers can do and how they're used by the pros.  

# 
# ## Our language of choice: `python`
# 
# Python, or more commonly `python`, is a general-purpose, object-oriented, interpreted programming language that has several benefits relevant to this course:
# 
# - It is F R E E.  You can/should install it on your personal computer.  If you are interested in doing so, get the Anaconda distribution that is maintained by Continuum.  Check out the downloads [here](https://www.anaconda.com/download).
# - Python is (relatively) simple to learn.  Most of the syntax is human-readable and intuitive (once you learn a little bit about it).
# - It's ubiquitous!  python is platform-independent (will work on almost any OS).  Even though it's simple, many people use python to do meaningful programming.  Python is also nearly ubiquitous for applications in economics, robotics, artificial intelligence, finance, computational biology, *etc.*, *etc.*, *etc*.  As such, it is VERY well documented...
# - Documentation/support network.  Many smart people use python, and the on-line community is excellent.  The answer to most of your python questions is just a Google/Yahoo/AltaVista/AskJeeves away.  (Similar to LaTeX!)
# - It has this convenient Jupyter-notebook thing.  More on that later...

# ## *The* problem of programming
# 
# One of the difficulties that students sometimes have with learning programming what I call the "WHAT THE H%&! IS GOING ON PROBLEM" (TM).  If you're new to programming and to using a computer in a meaningful way, it's difficult to form a conceptual model of what is happening where.  Here is all you need to know:
# 
# What is computer programming?
# Computer programming is the name given to the process of writing *programs* ("code") that tell a computer what to do.  Programs are written in a *language* (python is a language) and interpreted by the computer to manipulate the computer's hardware.  Learning how to program is a two-tiered process: you need to learn what types of things a computer can be told to do, and you need to learn the language ("syntax" in a given programming language) that allows you to instruct the computer.
# 
# Many parallels can be drawn between this process and human language acquisition.  Think about the steps that you had to go through to learn to speak your first language.  (If you speak more than one language) Did you go through the same steps in learning your second langauge?
# 
# That's it!  (Not really.)  If you keep this in mind, however, you can't get lost.  (Well, NOT REALLY.)  But, it's a pretty good mantra: *I'm telling the computer what to do.*

# ## Jupyter notebooks
# 
# For the first few weeks and for your final project, you'll be working partly in this integrated development environment inside of a browser.  This is called a "Jupyter notebook."  This isn't the way that most "real programmers" write code, but this will serve as a nice sandbox in which we can play and in which I can interleave comments and instructions.  There are (at least) two types of "cells" here.
# 
# - **Markdown cells** (like this one) are just text that is intended to be read.  (...As you are doing that right now.)
# - **Code cells** are `python` code that gets executed.  Code cells are usually followed by output cells.
#     
# When you want to execute a cell, you place the cursor in the cell and hit [SHIFT + ENTER].
# 
# Again, this might look a bit Mickey-Mouse-y, but it works well for getting up to speed.  I assure that in a few weeks you'll be doing some rad stuff.
# 
# An IMPORTANT thing to know is that even though you are writing and running these programs in your browser, they are manipulating the hardware of your computer.  The browser only acts as a canvas here; no networking is happening.
# 
# Python is an example of a "high-level" language, meaning that the instructions and syntax that you will type are easy to read and interpret by humans.  The python knows how to interpret these commands into instructions for the computer's hardware.  There are other languages that are "closer to the metal", but python will be better for learning the basics of what a program is and does.
# 
# ***
# 

# 
# ## Let's get started: basic syntax
# 
# A not completely terrible way to get started with programming is to learn a couple of basic syntactical structures and then solve some problems.  This is the approach that we'll use.  If you're confused/lost/perturbed/desparate, IT'S NOT YOU.  Please ask a question.  Syntax can be tough to learn, but you have to exercise to get stronger.  Pressure makes diamonds.
# 
# LET'S DO IT!

# Okay, more markdown here.  
# 
# First up, let's do some simple calculations.  Execute each of the following code cells by placing your cursor in the cell and pressing [SHIFT+ENTER].  You can modify any of these cells at any time!  Notice that code cells have numbers beside them...

# In[1]:


2 + 2


# In[2]:


3 * 2


# In[3]:


3*4*1*4*5*6/2/6/8/3*10*100


# In[4]:


2^10


# WHAT???

# In[5]:


2**10


# Oh, okay.  So it looks like the operator for "raise to the power" is [fill in this blank]//, not a caret!  We can deal with that.  
# 
# I don't know what caret does... can you figure it out?
# 
# Let's try this:

# In[6]:


29**0.5


# In[7]:


29**(0.5), 29**0.4, 29**0.3, 29**0.2, 29**0.1


# The expression in the following cell is "commented out", meaning that the \# that begins the line causes `python` to not evaluate the line.  If you run the cell as is, nothing will happen... but if you delete the \#, something *will* happen.  Give it a try!

# In[8]:


#29^0.5


# OH NUTS.  What happened?
# 
# This is the first example of what's called a run-time error.  Something about the code that we wrote above didn't work with how python knows how to interpret instructions.  In this case, the error that `python` threw 
# >`TypeError: unsupported operand type(s) for ^: 'int' and 'float'`
# 
# is pretty instructive (usually the case for python).  It seems like `^` is not a recognized operator for floats (numbers that are not integers); *i.e.*, `python` doesn't know what to **do** when you put a `^` between two floats.  Here are some similar problems you may encounter -- uncomment each and try it out:

# In[9]:


#(29


# In[10]:


#4.1.6


# In[11]:


#23 + 23598753 + a


# Ewps!  python will usually yell at you when you make a run-time error.  The really insidious errors are those that cause code to run but produce incorrect behavior.  They are harder to diagnose and fix.
# 
# * * * 
# ## Variables
# 
# So, the next step in complexity is to declare variables and use them for calculations.  Variables are quite interesting in python for quite complicated reasons.  The following statement declares the variable `a` and sets its value to `2.0e-9` (which is shorthand for scientific notation):

# In[12]:


a = -2.0*10**-9


# Note that no output is displayed here.  python did do something: it set aside some space in memory for `a` and then put the value `2.0e-9` there.
# 
# Let's check the value of `a`:

# In[13]:


print(a)


# Cool.  Looks good.
# 
# So, a single `=` is a type of operation that stores a value in a variable.  This is very similar to what you do when you do algebra with an expression like $x = 12$.  $x$ has this value in any other equations that you use later.
# 
# Let's do something more useful:

# In[14]:


press = 101300
volume = 1.12
n = 26.08
R = 8.31

temp = press * volume / n / R
print(temp)


# We did it!  Storing the values of four quantities, we were able to calculate the a fifth quantity symbolically.  Note also that the block of code above did several things in a specific order -- each line of code was a separate command, either initializing/setting a variable or doing a calculation (or printing). 
# 
# This isn't all THAT impressive, but now that we've stored these values in variables, we can use them again.  What if we have a different pressure?

# In[15]:


press = 180000

temp = press * volume / n / R
print(temp)


# So, I stored a new value in the `press` variable, but the other variable values remained the same and I could just reuse them.  This Jupyter notebook keeps information from cell to cell.
# 
# What's that you say?  You're a Fahernheit person?  OK!

# In[16]:


tempF = temp * 9 / 5 + 32
print(tempF)


# WOOP WOOP.
# 
# Make sure you take a good long look at the code two lines above and understand what's happening.  This type of syntax is going to become super important for our later work.
# 
# Okay, act cool.  I know that we're all really excited right now.  
# 
# ### Caveat:
# Once a variable is declared, it exists for the rest of a program (unless it's inside a loop; more on that later).  So, you don't want to reuse variable names unless you have a really good reason for doing so.
# 
# This also makes the order in which you evaluate cells VERY important!  The cell numbers that appear beside code cells are useful if your code is ever behaving strangely.
# 
# ***
# 
# ## Functions
# 
# Wouldn't it be "cool" to be able to use these variables more efficiently?  One can do so by declaring functions.  I'm going to write a function that calculates the temperature of an ideal gas with a pressure and volume value that are supplied by the user:

# In[17]:


def ideal_gas_temp(press, vol):
    n_moles = 26.08
    num = press * vol
    denom = n_moles * 8.31
    return num / denom


# NB: the meat of the function definition is indented to the right.  Indentation is very important in python, and one must take care to do it properly.
# 
# Now we can use this function as many times as we want!

# In[18]:


ideal_gas_temp(101300, 1.12)


# In[19]:


ideal_gas_temp(200000, 1.12)


# In[20]:


ideal_gas_temp(80000, 0.08)


# ***
# 
# ## A taste of loops
# 
# At this point, you're probably not very impressed.  I don't blame you -- we've basically just made your computer function like a $10 calculator.
# 
# One of the things that computers are really, really useful for is mindless, repetitive tasks.  We can make computers do this (they aren't unionized) using *loops*.
# 
# There are several ways to control loops, referred to as *control structures*.  In this lesson, we'll introduce definite loops, and we'll expand on control structures in the next lesson.
# 
# ### Definite Loops
# 
# The first control structure that we'll use is the `for` loop.  A `for` loop performs the tasks inside of the loop FOR (get it?) a fixed number of times.  The syntax for writing a `for` loop in python looks like this:

# In[21]:


for i in range(10):
    print(i)


# Yes, I know.  It's very impressive that I taught this computer how to count to 9.  That's why I have a PhD.
# 
# Note that there is a colon (`:`) and indendation in this syntax.  The colon works like it does in english syntax:
# 
# "Hey, computer, do the following things: print 0, print 1, print 2, print 3, ..."  Notice that the command in the loop isn't changing; rather, it's the value of the variable `i` that is changing!
# 
# The indentation tells python what instructions happen "inside" the loop.  The first line that's not indented is not part of the loop.
# 
# I wonder what this `range()` thing does???  Now would be a good time to show off some of `python`'s excellent online documentation!
# 
# ***
# 
# This looks really dumb, but it's a very useful structure if we add calculation to it.  For example, we can sum the numbers from 0 to 2022:

# In[22]:


sum = 0
for i in range(2023):
    sum = sum + i  

print(sum)


# Here's another common sum!

# In[23]:


summation = 0
for i in range(10000):
    summation = summation + 1/(i+1)**2
    
print(summation)


# Or we can list some terms from a geometric series of 2:

# In[24]:


for i in range(20):
    print(2**i)


# `for` loops are an implementation of what we call a **Definite Loop**.  "Definite" here means that the loop executes a definite, pre-defined, explicity stated (hard-coded) number of times.
# 
# These aren't particularly enlightening problems, but they would be annoying to do without a computer.
# 
# The way that the loop executes is actually kind of interesting, but we'll have to wait until our next lesson to get into this.

# Nice.
# ***
# ## In summary  
# Now you know what you need to know to get started.  There are homework problems.  Do them in chunks.  Don't try to write a whole program all at one time.
# 
# Please, please, please try to write each problem's solution in a cell (or set of cells) and give the reader direction/explanation in markdown cells.  Markdown is really great once you get familiar with it.  Please make your variable names helpful and be careful not to reuse variable names unless you mean to!
# 
# Here are some problems on which you can cut your teeth before you begin the hand-in homework:
# 
# * * *
# 
# ## Problems
# When it comes to programming, the most learning happens when you *do* to the programming!  The problems at the end of each lesson are designed to get you flexing those `python` muscles!  
# 
# (If you're taking this as the PHY 220 course at W\&J College) Please begin each problem in a separate pair of markdown and code cells below.  (You'll have to create the cells.)  In the markdown cell, give the problem number and a brief description of how you coded up your solution.
# 
# ### Regulars
# 1. Define a function that takes in a single value, x, and returns the value of the function 
# \begin{equation}
#   f(x) = 4x^2 - 6x - 1.5
# \end{equation}
# Apply this function to the values $-2.0,\, -1.99, ...,\, 2.99,\, 3.0$.  Print out the values of the function.  Use these results to approximate the values of $x$ for which $f(x) = 0$.
# 1. Print out the products in the multiplication table of numbers between 11 and 20.
# 1. Write a function `factorial(n)` that computes the factorial of an input value `n`. Note that there is a really "cute" way to do this... but it will take an enormous amount of time to run for modest numbers (say, 4 or more digits).  Don't do it that way!  Your program should run pretty quickly for numbers up to 6 digits.
# 1. Recall or learn that the exponential function is commonly *defined* by the series expansion 
# \begin{equation}
#   e^x = \displaystyle\sum_{j=0}^{\infty} \frac{x^j}{j!}
# \end{equation}
# where the "!" means factorial.  Write a short program that approximates $e = e^1$ with the first ten terms in the sum.
# 1. Let's say that I get \$100 and deposit in the bank at a *montly* interest rate of 1.8\%.  What will the value of this investment be after 10 years?  Write a program that calculates this!
# 
