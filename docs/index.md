Kyle O’Donnell  
August 24, 2020  
Foundations of Programming: Python  
Assignment07  

# Pickling and Exception Handling in Python 

## Introduction  
This paper documents the process of creating a Python script that demonstrates pickling and structured error-handling. The product of this week’s assignment is a simple program, Assignment07.py, that lets dog-oriented businesses manage their database of dog clients. Topics covered in this assignment include binary files and exceptions. Additionally, the paper discusses online resources that were used for this assignment. 

## Writing the Script 
Assignment07.py was created from scratch in PyCharm. Although it did not have a starting template, the structure of the script and several of its custom functions were based on previous assignments. As a first step, I created a new Python project in the Assignment07 directory and updated the header for this project (Figure 1).

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture1.png "Screenshot of Script in PyCharm")
Figure 1. Screenshot of Script in PyCharm

This program is designed to be used by dog-oriented businesses, such as groomers, dog-walkers and boarders. When users launch the program, they can select one of the following options to help manage their dog database:
1)	View a list of their clients by name
2)	Add a new client
3)	Search information for a specific client
4)	Save new data to their database
5)	Exit the program



### Script Overview
The script has three main sections – data, processing and presentation. 

The data layer declares objects that are used by the program (Figure 2).
![Data Section of Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture2.png "Data Section of Script")   
Figure 2. Data Section of Script  

The processing section includes custom functions for processing, input/output functions and custom exception classes (Figure 3-5).
![Processing Functions](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture3.png "Processing Functions")
Figure 3. Processing Functions

![Input/Output Functions](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture4.png "Input/Output Functions")
Figure 4. Input/Output Functions

![Custom Exceptions](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture5.png "Custom Exceptions")
Figure 5. Custom Exceptions

The last section is the main body of the script, which provides logic for calling functions and interacting with users (Figure 6).

![Main Boy of Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture6.png "Main Boy of Script")
Figure 6. Main Boy of Script

### Pickling
In previous assignments, I have read, written and appended data to text files. In contrast, this week’s program uses pickling to load and save data to a binary file. There are several reasons to pickle data instead of using a text file. First, pickling can preserve the structure of complex Python objects which might otherwise be lost when saving to a text file. Second, pickling is used with binary files which take up less memory than other types of files. Some of the limitations of pickling include the fact it can only work with certain types of objects, is limited to Python structures, and the output is not user-friendly (i.e. difficult to read).


The first line of the Assignment07.py script imports the pickle module so that pickle functions can be used later in the script:
```
import pickle
```
Listing 1

#### Loading Data with Pickle
The first custom function, read_data_from_file(), uses pickle.load() to read data from a binary file (the objFile is assigned to the file ClientData.dat in the data section). More specifically, the function is “de-serializing” data into Python data structures from the binary stream that it was previously saved to.  
```
def read_data_from_file(file_name, list_of_clients):
    try:
         objFile = open(file_name, "rb")
         list_of_clients = pickle.load(objFile)
          objFile.close()
     except FileNotFoundError:
         print("I see you haven't started a database yet!\nThat's okay! We're here to help you get started.\n")
     return list_of_clients
```
Listing 2

The pickle.load() function will only load one object at a time (picking up where it left off within the open file). In this case, the program saves the database to a single list object that can be loaded all at once, otherwise that would have to be further accounted for in the program. The file is opened in “rb” or “read binary” mode, because it needs to read data from a binary file.


Figure 7 shows how binary data appears within a text editor. Although the format is not user-friendly, it is still somewhat interpretable.
![Binary File in Text Editor](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture7.png "Binary File in Text Editor")
Figure 7. Binary File in Text Editor

Once the data is loaded into a python list through pickling (Figure 8), it looks like a normal Python dictionary within a list (Figure 9).

![Loading Data with Pickle](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture8.png "Loading Data with Pickle")
Figure 8. Loading Data with Pickle

![Print Data Loaded from Binary File with Pickle](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture9.png "Print Data Loaded from Binary File with Pickle")
Figure 9. Print Data Loaded from Binary File with Pickle

#### Saving Data with Pickle 
Pickling can also be used to store data. In the function save_data_to_file, I use pickle.dump() to “serialize” the current client data back to the binary format. In this case, the file is opened in “wb” or “write binary” mode to write data to a binary file.
```
    def save_data_to_file(file_name, list_of_clients):
        object_file = open(file_name, "wb")
        pickle.dump(list_of_clients, object_file)
        object_file.close()
        return list_of_clients
```
Listing 3

#### Pickling Research
While working on this script, I read through several online resources about Python pickle. The one I found most useful was a Medium article appropriately titled **Pickling in Python** by Alison Salerno. I appreciated that was a high-level overview that did not presuppose prior knowledge of other programming languages. Other articles either seemed to provide a comprehensive overview of pickling parameters or were meant to address specific use-cases for developers. This article concisely distilled high-level concepts, balancing prose with images and code examples. The article is available at the following link:

https://medium.com/swlh/pickling-in-python-ac3c7a045ae5

### Exception Handling
#### Built-in Exceptions
Another concept explored thoroughly in week 7 was Try-Except error handling. When an error occurs while running Python, the program provides information on the type of error that occurred. For example, if you try to cast a string of letters as an integer, Python will return a ValueError, because it cannot perform that function on that value (Figure 10):
![Built-in ValueError in Python](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture10.png "Built-in ValueError in Python")
Figure 10. Built-in ValueError in Python

