#take input for the students that he can attend the exam or not 
medical_cause=input("did you have a medical cause Y or N:")
#take input of the attendance
atten=int(input("enter the attendance of the students"))

#checking the user input predicting output accordingly

if medical_cause=='Y':#checking the condition 1
    print("you are allowed")
else:
    if atten>75: #checking the condition 2
        print("allowed")
    else:
        print("not allowed")
