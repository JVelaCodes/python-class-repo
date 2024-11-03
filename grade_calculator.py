from random import choice

def main():
    all_grades = []
    
    #Create list of grades using user input
    print("Enter grades to use or '-1' to calculate grades: ")
    while (grade := int(input("Grade: "))) != -1:
        all_grades.append(grade)
    print(f"Grades input: {all_grades}")
    
    #Remove the lowest grade from the list
    print("\nRemoving lowest grade from list...")
    all_grades.pop(all_grades.index(min(all_grades)))
    print(f"New list: {all_grades}")
    
    #Remove a random grade from the list
    print("\nRemoving random grade from list...")
    all_grades.remove(choice(all_grades))
    print(f"New list: {all_grades}")
    
    #Edit one grade from the list using user input on the index and new grade
    print("\n-- Edit grade list --")
    for i in all_grades:
        print(f"Index: {all_grades.index(i) + 1} ; Grade: {i}")
    while (change_index := int(input(f"\nEnter the index of the grade to change (1-{len(all_grades)}): "))) not in range(1,len(all_grades)+1):
        print("Please input an index within the list")
    all_grades[change_index - 1] = int(input("Enter the new grade: "))
    print(f"New list: {all_grades}")
    
    #Sort and reverse the list
    print("\nSorting and Reversing list...")
    all_grades.sort()
    all_grades = all_grades[::-1]
    print(f"New list: {all_grades}")
    
    #Get total and average of grades in list
    print("\nCalculating grades total and average...")
    print(f"Total of grades: {sum(all_grades)}")
    print(f"Average of grades: {sum(all_grades) / len(all_grades)}")
    
    
if __name__ == "__main__":
    main()
    print("\nCompleted by, Jeremiah Vela")
