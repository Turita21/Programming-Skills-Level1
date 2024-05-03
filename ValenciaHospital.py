"""3. 

The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot."""

class Person:
    def __init__(self, name, surname, mail, edad, address,password):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.edad = edad
        self.address = address
        self.password = password
    
    def singup(self):
        print("Welcome to the service of sing up to the Valencia Hospital\n")
        self.name = input("\tWrite your Name: ")
        self.surname = input("\tWrite your Surname: ")
        self.mail = input("\tWrite your Mail: ")
        self.edad = int(input("\tWrite your Age: "))
        self.address = input("\tWrite your address: ")
        self.password = input("\tWrite your password: ")
    
        print("Registration Successful\n")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Mail: {self.mail}")
        print(f"Age: {self.edad}")
        print(f"Address: {self.address}")

 
    def verify_user(self):
        print("\nFillout the information to enter to the system\n")
        attempts = 0
        while attempts < 3:
            username = input("Enter your mail: ").lower()
            password = input("Enter your password: ").lower()
            if username == self.mail and password == self.password:
                message = "You have login succesfully! "
                break
            else:
                attempts += 1
                if attempts < 3:
                    print("Wrong data, please try again.")
                else:
                    message = "Your account has been lockedown. Try again later. The system is shuttingdown"
        return message

class Doctor:
    def __init__(self, name, surname, speciality):
        self.name = name
        self.surname = surname
        self.speciality = speciality
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def is_available(self, date, time):
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True

        
    def show_speciality(self,speciality):
        if self.speciality == 1:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 2:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 3:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 4:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif speciality == 5 and self.speciality == 5:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 6:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 7:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 8:
            print(f"Doctor Name: {self.name} {self.surname} \n")
        elif self.speciality == 9:
            print(f"Doctor Name: {self.name} {self.surname} \n")


class Appointment:
    def __init__(self):
        self.patient_name = ""
        self.date = ""
        self.time = ""
        self.doctor = ""

    
    def create_appoinment(self,doctors1,doctors2):
        print("\nYou are going to create a new appoinment\n")
        self.patient_name=input("\tEnter the patient's name: ")
        time = input("\nTo confirm the time slot, please introduce the time slot of your preference, morning/afternoon: \n")
        if time == "morning":
            self.date = input("\tEnter the day of the appointment (DD/MM/YY): ")
            hours_available = ["8:00", "10:00", "11:00", "12:00", "13:00"]
            print("\n"+str(hours_available)+"\n")
            self.time = input("\tChoose an available hour from this list: ")
            if self.time in hours_available:
                self.doctor = input("Enter the doctor's name: ").capitalize()
                for doctor in doctors1:
                    if self.doctor == doctor.name:
                        if doctor.is_available(self.date, self.time):
                            doctor.add_appointment(self)
                            print("You have created a new appointment.")
                            print(f'\t Patient Name: {self.patient_name}')
                            print(f"\t Date: {self.date}")
                            print(f"\t Hour: {self.time}")
                            print(f"\t Doctors Name: {self.doctor}")
                        else:
                            print("The doctor is not available at that time.")
                        break
                if self.doctor not in [doctor.name for doctor in doctors1]:
                    print("The doctor that you have selected does not exist in our system. Please try again.")
        elif time == "afternoon":
            self.date = input("\tEnter the day of the appointment (DD/MM/YY): ")
            hours_available = ["14:00","16:00","17:00","18:00","20:00"]
            chosen_hour = input("\tChoose an available hour from this list")

        




