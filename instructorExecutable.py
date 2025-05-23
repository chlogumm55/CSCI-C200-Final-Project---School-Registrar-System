"""
Filename: instructorExecutable.py

Problem Description: This design demonstrates the algorithm for the Instructor Module of the course project. An instructor can login to the system and see all the courses assigned to teach. The csv file generated in the Admin module will be used to authenticate a user. The csv file contains 5 columns, with the username stored in the third column and password stored in the fourth column. Users will be allowed to enter the wrong username and password 5 times. Course information is stored in the csv file generated by the Admin module. The csv file contains course numbers, course titles, and instructor usernames. Only rows with the matching username will be displayed.
 

First Create Date: April 23rd, 2025
Last Update Date: May 2nd, 2025
Author: Chloie Gummer
Version: 1.1
"""
from instructorsClass import Instructor; #Import instructor class
import utility; #Import utility file
import csv; #Import csv module
import sys; #Import sys module for exiting the program

print("Welcome to the Instructor Module!"); #Display welcome message

#Initialize a list to store multiple instructors
instructors = [];

#Load existing instructors from the csv file
try:
    with open("instructors.csv", "r") as file:
        reader = csv.reader(file); #Read the csv file
        next(reader); #Skip the header row
        for row in reader:
            instructors.append(Instructor(row[0], row[1], row[2], row[3], row[4])); #Create instructor objects and store them
except FileNotFoundError: #File processing error
    print("No instructors found. Starting fresh.");

#Prompt user for credentials
username = input("Enter your username: ");
password = input("Enter your password: ");

attempts = 5; #Set a maximum of 5 login attempts

while attempts > 0:
    #Attempt authentication by matching credentials in the list of instructors
    authenticatedInstructor = next((instructor for instructor in instructors if instructor.username == username and instructor.password == password), None);

    if authenticatedInstructor:
        print("Login Successful!");
        break; #Successfully authenticated and break 
    else:
        attempts = attempts - 1; #Decrement remaining attempts
        if attempts == 0: #Out of attempts
            print("Too many failed attemps. Exiting program.");
            sys.exit(); #Exit the program if authentication fails
        print("Invalid credentials. " + str(attempts) + " attempts remaining.");
        username = input("Enter your username: ");
        password = input("Enter your password: ");

#Display instructor menu options
while True:
    print("Instructor Menu: \n");
    print("1. View Assigned Courses \n");
    print("2. Exit \n");

    choice = input("Enter your choice (1-2): ");

    #Handle user choices
    if choice == "1": #Option one is viewing courses assigned to teach
        authenticatedInstructor.viewAssignedCourses(); 

    elif choice == "2": #Option two is exiting the module
        print("Exiting Instructor Module.");
        break; #Exit menu loop


    else: #Invalid choice
        print("Invalid choice. Please enter a number 1 or 2.");
        choice = input("Enter your choice (1-2): ");



