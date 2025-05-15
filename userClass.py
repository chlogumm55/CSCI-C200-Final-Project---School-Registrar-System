"""
Filename: userClass.py

Problem Description: This design demonstrates the algorithm for the user class of the course project. The user class will be the parent class of the instructor, student, and admin classes. The user class includes the universal properties of every user, an init method to intialize the properties, setter and getter methods to access or change the values, and lastly two action methods. The first is the login method to validate the user entering the program, and lasatly is a method to exit the program at any time.
 

First Create Date: April 22nd, 2025
Last Update Date: April 23rd, 2025
Author: Chloie Gummer
Version: 1.1
"""
import utility; #Importing utility file

class User: #The main parent class of the project
    firstName = ""; #Default first name
    lastName = ""; #Default last name
    username = ""; #Default username
    password = ""; #Default password

    #Constructor to initalize a user object with personal details
    def __init__(self, firstName, lastName, username, password):
        self.firstName = firstName;
        self.lastName = lastName;
        self.username = username;
        self.password = password;

    def __str__(self):
        return{
            #String representation of a User object
            "User: \n"
            "First Name - " + self.firstName + "\n"
            "Last Name - " + self.lastName + "\n"
            "Username - " + self.username + "\n"
            "Password - " + self.password + "\n"
        };

    #Setter methods for updating user attributes
    def setFirstName(self, firstName):
        self.firstName = firstName; #Updates the first name of the user

    def setLastName(self, lastName):
        self.lastName = lastName; #Updates the last name of the user

    def setUsername(self, username):
        self.username = username; #Updates the username of the user

    def setPassword(self, password):
        self.password = password; #Updates the password of the user

    #Getter methods for retrieving user attributes
    def getFirstName(self):
        return self.firstName; #Returns the first name of the user

    def getLastName(self):
        return self.lastName; #Returns the last name of the user

    def getUsername(self):
        return self.username; #Returns the username of the user

    def getPassword(self):
        return self.password; #Returns the password of the user

    #Action Methods

    #Authenticates the user by calling the utility files authentication function
    def login(self, tag):
        userObj = {"username": self.username, "password": self.password};
        return utility.authenticateUser(userObj, tag);

    #Exits the program with a message
    def exit(self):
        print("Exiting the Program.");