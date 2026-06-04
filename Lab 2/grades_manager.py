#Scripting Applications - Lab 2 - Justin Lee - 10052040

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

#Part 3: File Reading and Writing - created a function
def WriteTheReport(Students, Grades):
    #Make a variable to open and save details of the report
    report_file = open("report.txt", "w")

    #Write stuff in the report - this is the title
    report_file.write("Student Grades Report\n")
    report_file.write("-----------------\n")

    # making a for loop to get the index so we can call each one on any list[] index for students and grades
    # This allow us to write each student name and grades into the repot file
    for i in range(len(Students)):
        report_file.write(Students[i] + " : " + str(Grades[i]) + "\n")

    #close the file - very important when opening the file
    report_file.close()

    #Print that the report was successfully
    print("\nReport file created successfully.")

    #Return to the main 
    return

#Read the student report and grades + Error handling Part 4
def ReadTheReport():

    #Try to see if the code below works, if not there is an error
    try:
        #input - getting the user input information for this case file name
        file_name = input("Enter filename to read: ")

        #Create a variable to hold onto the report by calling it and saving details
        report_file = open(file_name, "r")

        #Read the variable
        content = report_file.read()

        #print the content in the variable
        print("\nReading Report File:")
        print(content)

        #close to file, always do this
        report_file.close();

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Unexpected error:", e)
    #always return to main
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

    #Function to write the report
    WriteTheReport(students,grades)

    #Function to read the report that was created
    ReadTheReport()
    return

# Created when creating the main
if __name__ == '__main__': #very important when doing the main
    main()

#Discussion Questions:
#Questions 1: Why are tuples considered more secure than list in some situations?
#Answer: This allow us to keep it static so there will be no changes that can occur or affect the list
#used in tuples. In list, it can expend or decrease and change or add which can cause a lot of problems.
#
#Question 2: Why is error handling important in security scripting?
#Answer: It is important as it allow us to catch whatever is coming by and see if what is coming by is correct
#if not, we can catch it before it keeps going and show an error is occuring.
#This also allow us to check everything that is coming by and make sure whatever is being called is correct.
#Mainly this is useful in catching before information is leaked, make sure cache is good, ensure system is running
#smoothly and can be useful to check what inforamtion is coming by.