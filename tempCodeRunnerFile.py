import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Import the necessary modules for image handling
from hospital_db import add_patient, get_patients, add_doctor, get_doctors, create_appointment, add_test, get_tests


class HospitalManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("600x500")
        self.config(bg="#e3f2fd")  # Light blue background for the window

        self.load_image()  # Load the image on initialization

        # Initialize frames
        self.frame = tk.Frame(self, bg="#e3f2fd")
        self.frame.pack(pady=30)

        # Create the main menu
        self.create_menu()

    def load_image(self):
        try:
            img = Image.open("imagehospital.jpg")  # Replace with your image file
            img = img.resize((200, 200), Image.ANTIALIAS)  # Resize image if needed
            img = ImageTk.PhotoImage(img)  # Convert image to Tkinter compatible format

            label = tk.Label(self.frame, image=img, bg="#e3f2fd")
            label.image = img  # Keep a reference to the image
            label.grid(row=0, column=0, pady=10)  # Display the image
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def create_menu(self):
        menu_label = tk.Label(self.frame, text="Hospital Management System", font=("Arial", 24, "bold"), bg="#e3f2fd", fg="#3f51b5")
        menu_label.grid(row=1, column=0, columnspan=2, pady=20)

        add_patient_button = self.create_button("Add Patient", "#4CAF50", self.add_patient_window)
        add_patient_button.grid(row=2, column=0, pady=10, padx=10)

        add_doctor_button = self.create_button("Add Doctor", "#2196F3", self.add_doctor_window)
        add_doctor_button.grid(row=3, column=0, pady=10, padx=10)

        add_appointment_button = self.create_button("Create Appointment", "#FF5722", self.create_appointment_window)
        add_appointment_button.grid(row=4, column=0, pady=10, padx=10)

        add_test_button = self.create_button("Add Test", "#9C27B0", self.add_test_window)
        add_test_button.grid(row=5, column=0, pady=10, padx=10)

        view_patients_button = self.create_button("View Patients", "#8BC34A", self.view_patients)
        view_patients_button.grid(row=6, column=0, pady=10, padx=10)

        view_doctors_button = self.create_button("View Doctors", "#3F51B5", self.view_doctors)
        view_doctors_button.grid(row=7, column=0, pady=10, padx=10)

        view_tests_button = self.create_button("View Tests", "#FFC107", self.view_tests)
        view_tests_button.grid(row=8, column=0, pady=10, padx=10)

    def create_button(self, text, bg_color, command):
        return tk.Button(self.frame, text=text, width=20, height=2, bg=bg_color, fg="white", font=("Arial", 12, "bold"), relief="flat", bd=0, command=command)

    def add_patient_window(self):
        add_window = self.create_toplevel_window("Add Patient")

        name_label = self.create_label(add_window, "Name")
        name_entry = self.create_entry(add_window)

        age_label = self.create_label(add_window, "Age")
        age_entry = self.create_entry(add_window)

        gender_label = self.create_label(add_window, "Gender")
        gender_entry = self.create_entry(add_window)

        disease_label = self.create_label(add_window, "Disease")
        disease_entry = self.create_entry(add_window)

        contact_no_label = self.create_label(add_window, "Contact No")
        contact_no_entry = self.create_entry(add_window)

        address_label = self.create_label(add_window, "Address")
        address_entry = self.create_entry(add_window)

        submit_button = self.create_button("Add Patient", "#4CAF50", lambda: self.add_patient(name_entry, age_entry, gender_entry, disease_entry, contact_no_entry, address_entry, add_window))
        submit_button.grid(row=6, column=0, columnspan=2, pady=20)

    def create_label(self, window, text):
        return tk.Label(window, text=text, font=("Arial", 12), bg="#f7f7f7", anchor="e")

    def create_entry(self, window):
        entry = tk.Entry(window, font=("Arial", 12))
        entry.grid(pady=5, padx=10)
        return entry

    def create_toplevel_window(self, title):
        add_window = tk.Toplevel(self)
        add_window.title(title)
        add_window.geometry("400x350")
        add_window.config(bg="#f7f7f7")
        return add_window

    def add_patient(self, name_entry, age_entry, gender_entry, disease_entry, contact_no_entry, address_entry, window):
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        disease = disease_entry.get()
        contact_no = contact_no_entry.get()
        address = address_entry.get()

        if name and age and gender and disease and contact_no and address:
            add_patient(name, age, gender, disease, contact_no, address)
            window.destroy()
            messagebox.showinfo("Success", f"Patient '{name}' added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def add_doctor_window(self):
        add_window = self.create_toplevel_window("Add Doctor")

        name_label = self.create_label(add_window, "Name")
        name_entry = self.create_entry(add_window)

        specialization_label = self.create_label(add_window, "Specialization")
        specialization_entry = self.create_entry(add_window)

        contact_no_label = self.create_label(add_window, "Contact No")
        contact_no_entry = self.create_entry(add_window)

        email_label = self.create_label(add_window, "Email")
        email_entry = self.create_entry(add_window)

        department_label = self.create_label(add_window, "Department")
        department_entry = self.create_entry(add_window)

        submit_button = self.create_button("Add Doctor", "#4CAF50", lambda: self.add_doctor(name_entry, specialization_entry, contact_no_entry, email_entry, department_entry, add_window))
        submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    def add_doctor(self, name_entry, specialization_entry, contact_no_entry, email_entry, department_entry, window):
        name = name_entry.get()
        specialization = specialization_entry.get()
        contact_no = contact_no_entry.get()
        email = email_entry.get()
        department = department_entry.get()

        if name and specialization and contact_no and email and department:
            add_doctor(name, specialization, contact_no, email, department)
            window.destroy()
            messagebox.showinfo("Success", f"Doctor '{name}' added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def create_appointment_window(self):
        pass

    def add_test_window(self):
        add_window = self.create_toplevel_window("Add Test")

        type_label = self.create_label(add_window, "Test Type")
        type_entry = self.create_entry(add_window)

        description_label = self.create_label(add_window, "Test Description")
        description_entry = self.create_entry(add_window)

        submit_button = self.create_button("Add Test", "#4CAF50", lambda: self.add_test(type_entry, description_entry, add_window))
        submit_button.grid(row=2, column=0, columnspan=2, pady=20)

    def add_test(self, type_entry, description_entry, window):
        test_type = type_entry.get()
        description = description_entry.get()

        if test_type and description:
            add_test(test_type, description)
            window.destroy()
            messagebox.showinfo("Success", f"Test '{test_type}' added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def view_patients(self):
        patients = get_patients()
        patient_list = "\n".join([f"ID: {p[0]}, Name: {p[1]}, Disease: {p[4]}" for p in patients])
        messagebox.showinfo("Patients List", patient_list)

    def view_doctors(self):
        doctors = get_doctors()
        doctor_list = "\n".join([f"ID: {d[0]}, Name: {d[1]}, Specialization: {d[2]}" for d in doctors])
        messagebox.showinfo("Doctors List", doctor_list)

    def view_tests(self):
        tests = get_tests()
        test_list = "\n".join([f"ID: {t[0]}, Type: {t[1]}, Description: {t[2]}" for t in tests])
        messagebox.showinfo("Tests List", test_list)


if __name__ == "__main__":
    app = HospitalManagementSystem()
    app.mainloop()
