"""
Component - Export
Diane Kim
28/08/21
Version 1b - Change feedback to message box
"""

import tkinter.messagebox as msgbox
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
        global export_button
        Export()
        export_button.config(state=DISABLED)


# Export window
class Export:
    def __init__(self):
        # Format BG color
        background = "lemon chiffon"

        # Sets up child window (IE, Export box)
        self.export_box = Toplevel()
        self.export_box.protocol("WM_DELETE_WINDOW", self.close_export)

        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, height=200, bg=background, pady=10)
        self.export_frame.grid()

        # Set up Export Heading (row 0)
        export_heading = Label(self.export_frame,
                               text="Export",
                               font=("lucida console", "18", "bold"),
                               bg=background,
                               padx=10,
                               pady=10)
        export_heading.grid(row=0)

        # Set up Export text (label, row 1)
        instruction_label = Label(self.export_frame,
                                  text="The file will be exported into the same folder as the program."
                                       "\nOnly, letters, numbers and '_' are allowed."
                                       "\nIf both checkmarks are left unchecked, both country mode scores"
                                       "\nand random mode scores will be exported.",
                                  font=("lucida console", "14"),
                                  bg=background)
        instruction_label.grid(row=1, padx=5, pady=5)

        # Set up entry field
        self.file_name_entry = Entry(self.export_frame,
                                font=('lucida console', '14'),
                                width=40)
        self.file_name_entry.grid(row=3, padx=10, pady=5)

        # Set up export option
        self.var_country = IntVar()
        self.var_random = IntVar()
        self.export_country_check = Checkbutton(self.export_frame,
                                           text="Country scores only",
                                           bg=background,
                                           font=("lucida console", "8"),
                                           variable=self.var_country,
                                           command=lambda: self.check_mode(self.export_country_check),
                                           activebackground=background)
        self.export_country_check.grid(row=5)
        self.export_random_check = Checkbutton(self.export_frame,
                                          text="Random scores only",
                                          bg=background,
                                          font=("lucida console", "8"),
                                          variable=self.var_random,
                                          command=lambda: self.check_mode(self.export_random_check),
                                          activebackground=background)
        self.export_random_check.grid(row=6, pady=5)

        # Set up Dismiss and export button (button, row 4)
        final_export_button = Button(self.export_frame,
                                     text="Export",
                                     font=("lucida console", "14"),
                                     bg="gold",
                                     padx=10,
                                     width=9,
                                     command=self.export_file,
                                     activebackground='light goldenrod')
        final_export_button.grid(row=8, pady=5)

        export_dismiss_button = Button(self.export_frame,
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
        global export_button
        self.export_box.destroy()
        export_button.configure(state=NORMAL)

    # Only allow one checkbox to be selected
    def check_mode(self, event):
        if event == self.export_country_check:
            self.var_random.set(0)
        else:
            self.var_country.set(0)

    # Validate and check option, start export
    def export_file(self):
        # Get filename
        filename = self.file_name_entry.get()

        # Validate
        characters = ""
        valid = "[A-Za-z0-9_]"

        accepted = True

        if filename:
            errors = []  # Feedback list
            for letter in filename:
                if re.match(valid, letter):
                    continue
                else:
                    errors.append(letter)
                    accepted = False
            if " " in errors:
                errors.remove(" ")
                if errors:
                    errors = dict.fromkeys(errors)
                    errors = list(errors)
                    if len(errors) == 1:
                        self.error = "Spaces and the character {} are not allowed!".format(errors[0])  # Feedback
                    else:
                        for number in range(0, len(errors)):
                            characters = characters + " " + errors[number]
                        self.error = "Spaces and the characters{} are not allowed!".format(characters)
                else:
                    self.error = "No spaces allowed!"
                    characters = "Space"
                print("Invalid, '{}'".format(characters))
            else:
                if len(errors) == 1:
                    self.error = "The character '{}' is not allowed!".format(errors[0])
                    print("Invalid, '{}'".format(errors[0]))
                elif not errors:
                    pass
                else:
                    errors = dict.fromkeys(errors)
                    errors = list(errors)
                    characters = ""
                    for number in range(0, len(errors)):
                        characters = characters + " " + errors[number]
                    self.error = "The characters{} are not allowed!".format(characters)
                    print("Invalid, {}".format(characters))
        else:
            self.error = "Please enter a valid file name."
            accepted = False

        # Configure error messages
        if not accepted:
            self.show_error()
        else:
            # Create file
            global export
            self.filename = filename + ".txt"
            export = open(self.filename, "w+")

            # Export file info
            timestamp = str(datetime.now())
            export.write("Country Quiz Scores\nExported " + str(timestamp[:timestamp.rindex(":")]) + "\n")

            # Write file according to option
            if self.var_random.get() == 1:
                self.write_random()
                self.exports = "Random mode scores"
            elif self.var_country.get() == 1:
                self.write_country()
                self.exports = "Country mode scores"
            else:
                self.write_country()
                self.write_random()
                self.exports = "Country mode scores and Random mode scores"
            self.show_export()

            # Close file
            export.close()
            print("File written!")

    # Message box for errors
    def show_error(self):
        msgbox.showerror("Error", self.error, parent=self.export_box)

    # Message box for successful exports
    def show_export(self):
        msgbox.showinfo("Successfully Exported", f"{self.exports} successfully exported to {self.filename}!", parent=self.export_box)

    # Export random scores
    def write_random(self):
        global export
        export.write("\n----------Random Mode----------\n\n")
        if random_scores:
            for record in range(0, len(random_scores)):
                export.write(
                    f"-{record + 1}-\nUsername: {random_scores[record][1]}\nScore: {random_scores[record][0]}\n\n")
        else:
            export.write("No records")

    # Export country scores
    def write_country(self):
        global export
        export.write("\n----------Country Mode----------\n\n")
        if scores:
            for record in range(0, len(random_scores)):
                export.write(
                    f"-{record + 1}-\nUsername: {scores[record][1]}\nScore: {scores[record][0]}\nCountry: {scores[record][2]}\n\n")
        else:
            export.write("No records")


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
