

def calculate_average(grades): #creating a function to get the average grades that is being provided

    total = 0; #creating a placeholder variable to use to get the total
    for grade in grades: #creating a for loop to go and use every grade in the list that was provided
        total +=grade #adding the current grade variable to the total and get the equal of it

    average = total / len(grades) #grabing the total variable and divide by length of grades list array (which has int variables inside)

    return average #return, must always include this in a function for this case, return the average number

def main(): #main function

    students = ["Ali", "sara", "John", "david"] #A list array that holds onto variables which is in this case is a string
    grades = [85,92,78,90] #A list of array that holds onto variables which is currently int variables

    #print(students) #to print in the consule of what is in the variable students list array
    #print(grades) #to print in the consule of what is in the variable grades list array

    course_info = ("Scripting Applications", "comp593", 2) #this is a tuples that cannot be changed and is called course_info

    #print("This is the course information") #create another print to explain what is below
    #print(course_info) #To print in the consule of what is in the variable course_info and this is a tuples

    print(f"This is the course information : {course_info}") #using f string to send out text and string from variable

    for student in students: #creating a for loop for students list
        { #starting bracket
            print(f"Name: {student.capitalize()}") #print the student list one by one
        } #ending bracket

    average_grade = calculate_average(grades);

    print(f"The average grades in the class is: {average_grade}.")

    return



if __name__ == '__main__': #very important when doing the main
    main()