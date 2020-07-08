import os
import pickle

class Components(object):
    def __init__(self, name, number, price, stock):
        self.name=name
        self.number=number
        self.price=price
        self.stock=stock
    def retname(self):
        return self.name
    def retnumber(self):
        return self.number
    def retprice(self):
        return self.price
    def retstock(self):
        return self.stock

class Teachers(object):
    def __init__(self, name, eid, dept):
        self.name=name
        self.eid=eid
        self.dept=dept
    def retname(self):
        return self.name
    def reteid(self):
        return self.eid
    def retdept(self):
        return self.dept
    
class Students(object):
    def __init__(self, name, regno, email, phone):
        self.name=name
        self.regno=regno
        self.email=email
        self.phone=phone
    def retname(self):
        return self.name
    def retregno(self):
        return self.regno
    def retemail(self):
        return self.email
    def retphone(self):
        return self.phone

def inpComponents():
    pco=input("Enter Barcode Number: ")
    name=input("Enter Component Name: ")
    price=int(input("Enter Component Price: "))
    stock=int(input("Enter the Stock of the component"))
    comp=Components(name, pco, price, stock)
    return comp

def inpTeachers():
    eid=input("Enter the Employee ID of the faculty: ")
    name=input("ENter the name of the Faculty: ")
    dept=input("Enter the Department the Faculty is a part of: ")
    teacher=Teachers(name, eid, dept)
    return teacher

def inpStudents():
    name=input("Enter the Name of the Student: ")
    regno=input("Enter the Registration Number of the Student: ")
    email=input("Enter the Email ID of the Student: ")
    phone=input("Enter the Phone Number of the Student: ")
    student=Students(name, regno, email, phone)
    return student

def sendComponents(c):
    st=open("component_list.boo","ab")
    pickle.dump(c,st)
    st.close()

def sendTeachers(t):
    st=open("teacher_list.boo","ab")
    pickle.dump(t,st)
    st.close()
    
def sendStudents(s):
    st=open("students_list.boo","ab")
    pickle.dump(s,st)
    st.close()

def readComponents():
    st=open("component_list.boo","rb")
    ans=[]
    while True:
        try:
            a=pickle.load(st)
        except EOFError:
            break
        else:
            ans.append(a)
    st.close()
    return ans
    

def readTeachers():
    st=open("teacher_list.boo","rb")
    ans=[]
    while True:
        try:
            a=pickle.load(st)
        except EOFError:
            break
        else:
            ans.append(a)
    st.close()
    return ans

def readStudents():
    st=open("students_list.boo","rb")
    ans=[]
    while True:
        try:
            a=pickle.load(st)
        except EOFError:
            break
        else:
            ans.append(a)
    st.close()
    return ans

def findComponents(b_no):
    complist=readComponents()
    for i in complist:
        if (i.retnumber()==b_no):
            return i
    
def findTeachers(b_no):
    teacherlist=readTeachers()
    for i in teacherlist:
        if(i.reteid()==b_no):
            return i
        
def findStudents(b_no):
    studentlist=readStudents()
    for i in studentlist:
        if(i.retregno()==b_no):
            return i

