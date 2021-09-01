"""
Component - Username
Diane Kim
01/09/21
Version 2 - Change feedback to messagebox
"""
import tkinter.messagebox as msgbox
from tkinter import *
import re


# Message box for errors
def show_error(error_msg, parent_box): # Use as external method as export class will use the same function
    msgbox.showerror("Error", error_msg, parent=parent_box)


class Quiz:
    def __init__(self):
        global a, b, c, id_entry_a, id_entry_b, id_enter
        # Create frame
        self.id_frame = Frame(root,
                              background="Lemon Chiffon")
        self.id_frame.grid()

        # Heading
        id_heading = Label(self.id_frame,
                           bg='lemon chiffon',
                           text='Enter a 3 Letter Username:',
                           font=('lucida console', '18', 'bold'),
                           width=30)
        id_heading.grid(row=0, pady=20, padx=5, columnspan=3)

        # Set up text variables
        a = StringVar()
        b = StringVar()
        c = StringVar()
        a.set('A')
        b.set('A')
        c.set('A')

        # Set up entry fields
        id_entry_a = Entry(self.id_frame,
                           font=("Lucida console", "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=a)
        id_entry_a.grid(row=2, column=0, pady=10)
        id_entry_b = Entry(self.id_frame,
                           font=("Lucida console", "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=b)
        id_entry_b.grid(row=2, column=1, pady=10)
        id_entry_c = Entry(self.id_frame,
                           font=("Lucida console", "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=c)
        id_entry_c.grid(row=2, column=2, pady=10)

        # Bind to validate input
        id_entry_a.bind('<KeyRelease>', self.key_entered)
        id_entry_b.bind('<KeyRelease>', self.key_entered)
        id_entry_c.bind('<KeyRelease>', self.key_entered)

        # Prevent empty fields
        id_entry_a.bind('<FocusOut>', self.check_empty)
        id_entry_b.bind('<FocusOut>', self.check_empty)
        id_entry_c.bind('<FocusOut>', self.check_empty)

        # Continue button
        id_enter = Button(self.id_frame,
                          bg='gold',
                          activebackground='light goldenrod',
                          font=('lucida console', '14', 'bold'),
                          text='Enter',
                          command=self.save_username)
        id_enter.grid(row=3, column=1, pady=20)

    # Function to validate and change entry field
    def key_entered(self, event):
        global error_label
        if error_label:
            error_label.grid_forget()
        character = event.char
        caller = event.widget
        if caller == id_entry_a:
            setter = a
        elif caller == id_entry_b:
            setter = b
        else:
            setter = c
        error = f"Please enter a letter! '{character}' is not accepted."
        if character == "\t" or not character:
            error_label = Label(self.id_frame,
                                text=error,
                                font=('lucida console', '14', 'bold'),
                                bg='lemon chiffon',
                                fg='red')     # Hold var for .grid_forget()
            return("break")
        if character:
            error_label = Label(self.id_frame,
                                text=error,
                                font=('lucida console', '14', 'bold'),
                                bg='lemon chiffon',
                                fg='red')

        check = "[A-Za-z]"

        if re.match(check, character):
            setter.set(character.upper())
            print(character)
        else:
            setter.set('A')
            error_label.grid(row=1, columnspan=3, pady=10)

    # Prevent empty fields function
    def check_empty(self, event):
        global error_label
        caller = event.widget
        if caller == id_entry_a:
            setter = a
        elif caller == id_entry_b:
            setter = b
        else:
            setter = c
        value = caller.get()
        if not value:
            setter.set('A')

    # Prevent empty fields and continue command
    def save_username(self):
        a_txt = a.get()
        b_txt = b.get()
        c_txt = c.get()
        if a_txt and b_txt and c_txt:
            username = f"{a_txt}{b_txt}{c_txt}"
            print(username)
        else:
            error = "Please enter a 3 letter username."
            show_error(error, self.id_frame)


# Main routine
error_label = ''
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
