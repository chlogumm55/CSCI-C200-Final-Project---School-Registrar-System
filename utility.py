"""
Filename: utility.py

Problem Description: This file is used as a utility file across the entire program. It contains universal functions that will be used universally throughout different classes. The functions range from login validation, checking uniqueness, to tidying up rows of values.

First Create Date: April 22nd, 2025
Last Update Date: April 23rd, 2025
Author: Chloie Gummer
Version: 1.1
"""

import csv; #Importing the csv module

#Authenticates the user by checking their username and password against a csv file
def authenticateUser(userObj, filename):
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file); #Reading the csv file
            next(reader); # Skip the header row
            for row in reader:
                #Compare username and password and remove extra spaces using strip
                if row[2].strip() == userObj.username.strip() and row[3].strip() == userObj.password.strip():
                    return True; #True if match is found
        print("No match found in CSV."); #False if no match is found
        return False;
    except FileNotFoundError: #Error for file processing
        print("admin.csv file not found");
        return False; #Returns false


#Checks if the given username is unique within a csv file
def uniqueUsername(username, filepath):
    try:
        with open(filepath, newline='') as file:
            reader = csv.reader(file); #Reading the csv file
            next(reader); #Skip the header row
            for row in reader:
                if row[2] == username: #Check if username exists in the csv file
                    return False; #Username is not unique
    except FileNotFoundError: #Error for file processing
        return True;
    return True; #The username is unique

#Checks if the given course number is unique wwithin a csv file
def uniqueCourseNumber(courseNumber, filepath):
    try:
        with open(filepath, newline='') as file:
            reader=csv.reader(file); #Reading the csv file
            for row in reader:
                if row[0] == courseNumber: #Check if the course number exists in the csv file
                    return False; #Course number is not unique
    except FileNotFoundError: #Error for file processing
        return True;
    return True; #Course number is unique

#Appends a row to a csv file, optionally adding headers if the file is newly created
def appendCsv(filename, row, headers=None):
    fileExists = False;
    try:
        with open(filename, "r") as file:  # Check if file exists
            fileExists = True;
    except FileNotFoundError:
        pass  # File does not exist

    with open(filename, mode="a", newline="") as file:  # Open in append mode
        writer = csv.writer(file);
        if not fileExists and headers:  # Add headers if file is being created
            writer.writerow(headers);
        writer.writerow(row);  # Append the row
