"""
Component - Game Play : Test Images
Diane Kim
3/08/21
Version 1
"""

from tkinter import *



class Quiz:
    def __init__(self):
        # Create frame
        self.quiz_frame = Frame(root,
                                background="Lemon Chiffon",
                                width=300,
                                height=400)
        self.quiz_frame.grid()

        # Title
        self.quiz_label = Label(self.quiz_frame,
                                text="Country Quiz",
                                font=("Lucida Console", "18", "bold"),
                                background="Lemon Chiffon",
                                width=20)
        self.quiz_label.grid(row=0, pady=20)

        # Description
        self.quiz_description = Label(self.quiz_frame,
                                      text="Test your knowledge\n"
                                           "of countries around\n"
                                           "the World!",
                                      font=("Lucida Console", "14"),
                                      background="Lemon Chiffon")
        self.quiz_description.grid(row=1, pady=5, padx=10)

        # Image button
        global test_image
        test_image = PhotoImage(file='Images\\01a.png')
        self.image_button = Button(self.quiz_frame,
                                   image=test_image,
                                   background="gold",
                                   activebackground="Light goldenrod",
                                   font=("Lucida Console", "14", "bold"))
        self.image_button.grid(row=2, pady=10, padx=10)

        # Score button
        self.score_button = Button(self.quiz_frame,
                                   text="View Scores",
                                   background="gold",
                                   activebackground="Light goldenrod",
                                   font=("Lucida Console", "14", "bold"))
        self.score_button.grid(row=3, pady=10, padx=10)

        # Help button
        self.help_button = Button(self.quiz_frame,
                                  text="Help",
                                  background="gold",
                                  activebackground="Light goldenrod",
                                  font=("Lucida Console", "14", "bold"))
        self.help_button.grid(row=4, pady=10, padx=10)

        # Exit button
        self.exit_button = Button(self.quiz_frame,
                                  text="Quit",
                                  background="gold",
                                  activebackground="Light goldenrod",
                                  font=("Lucida Console", "14", "bold"))
        self.exit_button.grid(row=5, pady=10, padx=10)

        # Position holder
        self.space_label = Label(self.quiz_frame, bg="Lemon Chiffon")
        self.space_label.grid(row=6)


if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
