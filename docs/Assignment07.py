# ------------------------------------------------- #
# Title: Assignment07.py
# Description: Simple Program that uses pickle and exceptions
# ChangeLog: (Who, When, What)
# KODonnell,<8.23.2020>,Created Script
# ------------------------------------------------- #


import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
# Declare variables and constants

strFileName = 'ClientData.dat'  # Name of binary data file
objFile = None   # Object that represents the file
strClientName = ''  # Client name string
lstClients = []   # List of clients
strChoice = ''   # Menu option string
intChoice = None   # Menu option integer
dicNewClientInfo = {}  # Dictionary with new client info

# Processing -------------------------------------- #
class Processor:
    """  Performs Processing tasks """    \

    @staticmethod
    def read_data_from_file(file_name, list_of_clients):  # Load data from binary file
        """ Reads data from a binary file into a list
        :param file_name: (string) with name of file:
        :param list_of_clients: (list) you want filled with file data:
        :return: (list) of data
        """
        try:
            objFile = open(file_name, "rb")
            list_of_clients = pickle.load(objFile)  # Save data to list
            objFile.close()
        except FileNotFoundError:
           print("I see you haven't started a database yet!\nThat's okay! We're here to help you get started.\n")
        return list_of_clients

    @staticmethod
    def save_data_to_file(file_name, list_of_clients):  # Save list to file
        """ Saves data to a binary file
        :param file_name: (string) with name of file:
        :param list_of_clients: (list) you want to save to file:
        :return: (list) of data
        """
        object_file = open(file_name, "wb")
        pickle.dump(list_of_clients, object_file)
        object_file.close()
        return list_of_clients

    @staticmethod
    def add_new_client(client_data, list_of_clients):  # Add data for new client to list
        """ Adds new client data to client database
        :param client_data: (dic) with client data:
        :param list_of_clients: (list) you want to add new client to:
        :return: (list) of data
        """
        dicRow = (client_data)
        list_of_clients.append(dicRow)
        return list_of_clients

    @staticmethod
    def search_client_info(client, list_of_clients):  # Search client info by name
        """ Retrieves data for specific client
        :param client: (string) name of client being searched for:
        :param list_of_clients: (list) database with client information:
        :return: nothing
        """
        for dicRow in list_of_clients:
            if dicRow["Name"].lower().strip() == client.lower().strip():
                print("\n\tClient Name:", dicRow["Name"],
                      "\n\tAge:", dicRow["Age"],
                      "\n\tBreed:", dicRow["Breed"],
                      "\n\tNotes:", dicRow["Notes"])

# Presentation ------------------------------------ #
class IO:

    @staticmethod
    def welcome_message():  # Prints welcome message
        """ Welcome users to program
        :return: nothing
        """
        print("\nWelcome to your DogForce - Your Business' Best Friend!!!!\n"
              "We'll help you manage your growing list of dog clients!")
        print()

    @staticmethod
    def press_enter():  # Creates pauses in program
        """ Provide pauses while running program
        :return: nothing
        """
        enter = input("Press enter to continue ")

    @staticmethod
    def print_menu_tasks():  # Print options menu
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) See List of Clients
        2) Add a New Client
        3) Search for Client Information
        4) Save Data to Computer      
        5) Exit Program
        ''')
        print()  # Add an extra line for looks


    @staticmethod
    def input_menu_choice():  # Prompt users for menu choice
        """ Prompt user for menu choice
        :return: choice
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_clients(list_of_rows):  # Print list of client names
        """ Print list of current clients
        :return: nothing
        """
        print("******* Current Client List: *******")
        count = 0
        for row in list_of_rows:
            count += 1
            print(str(count) + ". " + row["Name"].capitalize())
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def get_client_data():  # Prompt user for new client data
        """ Search data by client
        :return: client_data
        """
        client = str(input("Enter name: \n ").capitalize())
        while True:
            try:
                age = int(input("Enter age: \n "))
                break
            except ValueError:
                print("Please enter age as the nearest round number!")
        breed = str(input("Enter breed: \n "))
        notes = str(input("Enter any additional notes on {}.\n ".format(client)))
        client_data = {"Name": client, "Age": age, "Breed": breed, "Notes": notes}
        return client_data


    @staticmethod
    def input_search_client():  # Prompt for client name to search
        client = str(input("What client would you like to look up? \n "))
        return client


# Exceptions ------------------------------------------------------ #

class ValueTooLargeError(Exception):  # Exception for numbers over 5
    """ Value too large for menu input """
    def __str__(self):
        return 'Please select an option between 1-5!'


class StopError(Exception):  # Exception for users that want to quit
    """ Close program  """
    def __str__(self):
        return 'Closing Program...Goodbye!'

# Main Body of Script  ------------------------------------------------------ #

IO.welcome_message()  # Print welcome
IO.press_enter()
lstClients = Processor.read_data_from_file(strFileName, lstClients)  # Read file data


while True:

    IO.print_menu_tasks()  # Prompt for menu choice
    try:
        strChoice = IO.input_menu_choice()
        if strChoice in ["quit", "close", "leave", "exit", "stop"]:  # Raise exception for "quit" words
            raise StopError
        intChoice = int(strChoice)  # Raise exception for non-integers
        if intChoice > 5:  # Raise exception for values over 5
            raise ValueTooLargeError
    except ValueError:
            print("Please provide a number input!")
    except ValueTooLargeError as e:
        print(e)
    except StopError as e:
        print(e)
        break
    else:
        if intChoice == 1:  # Print current list
            IO.print_current_clients(lstClients)
            IO.press_enter()
            continue
        elif intChoice == 2:  # Add new client info
            dicNewClientInfo = IO.get_client_data()
            Processor.add_new_client(dicNewClientInfo, lstClients)
            print(dicNewClientInfo["Name"], "has been saved to your database!")
            IO.press_enter()
            continue
        elif intChoice == 3:  # Search existing client
            strClientName = IO.input_search_client()
            Processor.search_client_info(strClientName, lstClients)
            IO.press_enter()
            continue
        elif intChoice == 4:  # Save list to binary file
            Processor.save_data_to_file(strFileName, lstClients)
            print("Data Saved to ClientData.dat")
            IO.press_enter()
            continue
        elif intChoice == 5:   # Close program
            print("Goodbye")
            break




