# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from hospital_db import add_patient, delete_patient  # Import delete function

# Function to add patient from GUI
def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    disease = disease_entry.get()

    if not (name and age and gender and disease):
        messagebox.showerror("Error", "All fields are required!")
        return

    add_patient(name, int(age), gender, disease)
    messagebox.showinfo("Success", "Patient added successfully!")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    disease_entry.delete(0, tk.END)

# Function to delete patient from GUI
def delete():
    name = delete_entry.get()
    if not name:
        messagebox.showerror("Error", "Please enter a name to delete!")
        return
    
    delete_patient(name)
    messagebox.showinfo("Success", f"Patient '{name}' deleted successfully!")
    delete_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("400x400")  # Increased height for delete section
root.configure(bg="#0D47A1")  # Dark blue background

# Configure ttk styles
ttstyle = ttk.Style()
ttstyle.configure("TFrame", background="#0D47A1")
ttstyle.configure("TLabel", background="#0D47A1", font=("Arial", 11), foreground="white")
ttstyle.configure("TButton", font=("Arial", 10, "bold"), background="#00796b", foreground="black")

ttstyle.map("TButton", background=[("active", "#004D40")])  # Darker green on hover

frame = ttk.Frame(root, padding="10")
frame.pack(pady=20)

title_label = ttk.Label(frame, text="Hospital Management System", font=("Arial", 14, "bold"), foreground="#FFD700", background="#0D47A1")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

tt_labels = ["Name:", "Age:", "Gender:", "Disease:"]
for i, label in enumerate(tt_labels):
    ttk.Label(frame, text=label).grid(row=i+1, column=0, sticky="w", pady=5)

name_entry = ttk.Entry(frame, width=30)
age_entry = ttk.Entry(frame, width=30)
disease_entry = ttk.Entry(frame, width=30)
name_entry.grid(row=1, column=1, pady=5)
age_entry.grid(row=2, column=1, pady=5)
disease_entry.grid(row=4, column=1, pady=5)

gender_var = tk.StringVar(value="Male")
gender_frame = ttk.Frame(frame)
gender_frame.grid(row=3, column=1, pady=5)
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")

submit_btn = ttk.Button(frame, text="Add Patient", command=submit, style="TButton")
submit_btn.grid(row=5, column=0, columnspan=2, pady=10)

# Delete Patient Section
delete_label = ttk.Label(frame, text="Delete Patient:")
delete_label.grid(row=6, column=0, sticky="w", pady=10)
delete_entry = ttk.Entry(frame, width=30)
delete_entry.grid(row=6, column=1, pady=5)
delete_btn = ttk.Button(frame, text="Delete Patient", command=delete, style="TButton")
delete_btn.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()