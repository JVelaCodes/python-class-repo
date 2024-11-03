from random import randint


def employee_creation(employees):
    #Ask for employee name; check name doesn't exist, add name to list
    while (name := input("Input new employee name: ").lower().title()) in [i['Employee'] for i in employees]: 
        print("Error: Name Already Exists; Input a different name")
    
    #generate randint 1-500 for ID; check id isn't being used, add id to list
    while (ID := randint(1, 500)) in [employee_info['ID'] for employee_info in employees]:
        continue
    
    #create employee dictionary with name & id fields; add new employee dictionary to employee list
    employees.append({'Employee':name, 'ID':ID})


def employee_output(employee):
        print("Created Employee:\t{Employee}\nEmployee ID:\t\t{ID}".format(**employee))


def main():
    line = "=================================================="
    print(f"{line}\nOrganization Employee Log\n{line}")
    
    #Employee Information Variables
    employee_info = [{'Employee':'FLAG', 'ID':123}]
    
    #Get number of employees to add
    for i in range(total := int(input("\nInput the number of employees to add to the Employee Log: "))):
        if i == 0: print(f"\n{line}")
        
        #Adding to Log
        employee_creation(employee_info)
        
        #Outputting additions from Log
        if i == total - 1:
            print(f"{line}\n\nCreated User Information")
            for j in range(total):
                print(line)
                employee_output(employee_info[(total - j) * -1]) #will only output for new employees, even if start_list !empty
    
    print(f"\n{line}")
    
    
if __name__ == '__main__':
    main()
    print('Completed by, Jeremiah Vela')