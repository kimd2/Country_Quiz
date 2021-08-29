"""
Component - Export
Diane Kim
28/08/21
Version 2 - Change to checkbuttons to radiobutton
"""
from tkinter import *
import re
from datetime import datetime


# Would be scoreboard GUI
class Quiz:
    def __init__(self):
        global export_button
        # Export button
        menu_frame = Frame(root,
                           bg='gold',
                           background="Lemon Chiffon")
        menu_frame.grid()
        export_button = Button(menu_frame,
                               bg='gold',
                               activebackground='light goldenrod',
                               font=('lucida console', '14', 'bold'),
                               text='Export...',
                               command=self.open_export)
        export_button.grid(row=3, column=0, pady=20, padx=10)

    # Open export window and disable button
    def open_export(self):
        Export()
        export_button.config(state=DISABLED)


# Export window
class Export:
    def __init__(self):
        global file_name_entry, var_country, var_random, error_count, export_random_check, export_country_check, export_box, export_frame, error_label
        # Format BG color
        background = "lemon chiffon"

        # Sets up child window (IE, Export box)
        export_box = Toplevel()
        export_box.protocol("WM_DELETE_WINDOW", self.close_export)

        # Set up GUI frame
        export_frame = Frame(export_box, width=300, height=200, bg=background, pady=10)
        export_frame.grid()

        # Set up Export Heading (row 0)
        export_heading = Label(export_frame,
                               text="Export",
                               font=("lucida console", "18", "bold"),
                               bg=background,
                               padx=10,
                               pady=10)
        export_heading.grid(row=0)

        # Set up Export text (label, row 1)
        instruction_label = Label(export_frame,
                                  text="The file will be exported into the same folder as the program."
                                       "\nOnly, letters, numbers and '_' are allowed."
                                       "\nIf both checkmarks are left unchecked, both country mode scores"
                                       "\nand random mode scores will be exported.",
                                  font=("lucida console", "14"),
                                  bg=background)
        instruction_label.grid(row=1, padx=5, pady=5)
        error_label = Label(export_frame,
                            font=("lucida console", "14"),
                            bg=background,
                            padx=10,
                            pady=10)

        # Set up entry field
        error_count = 0
        file_name_entry = Entry(export_frame,
                                font=('lucida console', '14'),
                                width=40)
        file_name_entry.grid(row=3, padx=10, pady=5)

        # Set up export option
        self.var_mode = IntVar()
        self.var_mode.set(3)
        export_country_check = Radiobutton(export_frame,
                                           text="Country scores only",
                                           bg=background,
                                           font=("lucida console", "8"),
                                           variable=self.var_mode,
                                           value=1,
                                           activebackground=background)
        export_country_check.grid(row=5)
        export_random_check = Radiobutton(export_frame,
                                          text="Random scores only",
                                          bg=background,
                                          font=("lucida console", "8"),
                                          variable=self.var_mode,
                                          value=2,
                                          activebackground=background)
        export_random_check.grid(row=6, pady=5)
        export_both_check = Radiobutton(export_frame,
                                        text="Country and Random Scores",
                                        bg=background,
                                        font=("lucida console", "8"),
                                        variable=self.var_mode,
                                        value=3,
                                        activebackground=background)
        export_both_check.grid(row=7, pady=5)

        # Set up Dismiss and export button (button, row 4)
        final_export_button = Button(export_frame,
                                     text="Export",
                                     font=("lucida console", "14"),
                                     bg="gold",
                                     padx=10,
                                     width=9,
                                     command=self.export_file,
                                     activebackground='light goldenrod')
        final_export_button.grid(row=8, pady=5)

        export_dismiss_button = Button(export_frame,
                                       text="Dismiss",
                                       font=("lucida console", "14"),
                                       bg="gold",
                                       padx=10,
                                       width=9,
                                       command=self.close_export,
                                       activebackground='light goldenrod')
        export_dismiss_button.grid(row=9, pady=20)

    # Re-enable export... button
    def close_export(self):
        global export_box, export_button
        export_box.destroy()
        export_button.configure(state=NORMAL)

    # Only allow one checkbox to be selected
    def check_mode(self, event):
        global export_country_check, export_random_check, var_random, var_country
        caller = event
        if caller == export_country_check:
            var_random.set(0)
        else:
            var_country.set(0)

    # Validate and check option, start export
    def export_file(self):
        global file_name_entry, var_random, var_country, error_count, export_frame, error_label
        # Remove previous error
        if error_label:
            error_label.grid_forget()

        # Get filename
        filename = file_name_entry.get()

        # Get options
        country_only = var_country.get()
        random_only = var_random.get()

        # Validate
        characters = ""
        valid = "[A-Za-z0-9_]"
        if filename:
            errors = []  # Feedback list
            for letter in filename:
                if re.match(valid, letter):
                    continue
                else:
                    errors.append(letter)
            if " " in errors:
                errors.remove(" ")
                if errors:
                    errors = dict.fromkeys(errors)
                    errors = list(errors)
                    if len(errors) == 1:
                        error = "Spaces and the character {} are not allowed!".format(errors[0])  # Feedback
                    else:
                        for number in range(0, len(errors)):
                            characters = characters + " " + errors[number]
                        error = "Spaces and the characters{} are not allowed!".format(characters)
                else:
                    error = "No spaces allowed!"
                    characters = "Space"
                print("Invalid, '{}'".format(characters))
            else:
                if len(errors) == 1:
                    error = "The character '{}' is not allowed!".format(errors[0])
                    print("Invalid, '{}'".format(errors[0]))
                elif not errors:
                    error = False
                else:
                    errors = dict.fromkeys(errors)
                    errors = list(errors)
                    characters = ""
                    for number in range(0, len(errors)):
                        characters = characters + " " + errors[number]
                    error = "The characters{} are not allowed!".format(characters)
                    print("Invalid, {}".format(characters))
        else:
            error = "Please enter a valid file name."

        # Display feedback
        error_label = Label(export_frame,
                            text=error,
                            font=("lucida console", "14"),
                            bg="lemon chiffon",
                            fg='red',
                            padx=30)
        error_label.grid(row=2)

        # Configure error messages
        if error and error_count == 0:
            error_label.configure(text=error, fg='red')
            error_count = 1
            print("New error. {}".format(error))
        elif error and error_count == 1:
            error_label.configure(text=error, fg='red')
            print("Error. {}".format(error))
            error_count = 1
        elif not error and error_count == 1:
            error_label.configure(text="File successfully written!", fg='red')
            print("Error cleared.")
            error_count = 0
        else:
            error_count = 0
            error_label.configure(text="File successfully written!", fg='red')
            print("No error file written")
        if not error_count:
            # Create file
            filename = filename + ".txt"
            export = open(filename, "w+")

            # Export file info
            timestamp = str(datetime.now())
            export.write("Country Quiz Scores\nExported " + str(timestamp[:timestamp.rindex(":")]) + "\n")

            # Write file according to option
            if self.var_mode == 2:
                self.write_random(export)
            elif self.var_mode == 1:
                self.write_country(export)
            else:
                self.write_random(export)
                self.write_country(export)

            # Close file
            export.close()
            print("File written!")

    # Export random scores
    def write_random(self, name):
        name.write("\n----------Random Mode----------\n\n")
        if random_scores:
            for record in range(0, len(random_scores)):
                name.write(
                    f"-{record + 1}-\nUsername: {random_scores[record][1]}\nScore: {random_scores[record][0]}\n\n")
        else:
            name.write("No records")

    # Export country scores
    def write_country(self, name):
        name.write("\n----------Country Mode----------\n\n")
        if scores:
            for record in range(0, len(random_scores)):
                name.write(
                    f"-{record + 1}-\nUsername: {scores[record][1]}\nScore: {scores[record][0]}\nCountry: {scores[record][2]}\n\n")
        else:
            name.write("No records")


# Sample data
random_scores = [[9, "GCS"], [9, "JJY"], [9, "LJH"], [8, "CSW"], [7, "SDW"], [6, "BNA"], [3, "BAA"], [1, "KDI"]]
scores = [[10, "JJY", "New Zealand"], [9, "CSW", "South Korea"], [9, "JJY", "Japan"], [8, "SDW", "South Korea"],
          [4, "GCS", "France"], [4, "LJH", "Colombia"], [2, "DIN", "China"], [2, "DAN", "Netherlands"],
          [1, "ABD", "Jamaica"]]

# Main routine
error = ''
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
