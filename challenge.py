"""
  A function which takes name as a parameter and print name with a random number
  between 6 and 15 

  How to call this function ? python challenge.py arg1
"""
import random,sys

def challenge(name):
    # randint generates a random number between the range specified and str to parse it into a string
    print name + " "+ str(random.randint(6,15))

# First block to be excuted when python file is run
if __name__ == "__main__":
   challenge(sys.argv[1])
