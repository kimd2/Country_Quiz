"""
Component 2 - Help
Diane Kim
28/07/21
Version 2 - Added close help message and disable/enable button function
"""

from tkinter import *


class Quiz:
    def __init__(self):
        # Create frame
        self.quiz_frame = Frame(root,
                                background=background,
                                width=300,
                                height=400)
        self.quiz_frame.grid()

        # Help button
        global help_button
        help_button = Button(self.quiz_frame,
                             text="Help",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=(font_default, "14", "bold"),
                             command=self.open_help)
        help_button.grid(row=4,
                         pady=10,
                         padx=30)

        # Position holder
        self.space_label = Label(self.quiz_frame,
                                 bg=background)
        self.space_label.grid(row=6)

    # Open Help window
    def open_help(self):
        print("Help Opened")
        get_help = Help()
        get_help.help_text.configure(text="Click play to begin!\n"
                                      "There are 2 modes:\n"
                                      "Random mode and Country mode.\n"
                                      "Random will run through 1- questions\n"
                                      "on different countries selected\n"
                                      "randomly.\n"
                                      "Country mode will enable you to\n"
                                      "choose a country to get tested on.\n"
                                      "Select the country to be tested on\n"
                                      "on the start menu.\n"
                                      "Click the correct button or enter\n"
                                      "the right answer to 8 or more\n"
                                      "questions to win.\n\n"
                                      "You can view the top 10 scores and\n"
                                      "export scores to both modes by\n"
                                      "clicking 'View Scores'.",
                                     bg=background,
                                     justify=LEFT)
        help_button["state"] = DISABLED


# Help window
class Help:
    def __init__(self):
        # Create frame
        global help_box
        help_box = Toplevel()

        self.help_frame = Frame(help_box,
                                bg=background)
        self.help_frame.grid()

        # Help Title
        help_label = Label(self.help_frame, text="Help",
                           bg=background,
                           font=(font_default, 18, "bold"))
        help_label.grid(row=0, padx=20, pady=10, sticky=W)

        # Help text
        self.help_text = Label(self.help_frame,
                          font=(font_default, 14))
        self.help_text.grid(row=1, pady=10, padx=20, sticky=W)

        # Help dismiss button
        close_help = Button(self.help_frame,
                            bg="Gold",
                            activebackground="Light goldenrod",
                            text="Dismiss",
                            font=(font_default, 14, "bold"),
                            command=self.close_help)
        close_help.grid(row=2,
                        pady=30)

        help_box.protocol("WM_DELETE_WINDOW", self.close_help)

    # Close window
    def close_help(self):
        help_box.destroy()
        print("Help closed")
        help_button["state"] = NORMAL



background = "Lemon Chiffon"
font_default = "Lucida Console"
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