def modifyStudents(regnumber):
    students_list=readStudents()
    fw=open('students_list1.boo','ab')
    for i in students_list:
        if(i.retregno()==regnumber):
            f=inpStudents()
            pickle.dump(f,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('students_list.boo')
    os.rename('students_list1.boo','students_list.boo')

def modifyComponents(retnumber):
    comp_list=readComponents()
    fw=open('component_list1.boo','ab')
    for i in comp_list:
        if(i.retnumber()==retnumber):
            f=inpComponents()
            pickle.dump(f,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('component_list.boo')
    os.rename('component_list1.boo','component_list.boo')

def modifyFaculty(eid):
    teachers_list=readTeachers()
    fw=open('teacher_list1.boo','ab')
    for i in teachers_list:
        if(i.reteid()==eid):
            f=inpTeachers()
            pickle.dump(f,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('teacher_list.boo')
    os.rename('teacher_list1.boo','teacher_list.boo')

def deleteStudent(regno):
    students_list=readStudents()
    fw=open('students_list1.boo','ab')
    for i in students_list:
        if(i.retregno()==regno):
            continue
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('students_list.boo')
    os.rename('students_list1.boo','students_list.boo')
    
def deleteTeacher(eid):
    teachers_list=readTeachers()
    fw=open('teacher_list1.boo','ab')
    for i in teachers_list:
        if(i.reteid()==eid):
            continue
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('teacher_list.boo')
    os.rename('teacher_list1.boo','teacher_list.boo')
    
def deleteComponents(number):
    components_list=readComponents()
    fw=open('component_list1.boo','ab')
    for i in components_list:
        if(i.retnumber()==number):
            continue
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('component_list.boo')
    os.rename('component_list1.boo','component_list.boo')

def componentIssueStudent(number,regno):
    b=findComponents(number)
    if(int(b.retstock())>0):
        fw=open("CompIssueStudent.boo",'ab')
        writeList=(regno,number)
        pickle.dump(writeList,fw)
        fw.close()
        b.stock=int(b.stock)-1
        studList=readComponents()
        fw=open('component_list1.boo','ab')
        for i in studList:
            if(i.retnumber()==number):
                pickle.dump(b,fw)
            else:
                pickle.dump(i,fw)
        fw.close()
        os.remove('component_list.boo')
        os.rename('component_list1.boo','component_list.boo')
        
    else:
        print("Component not in stock!")

def componentIssueFaculty(number,eid):
    b=findComponents(number)
    if(int(b.getstock())>0):
        fw=open("CompIssueFaculty.boo",'ab')
        writeList=(eid,number)
        pickle.dump(writeList,fw)
        fw.close()
        b.stock=int(b.stock)-1
        compList=readComponents()
        fw=open('component_list1.boo','ab')
        for i in compList:
            if(i.retnumber()==number):
                pickle.dump(b,fw)
            else:
                pickle.dump(i,fw)
        os.remove('component_list.boo')
        os.rename('component_list1.boo','component_list.boo')
        fw.close()
    else:
        print("Component not in stock!")
    
def ComponentReturnStudent(number,regno):
    b=findComponents(number)
    fr=open("compIssueStudent.boo",'rb')
    fw=open("compIssueStudent1.boo",'ab')
    a=[]
    while True:
        try:
            f=pickle.load(fr)
        except EOFError:
            break
        else:
            a.append(f)
    fr.close()
    for i in a:
        if((i.retnumber()==number and i.retregno()==regno)==False):
            pickle.dump(i,fw)
    fw.close()
    os.remove('compIssueStudent.boo')
    os.rename('compIssueStudent1.boo','compIssueStudent.boo')
    b.stock=int(b.stock)+1
    compList=readComponents()
    fw=open('component_list1.boo','ab')
    for i in compList:
        if(i.retnumber()==number):
            pickle.dump(b,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('component_list.boo')
    os.rename('component_list1.boo','component_list.boo')


def ComponentReturnFaculty(number,eid):
    b=findComponents(number)
    fr=open("compIssueFaculty.boo",'rb')
    fw=open("compIssueFaculty1.boo",'ab')
    a=[]
    while True:
        try:
            f=pickle.load(fr)
        except EOFError:
            break
        else:
            a.append(f)
    fr.close()
    for i in a:
        if((i.retnumber()==number and i.reteid()==eid)==False):
            pickle.dump(i,fw)
    fw.close()
    os.remove('compIssueFaculty.boo')
    os.rename('compIssueFaculty1.boo','compIssueFaculty.boo')
    b.stock=int(b.stock)+1
    compList=readComponents()
    fw=open('components_list1.boo','ab')
    for i in compList:
        if(i.retnumber()==number):
            pickle.dump(b,fw)
        else:
            pickle.dump(i,fw)
    fw.close()
    os.remove('component_list.boo')
    os.rename('component_list1.boo','component_list.boo')

def SearchStudentComponents(reg_no):
    '''
    Function which searches for the list of books which a student has borrowed
    Arguments: reg_no of type str
    Return: List of Books of type Books
    '''
    fr=open('CompIssueStudent.boo','rb')
    borrowedComponents=[]
    borrowedComp=[]
    while True:
        try:
            borrowedComponents.append(pickle.load(fr))
        except EOFError:
            break
    fr.close()
    for i in borrowedComponents:
        borrowedComp.append(findComponents(i[1]))
    return borrowedComp

def SearchFacultyComponents(e_no):
    '''
    Function which searches for the list of books which a faculty has borrowed
    Arguments: e_no of type str
    Return: List of Books of type Books
    '''
    fr=open('CompIssueFaculty.boo','rb')
    borrowedBooks=[]
    borrowedBooks1=[]
    while True:
        try:
            borrowedBooks.append(pickle.load(fr))
        except EOFError:
            break
    fr.close()
    for i in borrowedBooks:
        borrowedBooks1.append(findComponents(i))
    return borrowedBooks1
            
def menu():
    
    '''
    A Function which acts as a menu to the program which takes in the input of the user and performs function calls as necessary
    Arguments: None
    Return: None
    '''
    
    while True:
        os.system('cls')
        print("Main Menu".center(40))
        print("\n\n")
        print("1. Add Component")
        print("2. Add Student Member")
        print("3. Add Faculty Member")
        print("4. View Component Details")
        print("5. View Student Details")
        print("6. View Faculty Details")
        print("7. Modify Component Details")
        print("8. Modify Student Details")
        print("9. Modify Faculty Details")
        print("10. Delete Component")
        print("11. Delete Student Member")
        print("12. Delete Faculty Member")
        print("13. Component Issue for Students")
        print("14. Component Issue for Faculty")
        print("15. Component Return for Students")
        print("16. Component Return for Faculty")
        print("17. Exit")
        ch=int(input("Enter your choice: " ))
        if(ch in range(1,18)):
            break
        else:
            print("Please Enter a valid choice!")
            input("Press <Enter> to return back to the menu.")
    if(ch==1):
        os.system('cls')
        print("Add a Component".center(40))
        b=inpComponents()
        sendComponents(b)
        print("Component Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu()
    if(ch==2):
        os.system('cls')
        print("Add a Student Member".center(40))
        s=inpStudents()
        sendStudents(s)
        print("Student Member Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu() 
    if(ch==3):
        os.system('cls')
        print("Add a Faculty Member".center(40))
        s=inpTeachers()
        sendTeachers(s)
        print("Faculty Member Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu()   
    if(ch==4):
        try:
            os.system('cls')
            isbn=input("Enter the Barcode Number to display the details: ")
            b=findComponents(isbn)
            os.system('cls')
            print("Component Details".center(40))
            print("Barcode Number:",b.retnumber())
            print("Name:",b.retname())
            print("Stock:",b.retstock())
            print("Price:",b.retprice())
        except:
            print("Component not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==5):
        try:
            os.system('cls')
            reg_no=input("Enter the Registration Number of the Student to display the details: ")
            s=findStudents(reg_no)
            sb=SearchStudentComponents(reg_no)
            os.system('cls')
            print("Student Details".center(40))
            print("Registration Number:",s.retregno())
            print("Name:",s.retname())
            print("E-Mail ID:",s.retemail())
            print("Phone Number:",s.retphone())
            print("Borrowed Components: ")
            x=1
            for i in sb:
               print(str(x)+'.',i.retname())
               x+=1
        except:
            print("Student not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==6):
        try:
            os.system('cls')
            e_no=input("Enter the Employee Number of the Faculty to display the details: ")
            f=findTeachers(e_no)
            sb=SearchFacultyComponents(e_no)
            os.system('cls')
            print("Faculty Details".center(40))
            print("Employee Number:",f.reteid())
            print("Name:",f.retname())
            print("Department: ",f.retdept())
            print("Borrowed Books: ")
            x=1
            for i in sb:
               print(str(x)+'.',i.getname())
               x+=1
        except:
            print("Faculty not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==7):
        try:
            os.system('cls')
            bno=input("Enter the barcode number of the component to modify: ")
            if(findComponents(bno)==None):
                raise ValueError("X")
            modifyComponents(bno)
            print("Successfully Modified!")
        except:
            print("Component not found/Unable to modify the component.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()            
    if(ch==8):
        try:
            os.system('cls')
            reg_no=input("Enter the Registration Number of the Student to modify: ")
            if(findStudents(reg_no)==None):
                raise ValueError("X")
            modifyStudents(reg_no)
            print("Successfully Modified!")
        except:
            print("Student not found/Unable to modify the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()             
    if(ch==9):
        try:
            os.system('cls')
            e_no=input("Enter the Employee Number of the Faculty to modify: ")
            if(findTeachers(e_no)==None):
                raise ValueError("X")
            modifyFaculty(e_no)
            print("Successfully Modified!")
        except:
            print("Faculty not found/Unable to modify the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu() 
             
    if(ch==10):
        try:
            os.system('cls')
            bno=input("Enter the Barcode Number of the product to delete: ")
            if(findComponents(bno)==None):
                raise ValueError("X")
            deleteComponents(bno)
            print("Successfully Deleted!")
        except:
            print("Components not found/Unable to delete the Components.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu() 
    if(ch==11):
        try:
            os.system('cls')
            reg_no=input("Enter the Registration Number of the Student to delete: ")
            if(findStudents(reg_no)==None):
                raise ValueError("X")
            deleteStudent(reg_no)
            print("Successfully deleted!")
        except:
            print("Student not found/Unable to remove the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==12):
        try:
            os.system('cls')
            e_no=input("Enter the Employee Number of the Faculty to delete: ")
            if(findTeachers(e_no)==None):
                raise ValueError("X")
            deleteTeacher(e_no)
            print("Successfully Deleted!")
        except:
            print("Faculty not found/Unable to delete the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==13):
        os.system('cls')
        reg_no=input("Enter the Registration Number of the Student: ")
        isbn=input("Enter the Barcode number of the component to be issued: ")
        if(findComponents(isbn)==None):
            print("Component not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(findStudents(reg_no)==None):
            print("Student Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            componentIssueStudent(isbn,reg_no)
            print("Component Successfully issued!")
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==14):
        os.system('cls')
        e_no=input("Enter the Employee Number of the Faculty: ")
        isbn=input("Enter the Barcode number of the component to be issued: ")
        if(findComponents(isbn)==None):
            print("Component not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(findTeachers(e_no)==None):
            print("Faculty Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            componentIssueFaculty(isbn,e_no)
            print("Component Successfully issued!")
            input("Press <Enter> to return back to the menu.")
            menu()
                                 
    if(ch==15):
        os.system('cls')
        reg_no=input("Enter the Registration Number of the Student: ")
        isbn=input("Enter the Barcode number of the component to be returned: ")
        fr=open("compIssueStudent.boo",'rb')
        a=[]
        while True:
            try:
                b=pickle.load(fr)
                a.append(b.retregno(),b.retnumber())
            except EOFError:
                break
        fr.close()
        if(findComponents(isbn)==None):
            print("Component not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(findStudents(reg_no)==None):
            print("Student Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif((reg_no,isbn) not in a):
            print("Student has not borrowed the Component of given Barcode Number.")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            ComponentReturnStudent(isbn,reg_no)
            print("Component Successfully returned!")
            input("Press <Enter> to return back to the menu.")
            menu()
    
    if(ch==16):
        os.system('cls')
        e_no=input("Enter the Employee Number of the Faculty: ")
        isbn=input("Enter the Barcode number of the component to be issued: ")
        fr=open("compIssueFaculty.boo",'rb')
        a=[]
        while True:
            try:
                b=pickle.load(fr)
                a.append(b.reteid(),b.retnumber())
            except EOFError:
                break
        fr.close()
        if(findComponents(isbn)==None):
            print("Component not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(findTeachers(e_no)==None):
            print("Faculty Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif((e_no,isbn) not in a):
            print("Faculty has not borrowed the Component of given Barcode Number.")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            ComponentReturnFaculty(isbn,e_no)
            print("Component Successfully returned!")
            input("Press <Enter> to return back to the menu.")
            menu()    
             
menu() 
    
    
