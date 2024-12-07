#function to obtain string input 
def user_input(prompt):     #prompt as arg
    output = input(prompt)
    return output           #returns input to save as var

#function to determine if substring is in main string
def search(main_string, substring):
    print("\nSearching for substring within main string..." + '\n' + '-'*45)
    if (index := main_string.find(substring)) != -1:                #finds out if substring is in main string; finds where using .find() method
        print(f"String: '{substring}' found at index {index}")      #prints starting index if substring is found in main string
    else:
        print("String not found")
    return index    #returns the index of substring in main string if found, else -1

def replace_string(main_string, substring):                        
    print("\nStarting string replacement process...",
        '\n' + '-'*40)
    while (choice := user_input("Do you want to replace the string? (y/n): ").lower()) not in ('y','n'):    #use custom input func to ask if the user wants to replace the found string
        print("Invalid choice. Please enter 'y' or 'n'")                                                    #reprompts user if input isn't "y" or "n" (invalid entry)
    if choice == 'y':                                               #check that user enters 'y'
        replacement = user_input("Input replacement string: ")      #get replacement string
        main_string = main_string.replace(substring, replacement)   #replace substring with replacement string in main string
        print(f"New String: {main_string}")                         #output new main string
    else:
        print("No replacement made")    #outputs that no replacement was made if user enters 'n'

def main():
    print("Welcome to the String Replacement Tool!" + 
          "\n" + "-"*40)
    main_string = user_input("Input string to search through: ")    #custom input func for getting main string
    substring = user_input("Input string to search for: ")          #custom input func for getting substring
    
    if search(main_string, substring) != -1:    #check if index is an acceptable value
        replace_string(main_string, substring)  #use a function to check if the user wants to replace a string, and replace it if yes

    print("\nThanks for using this program!")   #output a message thanking the user for using the program

if __name__ == "__main__":
    main()
    print("Completed by, Jeremiah Vela")        #print completed by statement
