first_name = input("Input your First Name: ")
last_name = input("Input your Last Name: ")
current_year = int(input("Input the Current Year: "))
birth_year = int(input("Input your Birth Year: "))

age = current_year - birth_year


print('\n' + "Hello", first_name, last_name + "!",'\n' + "You are",str(age),"years old this year.")

age += 1

print('\n' + f"In the next year {current_year + 1}, you will be {age} years old.")
print('\n' + "------------------------------",'\n' + "Completed by, Jeremiah Vela")
