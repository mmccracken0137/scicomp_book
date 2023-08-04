#!/usr/bin/env python
# coding: utf-8

# # Types, random numbers, lists, dictionaries

# ### Recap
# 
# Let's just take a moment to remind ourselves how far we've come.  Here are some of the many things that we know how to do already:
# - basic mathematical operations
# - function definition
# - iteration and recursion with loop control structures `for` and `while`
# - keeping track of variables outside of loops (i.e., counting and summing)
# - function definition and using function *inside* of loops
# - conditionals with `if`, `else`, and `elif`
# 
# ### Motivation
# 
# I mentioned at the beginning of the class that one of the uses of computation in the physical sciences was for simulating experiments or apparatus that are prohibitively complicated.  It's important to note that studying a simulation is **not** the same as studying the "real world" -- the behavior of the simulation will depend on our current understanding of the laws that govern the real world, and these may not be correct!  Still, simulations are very useful for hypothesis testing.  To that end, check this out:
# - Cue evolution simulation code.  What hypotheses can we test? (Note: If you're not actually enrolled in the course, you won't get to see this!  The demo is similar-ish to David Randall Miller's work [here](https://www.youtube.com/watch?v=N3tRFayqVtk).  Very cool!

# ### Types and casting
# 
# When we use a computer to do a calculation, the quantities input and output quantities need to be stored/accessed by the computer.  **How** the computer does this depends on what **type** of quantity we're storing.  "Type" is an important concept in computer science.
# 
# We have so far encountered a few different types of quantities that `python` know about:
# 
# #### `int` --> Integers 
# 
# Integers can be signed (positive or negative (or 0))

# In[1]:


a = 4
b = -2
c = 180753806735751753
d = -200000000000000000000000000000000000000000000000000000
print(a, b, c, d)


# #### `float` --> Floats 
# 
# Floats are real numbers.  They can be expressed in regular decimal form or in scientific notation.

# In[2]:


e = 2.71828
f = -358735.3582636827067923067236e-10
g = -2.0e10
print(e, f, g)


# #### `bool` --> Booleans 
# 
# Booleans are the outcomes of logical operations.  There are only two boolean values: `True` and `False`.  When we implement comparison operators, the outcomes are booleans.

# In[3]:


h = True
i = False
j = 1 == 1.00000000000000000001
print(h, i, j)


# #### `string` --> Strings
# 
# Strings are... um... strings of alphanumeric characters.  We've used strings a little bit in our `print` statements.  Strings are initialized with either quotes (`"   "`) or apostrophes (`'   '`).

# In[4]:


k = "Mikey"
m = 'likes'
n = 'bikes'
print(k, m, n)


# ***
# 
# There are several other data types in `python`, some of which we'll encounter later.
# 
# You may wonder why this is necessary.  (Do you?)  There are two reasons why type is important:
# 
# **First**, in order to make efficient use of memory, the computer stores/accesses different types of data differently.  For example, there is a maximum size real number that `python` can handle:

# In[5]:


a = 2.0e309
print(a)


# Haha, oops.  This is less of an issue these days, as computer memory and speed are essentially infinitely larger than they were in the early days of computing.  
# 
# **Second**, what types of operations can be done with a piece of data depend on what type of data it is!  Most programming languages have built-in rules that prevent you from doing something nonsensical.  For example, the following operations are allowed:

# In[6]:


print(a + e)
print(b / f)
print(k + " " + n)
print(h and j)


# The following is not.  Uncomment it, and give it a whirl!  Can you decypher what the error message?

# In[7]:


#a + k


# `python` handles all of this by treating each value as an instance of a *class*; we'll come to this much later on.
# 
# ***
# 
# What about the following:

# In[8]:


var1 = 62
var2 = True
print(var1 + var2)


# What the WHAT!?
# 
# `python` is what's called a *dynamically typed* language, meaning that it/you can change the type of a variable on the fly.  So, when we ask `python` to add `var2` to an integer, `python` *interprets* `var2` in a way that seems reasonable to it.  In fact, most languages have this equivalence between the booleans and integers: `True` --> 1, `False` --> 0.
# 
# Another consequence of dynamic typing is that if I initialize a variable as a certain type, the type can changed based on what I do with the variable.  Let's use the `type()` function to check the type of a variable:

# In[9]:


var3 = 2
print(var3)
print(type(var3))
var3 = var3 + 0.1
print(var3)
print(type(var3))


# In most implementations, this feature of `python` allows us to be a bit careless/sloppy with quantities.  Yay!  But, there are instances where this sloppiness could cause problems.  Boo!
# 
# One last feature having to do with types.  We can actively change the type of a quantity by *casting* it to another type.  We do this with functions named after the various types. There's a lot of interesting stuff that goes on behind the scenes when casting, but we'll ignore this for now.  Check these operations out:

