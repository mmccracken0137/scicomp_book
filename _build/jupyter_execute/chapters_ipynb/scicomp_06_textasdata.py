#!/usr/bin/env python
# coding: utf-8

# # Text as data

# ## Recap
# 
# We're way past the point of no return in becoming meaningful users of computers!  Just check out this non-exhaustive list of basic skills that we've covered:
# - basic mathematical operations
# - iteration and recursion with loop control structures `for` and `while`
# - keeping track of variables outside of loops (i.e., counting and summing)
# - function definition and using functions *inside* of loops
# - conditionals with `if`, `else`, and `elif`
# - types: `int`, `float`, `string`
# - containers such as `list` and `dict`
# - randm number generation
# - accessing and iterating over elements in lists and dicts
# - file I/O
# - basic (and semi-advanced) data visualization: histograms, scatter plots, higher-dimensions in 2-d
# - fitting models to data and extracting results (with uncertainties)
# 
# **Wow**, that's a LOT of stuff.  You're scaring me with that big brain of yours.
# 
# ***
# 
# ## This lesson: Something completely different
# 
# In this lesson we're going to pause the accumulation of new skills to do some applications.  We have a lot of tools in our toolboxes!  Let's take some time to explore how these tools can help us answer questions outside of the physical sciences.

# ## Word analysis
# 
# Let's turn our attention to the quantitative analysis of textual information.  In some of your other classes, you're learning to use the close reading or synthesis of texts to gain understanding of history, human experiences, emotions, *etc.*  This is awesome!  That's not what we're going to do today.
# 
# Today we're going to treat texts as data!  We'll work with a dataset consisting of several texts that are in the public domain (*i.e.*, they're old and can be accessed without copyright issues).  What can we learn from quantitative analysis of text?  What kinds of questions can we ask about language and narrative structure?
# 
# The exception, however, is `words_alpha.txt`; this file lists 370102 English-language words.  [[Source]](https://github.com/dwyl/english-words)  The question whether this is "all" of the words in the English language is perhaps not valid, but this file certainly contains a lot of them.  Let's do some warm-up with this file.  Get ready to flex those `string`-manipulation muscles, and remember that characters in a string can be accessed by index (like elements in a list).

# #### Warm-up 1
# 
# Read in the file line by line, and determine how many words begin with the letter "m".  Are there any that begin with "M"?

# In[1]:


# here is some skeleton code that parses through the file...
import numpy as np

file = open('data_files/words_alpha.txt', 'r')
line = file.readline()

while len(line) > 0:
    
    line = file.readline()
    
file.close()


# #### Warm-up 2
# 
# - How long is the longest word in the list?
# - What is the longest word in the list?
# - What word(s) have the most 'z's in them?

# In[2]:


# more code goes here :^O


# #### Warm-up 3
# 
# How many five-letter words are there?  (How long before Wordle has to reuse a word?)  How many words have all five vowels in them?

# In[3]:


# yet more code goes here!  


# ***
# 
# Well, I'm certainly feeling warm now!  Those were some fun spot checks of English vocabulary.  What about high-level aggregate information?
# 
# ***
# 
# #### Warm-up 4
# 
# Make a histogram of word lengths.

# In[4]:


# code goes here


# ***
# 
# The information contained in `words_alpha.txt` tells us about the structure of words in the English language.  This is interesting, but it can't really tell us about *how* these words are used or how a given person uses these words.  This seems dumb to point out, but  we can generalize to the universal lesson
# 
# > Your analysis is only as good as your data.
# 
# ## Text analysis
# 
# Let's move on to datasets containing words used in their natural habitat: sentences that convey ideas!  All of the texts used below can be found on [Project Gutenberg's website](https://www.gutenberg.org/).  Search for each novel, and download a txt/ascii version.  Enjoy!  I've also included a few of them in this repo.
# 
# First, we have to figure out how to correctly deal with these files.  Each file contains a header and a footer that tell you about copyright information.  Obviously when we analyzed the text of the novel, we want to exclude the header and footer.  Look through the files to find the text signifying the header and footer.  I'll show you hor to work around this when reading in the file.  Let's work on Jane Austen's <u>Pride & Prejudice</u> first.

# In[5]:


file = open('data_files/JaneAusten_PrideAndPrejudice_1813_ProjGutenberg.ascii', 'r')
line = file.readline()

# read off the lines in the header, don't do anything with them...
while '*** START' not in line:
    line = file.readline()
    
# read off the lines in the body of the novel, quit once we get to the footer
while '*** END' not in line:
    # do some calculations...
    line = file.readline()
    
file.close()


# Now we just have to be creative!  What types of questions can we ask (should we ask) of the text of a novel?  What could we learn about the author or the characters?
# 
# #### Warm-up 5
# 
# The main character of <u>P+P</u> is Elizabeth Bennett.  Count how many times "Elizabeth"  and "Bennett" and appear in the text.  Don't forget to consider *e.g.* "Elizabeth's".

# In[6]:


# Pride!


# #### Warm-up 6
# 
# Elizabeth Bennet's romantic interest in <u>P+P</u> is Mr. Fitzwilliam Darcy.  Let's investigate how Austen (or British people in Austen's time) used first names.  Find the numbers of appearances of "Elizabeth", "Bennett", "Fitzwilliam", and "Darcy" in the text.  Calculate the ratio of first-name to last-name appearances for each character.  Calculate the ratio of these ratios -- are they similar?  Do you have any theories about why the relative sizes of these ratios?
# 

