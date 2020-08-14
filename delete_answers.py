#! ./venv/bin/python

from pyautogui import press
from common import setup, TOTAL_QUESTIONS
import sys

def delete_letter():
    press("delete")
    press("tab")

setup()
for i in range(TOTAL_QUESTIONS):
    sys.stdout.write("\r")
    sys.stdout.write(f"{i + 1}/{TOTAL_QUESTIONS} deleted")
    sys.stdout.flush()
    delete_letter()
print("\nDONE!")
