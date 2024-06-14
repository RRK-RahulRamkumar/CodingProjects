from customtkinter import *
import pandas as pd

class Application:
    def __init__(self, root):
        # Application window configuration
        self.root = root
        root.geometry("500x340")
        root.resizable(False, False)
        root.title("Student Manager")

        # Used to support the creation of tabs
        self.tab_controller = CTkTabview(master=root, width=450, height=320)
        self.tab_controller.pack()

        # Calling the key methods
        self.ManageStudentTab()
        self.StudentDataTab()
        self.ValidationSettingsTab()
        self.ValidationSettings(True)

        # Initializing the dataframe
        self.students_data = {
            "first_name": [],
            "last_name": [],
            "age": [],
            "id": []
        }

        self.students_table = pd.DataFrame(self.students_data)

    def ValidationSettings(self, configure):
        self.configure = configure
        self.data_valid = False

        if self.configure:
            self.minimum_name_characters = 5 if not self.minimum_name_characters_entry.get() else int(self.minimum_name_characters_entry.get())
            self.maximum_name_characters = 20 if not self.maximum_name_characters_entry.get() else int(self.maximum_name_characters_entry.get())
            self.minimum_age = 1 if not self.minimum_age_entry.get() else int(self.minimum_age_entry.get())
            self.maximum_age = 19 if not self.maximum_age_entry.get() else int(self.maximum_age_entry.get())
            self.minimum_id_characters = 5 if not self.minimum_id_characters_entry.get() else int(self.minimum_id_characters_entry.get())
            self.maximum_id_characters = 10 if not self.maximum_id_characters_entry.get() else int(self.maximum_id_characters_entry.get())

            self.validation_label_7.configure(text="Configuration sucessful")
            self.validation_label_7.after(5000, lambda: self.validation_label_7.configure(text=""))
        else:
            self.first_name = self.manage_entry_1.get().strip()
            self.last_name = self.manage_entry_2.get().strip()
            self.age = self.manage_entry_3.get().strip()
            self.id = self.manage_entry_4.get().strip()

            if (self.first_name and self.last_name and self.age and self.id):
                if (len(self.first_name) >= self.minimum_name_characters and len(self.first_name) <= self.maximum_name_characters):
                    if (len(self.last_name) >= self.minimum_name_characters and len(self.last_name) <= self.maximum_name_characters):
                        if (int(self.age) >= self.minimum_age and int(self.age) <= self.maximum_age):
                            if (len(self.id) >= self.minimum_id_characters and len(self.id) <= self.maximum_id_characters):
                                self.data_valid = True
        
            if self.data_valid:
                self.AddStudent(data_valid=True)
            else:
                self.AddStudent(data_valid=False)

    def UpdateStudentLabels(self):
        # .shape returns a tuple containing (number of rows, number of columns)
        self.student_label_7.configure(text=f"Number of students: {self.students_table.shape[0]}")

        # boolean masking used to filter out rows where age > 18 then using len()
        self.student_label_8.configure(text=f"Students above 18: {len(self.students_table[self.students_table["age"] > 18])}")

    def AddStudent(self, data_valid):
        try:
            self.data_valid = data_valid

            if self.data_valid:
                
                # Appending the data to the dataframe using .concat()
                self.new_student_data = {
                    "first_name": [self.first_name],
                    "last_name": [self.last_name],
                    "age": [int(self.age)],
                    "id": [self.id]
                }

                new_student_df = pd.DataFrame(self.new_student_data)
                self.students_table = pd.concat([self.students_table, new_student_df], ignore_index=True)
                
                # Used for testing purposes
                print(self.students_table)
                
                # Resetting the error label
                self.manage_label_5.configure(text="Added Successfully")
                self.manage_label_5.after(5000, lambda: self.manage_label_5.configure(text=""))

                # To clear the entries
                self.manage_entry_1.delete(0, "end")
                self.manage_entry_2.delete(0, "end")
                self.manage_entry_3.delete(0, "end")
                self.manage_entry_4.delete(0, "end")

                self.UpdateStudentLabels()
                self.data_validation = False

            else:
                self.manage_label_5.configure(text="Invalid parameters")
                self.manage_label_5.after(5000, lambda: self.manage_label_5.configure(text=""))
        except:
            print("Error occured in AddStudent")

    def RemoveStudent(self):
        try:
            self.id = self.manage_entry_4.get().strip()

            if self.id:
                # .values returns an array of values in the column
                if self.id in self.students_table["id"].values:
                    # Uses boolean masking to filter and find index
                    # .index can return an array of indexs/labels or just a single one
                    self.id_index = self.students_table[self.students_table['id'] == self.id].index

                    # .drop can drop an array of indexs/labels or just a single one, in a single statement
                    self.students_table = self.students_table.drop(self.id_index)

                    # Used for testing purposes
                    print(self.students_table)

                    self.manage_entry_4.delete(0, "end")
                    self.manage_label_6.configure(text="Student deleted successfully")
                    self.manage_label_6.after(5000, lambda: self.manage_label_6.configure(text=""))

                    self.UpdateStudentLabels()

                else:
                    self.manage_label_6.configure(text="ID not found in database")
                    self.manage_label_6.after(5000, lambda: self.manage_label_6.configure(text=""))
            else:
                self.manage_label_6.configure(text="Invalid parameter for ID")
                self.manage_label_6.after(5000, lambda: self.manage_label_6.configure(text=""))
        except:
            print("Error occured in RemoveStudent")

    def SearchStudent(self):
        try:
            self.id = self.student_entry_1.get().strip()

            if self.id:
                if self.id in self.students_table['id'].values:
                    # .iloc[] is integer location, it will access the element at the specified index for a row
                    filtered_data = self.students_table[self.students_table['id'] == self.id]
                    self.student_label_2a.configure(text=f"{filtered_data['first_name'].iloc[0]}")
                    self.student_label_3a.configure(text=f"{filtered_data['last_name'].iloc[0]}")
                    self.student_label_4a.configure(text=f"{filtered_data['age'].iloc[0]}")

                    self.student_label_5.configure(text="Student found successfully")
                    self.student_label_5.after(5000, lambda: self.student_label_5.configure(text=""))

                    self.student_label_5.after(6000, lambda: self.student_label_2a.configure(text=""))
                    self.student_label_5.after(6000, lambda: self.student_label_3a.configure(text=""))
                    self.student_label_5.after(6000, lambda: self.student_label_4a.configure(text=""))

                else:
                    self.student_label_5.configure(text="ID not found in database")
                    self.student_label_5.after(5000, lambda: self.student_label_5.configure(text=""))
            else:
                self.student_label_5.configure(text="Missing parameters")
                self.student_label_5.after(5000, lambda: self.student_label_5.configure(text=""))
        except:
            print("Error occured in SearchStudent")

    def ManageStudentTab(self):
        self.tab_controller.add("Manage Student")
        self.manage_tab_reference = self.tab_controller.tab("Manage Student")

        self.manage_label_1 = CTkLabel(self.manage_tab_reference, text="First name:")
        self.manage_label_1.grid(row=0, column=0, pady=10)

        self.manage_entry_1 = CTkEntry(self.manage_tab_reference, width=200)
        self.manage_entry_1.grid(row=0, column=1)

        self.manage_label_2 = CTkLabel(self.manage_tab_reference, text="Last name:")
        self.manage_label_2.grid(row=1, column=0, pady=10)

        self.manage_entry_2 = CTkEntry(self.manage_tab_reference, width=200)
        self.manage_entry_2.grid(row=1, column=1)

        self.manage_label_3 = CTkLabel(self.manage_tab_reference, text="Age:")
        self.manage_label_3.grid(row=2, column=0, pady=10)

        self.manage_entry_3 = CTkEntry(self.manage_tab_reference, width=200)
        self.manage_entry_3.grid(row=2, column=1)

        self.manage_label_4 = CTkLabel(self.manage_tab_reference, text="ID:")
        self.manage_label_4.grid(row=3, column=0, pady=10)

        self.manage_entry_4 = CTkEntry(self.manage_tab_reference, width=200)
        self.manage_entry_4.grid(row=3, column=1)

        self.manage_button_1 = CTkButton(self.manage_tab_reference, text="Add Student", command= lambda: self.ValidationSettings(False))
        self.manage_button_1.grid(row=4, column=0, pady=10)

        self.manage_label_5 = CTkLabel(self.manage_tab_reference, text="")
        self.manage_label_5.grid(row=4, column=1)

        self.manage_button_2 = CTkButton(self.manage_tab_reference, text="Remove Student (ID)", command=self.RemoveStudent)
        self.manage_button_2.grid(row=5, column=0)

        self.manage_label_6 = CTkLabel(self.manage_tab_reference, text="")
        self.manage_label_6.grid(row=5, column=1)

    def CreateCSV(self):
        if len(self.students_table['id'].values) >= 1:

            with open("StudentManagerFolder/Students.csv", "w") as students_file:
                self.students_table.to_csv(students_file, index=False)
            
            self.student_label_9.configure(text='"Students.csv" file has been created')
            self.student_label_9.after(5000, lambda: self.student_label_9.configure(text=""))

        else:
            self.student_label_9.configure(text="Insufficient data")
            self.student_label_9.after(5000, lambda: self.student_label_9.configure(text=""))

    def StudentDataTab(self):
        self.tab_controller.add("Student Data")
        self.student_tab = self.tab_controller.tab("Student Data")

        self.student_label_1 = CTkLabel(self.student_tab, text="Search by ID: ")
        self.student_label_1.grid(row=0, column=0, pady=10)

        self.student_entry_1 = CTkEntry(self.student_tab, width=200)
        self.student_entry_1.grid(row=0, column=1)

        self.student_label_2 = CTkLabel(self.student_tab, text="First name:")
        self.student_label_2.grid(row=1, column=0)
        self.student_label_2a = CTkLabel(self.student_tab, text="")
        self.student_label_2a.grid(row=1, column=1)

        self.student_label_3 = CTkLabel(self.student_tab, text="Last name:")
        self.student_label_3.grid(row=2, column=0)
        self.student_label_3a = CTkLabel(self.student_tab, text="")
        self.student_label_3a.grid(row=2, column=1)

        self.student_label_4 = CTkLabel(self.student_tab, text="Age:")
        self.student_label_4.grid(row=3, column=0)
        self.student_label_4a = CTkLabel(self.student_tab, text="")
        self.student_label_4a.grid(row=3, column=1)

        self.student_button_1 = CTkButton(self.student_tab, text="Search", command=self.SearchStudent)
        self.student_button_1.grid(row=4, column=0, pady=10)

        self.student_label_5 = CTkLabel(self.student_tab, text="")
        self.student_label_5.grid(row=4, column=1)

        self.student_label_6 = CTkLabel(self.student_tab, text="____________")
        self.student_label_6.grid(row=5, column=0, pady=3)

        self.student_label_7 = CTkLabel(self.student_tab, text='Number of students: N/A')
        self.student_label_7.grid(row=6, column=0)

        self.student_button_2 = CTkButton(self.student_tab, text="Create CSV", command= self.CreateCSV)
        self.student_button_2.grid(row=6, column=1)

        self.student_label_8 = CTkLabel(self.student_tab, text='Students above 18: N/A')
        self.student_label_8.grid(row=7, column=0)

        self.student_label_9 = CTkLabel(self.student_tab, text="")
        self.student_label_9.grid(row=7, column=1)

    def ValidationSettingsTab(self):
        self.tab_controller.add("Validation Settings")
        self.validation_tab = self.tab_controller.tab("Validation Settings")

        self.validation_label_1 = CTkLabel(self.validation_tab, text="Minimum Name Characters:")
        self.validation_label_1.grid(row=0, column=0, pady=5)

        self.minimum_name_characters_entry = CTkEntry(self.validation_tab, width=200)
        self.minimum_name_characters_entry.grid(row=0, column=1)

        self.validation_label_2 = CTkLabel(self.validation_tab, text="Maximum Name Characters:")
        self.validation_label_2.grid(row=1, column=0, pady=5)

        self.maximum_name_characters_entry = CTkEntry(self.validation_tab, width=200)
        self.maximum_name_characters_entry.grid(row=1, column=1)

        self.validation_label_3 = CTkLabel(self.validation_tab, text="Minimum Age:")
        self.validation_label_3.grid(row=2, column=0, pady=5)

        self.minimum_age_entry = CTkEntry(self.validation_tab, width=200)
        self.minimum_age_entry.grid(row=2, column=1)

        self.validation_label_4 = CTkLabel(self.validation_tab, text="Maximum Age:")
        self.validation_label_4.grid(row=3, column=0, pady=5)

        self.maximum_age_entry = CTkEntry(self.validation_tab, width=200)
        self.maximum_age_entry.grid(row=3, column=1)

        self.validation_label_5 = CTkLabel(self.validation_tab, text="Minimum ID characters:")
        self.validation_label_5.grid(row=4, column=0, pady=5)

        self.minimum_id_characters_entry = CTkEntry(self.validation_tab, width=200)
        self.minimum_id_characters_entry.grid(row=4, column=1)

        self.validation_label_6 = CTkLabel(self.validation_tab, text="Maximum ID characters:")
        self.validation_label_6.grid(row=5, column=0, pady=5)

        self.maximum_id_characters_entry = CTkEntry(self.validation_tab, width=200)
        self.maximum_id_characters_entry.grid(row=5, column=1)

        self.validation_button_1 = CTkButton(self.validation_tab, text="Set Configuration", command= lambda: self.ValidationSettings(True))
        self.validation_button_1.grid(row=6, column=0)

        self.validation_label_7 = CTkLabel(self.validation_tab, text="")
        self.validation_label_7.grid(row=6, column=1)


root = CTk()
app_instance = Application(root)
root.mainloop()
