#! ./venv/bin/python

import argparse
from common import MATH_CALC_QUESTIONS, MATH_NO_CALC_QUESTIONS, WRITING_QUESTIONS, READING_QUESTIONS


parser = argparse.ArgumentParser()
parser.add_argument("name", help="Name of the file", type=str)
parser.add_argument("filename", help="File Directory", type=str)
args = parser.parse_args()

def write_section(file, section_name, num_questions):
    file.write(section_name + "\n")
    for i in range(num_questions):
        file.write(f"{i+1}. \n")
    print("Generated section: " + section_name)

with open(args.filename, "w+") as file:
    file.write(args.name + "\n")
    write_section(file, "READING SECTION", READING_QUESTIONS)
    write_section(file, "WRITING SECTION", WRITING_QUESTIONS)
    write_section(file, "MATH NO CALCULATOR SECTION", MATH_NO_CALC_QUESTIONS)
    write_section(file, "MATH WITH CALCULATOR SECTION", MATH_CALC_QUESTIONS)

print("Done")