# In[7]:


# Prejudice!


# Now, these two calculations are somewhat trivial, but they give you some odea of the types of things that we can investigate when we treat a text as data.  Can you think of other interesting questions to ask with this approach?
# 
# *** 
# 
# If this seems far removed from the sciences, you might consider the following text:
# 
# `GCTCGGGTGACACGAATTGGATCACGGACATCAAGCACTG`<br>
# `GCTTTTATAGAGGACGGGGTGCCACTCACCCTGCCGGTGC...`
# 
# What kinds of questions might you ask about a string of text like this?
# 
# ***
# 
# ## Machine cryptography and cryptanalysis
# 
# We could do an entire semester on cryptography, the science of hidden writing!  It's a rich and fascinating (and useful and potentiall lucrative) subject.  For now, I'll mention that you have the basic skills to do some straight-forward cryptography (coding) and cryptanalysis (de-coding) of secret messages.  For example, say you're given the following cipher (encoded message):
# 
# `MWFCK KEYFL ZLRLQ CKZZW`<br>
# `ALVVW VJLWZ ESNQA FKNXL`<br>
# `RLDZK XZLWU SKASL QPKQM`<br>
# `KVKZC FKNQS LWQAM YLLZW`<br>
# `USJZC YNAFK NQLAK KMSFA`<br>
# `KMWFJ AJZMJ ELXLY KASDZ`<br>
# `KXXSW AMYLL ZCKJZ CKZXL`<br>
# `DZKXA SLCWT LWZEX LQLCK`<br>
# `ZZWHV WFJAW ZEJPF KNWMD`<br>
# `TLSKX JTPLL VJZCE KZAAL`<br>
# `VVTLF KNQLA KKYVJ ZEAKM`<br>
# `LLZLR LQCKZ ZWCJR LFKNN`<br>
# `HZLRL QCKZZ WVLAF KNEKX`<br>
# 
# What the what???  Look familiar?  Yeah, me neither.  We can begin the decryption process by doing some simple letter-frequency analysis and comparing to a known (and hopefully representative corpus (sample).  I'll include the cipher on Sakai as `cipher.txt`.
# 
# #### Decryption warm-up
# 
# Make a bar graph of the letter frequency in the cipher.  Make a bar graph of the frequency of letters in <u>P+P</u>.  Can you see any likely letter equivalences for a single-character substitution?  Bonus points if you can sort the bars from high to low frequency.

# In[8]:


# decryption warm-up goes here


# #### Decryption warm-up
# 
# Let's take the result of the previous warm-up as a good estimate of the frequency of letters in the English language.  The encoded text above was produced with a simple substitution key -- each letter in the cypher is a substitution for a letter in the original text.  For example (though this isn't acutally true), all `X`'s in the cypher represent `D`'s in the original text.  Make a letter frequency bar graph for the cypher text.  Compare it to the bar graph for <u>P+P</u> and identify some likely substitutions.

# In[9]:


# I'll make the cypher a string for you to use:
cyph = 'MWFCKKEYFLZLRLQCKZZWALVVWVJLWZESNQAFKNXL'
cyph += 'RLDZKXZLWUSKASLQPKQMKVKZCFKNQSLWQAMYLLZW'
cyph += 'USJZCYNAFKNQLAKKMSFAKMWFJAJZMJELXLYKASDZ'
cyph += 'KXXSWAMYLLZCKJZCKZXLDZKXASLCWTLWZEXLQLCK'
cyph += 'ZZWHVWFJAWZEJPFKNWMDTLSKXJTPLLVJZCEKZAAL'
cyph += 'VVTLFKNQLAKKYVJZEAKMLLZLRLQCKZZWCJRLFKNN'
cyph += 'HZLRLQCKZZWVLAFKNEKX'

# unlock secrets here!!!


# ***
# 
# ## Problems
# 
# Your homework is to complete three (3) of the following problems.
# 
# ### Regulars
# 
# 1. Use `words_alpha.txt` to make a histogram displaying the number of words beginning with each letter of the alphabet.
# 1. Use `words_alpha.txt` to make a bar graph displaying the frequency of each letter of the alphabet.  Hint: Use a `dictionary`!
# 1. Compute how many words in `words_alpha.txt` contain the following digraphs: "ae", "aa", "eu", "ph".
# 1. Compute the average sentence length (in words) of **each** of the Jane Austen novels.  Hint: What would be an easier way to count the number of sentences in a text?
# 1. Determine which of the 15 books is most likely about a dog by counting the relative number of times the word "dog" appears in each.  Write a block of explanatory markdown to explain your conclusions.
# 
# ### Meanies
# 
# 6. Make a bar graph of the average sentence length for each of the following authors: Austen, Hawthorne, London, Wells, Dostoevsky.  Use all of each author's texts to do so.
# 6. Which of the five authors uses the biggest words (on average)?  Include a graph(s) or some text to convince me.
# 
# ### Mega-meanies
# 
# 8. Provide quantitative evidence that suggests that <u>Crime & Punishment</u> was not written by Jane Austen.  Write a block of explanatory markdown to accompany your code.
# 8. How many different proper nouns appear in <u>The Brothers Karamazov</u>?
# 8. I made it to the end of Part I, Book II, Chapter V of <u>The Brothers Karamazov</u>.  Tell me how it ends, please.   (No don't.)
# 8. Continue decryption of `cipher.txt`.  Write a block of markdown that explains your process.
# 