if __name__ == "__main__":
    user = Person("", "", "", 0, "","")
    user.singup()
    user.verify_user()
    def specialitys():
        print("\nWELCOME TO THE APPOINTMENTS SYSTEM\n")
        print("\t1- General Medicine")
        print("\t2- Emergency Care")
        print("\t3- Clinical Analysis")
        print("\t4- Cardiology")
        print("\t5- Neurology")
        print("\t6- Nutrition")
        print("\t7- Physiotherapy")
        print("\t8- Traumatology")
        print("\t9- Internal Medicine")
        speciality = int(input("\tWrite the number of the speciality that you want do an appoinment: "))
        return speciality
    
    def specialitys_time(speciality,doctores1,doctores2):
        time = input("\nDo you want to set an appointment in the morning or in the afternoon?: (morning/afternoon) ").lower()
        if time == "morning":
            for doctor in doctores1:
                if doctor.speciality == speciality:
                    if speciality < 1 and speciality > 9:
                        print("Invalid option.\nPlease select a valid option.")
                    elif speciality == 1:
                        print("\nGeneral Medicine Doctors")
                    elif speciality == 2:
                        print("\nEmergency Care Doctors")
                    elif speciality == 3:
                        print("\nClinical Analysis")            
                    elif speciality == 4:
                        print("\nCardiology Doctors")           
                    elif speciality == 5:
                        print("\nNeurolgy Doctors")
                    elif speciality == 6:
                        print("\nNutrition Specialist")
                    elif speciality == 7:
                        print("\nPhysiotherapists")
                    elif speciality == 8:
                        print("\nTraumautology Doctors")
                    elif speciality == 9:
                        print("\nInternal Medicine Doctors")
                    doctor.show_speciality(speciality)
                    message = "This are the available doctors for the morning time"
        elif time == "afternoon":
            for doctor in doctores2:
                if doctor.speciality == speciality:
                    if speciality < 1 and speciality > 9:
                        print("Invalid option.\nPlease select a valid option.")
                    elif speciality == 1:
                        print("\nGeneral Medicine Doctors")
                    elif speciality == 2:
                        print("\nEmergency Care Doctors")
                    elif speciality == 3:
                        print("\nClinical Analysis")            
                    elif speciality == 4:
                        print("\nCardiology Doctors")           
                    elif speciality == 5:
                        print("\nNeurolgy Doctors")
                    elif speciality == 6:
                        print("\nNutrition Specialist")
                    elif speciality == 7:
                        print("\nPhysiotherapists")
                    elif speciality == 8:
                        print("\nTraumautology Doctors")
                    elif speciality == 9:
                        print("\nInternal Medicine Doctors")
                    doctor.show_speciality(speciality)
                    message = "This are the available doctors for the afternoon time"
        else:
            print("\nError. Please enter only the word morning or afternoon, depending of your preference")
        return message

    
    speciality = specialitys()
    doctor1 = Doctor("Amelia","Shepeard",5)
    doctor2 = Doctor("Derek", "Shepeard",5)
    doctor3 = Doctor("Meredith", "Grey", 1)
    doctor4 = Doctor("Calliope","Torres",8)
    doctor5 = Doctor("Cristina", "Yang", 4)
    doctor6 = Doctor("Owen", "Hunt",2)
    doctor7 = Doctor("George","Omalley",3)
    doctor8 = Doctor("Izzie", "Stevens",6)
    doctor9 = Doctor("Alex","Karev",9)
    doctor10 =Doctor("Arizona", "Robbins",9)
    doctor11 = Doctor("April", "Kepner",7)
    doctor12 = Doctor("Lexie", "Grey",5)
    doctor13 = Doctor("Miranda", "Bailey", 1)
    doctor14 = Doctor("Josephine", "Wilson",1)
    doctor15 = Doctor("Maggie", "Pierce",4)
    doctor16 = Doctor("Teddy", "Altman",4)
    doctor17 = Doctor("Charlotte", "King",2)
    doctor18 = Doctor("Pete", "Wilder",2)
    doctor19 = Doctor("Naomi", "Bennet",3)
    doctor20 = Doctor("Sam", "Bennet",3)
    doctor21 = Doctor("Tom", "Koracick",6)
    doctor22  =Doctor("Shane", "Ross", 3)
    doctor23 = Doctor("Carina", "Deluca",9)
    doctor24 = Doctor("Andrew", "Deluca",7)
    doctor25 = Doctor("Atticus", "Lincoln",8)
    doctor26 = Doctor("Jackson", "Avery",8)
    doctor27 = Doctor("Benjamin", "Warren",7)
    doctores1 = [doctor1,doctor2,doctor3,doctor4,doctor5,doctor6,doctor7,doctor8,doctor9,doctor10,doctor11,doctor26,doctor27]
    doctores2 = [doctor12,doctor13,doctor14,doctor15,doctor16,doctor17,doctor18,doctor19,doctor20,doctor21,doctor22,doctor23,doctor24,doctor25]
    print(specialitys_time(speciality,doctores1,doctores2))
    appointment = Appointment()
    appointment.create_appoinment(doctores1,doctores2)
    print(appointment)