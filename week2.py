# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# Bu öğrenci kayıt sistemine;
# Aldığı isim soy isim ile listeye öğrenci ekleyen 
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran 
# Listeye birden fazla öğrenci eklemeyi mümkün kılan 
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan 
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız) 
# Fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

students = ["Melike Dönmez","Zeynep Baran","Kübra Kılıç","Sariye Yaman"]
print(students)


def addStudent():

    print("************ Adding Students To The List *************\n\n")
    name = input("Enter the name of the student to be added to the list : ")
    surname = input("Enter the surname of the student to be added to the list : ")

    students.append(name + " " + surname)
    print(f"The student named {name} {surname} was added to the list.")
    print(students)

#addStudent()  

def removeStudent():

    print("*********** Removing students From The List **************\n\n")
    name = input("Enter the name of the student to be removed from the list : ")
    surname = input("Enter the surname of the student to be removed from the list : ")
    
    students.remove(name + " " + surname)
    print(f"The student named {name} {surname} has been removed from the list.")
    print(students)

#removeStudent()    

def addingMultipleStudents():

    print("*********** Adding Multiple Students To The List **************\n\n")
    number = int(input("Enter the number of students to be added : "))
    i = 0

    while i < number:
        name = input("Enter the name of the student to be added to the list : ")
        surname = input("Enter the surname of the student to be added to the list : ")
        students.append(name + " " + surname)
        i += 1
        print(f"The student named {name} {surname} was added to the list.")

    print(students)

#addingMultipleStudents()

def studentList():
    print("*********** Printing All The Students In The List One By One To The Screen **************\n")
    student = 0

    for student in range(len(students)):
        print(students[student])
        student = student + 1

    print("All the students in the list were printed on the screen one by one.") 

#studentList()

def findStudentNumber():

    print("*********** Learning the Student's Number **************\n\n")
    name = input("Please enter the name of the student whose number will be questioned : ")
    surname = input("Please enter the surname of the student whose number will be questioned : ")
    student = name + " " + surname
    i = 0 

    while i < len(students):
        if students[i] == student:
            print(f"The number of the student named {name} {surname} : {i}")

        i = i + 1
    
#findStudentNumber()    

def removingMultipleStudents():
    
    print("*********** Removing Multiple Students From The List **************\n\n")
    number = int(input("Enter the number of students to be removed from the list : "))
    i = 0

    while i < number:
        name = input("Enter the name of the student to be removed to the list : ")
        surname = input("Enter the surname of the student to be removed to the list : ")
        students.remove(name + " " + surname)
        i += 1
        print(f"The student named {name} {surname} was removed to the list.")

    print(students)

#removingMultipleStudents()        


def options():
    choice = int(input(
                    "\n1  - Adding Students To The List"
                    "\n2  - Removing Students From The List"
                    "\n3  - Adding Multiple Students To The List"
                    "\n4  - Printing All The Students In The List One By One To The Screen"
                    "\n5  - Learning The Student's Number"
                    "\n6  - Removing Multiple Students From The List"
                    "\n7  - Log Out"
                    "\n\nPlease enter the number of the transaction you want to perform : "))

    if choice == 1:
        addStudent()

    if choice == 2:
        removeStudent()

    if choice == 3:
        addingMultipleStudents()

    if choice == 4:
        studentList()

    if choice == 5:
        findStudentNumber()

    if choice == 6:
        removingMultipleStudents()

    if choice == 7:
        print("Your exit is being made, please wait..\n")
        exit()

    if choice > 7 or choice < 1:
        print("An undefined transaction entry has been detected !!")

options()
