import datetime as dt
import csv

def created_by(name):
    print(f"Created by, {name}")

def get_current_time():
    return dt.datetime.now().strftime("%m/%d/%y %H:%M")

def read_file():
    with open('employee_contact_info.txt', 'r') as file:
        return [line.strip().split() for line in file]

def list_directory(employee_info):
    print(f"{'':4} {'Name':20} {'Email':30}")
    for index, employee in enumerate(employee_info, start=1):
        print(f"{str(index)+'.':4} {employee[0]:20} {employee[1]:30}")

def output_file(employee_info):
    filename = input("Enter your chosen file name (no extension): ")
    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employee_info)

def edit_directory(employee_info):
    list_directory(employee_info)

    while True:
        try:
            user_selection = int(input("Enter the index of the item you would like to edit (0 to close): ")) - 1
            if user_selection == -1:
                break
            if user_selection < 0 or user_selection > len(employee_info) - 1:
                raise ValueError("Value is outside of valid range; please input a valid option")
            print(f"\nEditing employee information for user: {employee_info[user_selection][0]}\n" +
                  f"Current email: {employee_info[user_selection][1]}")
            new_name = input("\nEnter the new name (or leave blank to not change): ")
            new_email = input("Enter the new email address (or leave blank to not change): ")
            if new_name != '':
                employee_info[user_selection][0] = new_name
            if new_email != '':
                employee_info[user_selection][1] = new_email
            break
        except Exception as e:
            print(f"Error Occurred: {e}")

def delete_entry(employee_info):
    list_directory(employee_info)

    while True:
        try:
            user_selection = int(input("Enter the index of the item you would like to delete (0 to close): ")) - 1
            if user_selection == -1:
                break
            if user_selection < 0 or user_selection > len(employee_info) - 1:
                raise ValueError("Value is outside of valid range; please input a valid option")
            print(f"Deleting employee information for user: {employee_info[user_selection][0]}")
            del employee_info[user_selection]
            break
        except Exception as e:
            print(f"Error Occurred: {e}")


def main():
    print_line = '-'*45
    print("Welcome to the Employee Contact Directory\n" + print_line)
    print(f"Starting time: {get_current_time()}")

    employee_info = read_file()

    while True:
        print(print_line)
        list_directory(employee_info)
        try:
            print(print_line)
            print("Options:",
                  "\n1. Edit existing employee information",
                  "\n2. Delete existing employee information",
                  "\n3. Save the file and quit",
                  "\n4. Force exit the program without saving")
            user_option = int(input("Select the number of the action you would like to perform: "))
            if user_option == 1:
                edit_directory(employee_info)
            elif user_option == 2:
                delete_entry(employee_info)
            elif user_option == 3:
                output_file(employee_info)
                break
            elif user_option == 4:
                break
            else:
                raise ValueError("Value is outside of valid range; please input a valid option")
            print()

        except Exception as e:
            print(f"Error Occurred: {e}")
    
    print(f"Ending time: {get_current_time()}\n" + print_line)

if __name__ == "__main__":
    main()
    created_by("Jeremiah Vela")