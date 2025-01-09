'''
Created on Jul 10, 2023

@author: renan
'''

import copy
import random

class Hat:
    contents = ""
    # Initiate it and pass each term of the dictionary to the instance variable "contents" as many times as 
    # needed
    def __init__(self, **balls):
        self.contents = []
        for key in balls:
            for _ in range(balls[key]):
                self.contents.append(str(key))
    
    # The "draw" method which returns a random amount of balls from the list "contents"
    def draw(self, number):
        self.result = []
        self.number = number
        if self.number <= len(self.contents):
            for _ in range(self.number):
                self.hold = random.randint(0, len(self.contents) - 1)
                self.result.append(self.contents[self.hold])
                self.contents.pop(self.hold)
            return self.result
        else:
            return self.contents

    def __str__(self):
        return str(self.contents)


# Defining the experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls_drawn = num_balls_drawn
    amount_tests = num_experiments
    
    # I will save the expected_balls as a dictionary.
    expected_dic = dict(expected_balls)
    #print(expected_dic) TESTING
    
    # The variable 'counter' will hold the amount of iterations that get the balls expected
    counter = 0
    
    # This is the loop for the amount of iterations the user wants
    for _ in range(amount_tests):
        # 'expWorked' is the boolean variable that states if the iteration gets the expected balls
        exp_worked = True
        # 'the_urn' gets all the balls in the 'hat'
        the_urn = copy.deepcopy(hat)
        #print(the_urn) #TESTING
        
        # 'test_list' get a draw from hat and transform it into a list.
        test_list = list(the_urn.draw(balls_drawn))
        #print(test_list) #TESTING
        
        # This loop compares the amount of each color of balls in the draw with the amount in the expected, if
        # the amount expected is greater than the amount of the colored ball in the draw, the iteration is FALSE
        for color in expected_dic:
            #print(test_list.count(color), " and ", expected_dic[color]) TESTING
            if test_list.count(color) < expected_dic[color]:
                exp_worked = False
        
        # If all the balls expected are in the draw, the iteration is TRUE and we count this iteration
        if exp_worked:
            counter += 1
            #print("COUNTED", counter) #TESTING
        
    # Calculate the probability
    probability = counter / amount_tests
    #print(counter) TESTING
    return probability

