def main():
    student_info = {}
    student_info["Jim"] = {"ID" : 1,
                          "GPA" : 3.1,
                          "Credits_Completed" : 97,
                          "Grades" : [80,50,100,98]}
    
    student_info["Sarah"] = {"ID" : 2,
                          "GPA" : 3.6,
                          "Credits_Completed" : 40,
                          "Grades" : [80,98]}
    
    #Full Dictionary
    print(student_info)
    
    #Students
    print("\nList of students:")
    for student in student_info:
        print(student)
    
    #Student Info
    print("\nStudent Information:")
    print("Student ", '\t\t'.join(["ID","GPA","Credits Completed","Grades"]))
    for student, info in student_info.items():
        print(student, '\t', '\t\t'.join([str(info["ID"]), str(info["GPA"]), '\t\t' + str(info["Credits_Completed"]), '\t\t' + str(info["Grades"])]))
    
    #Accessing Student Info:
    print("\nAccessing Student Info Using the Key in a Loop:")
    for key in student_info:
        print(key + ':\t',student_info[key])
        
    #Student Removal
    print("\nRemoving Sarah from Registry:")
    student_info.pop("Sarah")
    print(student_info)
    
    #Access GPA
    print("\nAccessing GPA Info:")
    for student in student_info:
        print(f"{student}'s GPA: {student_info[student].get('GPA')}")
    
    #Clear Registry
    print("\nClearning Student Registry:")
    student_info.clear()
    print(student_info)
    
if __name__ == "__main__":
    main()
    print("\nCompleted by, Jeremiah Vela")
