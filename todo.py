#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Simple To-Do App")
parser.add_argument("task", type=str, help="Task to add")
args = parser.parse_args()

with open("tasks.txt", "a") as file:
    file.write(args.task + "\n")

print(f"Task added: {args.task}")
