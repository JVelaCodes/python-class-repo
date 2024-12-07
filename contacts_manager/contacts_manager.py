import csv

def create_csv():
    with open("contacts.csv", 'w', newline="") as file: #Create a new CSV file
        writer = csv.writer(file)
        writer.writerow(["Name\t","Phone\t","Email"]) #write row for header including Name, Phone, Email
    print("\nFile created successfully") #print that file was created successfully

def add_contact():
    new_info = [input("Enter name for new contact: ").lower().title(),  #get input for Name, Phone, Email
                input("Enter phone number for new contact: "),
                input("Enter email for new contact: ")]
    with open("contacts.csv", 'a', newline='') as file: #append row to bottom of CSV file with input values
        writer = csv.writer(file)
        writer.writerow(new_info)
    print("\nContact added successfully") #print that contact was added successfullyimport csv

def view_csv():
    print('All Contacts:')
    with open("contacts.csv", 'r', newline="") as file: #open CSV file and read all rows
        for row in csv.reader(file): #output with basic formatting and no empty lines between rows
            print(f"{row[0]}\t{row[1]}\t{row[2]}")


def edit_contact(): #done
    view_csv() #output existing contacts
    
    contacts = []
    with open("contacts.csv", 'r', newline="") as file: #read the content of file and save to array/list
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    while (entry := input("\nEnter the name of the contact to edit: ").lower().title()) not in [row[0] for row in contacts[1:]]: #ask user to select entry to edit; if contact not found, ouput not found error msg
        print("Please enter a valid contact name")
    
    #originally: contacts[['correct_row' if entry in row else '' for row in contacts].index('correct_row')] = [entry, input("Enter new phone number: "), input("Enter new email: ")] #ask user to input new values for Name, Phone, Email -- didn't keep current for blank inputs
    contacts[contacts.index(next(contact for contact in contacts if entry in contact))] = [entry, contacts[contacts.index(next(contact for contact in contacts if entry in contact))][1] if (new_phone := input("Enter new phone number (leave blank to keep current): ")) == '' else new_phone, contacts[contacts.index(next(contact for contact in contacts if entry in contact))][2] if (new_email := input("Enter new email (leave blank to keep current): ")) == '' else new_email] #iterate through sublists to find sublist with entry in it, and use value in that if values are left blank

    print("\nContact updated successfully") #output that contact was updated successfully
    with open("contacts.csv", 'w', newline="") as file: #write new values to CSV file
        writer = csv.writer(file)
        for contact in  contacts:
            writer.writerow(contact)

def main():

    #print purpose
    line = "-"*35
    print(f"{line}\nContacts Manager")

    while(True):
        print(f"{line}\n" + 
            "\n1 - Create a new contacts file" + 
            "\n2 - Add a new contact" + 
            "\n3 - View all contacts" +
            "\n4 - Modify an existing contact" +
            "\n5 - Exit" +
            "\n")
    
        while (user_choice := int(input("Enter an option to perform an action(1 - 5): "))) not in range(1,6):
            print("Please enter a valid number for an action")
        
        print('\n' + line + '\n')
        
        if user_choice == 1: create_csv() #create new contact csv file in new function
        elif user_choice == 2: add_contact() #add new contact to file using append method
        elif user_choice == 3: view_csv() #read all contacts in file and output through console
        elif user_choice == 4: edit_contact() #modify existing contact in file
        else: break #exit program

if __name__ == "__main__":
    main()
    print("Completed by, Jeremiah Vela")
