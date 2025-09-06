student={}
def add_student():
    rollno=input("enter your rollno: ")
    branch=input("enter your branch: ")
    name=input("enter your name: ")
    admission_year=input("enter your admission year: ")
    while True:
        mobile=input("enter your mobile no: ")
        if len(mobile)==10 and mobile.isdigit():
            break
        else:
            print(" Invalid mobile NUMBER.")
    while True:
        emailid=input("enter your emailid: ")
        if emailid[0].isdigit():
            print("emailid is not valid")
        elif "@" in emailid and "." in emailid:
            break
        else:
             print("Please enter a valid email address!")

    semester=input("enter your semester : ")
    CGPA=float(input("enetr your cgpa: "))
    current_year=input("enter your current yera: ")
    student[rollno]={"name":name,
                     "branch":branch,
                     "admission_year":admission_year,
                     "contact":(mobile,emailid),
                     "academic_history":(semester,CGPA,current_year)}
def fetch_student():
    rollno=input("enter your rollno")
    if rollno in student:
        print(student[rollno])
    else:
        print("student not found")
def update_student():
    rollno=input("enter the rollno you want to update: ")
    if rollno in student:
        while True:
            print("1.press 1 for update branch")
            print("2.press 2 for update name")
            print("3.press 3 for update admission year")
            print("4.press 4 for update mobile")
            print("5.press 5 for update emailid")
            print("6.press 6 for update semester")
            print("7.press 7 for update CGPA")
            print("8.press 8 for update current year")
            print("9.press 9 for exit ")
            choice=input("enter your choice to update: ")
            try:
                choice=int(choice)
            except:
                print("invalide input")
                choice=input("enter your choice to update: ")
                continue
            match choice:
                case 1:
                    student[rollno]["branch"]=input("enter your branch")
                case 2:
                    student[rollno]["name"]=input("enter your name: ")
                case 3:
                    student[rollno]["admission_year"]=input("enetr your admission year: ")
                case 4:
                    contactli=list(student[rollno]["contact"])
                    contactli[0]=input("enter your updated mobile number: ")
                    student[rollno]["contact"]=tuple(contactli)    
                case 5:
                    contactli=list(student[rollno]["contact"])
                    contactli[1]=input("enter your emailid: ")
                    student[rollno]["contact"]=tuple(contactli)
                case 6:
                    academiclihistory=list(student[rollno]["academic_history"])
                    academiclihistory[0]=input("enter your semester: ")
                    student[rollno]["academic_history"]=tuple(academiclihistory)
                case 7:
                    academiclihistory=list(student[rollno]["academic_history"])
                    academiclihistory[1]=float(input("enetr your CGPA: "))
                    student[rollno]["academic_history"]=tuple(academiclihistory)
                case 8:
                    academiclihistory=list(student[rollno]["academic_history"])
                    academiclihistory[2]=input("enter your current year: ")
                    student[rollno]["academic_history"]=tuple(academiclihistory)
                case 9:
                    print("student detailed is updated")
                    break
    else:
        print("student is not found")
def display_student():
    print("ROLLNO | Name | Branch | CGPA \n")
    for i,j in student.items():
        print(f"{i} | {j['name']} | {j['branch']} | {j['academic_history'][1]}")
def find_branch():
    branch=input("enetr your branch: ")
    found=False
    for i,j in student.items():
        if branch==j["branch"]:
            print(j)
            found=True
    if not found:
        print("no data found")

def compare_cgpa():
    rollno1=input("enter first rollno: ")
    rollno2=input("enter second rollno: ")
    if rollno1 in student and rollno2 in student:
        if student[rollno1]['academic_history'][1]>student[rollno2]['academic_history'][1]:
            print(f"{student[rollno1]['name']} has more cgpa ")
        elif student[rollno1]['academic_history'][1]==student[rollno2]['academic_history'][1]:
            print(f"{student[rollno1]['name']} and {student[rollno2]['name']} has equal cgpa ")
        else:
             print(f"{student[rollno2]['name']} has more cgpa ")
    else:
        print("rollno not found")


while True:
    print("1. press 1 for add student")
    print("2. press 2 for fetch student")
    print("3. press 3 for update student")
    print("4. press 4 for display student")
    print("5. press 5 for find my branch")
    print("6. press 6 for compare cgpa")
    choice=input("enter your choice: ")
    try:
        choice=int(choice)
    except:
        print("invalid input")
        choice=input("enter your choice: ")
        continue
    match choice:
        case 1:
            add_student()
        case 2:
            fetch_student()
        case 3:
            update_student()
        case 4:
            display_student()
        case 5:
            find_branch()
        case 6:
            compare_cgpa()
        case _:
            print("invalid input")
            break
        
