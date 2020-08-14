#! ./venv/bin/python

import argparse
from pyautogui import press, write
import sys
import os
from common import setup, TOTAL_QUESTIONS
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO", logger=logger, fmt="%(levelname)s: %(message)s")

parser = argparse.ArgumentParser(description="Converting listed answers to Excel Test")
parser.add_argument("file", help="The answer file for your test", type=str)
parser.add_argument("--denominator", help="The denominator between the number and answer", default=".", type=str)
parser.add_argument("--ignore", help="If you want to ignore validation", default=False, action="store_true")
args = parser.parse_args()

def exit_program():
    print("EXITING...")
    exit(1)

def answer_map(answer):
    cleaned_answer = list(map(lambda a: a.strip().upper(), answer.strip().split(args.denominator)))
    if len(cleaned_answer) > 4:
        logger.warning(f"QUESTION {cleaned_answer[0]} HAS MORE THAN 4 LETTERS!")
        exit_program()
    elif len(cleaned_answer) > 2:
        cleaned_answer[1] = f"{cleaned_answer[1]}{args.denominator}{cleaned_answer[2]}"
        cleaned_answer.remove(cleaned_answer[2])
        logger.info(f"ANSWER TO #{cleaned_answer[0]} IS ASSUMED AS {cleaned_answer[1]}")
    return cleaned_answer

def answer_filter(cleaned_answer):
    try:
        float(cleaned_answer[1])
        return True
    except ValueError:
        if cleaned_answer[1] in ["A", "B", "C", "D"] or "/" in cleaned_answer[1]:
            return True
    except:
        return False

def enter_letter(letter):
    write(letter)
    press("tab")

with open(args.file, "r") as file:
    answers = list(map(lambda x: x[1], filter(answer_filter, map(answer_map, file.readlines()))))
    num_answers = len(answers)

    if args.ignore:
        logger.warning("NOT CHECKING FOR NUMBER OF QUESTIONS!")
        # print("WARNING: NOT CHECKING FOR NUMBER OF QUESTIONS!")
    elif num_answers < TOTAL_QUESTIONS:
        logger.fatal(f"NUMBER OF QUESTIONS ({num_answers}) IS LESS THAN {TOTAL_QUESTIONS}!")
        exit_program()
    elif num_answers > TOTAL_QUESTIONS:
        logger.fatal(f"NUMBER OF QUESTIONS ({num_answers}) IS GREATER THAN {TOTAL_QUESTIONS}!")
        exit_program()

    setup()
    for num, answer in enumerate(answers):
        sys.stdout.write("\r")
        sys.stdout.write(f"{num + 1}/{num_answers} answers written.")
        sys.stdout.flush()
        enter_letter(answer)

    print("\nDONE!")