Although we ideally prefer to avoid errors, there are many instances in which its helpful to identify different types of errors so that they can be handled appropriately within a program. Python has a large number of built-in errors known as exceptions that can be leveraged for this purpose. In the read_data_from_file() function used at the beginning of the script, I employed try-except clauses and the built-in FileNotFoundError to handle instances in which the file being read does not yet exist. 
```
def read_data_from_file(file_name, list_of_clients):
    try:
         objFile = open(file_name, "rb")
         list_of_clients = pickle.load(objFile)
          objFile.close()
     except FileNotFoundError:
         print("I see you haven't started a database yet!\nThat's okay! We're here to help you get started.\n")
     return list_of_clients
```
Listing 4

First, the function will try to load data from the object file. If the file is not found, it will skip to the except clause for FileNotFoundError and print the string below it. Because the error value already exists in Python, I was able to create the except clause without having to add much additional logic. When the except clause is reached, it will simply print the string from the statement and the program will continue running (Figure 11). By contrast, if I did not include the clause, the error would still occur, but the displayed message would not be user-friendly (Figures 12).

![FileNotFoundError without Exception Clause in Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture11.png "FileNotFoundError without Exception Clause in Script")
Figure 11. FileNotFoundError without Exception Clause in Script

![FileNotFoundError with Excpetion Handling in Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture12.png "FileNotFoundError with Excpetion Handling in Script")
Figure 12. FileNotFoundError with Excpetion Handling in Script

In the get_client_data() function, I create an except clause for the built-in ValueError to catch instances in which the “age” input cannot be cast as an integer.
```
    def get_client_data():
        client = str(input("Enter name: \n ").capitalize())
        while True:
            try:
                age = int(input("Enter age: \n "))
                break
            except ValueError:
                print("Please enter age as the nearest round number!")
```
Listing 5

In this case, the try-except clause occurs within a while loop. If the user enters a non-integer value that goes to this exception, they will be prompted to reenter a menu option. Once they input a valid age, the loop breaks and the program moves on to the next line of code.

#### Custom Excpetions
In addition to leveraging existing exceptions, Python makes it easy to create custom exception classes derived from the same class. The advantage of the custom classes is that they can handle use-cases specific to your program design. In Assignment07.py, I created two custom classes shown in Listing 6.
```
class ValueTooLargeError(Exception):
    """ Value too large for menu input """
    def __str__(self):
        return '"Please select an option between 1-5!"'

class StopError(Exception):
    """ Close program  """
    def __str__(self):
        return 'Closing Program...Goodbye!'
```
Listing 6

The ValueTooLargeError catches instances in which the user menu option input is an integer above 5 (the menu options are 1-5).

The StopError handles instances in which the user has implemented a non-integer string that clearly indicates they want to leave the program. This error is included to distinguish these inputs from more generic ValueErrors in which the user has simply entered a non-integer value.

These exceptions are used in the main body of the script. 
```
while True:
    IO.print_menu_tasks()
    try:
        strChoice = IO.input_menu_choice()
        if strChoice in ["quit", "close", "leave", "exit", "stop"]:
            raise StopError
        intChoice = int(strChoice)
        if intChoice > 5:
            raise ValueTooLargeError
    except ValueError:
            print("Please provide a number input!")
    except ValueTooLargeError as e:
        print(e)
    except StopError as e:
        print(e)
        break
    else:
        if intChoice == 1:
```
Listing 7

When users provide an input, I first check to see if the string matches any “quit” words. I then raise the custom StopError, which prints the string from the Exception and breaks the loop. 

Next, I cast the input as an integer. If the input string cannot be cast as an integer, it will automatically raise a ValueError and go to the exception clauses for ValueError. If the input is an integer above 5, it was reach the ValueTooLargeError. Note that for the custom classes, the errors must be manually raised through logic built into the program. 

If none of the exceptions are raised, the program goes to the else clause and executes one of the menu functions.

#### Exception Handling Research
I found two sites that were particularly helpful for learning about exception handling:
•	TechBeamers (https://www.techbeamers.com/use-try-except-python/)
•	Programiz (https://www.programiz.com/python-programming/user-defined-exception)

Both pages provide high-level information about exceptions without including too much technical detail or requiring background knowledge of programming. The visual layouts make them easy to navigate and both use abundant images to help illustrate their points. Programiz has the additional feature of allowing visitors to run code directly on their site.


## Testing in PyCharm  
Once the script was completed, I tested it in Pycharm. Figures 13-17 show each of the exceptions being handled by the program as expected.

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture13.png)
Figure 13. Exception Handling for FileNotFoundError in Script

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture14.png)
Figure 14. Exception Handling for ValueError in Script - 1

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture15.png)
Figure 15. Exception Handling for ValueError in Script - 2

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture16.png)
Figure 16. Exception Handling for Custom Exception ValueTooLargeError

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/PictureLOST.png)
Figure 17. Excpetion Handling for Custom Exception StopError


## Running in Terminal 
Next, I ran the program in Terminal as a Console application. Figures 18-22 show the programs tasks and exceptions performing correctly.

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture17.png)
Figure 18. View Client List

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture18.png)
Figure 19. Add New Client

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture19.png)
Figure 20. Search Client Data

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture20.png)
Figure 21. Custom Exception ValueTooLargeError

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture21.png)
Figure 22. Custom Exception StopError

## Checking the Binary File 
As a final step, I checked the binary file "ClientData.dat" that the pickled data was saved to. Figure 23 shows the data from the previous step had been saved to the file.
![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture22.png)
Figure 23. Viewing Data with Saved Binary Data

## Summary 
