# CLI TODO List Application Specification

## Overview
A simple, interactive command-line application written in Python to manage a TODO list. The application should use a REPL (Read-Eval-Print Loop) interface.

## Data Storage
Tasks should be saved in a local text file or JSON file (e.g., `tasks.json`) so they persist between sessions.

## Core Features & Commands
The REPL should support the following commands:
* `add <task description>`: Creates a new task and assigns it a unique ID.
* `list`: Displays all active tasks with their IDs.
* `done <ID>`: Marks a specific task as completed.
* `delete <ID>`: Removes a task entirely from the list.
* `help`: Shows all available commands.
* `exit` / `quit`: Saves the data and closes the application.

## Requirements
* The code must be contained within a single file named `todo.py`.
* Handle errors gracefully (e.g., invalid IDs, empty descriptions).