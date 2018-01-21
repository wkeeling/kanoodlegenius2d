Kanoodle Genius 2D
==================

.. image:: https://travis-ci.org/wkeeling/kanoodlegenius2d.svg?branch=master
    :target: https://travis-ci.org/wkeeling/kanoodlegenius2d

An electronic version of the excellent `Kanoodle Genius <https://www.educationalinsights.com/product/kanoodle--174-+genius.do>`_ puzzle game. Kanoodle Genius 2D is written in Python using Tkinter.

|

.. image:: docs/images/sequence.gif
    :align: center

|

This game covers the first three levels of Kanoodle Genius (the 2-D levels), with 24 puzzles per level plus an extra 9 bonus puzzles at the end.

It runs in an 800x480 window which is optimised to run on the Rasperry PI touchscreen, but will just as easily run on your deskop or laptop.

I was inspired to create this version of Kanoodle Genius after watching my daughter beat me at the real life version by figuring far more puzzles than me. In desperation I reached for the one thing I am reasonable at - solving problems in software. Each puzzle has a "solve" button which you can press in emergencies when frustration gets the better of you.

Why Tkinter?
------------

- It comes with Python and is dead easy to get started with.
- This puzzle game did not require the high levels of animation provided by other frameworks - e.g. PyGame.
- I wanted to increase my Tkinter knowledge, whist demonstrating what is possible with the framework.

|

Play on the Raspberry PI touchscreen
------------------------------------

Kanoodle Genius 2D has been optimised for the `Raspberry PI touch display <https://www.raspberrypi.org/products/raspberry-pi-touch-display/>`_.

.. image:: docs/images/rasp.gif
    :align: center

|

Installation
------------

(Kanoodle Genius 2D requires Python 3.(

Clone the repo.

::

  git clone https://github.com/wkeeling/kanoodlegenius2d.git

Install the requirements.

::

  cd kanoodlegenius2d
  pip install -r docs/requirements.txt

Run the game.

::

  python kanoodlegenius2d.py

|

Author
------

Will Keeling