class Fields:
    pass
class Employer(Fields):
    employerlist = list()
    def __init__(self, id, first, last, age, job, salary, bonus, total):
        self.id = id
        self.first = first
        self.last = last
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total = total

    def add_employer(self):
        Employer.employerlist.append(self)

    def remove_employer(self,id):
        for emp in Employer.employerlist:
            if(emp.get_id() == id):
                Employer.employerlist.remove(emp)
                return True
        return False

    def get_employer_list(self):
        return Employer.employerlist

    def find_employer(self,id):
        for emp in Employer.employerlist:
            if(emp.get_id() == id):
                return emp
        return False

    def apply_bonus(self, id, value):
        for emp in Employer.employerlist:
            if (emp.get_id() == id):
                emp.bonus = value
                emp.total += value
                return True
        return False

    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id
        
    def set_first(self,first):
        self.first = first
    def get_first(self):
        return self.first

    def set_lat(self,last):
        self.last = last
    def get_last(self):
        return self.last

    def set_age(self,age):
        self.age = age
    def get_age(self):
        return self.age

    def set_job(self,job):
        self.job = job
    def get_job(self):
        return self.job

    def set_salary(self,salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

    def set_bonus(self,bonus):
        self.bonus = bonus
    def get_bonus(self):
        return self.bonus

    def set_total(self,bonus, salary):
        self.total = bonus + salary
    def get_total(self):
        return self.total

    def __str__(self):
        return "%d %s %s %d %s %d %d %d" % (self.id, self.first, self.last, self.age, self.job, self.salary, self.bonus, self.total)

Administration =[]
HR = []
IT = []
Sales = []
    

print("\n--------------------------------------------")
print("Welcome to Fields's Employer Managment System")
print("--------------------------------------------")
print("How can we help you today? Look below for possible actions.")
choice = 1
employer=Employer(0,"","",0,"",0,0,0)
while choice >= 1 :
    
    print("\n1. See our employers \n2. See our departments \n3. Add employer \n4. Remove employer \n5. Apply bonus \n6. Move employer to different department \n7. Find employer (you can print out the employer's invoice) \n8. Exit")

    choice = int((input("\nEnter your choice.  ")))

    if choice == 1:
        for i in employer.get_employer_list():
            print (i)

    elif choice == 2:
        print("\nOur departments are: \n1. Administration \n2. HR \n3. IT \n4. Sales")
        print("Which department's employers do you want to see:")
        x = int(input("Enter the department's number:  "))
        if x == 1:
            for i in Administration:
                print("\nHere are the employers:")
                print (employer.find_employer(i))
        if x == 2:
            for i in HR:
                print("\nHere are the employers:")
                print (employer.find_employer(i))
        if x == 3:
            for i in IT:
                print("\nHere are the employers:")
                print (employer.find_employer(i))
        if x == 4:
            for i in Sales:
                print("\nHere are the employers:")
                print (employer.find_employer(i))
                
    elif choice == 3:
        id = int(input("Enter employer ID:  "))
        first = input("Enter employer first name:  ")
        last = input("Enter employer last name:  ")
        age = int(input("Enter employer age:  "))
        job = input("Enter employer job title:  ")
        salary = int(input("Enter employer salary:  "))
        bonus = int(input("Enter employer bonus. If employer doesn't have a bonus type in 0:  "))
        total = bonus + salary
        emp = Employer(id,first,last,age,job,salary,bonus,total)
        emp.add_employer()
        
        print("\nOur departments are: \n1. Administration \n2. HR \n3. IT \n4. Sales")
        dep = input("Which department do you want the employer to go to?  ")
        
        if dep == "1":
            Administration.append(id)
        elif dep == "2":
            HR.append(id)
        elif dep == "3":
            IT.append(id)
        elif dep == "4":
            Sales.append(id)
        else:
            print("There is no department with given name")
        
        print("\nEmployer added.")   

    elif choice == 4:
        id = int(input("Enter employer ID:  "))
        emp = employer.find_employer(id)
        if (emp == False):
            print("There is no employer with given ID\n")
        else:
            employer.remove_employer(id)
        print("\nEmployer removed.")

    elif choice == 5:
        a = input("Do you want to apply the bonus to one employer or to the whole department? \nEnter 'employer' or 'department'  ")
        if a == "employer":
            id = int(input("Enter employer ID:  "))
            emp = employer.find_employer(id)
            if (emp == False):
                print("There is no employer with given ID\n")
            else:
                value = int(input("Enter the bonus:  "))
                employer.apply_bonus(id,value)
            print("\nBonus added.")
        elif a == "department":
            print("\nOur departments are: \n1. Administration \n2. HR \n3. IT \n4. Sales")
            x = int(input("Enter the department's number:  "))
            value = int(input("Enter the bonus:  "))
            if x == 1:
                for i in Administration:
                    employer.apply_bonus(id,value)  
            if x == 2:
                for i in HR:
                    employer.apply_bonus(id,value) 
            if x == 3:
                for i in IT:
                    employer.apply_bonus(id,value) 
            if x == 4:
                for i in Sales:
                    employer.apply_bonus(id,value) 

            print("\nBonus added.")  

    elif choice ==6:
        id = int(input("Enter employer ID:  "))
        print("\nOur departments are: \n1. Administration \n2. HR \n3. IT \n4. Sales")
        c,d =input("Enter the department' number where the employer currently is and the department's number you want the employer to go to. Separete them with space  ").split()
        if c == "1":
            Administration.remove(id)
        elif c == "2":
            HR.remove(id)
        elif c == "3":
            IT.remove(id)
        elif c == "4":
            Sales.remove(id)
        else:
            print("There is no department with given name")

        if d == "1":
            Administration.append(id)
        elif d == "2":
            HR.append(id)
        elif d == "3":
            IT.append(id)
        elif d == "4":
            Sales.append(id)
        else:
            print("There is no department with given name")

        print("\nEmployer moved.")

    elif choice == 7:
        id = int(input("Enter employer ID:  "))
        emp = employer.find_employer(id)
        if (emp == False):
            print("There is no employer with given ID\n")
        else:
            print(emp)
            decision = input("\nDo you want to print information about this employer? Enter 'yes' or 'no'.   ")
            if decision == "yes":
                
                f = open("employer.txt","x")
                f.write(str(emp.get_id()))
                f.write("\n")
                f.write(str(emp.get_first()))
                f.write("\n")
                f.write(str(emp.get_last()))
                f.write("\n")
                f.write(str(emp.get_age()))
                f.write("\n")
                f.write(str(emp.get_job()))
                f.write("\n")
                f.write(str(emp.get_salary()))
                f.write("\n")
                f.write(str(emp.get_bonus()))
                f.write("\n")
                f.write(str(emp.get_total()))
                f.close()

                print("\nInformation printed")
            

    elif choice == 8:
        print("\nHave a nice day. Hope to see you again.")
        break
    
    elif choice >8:
        print("\nWrong number. Try again.")



                
