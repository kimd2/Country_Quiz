"""
Component - Game Play
Diane Kim
29/07/21
Version 1 - Add questions, answers and format GUI
"""

from tkinter import *
from tkinter import ttk
from Country_Quiz.data import *
import random


class Quiz:
    def __init__(self):
        # Create frame
        global menu_frame
        menu_frame = Frame(root,
                           background=background)
        menu_frame.grid()

        # Help button
        global start_button
        start_button = Button(menu_frame,
                              text="Start!",
                              background="gold",
                              activebackground="Light goldenrod",
                              font=(font_default, "14", "bold"),
                              command=self.open_start)
        start_button.grid(row=4,
                          pady=10,
                          padx=30)

        # Position holder
        self.space_label = Label(menu_frame,
                                 bg=background)
        self.space_label.grid(row=6)

    # Game Function
    def open_play(self):
        global country, keys, mode, play_frame
        # Set up mode and GUI
        mode = mode_cb.get()
        print("Mode selected:", mode)
        start_frame.grid_forget()

        play_frame = Frame(root,
                           bg=background)
        play_frame.grid()

        # Get data
        country = give_dictionary(mode)
        keys = list(country.keys())

        self.level()

    def level(self):
        global country, keys, mode, others, answer, play_frame, play_next_button, play_button_1, play_button_2, play_button_3, play_button_4, level, play_label, play_question, play_short_answer, question, play_short_answer_button, image_1, image_2, image_3, image_4
        play_heading = Label(play_frame,
                             text=country['name'],
                             font=("Lucida Console", '18', 'bold'),
                             bg=background,
                             justify=CENTER,
                             width=20)
        play_heading.grid(row=0, padx=20, columnspan=2)

        # Set up game play
        if level == 1:
            answer = country[keys[level]]
            question = keys[level]

            play_label = Label(play_frame,
                               text="Level {}".format(level),
                               font=("Lucida Console", '14', 'bold'),
                               bg=background)
            play_label.grid(row=2, columnspan=2)

            play_question = Label(play_frame,
                                  text="What is the {} of {}?".format(question, mode),
                                  font=('Lucida console', '14'),
                                  bg=background)
            play_question.grid(row=3, columnspan=2)

            play_short_answer = Entry(play_frame,
                                      font=('Lucida console', '14')
                                      )
            play_short_answer.grid(row=4, columnspan=2)

            play_short_answer_button = Button(play_frame,
                                              text="Enter",
                                              font=('lucida console', '14'),
                                              bg= 'gold',
                                              activebackground='light goldenrod',
                                              command=self.check_answer_1)
            play_short_answer_button.grid(row=5, columnspan=2, pady=5)

        if level == 4:
            play_short_answer.grid_forget()
            play_short_answer_button.grid_forget()
            answer = country[keys[level]]
            question = keys[level]
            others = random_country(answer, question)
            random.shuffle(others)
            image_1 = PhotoImage(file=others[0][0])
            image_2 = PhotoImage(file=others[1][0])
            image_3 = PhotoImage(file=others[2][0])
            image_4 = PhotoImage(file=others[3][0])
            others[0][1] = "1"
            others[1][1] = "2"
            others[2][1] = "3"
            others[3][1] = "4"
            play_question.configure(text="What is the {} of {}?".format(question, mode))

            # Find longest length
            lengths = []
            for item in others:
                lengths.append(len(item))
            max_width = max(lengths)
            print(lengths)
            print(max_width)

            play_button_1 = Button(play_frame,
                                   bg="gold",
                                   image=image_1,
                                   compound='top',
                                   text=others[0][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_1
                                   )
            play_button_1.grid(row=4, column=0, pady=10, padx=10)

            play_button_2 = Button(play_frame,
                                   bg="gold",
                                   image=image_2,
                                   compound='top',
                                   text=others[1][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_2
                                   )

            play_button_2.grid(row=4, column=1, pady=10, padx=10)

            play_button_3 = Button(play_frame,
                                   bg="gold",
                                   image=image_3,
                                   compound='top',
                                   text=others[2][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_3
                                   )
            play_button_3.grid(row=5, column=0, pady=10, padx=10)

            play_button_4 = Button(play_frame,
                                   bg="gold",
                                   image=image_4,
                                   compound='top',
                                   text=others[3][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_4
                                   )
            play_button_4.grid(row=5, column=1, pady=10, padx=10)

        play_next_button = Button(play_frame,
                                  text='Next',
                                  bg='gold',
                                  activebackground='light goldenrod',
                                  font=('lucida console', '14'),
                                  command=self.next)

    def next(self):
        global country, keys, mode, others, answer, play_frame, play_next_button, play_button_1, play_button_2, play_button_3, play_button_4, level, play_question, play_feedback, play_label, play_short_answer, question, play_short_answer_button, image_1, image_2, image_3, image_4
        # Next question
        level += 1

        play_next_button.grid_forget()
        play_feedback.grid_forget()
        play_label.configure(text="Level {}".format(level))

        # After all 10 questions show results
        if level == 11:
            print("Finish")
            play_frame.grid_forget()
            self.open_start()
        # Question format changes to multichoice
        elif level == 4:
            self.level()
        elif type[question] == 'image multichoice' or type[question] == "multichoice":
            answer = country[keys[level]]
            question = keys[level]
            others = random_country(answer, question)
            random.shuffle(others)

            # Find longest length
            lengths = []
            for item in others:
                lengths.append(len(item))
            max_width = max(lengths)

            if type[question] == 'image multichoice':
                image_1 = PhotoImage(file=others[0][0])
                image_2 = PhotoImage(file=others[1][0])
                image_3 = PhotoImage(file=others[2][0])
                image_4 = PhotoImage(file=others[3][0])
                # Next question
                play_button_4.configure(text=others[3][1], image=image_4, state=NORMAL)
                play_button_3.configure(text=others[2][1], image=image_3, state=NORMAL)
                play_button_2.configure(text=others[1][1], image=image_2, state=NORMAL)
                play_button_1.configure(text=others[0][1], image=image_1, state=NORMAL)
                play_question.configure(text="What is the {} of {}?".format(question, mode))
            else:
                # Next question
                play_button_4.configure(text=others[3], image="", width=max_width, state=NORMAL)
                play_button_3.configure(text=others[2], image="", width=max_width, state=NORMAL)
                play_button_2.configure(text=others[1], image="", width=max_width, state=NORMAL)
                play_button_1.configure(text=others[0], image="", width=max_width, state=NORMAL)
            play_question.configure(text="What is the {} of {}?".format(question, mode))
        else:
            # Set question and answers
            answer = country[keys[level]]
            question = keys[level]
            play_short_answer.configure(state=NORMAL)
            play_short_answer.delete(0, 'end')
            play_question.configure(text="What is the {} of {}?".format(question, mode))
            play_short_answer_button.grid(row=5, pady=5, columnspan=2)

    def check_answer_1(self):
        global others, answer, play_frame, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4, question, play_short_answer, play_short_answer_button
        play_feedback = Label(play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        # Short answer questions check
        if level < 4:
            play_short_answer_button.grid_forget()
            value = play_short_answer.get()
            play_short_answer.configure(state=DISABLED)
            print(value, answer)
            case_sensitive_answers = []
            for i in answer:
                case_sensitive_answers.append(i.lower())
            if value.lower() not in case_sensitive_answers:
                message = answer[0]
                if len(answer) != 1:
                    for i in answer:
                        if message != i:
                            message = "{} or {}".format(message, i)
                play_feedback.configure(text="Incorrect! The correct answer was {}.".format(message))
                print(value)
                print(answer, value)
        # Multi choice questions check
        else:
            value = others[0]
            if answer != value:
                if type[question] == 'image multichoice':
                    answer = list(answer)
                    answer = answer[1]
                play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
                print(value)
            play_button_1.configure(state=DISABLED)
            play_button_2.configure(state=DISABLED)
            play_button_3.configure(state=DISABLED)
            play_button_4.configure(state=DISABLED)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_feedback.grid(row=6, columnspan=2, pady=10)
        print("Here1")
        return

    def check_answer_2(self):
        global others, answer, play_frame, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[1]
        play_feedback = Label(play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
                if type[question] == 'image multichoice':
                    answer = list(answer)
                    answer = answer[1]
                play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
                print(value)
        play_feedback.grid(row=6, columnspan=2, pady=10)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_button_1.configure(state=DISABLED)
        play_button_2.configure(state=DISABLED)
        play_button_3.configure(state=DISABLED)
        play_button_4.configure(state=DISABLED)
        print("Here2")
        return

    def check_answer_3(self):
        global others, answer, play_frame, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[2]
        play_feedback = Label(play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
                if type[question] == 'image multichoice':
                    answer = list(answer)
                    answer = answer[1]
                play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
                print(value)
        play_feedback.grid(row=6, columnspan=2, pady=10)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_button_1.configure(state=DISABLED)
        play_button_2.configure(state=DISABLED)
        play_button_3.configure(state=DISABLED)
        play_button_4.configure(state=DISABLED)
        print("Here3")
        return

    def check_answer_4(self):
        global others, answer, play_frame, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[3]
        play_feedback = Label(play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
                if type[question] == 'image multichoice':
                    answer = list(answer)
                    answer = answer[1]
                play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
                print(value)
        play_feedback.grid(row=6, columnspan=2, pady=10)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_button_1.configure(state=DISABLED)
        play_button_2.configure(state=DISABLED)
        play_button_3.configure(state=DISABLED)
        play_button_4.configure(state=DISABLED)
        print("Here4")
        return

    # Start menu
    def open_start(self):
        print("Start Opened")
        # Forget menu frame
        global menu_frame, mode_cb, start_frame
        menu_frame.grid_forget()

        # Create select mode frame
        start_frame = Frame(root,
                            bg=background)
        start_frame.grid()

        # Title
        start_label = Label(start_frame,
                            text="Select Mode",
                            font=("Lucida Console", "18", "bold"),
                            background="Lemon Chiffon",
                            width=20)
        start_label.grid(row=0, pady=20)

        # Description
        start_description = Label(start_frame,
                                  text="Test your knowledge\n"
                                       "of countries around\n"
                                       "the World!",
                                  font=("Lucida Console", "14"),
                                  background="Lemon Chiffon")
        start_description.grid(row=1, pady=5, padx=10)

        # Create combo box
        selected_mode = StringVar()
        keep_value = selected_mode.get()

        mode_cb = ttk.Combobox(start_frame,
                               textvariable=keep_value)
        mode_cb["values"] = modes
        mode_cb.current(0)
        # Format combo box
        mode_cb["state"] = "readonly"
        mode_cb["font"] = "Lucida Console", 14
        mode_cb["background"] = "Orange"
        mode_cb.grid(row=2, padx=10)

        start_frame.option_add('*TCombobox*Listbox.font', ("Lucida Console", "14"))
        start_frame.option_add('*TCombobox*Listbox.background', "Floral White")
        start_frame.option_add('*T.Combobox*TEntry.background', "Floral White")
        start_frame.option_add('*TCombobox*Listbox.selectBackground', "Gold")
        start_frame.option_add('*TCombobox*Listbox.selectForeground', "Gray")
        mode_cb.option_add('Vertical.TScrollbar.background', 'Floral White')

        style = ttk.Style()

        style.theme_use('alt')

        style.map('TCombobox', fieldbackground=[('readonly', "Floral White")])
        style.map('TCombobox', selectbackground=[('readonly', "Floral White")])
        style.map('TCombobox', selectforeground=[('readonly', "Black")])
        style.map('TCombobox', background=[('readonly', "Floral White")])
        style.map('TCombobox', foreground=[('readonly', "Black")])
        style.map('Vertical.TScrollbar', background=[('active', 'Ivory')])
        style.configure('Vertical.TScrollbar', background='Floral White', troughcolor='palegoldenrod')

        # Play button
        play_button = Button(start_frame,
                             text="Play!",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=("Lucida Console", "14", "bold"),
                             command=self.open_play)
        play_button.grid(row=3, pady=10, padx=10)


global play_frame
level = 1
background = "Lemon Chiffon"
font_default = "Lucida Console"
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
