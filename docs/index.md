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

The processing section includes custom functions for processing, input/output function and custom exception classes (Figure 3-5).
![Processing Functions](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture3.png "Processing Functions")
Figure 3. Processing Functions

![Input/Output Funcitons](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture4.png "Input/Output Funcitons")
Figure 4. Input/Output Funcitons

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

![Binary File in Text Editor](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture7.png "Binary File in Text Editor")
Figure 7. Binary File in Text Editor

![Loading Data with Pickle](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture8.png "Loading Data with Pickle")
Figure 8. Loading Data with Pickle

![Print Data Loaded from Binary File with Pickle](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture9.png "Print Data Loaded from Binary File with Pickle")
Figure 9. Print Data Loaded from Binary File with Pickle

#### Saving Data with Pickle 

```
    def save_data_to_file(file_name, list_of_clients):
        object_file = open(file_name, "wb")
        pickle.dump(list_of_clients, object_file)
        object_file.close()
        return list_of_clients
```
Listing 3


#### Pickling Research


### Exception Handling
#### Built-in Exceptions

![Built-in ValueError in Python](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture10.png "Built-in ValueError in Python")
Figure 10. Built-in ValueError in Python


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

![FileNotFoundError without Exception Clause in Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture11.png "FileNotFoundError without Exception Clause in Script")
Figure 11. FileNotFoundError without Exception Clause in Script

![FileNotFoundError with Excpetion Handling in Script](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture12.png "FileNotFoundError with Excpetion Handling in Script")
Figure 12. FileNotFoundError with Excpetion Handling in Script

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


#### Custom Excpetions

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



#### Exception Handling Research
## Testing in PyCharm  

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

![Screenshot of new script in PyCharm](https://raw.githubusercontent.com/kylenod/ITFDN-Mod07/master/Images/Picture22.png)
Figure 23. Viewing Data with Saved Binary Data

## Summary 