# In[10]:


var4 = 432
print(var4, float(var4))
print(var4, str(var4))
print(var4, bool(var4))
print()

var5 = True
print(var5, int(var5))
print(var5, str(var5))
print(var5, float(var5))
print()

var6 = 2.6835
print(var6, int(var6))
print()

var7 = "yowza"
print(var7)
#print(int(var7)) # this will fail... why???


# Note that casting a `float` to an `int` has a potentially useful behavior!
# 
# ### Random number generation
# 
# Computing has allowed us to make amazing progress in the statistical sciences.  Generating large random or pseudo-random datasets to study is difficult.  In the old days, if I wanted to investigate the large-scale/statistical properties of something like a game of blackjack (you know, for cheating reasons), I had to actually *deal* many games of blackjack.  Ugh!  Gross.  That would take so much time!  With computers, I can generate millions of blackjack hands according to the deck properties and history with a bit of sly programming.  This hinges on a) the computer's ability to do loops and b) the computer's ability to generate random numbers.
# 
# There are several Python libraries that provide random number generation.  We learned in Lesson 1 that a *library* is a bit of code that Python is able to use (almost like a book of extra knowledge), but that python doesn't pre-load.  In order to have access to the built-in stuff in the random number generation library, we need to tell Python to load it before we do any calculations.  
# 
# This process is analogous to the way that humans work.  Pretend that you and I are going on a camping trip on which we'll need to defend ourselves from bears.  You'll need to learn the skills before we go.  You *are capable* of doing it, you just don't know *how* to do it yet.  SO!  Before we leave and start camping, I ask you to go to the library and read the book "HOW TO DEFEND ONESELF FROM BEARS" to load the knowledge into your brain/mind.  After you do that, I can call on you to execute many bear-defense strategies: run, jump, climb tree, bear headlock, play dead, *etc*.
# 
# Okay enough goofing around.  Here's an example:

# In[11]:


import random as rand # this line adds the random 
                      # module and gives it a shorter handle 

a = rand.random()
print(a)


# In the first line, I imported the `random` module and called it something shorter, `rand` (a nickname of sorts so that I don't have to type as much).  In the second line, I told python to access the `random()` function of `rand`.  This function evidently generates a random number.  Execute the above a few times to see how the random number varies.
# 
# The random module has LOTS of features in addition to `random()`.  It's quite sophisticated.
# 
# Let's put `random()` inside of a loop to generate a whole mess of numbers:

# In[12]:


for i in range(20):
    num = rand.random()
    print(num)


# It looks like every time we call `random()`, it generates a new number between 0 and 1.  Good to know.
# 
# There are MANY ways to use this very simple tool.  One can transform the range of the numbers quite easily.  Here's a loop that prints 20 random numbers between -1 and 1:

# In[13]:


for i in range(20):
    rnum = rand.random()
    new_num = 2.0*rnum - 1.0
    print(new_num)


# Here's a snippet that writes a bunch of random points in two-dimensional space:

# In[14]:


for i in range(20):
    x = rand.random()
    y = rand.random()
    print("(" + str(x) + ", " + str(y) + ")")


# One can also input random numbers into a function:

# In[15]:


def parab(x):
    return x**2 - 4*x + 3

for i in range(20):
    input_x = rand.random()
    parab_value = parab(input_x)
    print(parab_value)


# These tools may all seem pretty weak, but they are the foundations of powerful techniques.  Physicists use the same fundamental processes to do things like study the performance of nuclear reactors, model galaxies, and simulate protein folding.  Generating random numbers is quite useful in studying quantum mechanics, too!  You may know that quantum-mechanical processes are non-deterministic; the outcome of a measurement is randomly selected according to the probabilities of all of the possible outcomes.  Computing has arguably allowed us to learn much about QM than we would have otherwise.
# 
# Random floats (remember what those are) are cool, but there are some systems that exhibit discrete behavior.  For example, if I wanted to write a random number generator to simulate you randomly choosing a card from a deck, I wouldn't want the outcome to be that you chose the 31.467459267th card.  That doesn't make sense.
# 
# The random module has tools for generating random integers:

# In[16]:


rand.randint(1,100)


# The above line generates a random integer between 1 and 100.  This is useful for many types of real-life decisions:
# 
# Hey, python, how many kids whould I have:

# In[17]:


rand.randint(1,100)


# Ummmmmmm, no.
# 
# Hey, python, how many tacos should I eat tonight?

# In[18]:


rand.randint(1,100)


