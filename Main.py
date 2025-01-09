'''
Created on Jul 10, 2023

@author: renan
'''
from probClass import Hat
from probClass import experiment

hat1 = Hat(yellow=4, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

probability = experiment(hat=hat1, expected_balls={"yellow": 1, "green": 1},num_balls_drawn=4,num_experiments=3000)

print("Probability:", probability)
print()