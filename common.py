import sys
from time import sleep

READING_QUESTIONS = 52
WRITING_QUESTIONS = 44
MATH_NO_CALC_QUESTIONS = 20
MATH_CALC_QUESTIONS = 38

TOTAL_QUESTIONS = 52 + 44 + 20 + 38

def timer(seconds):
    for second in range(seconds, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(second))
        sys.stdout.flush()
        sleep(1)

def setup():
    print("SWITCH TO YOUR GOOGLE TAB TO ENTER!")
    timer(10)
    print("\nRunning...")
