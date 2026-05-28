

def calculate_average(grades): #creating a function to get the average grades that is being provided

    total = 0; #creating a placeholder variable to use to get the total
    for grade in grades: #creating a for loop to go and use every grade in the list that was provided
        total +=grade #adding the current grade variable to the total and get the equal of it

    average = total / len(grades) #grabing the total variable and divide by length of grades list array (which has int variables inside)

    return average #return, must always include this in a function for this case, return the average number

def display(object): #creating another function
    for _ in object: #for loop
        print(_) #print _

    return #return

def passingGrades(Students, Grades): #function that takes in name list of student and grades list
    #Creating variables
    counter = 0;
    Passed = 0;
    Failed = 0;

    #For loop where it grabs a name from the student list and checks
    for Name in Students:  
        #If statement where it checks if the passing grade is over 80 or not in Grades list with its index than prints
        if Grades[counter] >= 80:
            print(f"Print current index: {counter}")
            print (f"Student {Name} has a passing grade of {Grades[counter]}")
            Passed +=1;
        #Else after the if statement if it faileds the over 80 in the Grades
        else:
            print(f"Print current index: {counter}")
            print (f"Student {Name} has not passed with a grade of {Grades[counter]}")
            Failed +=1;
        counter +=1;
    
    #Print how many have passed and how many failed
    print(f"Passed: {Passed} \nFailed: {Failed}")
    
    return #return to main

def passingGrades2(Students, Grades):
    
    #Creating variables for students who passed or failed
    Passed = 0;
    Failed = 0;
    
    #Creating a range for loop using range to find the index and if statement
    for i in range(len(Students)):

        if Grades[i] >= 80:
            #print(f"Print current index: {i}")
            print (f"Student {Students[i]} has a passing grade of {Grades[i]}")
            Passed +=1;
        #Else after the if statement if it faileds the over 80 in the Grades
        else:
            #print(f"Print current index: {i}")
            print (f"Student {Students[i]} has not passed with a grade of {Grades[i]}")
            Failed +=1;
    
    #Print how many have passed and how many failed
    print(f"Passed: {Passed} \nFailed: {Failed}")

    #return to main
    return 

def main(): #main function 

    #Creating a list for name of Students and their Grades - A list can be adjusted or changed
    students = ["Ali", "sara", "John", "david"] 
    grades = [85,92,78,90] 

     #this is a tuples that cannot be changed and is called course_info
    course_info = ("Scripting Applications", "comp593", 2)

    #using f string to send out text and string from variable
    print(f"This is the course information : {course_info}") 

    #Calling the function of display to showcase the student names
    display(students)

    #Getting the average number using the function calculate_average
    average_grade = calculate_average(grades);

    #print the average base on the variabe saved and given from the function calculate_average
    print(f"The average grades in the class is: {average_grade}.")

    #Testing the function create of passingGrades
    #print("Test of function passingGrades")
    #passingGrades(students, grades);

    #Testing the function create of passingGrades2
    #print("Test function of passingGrades2")
    passingGrades2(students, grades)

    return

if __name__ == '__main__': #very important when doing the main
    main()