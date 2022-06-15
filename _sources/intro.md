# Welcome!

This book contains lessons from PHY 220 Introduction to the Physical Sciences course taught in the Physics Major at Washington & Jefferson College.  In the context of our curriculum, these materials are intended to prepare undergraduate students to use computation in upper-level lecture and courses, as well as in research settings in the department and beyond.  They should also be useful to students who need to develop some programming proficiency to apply to studies or research in quantitive, data-driven fields.

## Learning goals

The over-arching theme of this course is that computation (or more generally computer programming) is an essential skill in science, one that has made possible new ways of investigating the physical and social systems that make our Universe worth studying. Our physics curriculum centers programming and data analysis as core skills.

These materials are not designed to make students expert programmers, and we don't really delve into many core computer-science concepts.  Rather, the emphasis is on introducing the types of problems that are amenable to computation and helping the student become comfortable reading, modifying, and writing code.  

The topics covered are chosen to get students up to speed with techniques necessary to start doing research.  I'm biased, of course; these materials focus on the things that high-energy physicists usually do: cleaning big datasets, exploratory data analysis and visualization, fitting, *etc.*  That said, the core ideas here have allowed our students to apply computation to course work and research in condensed matter physics, astronomy and astrophysics, mathematics, and engineering.  The process seems to work: students who have completed this course have hit the ground running in REUs and in careers in data science.

This work has an epi-objective of making students more comfortable with quantitative information.  These materials engage with concepts like data *vs* results, experimental uncertainties and their propagation, interpreting graphs, and statistical thinking.

## Who is the student?

We require our physics majors to take the PHY 220 course in (or before) their fourth semester of study.  That said, the course is open to students from all majors, with prerequisites of Calculus I and an introductory course from *one* of the following disciplines: physics, chemistry, biology, or economics.  The second of these prerequisites is intended to ensure that the student has *some* scientific context in which to do programming.

The materials are structured for students who are new to programming -- like new new.  I've tried to provide enough explanatory text that a new programmer can make it through the tutorials with little guidance.  With an instructor available to walk students through the lessons, do live demos, and answer questions the materials seem to work pretty well for newbies.

That said, roughly half of the students who take this course have some robust prior programming experience, typically in another language like C or Java.  These students are able to move through the lessons in Part I quickly, *but* I've found that the applications in Parts II and beyond are, in most cases, novel.  Said another way, scientific computation is complementary to the prior programming experience, which typically focuses on web, app, or game development.

If you'd like to use the materials for a similar semester-long credit-bearing course, please contact me for other materials like syllabus and final-project assignments.

## How to use these resources

### Accessing the lessons

The book format that you're reading now is really just a way of gathering all of these lessons into one semi-coherent package.  If you actually want to use these notebooks (modify code, work on the homework problems) you'll want to download the notebook (.ipynb) files and work on them locally (or on a cloud platform like Google Colab).  You can download using the appropriate icon in the upper-right of this window.

### Data files

Some of the lessons rely on data files that I've generated or that freely available online.  I've cited sources and provided links where appropriate.  Most of the files are available on my [github](tktktk).  When you download these data files, you will either need to place them in the right directory (`<location of your .ipynb>/data_files/`) or change the file path in the notebooks to point python to the correct location.  Note that these lessons were written on a Unix-derivative OS; if you're using Windows your file paths might look a bit different.

### Software

To run these notebooks locally, you will need to have `python` and several common packages installed on your computer.  An easy way to get all of the necessary software is to install [Anaconda](https://www.anaconda.com/), an open-source distribution of python, R, and a bunch of other industry-standard data science tools.  This is a great solution for new programmers (who have enough disk space), as it's pretty self-contained and will give you access to many of the resources you need for taking the next steps beyond these lessons.

There are only two packages referenced in these lessons that aren't included in base Anaconda.  `rich`, which gives some really nice terminal print formatting, is completely unnecessary -- if you don't want to or can't install it, just comment out any references to it.  The packages necessary for microcontroller programming are a bit more difficult to install, but instructions are linked in the lesson on this topic.

### Live demos

If you're an instructor or a research advisor, please consider working through these materials *with* your students.  Most of the lessons include "warm-up" problems or "live demos".  In class, I take a Socratic approach to these, having students guide me through coding up a solution while I'm sharing or projecting my screen.  This is a great, interactive way to get students to make guesses and test ideas... and they *love* seeing me screw things up and have to debug.  Showing students how a professional breaks software and then works through the steps of fixing it is a high-impact teaching practice.  I like to reinforce that I rarely know exactly how to solve a problem when I start coding.  Getting from A to B is rarely linear for me, and refactoring is an important process.

Dan Shiffman's approach at [The Coding Train](https://thecodingtrain.com/) is an excellent model, IMO!

## Let's collaborate!

Want to contribute to this project?  Please [get in touch with me](mailto:mmccracken@washjeff.edu)!  I'd love to collaborate to keep these materials fresh: fixing bugs, expanding tutorials, or building more projects in other scientific fields.

## Acknowledgements

Enormous thank you to the [Python Software Foundation](https://www.python.org)!

Most of the materials provided here are

The book format that you're looking at right now is powered by the excellent [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)

```{image} logo.png
:class: bg-primary mb-1
:width: 300px
:align: center
```

These materials are provided under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).  Enjoy!

<!--
***

These materials are offered under the MIT License

Copyright 2022 Michael McCracken

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-->

<!--
```{tableofcontents}
```
-->
