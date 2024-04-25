Employee Data Organizer
Overview
This project is designed to demonstrate the use of Python for accessing and organizing employee data via an API. It showcases the transition from traditional Bash scripting to more efficient and powerful programming languages like Python, especially for system administrators and SREs.

Background
System administrators traditionally rely on Bash for scripting. However, with the advent of the new generation of system administrators (SREs), who are more akin to software engineers, there's a shift towards using more powerful languages like Python. This project exemplifies the use of Python for tasks that are not suited for Bash scripting, such as accessing and organizing employee data via an API.

Learning Objectives
By the end of this project, you should be able to:

Understand the limitations of Bash scripting for certain tasks
Explain the concepts of APIs, REST APIs, and microservices
Understand the CSV and JSON data formats
Apply Pythonic naming conventions for packages, modules, classes, variables, functions, and constants
Recognize the significance of CapWords or CamelCase in Python
Requirements
Editors: vi, vim, emacs
Environment: Ubuntu 20.04 LTS with Python 3.8.5
File Format: All files must end with a new line and start with #!/usr/bin/python3
Libraries: Imported libraries must be organized in alphabetical order
Code Style: Follow PEP8 and pycodestyle (version 2.8.*)
Executability: All files must be executable
Documentation: All modules must have documentation
Error Handling: Use get to access dictionary values by key without throwing exceptions
Execution: Code should not execute when imported
Tasks
0. Gather Data from an API
Write a Python script that uses a REST API to fetch information about an employee's TODO list progress based on their ID. The script must accept an integer as a parameter (the employee ID) and display the employee's TODO list progress in a specific format.

1. Export to CSV
Extend the script from Task 0 to export the employee data in CSV format. The format must include the user ID, username, task completion status, and task title.

2. Export to JSON
Extend the script from Task 0 to export the employee data in JSON format. The format must include the user ID and an array of tasks, each with the task title, completion status, and username.
