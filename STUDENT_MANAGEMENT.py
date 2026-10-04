
import csv
import os
CSV_FILE="STUDENT_DATA.csv"


class student:
    def __init__(self,name,rollnumber,age,section):
        self.name=name
        self.rollnumber=rollnumber
        self.age=age
        self.section=section



class student_management():
    def __init__(self):
        self.student= []

    def csv_load(self):
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE,mod='r')as file:
                reader = csv.reader(file)
                for row in reader:
                    # Check if the row has exactly 4 items to avoid errors with empty lines
                    if len(row) == 4:
                        name, rollnumber, age, section = row
                        # Recreate the student object and add it to the list
                        self.student.append(student(name, rollnumber, age, section))

    def save_to_csv(self):
        """Writes the current list of students to the CSV file."""
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for s in self.students:
                writer.writerow([s.name, s.rollnumber, s.age, s.section])

    def add_student(self,name,rollnumber,age,section):
        new_student= student(name,rollnumber,age,section)
        print("==WELCOME TO STUDENT MANAGEMENT SYSTEM==")
        new_student=student(name,rollnumber,age,section)
        self.student.append(new_student) 
       

    def view_student(self):
        print("==ALL STUDENT==")
        
        if not self.student:
            print("No students in the system yet.\n")
            return
            
        for s in self.student:
            # Removed the invalid self.student.view() line
            print(f"Name: {s.name}, Roll Number: {s.rollnumber}, Age: {s.age}, Section: {s.section}")
            

    def delete_student(self,rollnumber):
        self.rollnumber=rollnumber
        print("==DELETE AN STUDENT==")
        ##rollnumber=input("ENTER THE ROLLNUMBER OF THE STUDENT")
        for s in self.student:
            if s.rollnumber==rollnumber:
                self.student.remove(s)
                print("DELETATION SUCESSFULLY")
                return
            print("STUDENT NOT FOUND")



if __name__=="__main__":
    system=student_management()

    while True:
        print("==STUDENT MANAGEMENT SYSTEM==")
        print("1.ADD AN STUDENT:")
        print("2.VIEW AN STUDENT:")
        print("3.DELETE AN STUDENT:")
        print("4.EXIT:")


        choice=input("ENTER YOUR CHOICE (1-4):")

        if choice=="1":
            name=input("ENTER THE NAME OF STUDENT:")
            rollnumber=input("ENTER THE ROLLNUMBER OF THE STUDENT:")
            age=input("ENTER THE AGE OF THE STUDENT:")
            section=input("ENTER THE SECTION OF THE STUDENT:")
            system.add_student(name,rollnumber,age,section)
    


        elif choice=="2":
            system.view_student()

        elif choice=="3":
            rollnumber=input("ENTER THE NAME OF THE STUDENT TO DELETE:")
            system.delete_student(rollnumber)
            print("STUDENT NAME DELETE SUCESSFUL:")

        elif choice=="4":
            print("THANKS FOR USING THE SYSTEM:")
            break



    
  


        
            
        


  
    


        
