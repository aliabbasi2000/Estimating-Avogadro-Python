# Estimating-Avogadro-Python
Processing microscopic images of Polystyrene Beads and tracking the Brownian motion of particles and matching the data to Einstein's model, and estimating Avogadro's number.

run the program with these commands:

% more displacements-run_1.txt

% python Avogadro.py < displacements-run_1.txt 

% python beadtracker.py 25 180.0 25.0 frames/*.jpg | python Avogadro.py

