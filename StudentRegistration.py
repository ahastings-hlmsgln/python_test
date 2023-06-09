#  StudentRegistration.py 
#  This program processes student details to register them into courses and then displays this information onto the screen.  
#  Author: Andrew Hastings
#  Date: 10/05/2023

def printHeadings(studentList, totalFees): #Define this function which prints all student details and the total fees.
  print("---HOLMESGLEN INSTITUTE---") 
  print("ID \t\t NAME \t\t COURSE \t FEE") #Print the table header with relevant formatting.

  for student in studentList: #Iterate for each student in studentList
    print(student[0], "\t", student[1], "\t", student[2], "\t", "$" + format(student[3], ".2f")) #Print each field of student details, with relevant formatting.

  outputTotalFee(totalFees)  #Define the function to display the total fees

def inputStudentDetails(): #Define the function to get student details and calculate the total fee.
  studentList = [] #Initialize a list to store student details.
  totalFees = 0 #Create the totalFees variable and set it to 0.

  for i in range(3): #Use a loop to get the details for 3 students.
    print("Enter details for student",i+1) #+1 as it starts at 0 (0,1,2)
    studentID = input("Input student ID: ") #get user input for each variable
    studentName = input("Input student name: ")
    courseName = input("Input course name: ")
    courseFee = float(input("Input course fee: "))
    totalFees += courseFee #add courseFee to totalFees
    studentList.append([studentID,studentName,courseName,courseFee])
    #Add student details to studentList for each iteration of the loop.

  return studentList, totalFees

def outputTotalFee(totalFees):
  print("\nTotal fee:", "$" + format(totalFees, ".2f")) #Print the total fee formatted with a line between it and the previously printed message.

students, fees = inputStudentDetails() #Call inputStudentDetails to get student details and the total fee.
printHeadings(students, fees) #Call printHeadings function to print student details and total fees. 