# Sage advice.  Now you're talking.
# 
# There are lots of other things that one can do with random numbers, but it's probably best to become acquainted with the simple code and then learn more once you have a need.  Let's do a warm-up problem to get the juices flowing.
# 
# #### Warm-up problem
# Generate 100 random integers between 0 and 40 or 60 and 100 (i.e., omit any numbers between 41 and 59).  You'll probably need an if statement.  Make sure there are 100!
# 

# In[19]:


# put your work in this cell!


# * * *
# 
# ### Lists
# 
# Now that we've talked about **types** we can talk about **containers**.  Here's an analogy to motivate us:
# 
# > An egg is a type of food.  There are many different containers that we can put eggs in: an egg carton, a box, your hand, a bookbag.  These containers could also be used for other types of food.  *E.g.* I could put raisins in an egg carton, a box, your hand, ...
# 
# Most programming languages have containers for packaging collections of values.  
# 
# Probably the most useful of these in `python` is the *list*.  A list is an ordered collection of objects.  In some ways, you can think about a list as a set (if you know about sets), or as a vector (if you know about vectors), with elements that are indexed by a number.
# 
# NB: In many other languages, similar objects are called *arrays*.  You instructor may accidentally call pyhton lists "arrays".  We'll encounter python arrays soon, and you'll see the differences.
# 
# The most basic way to initialize a list is the following:

# In[20]:


primes_lt20 = [2, 3, 5, 7, 11, 13, 17, 19]


# Lists are a big deal in python, and the language offers many ways to work with and manipulate them.  First, we can access an individual element of a list by specifying its index number:

# In[21]:


primes_lt20[4]


# This might look a little weird... after all, the 4th element of the list is 7 (7 is the 4th prime number).
# 
# The reason that this returns the fifth element in the list is that python is a "zero-indexed language", meaning that the indices of list elements begin with 0.  
# 
# Check this out:

# In[22]:


primes_lt20[0]


# OH *OKAY!*  This is one of those rules that is hard to internalize.  The indices just begin with 0 in python (and most other modern languages).
# 
# We can check the length of the list:

# In[23]:


len(primes_lt20)


# There are also a bunch of things that we can do with the index notation:

# In[24]:


primes_lt20[0:3]


# The call above returns a new list that is a subset of the original list that takes the 3 elements beginning at element 0.
# 
# You can also get the last element in the list by using the index -1:

# In[25]:


primes_lt20[-1]


# From here, you can get creative.

# In[26]:


primes_lt20[-3]


# We can also add to (append, insert) or remove from (pop, remove) a list:

# In[27]:


print(primes_lt20)
primes_lt20.append(23)
print(primes_lt20)


# In[28]:


print(primes_lt20)
primes_lt20.insert(3,301)
print(primes_lt20)


# In[29]:


print(primes_lt20)
primes_lt20.pop(3)
print(primes_lt20)


# In[30]:


print(primes_lt20)
primes_lt20.pop()
print(primes_lt20)


# In[31]:


print(primes_lt20)
primes_lt20.remove(11)
print(primes_lt20)


# That last one is a little funky.  `remove(n)` removes the first element in a list that matches `n`.
# 
# ***
# 
# Lists have all kinds of cool methods -- functions or behviors that are inherent to lists.  For example, we can loop over the elements in a list using `for`:

# In[32]:


for num in primes_lt20:
    print(num, num == 13)


# We can ask `python` whether a value appears in a list:

# In[33]:


13 in primes_lt20


# ... or we can ask `python` *where* a value appears in a list:

# In[34]:


primes_lt20.index(13)


# Here is a structure that I use all the time (and you will after our next lesson).  Let's say that I have a list of random numbers, I may not know how many, and want to loop over these numbers and square them.  Please try to understand each of the lines below. 

# In[35]:


# let's first create the list
list1 = []    
for i in range(rand.randint(1,100)):
    list1.append(rand.random())

print("We have " + str(len(list1)) + " elements in our list.\n")

# then we'll do a for loop
for i in range(len(list1)): 
    num = list1[i]
    print(i, '\t', list1[i], '\t', (list1[i])**2)


# The block above makes a list containing a random number of random numbers, and then "runs over" the elements in this list and applies the function squarep1 to each.
# 
# For my last list trick, I'll show you that python knows how to do some simple operations with lists.  In some cases, the outcomes are obvious.  In other situations, python's interpretation of the syntax may be surprising:

# In[36]:


aL = [1, 6, 3, 7, 9, 2, 4, 6, 7]
bL = [7, 8, 9, 0]

aL + bL


# In[37]:


aL.sort()
print(aL)


# It's also worth noting that `python` is perfectly happy with lists that contain different types of data.  For example, some programming languages would freak out about the following:

# In[38]:


mixed_list = [1, 2, 4.5, -6.2, 'a phrase', 99, "hey, another phrase"]
print(mixed_list)


