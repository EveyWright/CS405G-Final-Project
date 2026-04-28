# CS405G-Final-Project

## Overview:
This is a Python and MySQL-based command-line application designed to help a middle school manage its after-school club activities. It provides a centralized database system to track clubs, faculty advisors, student memberships, event scheduling (with conflict prevention), and club finances.

## Features:

### Club Management: 
Add, delete, and view club meetings and field trips.

### Faculty Management: 
Look up faculty IDs, assign advisors to clubs, and view advising history.

### Student Management: 
Manage student club memberships and view daily student schedules.

### Finances and Budgeting: 
Record annual budgets, track expenses, and generate financial reports for each club.

## Prerequisites:
Python 3.x

The my-sql-connector python library: run 'pip install my-sql-connector' in the root project folder

## To Run:
open terminal, navigate to the src folder and execute the main script (python main.py)

## Initialization & Security
### Automatic Setup: 
When you run main.py, the application will automatically initialize the database by reading and executing schema.sql and sample_data.sql from the sql directory. You do not need to manually import these tables.

### Credential Handling: 
Upon launch, the system will prompt you for your MySQL database credentials. These are temporarily saved for the duration of the session and are safely wiped from the system upon exiting the application.