This is a quick and dirty python code that is to be run after analyzing videos using IDTrackerAI. 
This specifically serves as post-processing for Stahlmann-Roeder's beetle winner-loser scent trials, where beetles have the option to choose between 3 slices of filter paper.
The three filter papers have scent from a winner of a beetle fight, a loser from the same beetle fight, and an unscented control. 

The input of the code takes the trajectory coordinates of a single beetle as well as the coordinates of 3 polygons, and then asks if the beetle is within any of these polygons
in any of the frames. The amount of true or false answers is then counted up and then converted to time (in minutes) spent on each filter paper. 
