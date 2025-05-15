"""
Filename: courseClass.py

Problem Description: This design demonstrates the algorithm for the course class of the final project. The course class will inherit an object instance of the instructor class, which is who's teaching the course. The course class includes properties related to courses, such as numbers and names, an init method, a str method, setter and getter methods to access or change the values. 
 

First Create Date: April 28th, 2025
Last Update Date: April 28th, 2025
Author: Chloie Gummer
Version: 1.1
"""

#Importing the necessary modules for csv files and operating systens 
import csv;
import os;
from instructorsClass import Instructor; #Importing the instructor class

class Course:
    courseNumber = 0; #Default course number
    courseName = ""; #Default course name

    #Constructor to initialize a course object with course number, course name, and instructor
    def __init__(self, courseNumber, courseName, instructor):
        self.courseNumber = courseNumber;
        self.courseName = courseName;
        self.instructor = instructor; #Instructor object

    def __str__(self):
        #A string representation of the details of the Course object
        return {
            "Course Number: " + str(self.courseNumber) + " \n"
            "Course Name: " + (self.courseName) + "\n"
            "Instructor: " + (self.instructor) + "\n"
        };

    #Setter Methods
    def setCourseName (self, courseName):
        self.courseName = courseName; #Updates the course name

    def setCourseNumber (self, courseNumber):
        self.courseNumber = courseNumber; #Updates the course number

    def setInstructor (self, instructor):
        self.instructor = instructor; #Updates the instructor assigned to the course

    #Getter Methods
    def getCourseNumber (self):
        return self.courseNumber; #Returns the course number

    def getCourseName (self):
        return self.courseName; #Returns the course name

    def getInstructor (self):
        return self.instructor; #Returns the instructor assigned to the course