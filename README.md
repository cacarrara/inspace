# InSpace

[![travis](https://travis-ci.org/mochaoss/inspace.svg?branch=master)](https://travis-ci.org/mochaoss/inspace/)
[![codecov](https://codecov.io/gh/mochaoss/inspace/branch/master/graph/badge.svg)](https://codecov.io/gh/mochaoss/inspace)

Inspace is a tool to help communities organize and share knowledge. Its based on information categorization that follows a well defined schema.


## Schema

The schema involves the following categories:

* [Galaxies](#galaxies)
* [Stars](#stars)
* [Planets](#planets)
* [Satellite](#satellite)

### Galaxies

This is the biggest Inspace information category. It may exist more than one Galaxy of information. It represents big area of knowledgement like Software Development, Entrepreneurship, Marketing, Sales, Human Resources, Mechanical Engineering, Philosophy, etc. Galaxies can be created by anyone anytime.
In course of time one galaxy can be merged with another one. For example, if there are two galaxies, one called Software Development and other called Programming it may be possible to merge both to keep related knowledge consistently organized.

### Stars

Stars are still group of knowledge big enough to have smaller categories of information around, but not so big as a Galaxy. However it can change during Star existance: a Star can grow up enough and become a Galaxy. As well, a Star can become too obsolete and die. That dynamic behaviour represents the community knowledge development.

### Planets

Usually Planet represent the smallest category of information. Planets orbits a Star and have special dependency relation with it. A Planet cannot exist without an Star and cannot exist around more than one Star at same time. It may be possible to migrate a Planet from a Star to another, although it's not desired.

### Satellite

Trying to bring one more level of specialization, Satellite may or may not exist around a Planet. If a Star start to have too much Planets around, a specialization of those Planets could be done and some of them may become a Satellite which is kind of information group not too big, but it's good to have them categorized.

#### Galaxies structure example

**Galaxy:** Programming  
**Stars:** Python, Javascript, C#, Text Editors  
**Planets:** Django, Node, Vim, Sublime, Meteor, Flask  
**Satellites:** Vim plugins, ExpressJS, Django Rest Framework  

**Galaxy:** Software Development  
**Star:** Agile,  
**Planet:** Scrum, XP, Refactoring, Continuous Integration  

**Galaxy:** Entrepreneurship  
**Star:** Startup  
**Planet:** Lean, Canvas  


## Resources

A Resource is the information which is stored in InSpace properly. It can be virtually anything: a small text, a hyperlink, a question with answers, link to multimedia content (video, sound, images).  
The Resources are stored following the InSpace schema. The only categories that can have a direct link to Resource are Planets and Satellites. So, a Galaxy or a Start will never have a Resource directly associated, only their Planets and Satellites. This is a restriction aiming organization consistency.


## Community validated editions

All content edited (inserted, updated, deleted) in InSpace will be instantly available, however it will be marked as "waiting community validation". All the editions must be validated by community. Not necessarily all community members must validate a content, but as soon as it be validated enough it will have a proper flag CVE (Community Validated Edition).  
Editions can involves Resources or Schema (Galaxies, Star, Planets and Satellites). All editions must be validated by community.


## Installing On Ubuntu 16.04 LTS

1. The first step is clone the repository on GitHub in your machine from mochaoss/inspace
```git clone github.com/mochaoss/inspace.git``` 
2. The second step is configure an virtual environment to Python, execute the following commands in the terminal: 
  1. **sudo apt install virtualenvwrapper**
  2. **mkvirtualenv --python=/usr/bin/python3 inspace**
  3. Now position the terminal in the folder that you cloned inspace form GitHub and execute: **mv loval.env .env**
  4. Now we are going to make it!! Execute the following commands in the terminal:
   1. **make install-local**
   2. **make install-test**
   3. **make run-migrate**
   4. **make run**
Notes:
- Python version 3.5.2
- Those steps works on Ubuntu 16.04 LTS, in other versions are not assured to work successfully



