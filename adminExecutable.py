"""
Filename: adminExecutable.py

Problem Description: This design demonstrates the algorithm for the Admin Module of the course project. An admin has many options available. They can add a new student, add an instructor, add a new course, see all the student information, see all thhe instructor information, see all the course information, and see all the enrollment information. The three csv files generated in the admin module are students, instructors, and courses. These files will be used continously throughout the program. The admin module is the only one that has a csv file to start, and it includes the administrators login information. They receive five tries to enter the wrong username and password. 
 

First Create Date: April 22nd, 2025
Last Update Date: May 2nd, 2025
Author: Chloie Gummer
Version: 1.1
"""

from adminClass import Admin; #Importing the admin class
import utility; #Importing the utility file
import sys; #Importing sys module for exiting the program
import csv; #Importing csv module

print("Welcome to the Admin Module"); #Welcome message

admins = []; #List to store admin objects

#Load admin data from the csv file
try:
    with open("admin.csv", "r") as file:
        reader = csv.reader(file); #Read csv file
        next(reader); #Skip the header row
        for row in reader:
            admins.append(Admin(row[0], row[1], row[2], row[3])); #Create admin objects and store them in the list
except FileNotFoundError: #File processing error and message
    print("Admin csv not found.");

#Prompt the user for admin login credentials
username = input("Enter your admin username: ");
password = input("Enter your admin password: ");

#Create a temporary admin object for authentication
tempAdmin = Admin("", "", username, password);

attempts = 5; #Set the number of allowed login attempts
while attempts > 0:
    # Authenticate the user directly using the CSV file and function from utiliuty file
    if utility.authenticateUser(tempAdmin, "admin.csv"):
        print("Login Successful!");
        for admin in admins:
            if admin.username.strip().lower() == username.strip().lower():  # Match found
                print("Welcome, " + admin.firstName + " " + admin.lastName + "! You are logged in as an admin.");  # Access matched admin's details
                break;
        break;  # Exit the loop immediately upon successful login

    else:
        attempts -= 1; #Reduce the number of attempts
        if attempts == 0:
            print("Too many failed attempts. Exiting the program."); #Exit program if authentication fails
            sys.exit();  # Exit the program entirely
        print(f"Invalid username or password. You have {attempts} attempts remaining.");
        username = input("Enter your admin username: ");
        password = input("Enter your admin password: ");
        tempAdmin = Admin("", "", username, password);  # Update tempAdmin with the new credentials


#Admin menu for managing students, instructors, and courses
while True:
    print("Admin Menu: \n");
    print("1. Add a Student \n");
    print("2. Add an Instructor \n");
    print("3. Add a Course \n");
    print("4. View all Students \n");
    print("5. View all Instructors \n");
    print("6. View all Courses \n");
    print("7. View all Enrollments \n");
    print("8. Exit \n");

    choice = input("Enter your choice (1-8): ");

    #Perform operations based on user choice
    if choice == "1": #Option one is adding a student
        admin.addStudent();

    elif choice == "2": #Option two is adding an instructor
        admin.addInstructor();

    elif choice == "3": #Option three is adding a course
        admin.addCourse();
 
    elif choice == "4": #Option four is viewing added students
        admin.viewStudents();

    elif choice == "5": #Option five is viewing added instructors
        admin.viewInstructors();

    elif choice == "6": #Option six is viewing added courses
        admin.viewCourses();

    elif choice == "7": #Option seven is viewing student enrollments
        admin.viewEnrollments();

    elif choice == "8": #Option eight is exiting the module
        print("Exiting Admin Module.");
        break; #Exit the menu loop

    else: #If an invalid option is selected
        print("Invalid chloice. Please enter a number between 1-8. ");
        choice = input("Enter your choice (1-8): ");


