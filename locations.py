# locations class
from sys import exit
from random import randint

class Locations(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class mainCave(Locations):
    
    def enter(self):
        print "You find yourself in the dark cave. You don't remember anything but you"
        print "know that you need to find you way back to home" 
        print " Now try to find something useful near you:"

        action = raw_input("> ")
        
        if action == "search":
            print 
        




test = mainCave()
test.enter()

