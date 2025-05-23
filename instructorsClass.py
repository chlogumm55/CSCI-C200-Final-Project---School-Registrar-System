"""
Filename: instructorsClass.py

Problem Description: This design demonstrates the algorithm for the Instructor Module of the course project. An instructor can login to the system and see all the courses assigned to teach. The csv file generated in the Admin module will be used to authenticate a user. The csv file contains 5 columns, with the username stored in the third column and password stored in the fourth column. Users will be allowed to enter the wrong username and password 5 times. Course information is stored in the csv file generated by the Admin module. The csv file contains course numbers, course titles, and instructor usernames. Only rows with the matching username will be displayed.

First Create Date: April 22nd, 2025
Last Update Date: April 23rd, 2025
Author: Chloie Gummer
Version: 1.1
"""
import utility; #Importing utility file
import csv; #Importing csv module
import os; #Importing operating system module
from userClass import User; #Importing User class as the parent

class Instructor (User): #Instructor class is the child of the User class
    title = "";  #Default title attribute

    #Constructor to initialize the instructor class using the User class
    def __init__(self, firstName, lastName, username, password, title): 
        super().__init__(firstName, lastName, username, password);
        self.title = title; #Assign instructor title

    def __str__(self):
        return{
            #String representation of an Instructor object
            "Instructor: \n"
            "First Name - " + self.firstName + "\n"
            "Last Name - " + self.lastName + "\n"
            "Username - " + self.username + "\n"
            "Password - " + self.password + "\n"
            "Title - " + self.title + "\n"
        };

    #Setter method 
    def setTitle(self, title):
        self.title = title; #Update the instructor's title

    #Getter method
    def getTitle(self):
        return self.title; #Returns the instructor's title

    #Action method

    #Displays the courses assigned to the instructor by checking courses.csv
    def viewAssignedCourses(self):
        fileExists = os.path.exists('courses.csv');
        if not fileExists:
            print("Please ensure courses have been added.");
            return;

        try:
            #Open and read the courses file
            with open('courses.csv', "r", newline="") as file:
                reader = csv.reader(file);
                headers = next(reader); #Get headers
                assignedCourses = [row for row in reader if row[2] == self.username]; #Filter courses assigned to the instructor

                if assignedCourses:
                    print("Courses Assigned to " + self.username + "\n");
                    print(" | ".join(headers)); #Display headers
                    for course in assignedCourses:
                        print(" | ".join(course)); #Loop through and display all assigned courses
                else:
                    print("No courses assigned to " + self.username);
        except FileNotFoundError: #File processing error
            print("Error: courses.csv file not found");

 

