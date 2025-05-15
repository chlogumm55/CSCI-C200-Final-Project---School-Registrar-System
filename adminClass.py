"""
Filename: adminClass.py


Problem Description: This design demonstrates the algorithm for the Admin Module of the course project. An admin has many options available. They can add a new student, add an instructor, add a new course, see all the student information, see all thhe instructor information, see all the course information, and see all the enrollment information. The three csv files generated in the admin module are students, instructors, and courses. These files will be used continously throughout the program. The admin module is the only one that has a csv file to start, and it includes the administrators login information. They receive five tries to enter the wrong username and password. 

First Create Date: April 22nd, 2025
Last Update Date: April 23rd, 2025
Author: Chloie Gummer
Version: 1.1
"""
import utility; #Import the utility file
import csv; #Import the csv module
import os; #Importing os module for file processing
from userClass import User; #Importing the user class as the parent class
from courseClass import Course; #Importing the course class

class Admin (User): #Admin class is a child of the User class
    
    #Constructor to initialize an Admin object using the parent User class
    def __init__(self, firstName, lastName, username, password):
        super().__init__(firstName, lastName, username, password);

    def __str__(self):
        return{
            #String representation of an Admin object
            "Admin: \n"
            "First Name - " + self.firstName + "\n"
            "Last Name - " + self.lastName + "\n"
            "Username - " + self.username  + "\n"
            "Password - " + self.password + "\n"
        };

    #Action Methods

    #Adds a student by collecting user details and saving them to students.csv
    def addStudent(self):
        #Collect student's name
        firstName = input("Enter student's first name: ");
        lastName = input("Enter student's last name: ");
        
        #Ensure the username is unique
        unique = False;
        while unique ==  False:
            username = input("Enter student's username: ");
            if utility.uniqueUsername(username, "students.csv"): #Use the utility function to check uniqueness
                unique = True; #The username is unique
                break; #Break the loop
            print("Username already exists. Choose a different username."); #Repeat the loop until unique username is chosen
        
        #Collect student password
        password = input("Enter student's password: ");

        fileExists = os.path.exists('students.csv'); #The file path for the students.csv file

         # Open the file in append mode (or create it if it doesn't exist)
        with open('students.csv', 'a', newline="") as file:
            writer = csv.writer(file);

            # Write headers if the file is being created for the first time
            if not fileExists:
                writer.writerow(["First Name", "Last Name", "Username", "Password"]);

            # Write the new student information
            writer.writerow([firstName, lastName, username, password]);

        print("Student added successfully."); #Student was added

    #Adding an instructor by collecting user details and saving them to instructors.csv
    def addInstructor(self):
        #Collect instructor's name
        firstName = input("Enter instructor's first name: ");
        lastName = input("Enter instructor's last name: ");

        #Ensure the username is unique
        uniqueName = False;
        while uniqueName == False:
            username = input("Enter instructor's username: ");
            if utility.uniqueUsername(username, "instructors.csv"): #Use the utility function to check uniqueness
                uniqueName = True; #The username is unique
                break; #Break the loop
            print("Username already exists. Choose a different username."); #Repeat the loop until unique username is chosen

        #Collect instructor password
        password = input("Enter instructor's password: ");

        #Assign a title based on user input
        title = input("Enter the instructor's title (enter 'a' for associate professor, enter 'p' for professor, enter 'l' for lecturer): ");
        if title == 'a': #a is an associate professor
            title = "Associate Professor";
        elif title == 'p': #p is a professor
            title = "Professor";
        elif title == 'l': #l is a lecturer
            title = "Lecturer";
        else: #Everything else will automatically be assigned other
            title = "Other";

        fileExists = os.path.exists('instructors.csv'); #The filepath for the instructors.csv file

        # Open the file in append mode (or create it if it doesn't exist)
        with open('instructors.csv', 'a', newline="") as file:
            writer = csv.writer(file);

            # Write headers if the file is being created for the first time
            if not fileExists:
                writer.writerow(["First Name", "Last Name", "Username", "Password", "Title"]);

            # Write the new instructor information
            writer.writerow([firstName, lastName, username, password, title]);
        
        print("Instructor added successfully."); #Instructor was added

    #Checks if the instructor exists in instructors.csv
    def checkInstructorExistence(instructorUsername):
                try:
                    with open('instructors.csv', 'r', newline="") as file:
                        reader = csv.reader(file); #Reads the file
                        next(reader); #Skip the header row
                        for row in reader:
                            if row[2] == instructorUsername: #Checks if username is in the csv file
                                return True; #Username matches
                    return False; #Username does not match
                except FileNotFoundError: #File processing error
                    print("Instructors.csv file not found.");
                    return False;

    #Adding a course by collecting course details and saving them to courses.csv
    def addCourse(self):
        while True:
            #Collect course information
            courseNumber = input("Enter course number: ");
            courseName = input("Enter course title: ");
            instructorUsername = input("Enter instructor's username: ");

            # Ensure the 'courses.csv' file exists with the correct header
            fileExists = os.path.exists('courses.csv'); #File path
            if not fileExists:
                with open('courses.csv', 'w', newline="") as file:
                    writer = csv.writer(file);
                    writer.writerow(["Course Number", "Course Title", "Instructor Username"]); #Write headers
            
            # Validate that the course number is unique
            while not utility.uniqueCourseNumber(courseNumber, "courses.csv"): #Use utiltiy function to validate unique course number
                print("Course number already exists. Choose a unique course number.");
                courseNumber = input("Enter course number: "); #Continue until a unique number is chosen

            # Validate that the instructor username exists
            while not Admin.checkInstructorExistence(instructorUsername): #Use the funtion to ensure the instructor is listed
                print("Instructor does not exist. You must add an instructor before adding a course.");
                instructorUsername = input("Enter instructor's username: "); #Continue until a valid instructor is chosen
            
            #Validate that the instructor is not already listed
            with open("courses.csv", "r", newline="") as file:
                reader = csv.reader(file);
                next(reader); #Skip the header
                for row in reader:
                    while row[2] == instructorUsername: #Checks to see if username matches csv file
                        print("Instructor username already exists. Please enter a unique username.");
                        instructorUsername = input("Enter instructor's username: "); #Continue until a unique instructor is chosen
                        # Validate that the instructor username exists
                        while not Admin.checkInstructorExistence(instructorUsername): #Use the funtion to ensure the instructor is listed
                            print("Instructor does not exist. You must add an instructor before adding a course.");
                            instructorUsername = input("Enter instructor's username: "); #Continue until a valid instructor is chosen

            #Create Course Object
            newCourse = Course(courseNumber, courseName, instructorUsername);
            
            #Save the course object data to the courses.csv file
            with open("courses.csv", "a", newline="") as file:
                writer = csv.writer(file);
                writer.writerow([
                    newCourse.getCourseNumber(), #Getter method for course number
                    newCourse.getCourseName(), #Getter method for course name
                    newCourse.getInstructor()]); #Getter method for instructor 
            
            print("Course added successfully!");
            print(
                newCourse.getCourseNumber(),
                newCourse.getCourseName(),
                newCourse.getInstructor()
            );

        
            # Ask the user if they want to add another course or go back to the main menu
            choice = input("Do you want to add another course? (yes/no): ").strip().lower();
            if choice != 'yes': #Exit to menu
                print("Returning to the main menu...");
                break; #Break the loop
              
    #View all students by reading the students.csv file
    def viewStudents(self):
        self.viewCsv("students.csv");

    #View all instructors by reading the instructors.csv file
    def viewInstructors(self):
        self.viewCsv("instructors.csv");

    #View all courses by reading the courses.csv file  
    def viewCourses(self):
        self.viewCsv("courses.csv");

    #View all enrollments by reading the enrollments.csv file    
    def viewEnrollments(self):
        self.viewCsv("enrollments.csv");

    #Action method
    def viewCsv(self, filename): #Reads a csv file and dispalys its content
        try:
            with open(filename, mode='r', newline="") as file:
                reader = csv.reader(file);
                for row in reader: #Loops through content and prints the rows
                        print(" | ".join(row));
        except FileNotFoundError: #File processing error
            print("File has not been created yet.");