# Estimating-Avogadro-Python
Processing microscopic images of Polystyrene Beads and tracking the Brownian motion of particles and matching the data to Einstein's model, and estimating Avogadro's number.

This is project of my first year of university so I used standard libraries Introduced by "Programming in Python" Book.
This library includes glob.py, color.py, luminance.py, stdio.py, stdarray.py, picture.py

for more information about libraries visit: https://introcs.cs.princeton.edu/python/home/
also these libraries use pygame in themselves. so you need to install pygame library using this command:

%pip install pygame


run the program with these commands:

% more displacements-run_1.txt

% python Avogadro.py < displacements-run_1.txt 

% python beadtracker.py 25 180.0 25.0 frames/*.jpg | python Avogadro.py

