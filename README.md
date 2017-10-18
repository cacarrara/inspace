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


## Installing
* Tested in Debian and derivatives with Python 3

1. Clone repository: `git clone github.com/mochaoss/inspace.git`
2. Now in the folder that you cloned set the configuration: `mv local.env .env`
3. `make install-local`
4. `make install-test`
5. `make run-migrate`
6. `make run`