# * * *
# 
# ### Dictionaries
# 
# Lists are ordered collections of data -- "ordered" means that the order of the elements is an important feature of the structure, and indexing these elements with an integer makes sense.  `python` also has a way of storing data for which ordering isn't that important (but still exists).  A **dictionary** is like a list, but the elements are indexed by strings.  In a `dict`, each **value** is associated with a **key**.  This might sound crazy, but works quite a bit like a simple 2-column data table.  Dictionaries are initialized in the following way:

# In[39]:


students_year = {'Abdoul': 2, 'Aiden': 2, 'Aimee': 2, 'Gannon': 2, 
                 'Gaurav': 2, 'Gia': 2, 'Maddy': 1, 'Alex': 4}

print(type(students_year))


# We can access the elements in the dictionary in the same way as for a list, but now the "indices" are the key strings:

# In[40]:


students_year['Abdoul']


# Note that there are **two** pieces of important information for each element in a dictionary: the key and the value.  Because order is less imporant for a dictionary, there are several ways of looping over the elements in it.  Check out these two implementations:

# In[41]:


# for k in students_year.keys():
#     print(k)

# for v in students_year.values():
#     print(v)
    
for key, value in students_year.items():
    print(key, 'is my favorite student in year', value, '!')


# Note that even though ordering is not important in a dictionary, there seems to be an assumed order, *viz.* the order in which we initialized it.  There are various other fancy ways to iterate over the dictionary.  Some of these impose an index on the dictionary.  Here's an example:

# In[42]:


for i, (k, v) in enumerate(students_year.items()):
    print(i, k, v)


# * * *
# 
# ### Spyder
# 
# Your instructor will introduce you to Spyder, a Python interactive development environment (IDE) that ships with Anaconda.  From now on, you may work in Spyder (or similar) and submit your homework as separte python scripts.

# * * *
# ## Problems
# 
# Your homework is to complete 4 of the following problems.  
# 
# ### Regulars
# 
# 1. A function which determines whether a number is prime is given below.  Use this function to generate a list of the first 1000 prime numbers.  Check that you have 1000 using the `len()` function.
# >```python
# def is_prime(n):
#     fact = 2
#     prime = True
#     while fact <= n**(0.5):
#         if n % fact == 0:
#             prime = False
#         fact = fact + 1
#     return prime
# ```
# 1. A bag of M\&M's contains only 88 reds and 12 browns.  Weird!  Simulate a process in which you pull 5 M\&M's out of the bag and count the number of browns.  Perform this simulation 1000 times and compute count the number of times that you pulled 2 or more browns.
# 1. Write a program that generates a list of 100 random integers between 0 and 100 (inclusive), and then finds the number of pairs in the list that add to 66.
# 1. SORT!  Write a program that generates a list of 100 random integers between 0 and 100 (inclusive), and then sorts the list in descending order.  Do not use a built-in function like `sort`!
# 
# ### Meanies
# 
# 5. SORT!  Write a program that generates a list of 10000 random integers between 0 and 100 (inclusive), and then sorts the list in descending order.  Use Google to find a way to track how long your program takes to run.  A bonus point will be awarded to the fastest sort algorithm in the class.
# 5. Do problem 1 from above, but modify the program to generate a list of the first 10000 prime numbers.  Then write a program that checks the list to see if there are any pairs of numbers that add up to another number in the list. 
# 5. Write a program that generates a list of 100 random integers between 0 and 10^6 (inclusive), and then finds the largest number in the list.  Your program should NOT use any built-in methods/functions like `max`.
# 
# ### Mega-meanies
# 
# 8. A bag of M\&M's contains a total of 100 pieces, $n$ of which are red and $(100-n)$ of which are brown.  Let's say that you randomly draw 8 M\&M's from the bag, yielding 2 red and 6 brown.  You want to use this sampling to predict the total number of browns in the bag. Obviously this one sample doesn't tell you exactly what's in the bag, but it can help you to update your *expectations* of what's in the bag.  For example, you now know that there's a 0\% probability that the bag contains only 3 brown M\&M's!  So, here's what you're going to do:
# - Choose a value for $n$ between 6 and 98.  Perform a simulation of 1000 draws of 8 M\&M's from the bag.  Calculate the percentage of these draws that yields 4 browns and 4 reds.  Call this percentage $p(n)$.
# - Now calculate $p(n)$ for **each** value of $n$ between 6 and 98.
# - The owner of the M\&M's opens the bag and counts the actual $n$ without showing you the results.  The owner offers to pay you \$100 if you can correctly guess the *actual* $n$.  You get 10 guesses.  Which values do you guess?
# 
# 

# In[ ]:




