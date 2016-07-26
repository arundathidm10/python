ABOUT THE CODE
==============

The challenge is a specific example of an assignment problem 
and a simple greedy algirthm will not work and that's why
I used the munkres alogrithm module to implement munkres solution 
(4 steps algorithm) to arrive to the solution.

Although I could have implemented the munkres 4 step algorithm myself,
It's a good practise to use existing modules because they have been well tested
by many users.


TESTING
=======

The file test_discount_offers.py contains 6 unit tests for 
my main program discout_offers.py 


USED MODULES
============
math module (for using gcd)
munkres (module)
sys
os


INSTALL MODULES
===============
I developed my code on Linux (Ubuntu, debian)
To install munkres on Ubuntu, simply run:

sudo apt-get install python3-munkres


CLASSES
=======

I created two classes:

SuitabiltyClassEntry & SuitabilityClass (both in the lib dir)


TODO
====

To run the program on the command line:

python3 discount_offers.py input.txt

or

python3 discount_offers.py

You can also run it on idle3 and you will be asked to enter a file name in your current directory.

To run the unit tests on the command line:

python3 test_discount_offers.py 

or

you can also run it on idle3 


OUTPUT
======

Below is a sample output

('Jack Abraham', 'iPad 2 - 4-pack', 6.0)
('John Evans', 'Girl Scouts Thin Mints', 6)
('Ted Dziuba', 'Nerf Crossbow', 9.0)
The total suitabilty score is: 21.0

('Jeffery Lebowski', 'Colt M1911A1', 13.5)
('Walter Sobchak', '16lb bowling ball', 13.5)
('Theodore Donald Kerabatsos', 'Half & Half', 22.5)
('Peter Gibbons', 'Red Swingline Stapler', 8)
('Michael Bolton', 'Vibe Magazine Subscriptions - 40 pack', 8)
('Samir Nagheenanajar', 'Printer paper', 18.0)
The total suitabilty score is: 83.5

('Jareau Wade', 'Batman No. 1', 13.5)
('Mahmoud Abdelkader', 'Football - Official Size', 10.5)
('Wenyi Cai', 'Bass Amplifying Headphones', 11.25)
('Justin Van Winkle', 'Elephant food - 1024 lbs', 15.0)
('Gabriel Sinkin', 'Dom Perignon 2000 Vintage', 7.5)
('Aaron Adelson', 'Three Wolf One Moon T-shirt', 13.5)
The total suitabilty score is: 71.25






