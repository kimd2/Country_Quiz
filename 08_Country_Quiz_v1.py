"""
Country Quiz
Diane Kim
02/09/21
Version 1 - Assemble components
"""
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import ttk
import re
from Country_Quiz.data import *
import random
from datetime import datetime


# Message box for errors
def show_error(error_msg, parent_box): # Use as external method as export class will use the same function
    msgbox.showerror("Error", error_msg, parent=parent_box)


class Quiz:
    def __init__(self):
        global help_button
        # Create frame
        self.menu_frame = Frame(root,
                                background="Lemon Chiffon",
                                width=300,
                                height=400)
        self.menu_frame.grid()

        # Title
        self.quiz_label = Label(self.menu_frame,
                                text="Country Quiz",
                                font=("Lucida Console", "18", "bold"),
                                background="Lemon Chiffon",
                                width=20)
        self.quiz_label.grid(row=0, pady=20)

        # Description
        self.quiz_description = Label(self.menu_frame,
                                      text="Test your knowledge\n"
                                           "of countries around\n"
                                           "the World!",
                                      font=("Lucida Console", "14"),
                                      background="Lemon Chiffon")
        self.quiz_description.grid(row=1, pady=5, padx=10)

        # Start button
        self.start_button = Button(self.menu_frame,
                                   text="Start!",
                                   background="gold",
                                   activebackground="Light goldenrod",
                                   font=("Lucida Console", "14", "bold"),
                                   command=self.open_start)
        self.start_button.grid(row=2, pady=10, padx=10)

        # Score button
        self.score_button = Button(self.menu_frame,
                                   text="View Scores",
                                   background="gold",
                                   activebackground="Light goldenrod",
                                   font=("Lucida Console", "14", "bold"),
                                   command=self.open_score)
        self.score_button.grid(row=3, pady=10, padx=10)

        # Help button
        help_button = Button(self.menu_frame,
                             text="Help",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=("Lucida Console", "14", "bold"),
                             command=self.open_help)
        help_button.grid(row=4, pady=10, padx=10)

        # Exit button
        self.exit_button = Button(self.menu_frame,
                                  text="Quit",
                                  background="gold",
                                  activebackground="Light goldenrod",
                                  font=("Lucida Console", "14", "bold"),
                                  command=quit)
        self.exit_button.grid(row=5, pady=10, padx=10)

        # Position holder
        self.space_label = Label(self.menu_frame, bg="Lemon Chiffon")
        self.space_label.grid(row=6)

        # Open Help window

    def open_help(self):
        print("Help Opened")
        get_help = Help()
        get_help.help_text.configure(text="Click play to begin!\n\n"
                                          "There are 2 modes:\n"
                                          "Random mode and Country mode.\n"
                                          "Random will run through 10 questions\n"
                                          "on different countries selected\n"
                                          "randomly.\n"
                                          "Country mode will enable you to\n"
                                          "choose a country to get tested on.\n"
                                          "Select the country to be tested on\n"
                                          "on the start menu.\n\n"
                                          "Click the correct button or enter\n"
                                          "the right answer to 8 or more\n"
                                          "questions to win.\n\n"
                                          "Exit the game at anytime during game\n"
                                          "play using the menubar on the top of \n"
                                          "window.\n\n"
                                          "You can view the top 10 scores and\n"
                                          "export scores of both modes by\n"
                                          "clicking 'View Scores'.",
                                     bg=background,
                                     justify=LEFT)
        help_button["state"] = DISABLED

    # Start menu
    def open_start(self):
        print("Start Opened")
        # Forget menu frame
        global mode_cb, start_frame, level, random_mode, score
        self.menu_frame.grid_forget()
        # Set starting variables
        level = 1
        random_mode = False
        score = 0

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

    def open_play(self):
        global country, keys, mode, random_mode
        # Set up mode and GUI
        mode = mode_cb.get()
        print("Mode selected:", mode)
        start_frame.grid_forget()

        self.play_frame = Frame(root,
                           bg=background)
        self.play_frame.grid()

        # Get data
        valid = False
        if mode == "Random":
            while not valid:
                mode = random.choice(modes)
                if mode != "Random":
                    valid = True
            random_mode = True
        country = give_dictionary(mode)
        keys = list(country.keys())

        self.level()

    # Initial Level setup
    def level(self):
        global country, keys, mode, others, answer, play_next_button, play_button_1, play_button_2, play_button_3, play_button_4, level, play_label, play_question, play_short_answer, question, play_short_answer_button, image_1, image_2, image_3, image_4
        play_heading = Label(self.play_frame,
                             text=country['name'],
                             font=("Lucida Console", '18', 'bold'),
                             bg=background,
                             justify=CENTER,
                             width=20)
        if random_mode:
            play_heading.configure(text="Random")
        play_heading.grid(row=0, padx=20, columnspan=2)

        # Set up game play
        if level == 1:
            answer = country[keys[level]]
            question = keys[level]

            # Level heading
            play_label = Label(self.play_frame,
                               text="Level {}".format(level),
                               font=("Lucida Console", '14', 'bold'),
                               bg=background)
            play_label.grid(row=2, columnspan=2)

            # Question
            play_question = Label(self.play_frame,
                                  text="What is the {} of {}?".format(question, mode),
                                  font=('Lucida console', '14'),
                                  bg=background)
            play_question.grid(row=3, columnspan=2)

            # Entry field
            play_short_answer = Entry(self.play_frame,
                                      font=('Lucida console', '14')
                                      )
            play_short_answer.grid(row=4, columnspan=2)

            # Check answer button
            play_short_answer_button = Button(self.play_frame,
                                              text="Enter",
                                              font=('lucida console', '14'),
                                              bg='gold',
                                              activebackground='light goldenrod',
                                              command=self.check_answer_1)
            play_short_answer_button.grid(row=5, columnspan=2, pady=5)


            # Create menu for quit option
            play_menu = Menu(root)
            menu_options = Menu(play_menu,
                             tearoff=0)
            menu_options.add_command(label="Menu", command=self.menu_menu)
            menu_options.add_command(label="Exit", command=self.menu_exit)
            menu_options.add_command(label="Quit", command=self.menu_quit)
            play_menu.add_cascade(label="Options", menu=menu_options)
            root.config(menu=play_menu)

        # Change mode to image mode
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

            # Create multichoice buttons
            play_button_1 = Button(self.play_frame,
                                   bg="gold",
                                   image=image_1,
                                   compound='top',
                                   text=others[0][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_1,
                                   width=303,
                                   height=229
                                   )
            play_button_1.grid(row=4, column=0, pady=10, padx=10)

            play_button_2 = Button(self.play_frame,
                                   bg="gold",
                                   image=image_2,
                                   compound='top',
                                   text=others[1][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_2,
                                   width=303,
                                   height=229
                                   )

            play_button_2.grid(row=4, column=1, pady=10, padx=10)

            play_button_3 = Button(self.play_frame,
                                   bg="gold",
                                   image=image_3,
                                   compound='top',
                                   text=others[2][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_3,
                                   width=303,
                                   height=229
                                   )
            play_button_3.grid(row=5, column=0, pady=10, padx=10)

            play_button_4 = Button(self.play_frame,
                                   bg="gold",
                                   image=image_4,
                                   compound='top',
                                   text=others[3][1],
                                   activebackground="light goldenrod",
                                   font=("Lucida Console", "14"),
                                   command=self.check_answer_4,
                                   width=303,
                                   height=229
                                   )
            play_button_4.grid(row=5, column=1, pady=10, padx=10)

        # Configure next button
        play_next_button = Button(self.play_frame,
                                  text='Next',
                                  bg='gold',
                                  activebackground='light goldenrod',
                                  font=('lucida console', '14'),
                                  command=self.next)

    # Commands for menu bar
    def menu_menu(self):    # Return to Menu
        global initial
        menu_response = msgbox.askokcancel("Return to Menu?", "You will be taken to the menu.\nYour current score will be saved, but this game will not be saved.")
        if menu_response:
            first = "Play"
            self.open_id(first)

    def menu_exit(self):    # Exit to scoreboard
        menu_response = msgbox.askokcancel("Exit Game?", "You will be taken to the scoreboard.\nYour current score will be saved, but this game will not be saved.")
        if menu_response:
            self.play_frame.grid_forget()
            root.config(menu=empty_menu)
            self.play_frame.grid_forget()
            self.open_id()

    def menu_quit(self):    # Quit game
        menu_response = msgbox.askokcancel("Quit Game?", "No games will be saved.\nTo view and export scores, please select the exit option.")
        if menu_response:
            root.destroy()


    # Configure the next levels
    def next(self):
        global score, random_mode, country, keys, mode, others, answer, play_next_button, play_button_1, play_button_2, play_button_3, play_button_4, level, play_question, play_feedback, play_label, play_short_answer, question, play_short_answer_button, image_1, image_2, image_3, image_4
        # Next question
        level += 1

        # Remove next button from GUI
        play_next_button.grid_forget()
        play_feedback.grid_forget()
        play_label.configure(text="Level {}".format(level))

        # If random, randomize the selected country
        if random_mode:
            valid = False
            while not valid:
                mode = random.choice(modes)
                if mode != "Random":
                    valid = True
            country = give_dictionary(mode)
            keys = list(country.keys())

        # After all 10 questions show results
        if level == 11:
            self.open_id()
        # Question format changes to multichoice
        elif level == 4:
            self.level()
        elif level ==7:
            answer = country[keys[level]]
            question = keys[level]
            others = random_country(answer, question)
            random.shuffle(others)

            others[0][1] = "1"
            others[1][1] = "2"
            others[2][1] = "3"
            others[3][1] = "4"

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
                play_button_4.configure(text=others[3], image="", width=max_width, height=1, state=NORMAL)
                play_button_3.configure(text=others[2], image="", width=max_width, height=1, state=NORMAL)
                play_button_2.configure(text=others[1], image="", width=max_width, height=1, state=NORMAL)
                play_button_1.configure(text=others[0], image="", width=max_width, height=1, state=NORMAL)
            play_question.configure(text="What is the {} of {}?".format(question, mode))
        else:
            # Set question and answers
            answer = country[keys[level]]
            question = keys[level]
            play_short_answer.configure(state=NORMAL)
            play_short_answer.delete(0, 'end')
            play_question.configure(text="What is the {} of {}?".format(question, mode))
            play_short_answer_button.grid(row=5, pady=5, columnspan=2)

    # Check answers
    def check_answer_1(self):
        global score, others, answer, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4, question, play_short_answer, play_short_answer_button
        score += 1
        play_feedback = Label(self.play_frame,
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
                score -= 1
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
                score -= 1
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
        global score, others, answer, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[1]
        score += 1
        play_feedback = Label(self.play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
            if type[question] == 'image multichoice':
                answer = list(answer)
                answer = answer[1]
            play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
            score -= 1
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
        global score, others, answer, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[2]
        score += 1
        play_feedback = Label(self.play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
            if type[question] == 'image multichoice':
                answer = list(answer)
                answer = answer[1]
            play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
            print(value)
            score -= 1
        play_feedback.grid(row=6, columnspan=2, pady=10)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_button_1.configure(state=DISABLED)
        play_button_2.configure(state=DISABLED)
        play_button_3.configure(state=DISABLED)
        play_button_4.configure(state=DISABLED)
        print("Here3")
        return

    def check_answer_4(self):
        global score, others, answer, level, play_feedback, play_button_1, play_button_2, play_button_3, play_button_4
        value = others[3]
        score += 1
        play_feedback = Label(self.play_frame,
                              bg=background,
                              text="Correct!",
                              font=('lucida console', '14'))
        if answer != value:
            if type[question] == 'image multichoice':
                answer = list(answer)
                answer = answer[1]
            play_feedback.configure(text="Incorrect! The correct answer was {}.".format(answer))
            print(value)
            score -= 1
        play_feedback.grid(row=6, columnspan=2, pady=10)
        play_next_button.grid(row=7, columnspan=2, pady=10)
        play_button_1.configure(state=DISABLED)
        play_button_2.configure(state=DISABLED)
        play_button_3.configure(state=DISABLED)
        play_button_4.configure(state=DISABLED)
        print("Here4")
        return

    def open_id(self, initial=False):
        global a, b, c, id_entry_a, id_entry_b, id_enter
        # Set up frame
        self.play_frame.grid_forget()
        root.configure(menu=empty_menu)
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
                          command=lambda: self.save_username(initial))
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
    def save_username(self, next=False):
        a_txt = a.get()
        b_txt = b.get()
        c_txt = c.get()
        if a_txt and b_txt and c_txt:
            self.username = f"{a_txt}{b_txt}{c_txt}"
            print(self.username)
            global score, random_mode, mode, level
            print(score)
            # Save scores
            if random_mode:
                random_scores.append([score, self.username])
            else:
                scores.append([score, self.username, mode])
            self.id_frame.grid_forget()
            if next:
                self.open_menu(next)
            else:
                self.open_score()
        else:
            error = "Please enter a 3 letter username."
            show_error(error, self.id_frame)

    # Open Score GUI
    def open_score(self):
        global score_frame, score_chart_frame, frame_random_score, frame_country_score, export_button
        # Set up Frame
        self.menu_frame.grid_forget()

        # Format GUI
        score_frame = Frame(root,
                            bg=background)
        score_frame.grid()

        # Heading
        score_label = Label(score_frame,
                            text="High Scores",
                            font=("Lucida Console", "18", "bold"),
                            bg=background,
                            width=20)
        score_label.grid(row=0, pady=20, padx=10, columnspan=2)

        # Frame for buttons
        score_chart_frame = Frame(score_frame,
                                  bg='gold')
        score_chart_frame.grid(row=1, padx=5, columnspan=2)

        # Button to change mode
        score_random_button = Button(score_chart_frame,
                                     text="Random",
                                     font=("Lucida Console", "14", "bold"),
                                     bg='gold',
                                     activebackground='light goldenrod',
                                     command=self.show_random_scores,
                                     width=20)
        score_random_button.grid(row=0, column=0)

        score_country_button = Button(score_chart_frame,
                                      text="Country",
                                      font=("Lucida Console", "14", "bold"),
                                      bg='light goldenrod',
                                      activebackground='gold',
                                      command=self.show_country_scores,
                                      width=20)
        score_country_button.grid(row=0, column=1)

        # Frame for random scoreboard
        frame_random_score = Frame(score_chart_frame,
                                   bg='gold')

        # Scoreboard Headings
        score_heading_1 = Label(frame_random_score,
                               text="Player",
                               font=("Lucida console", "14", "bold"),
                               background='gold',
                               width=20)
        score_heading_1.grid(row=0, column=0)
        score_heading_2 = Label(frame_random_score,
                               text="Score",
                               font=("Lucida console", "14", "bold"),
                               background='gold',
                               width=20)
        score_heading_2.grid(row=0, column=1)

        # Set up Scoreboard
        random_scores.sort(reverse=True)
        if random_scores:
            for i in range(0, len(random_scores)):
                name_temp = Label(frame_random_score,
                                  bg='gold',
                                  font=('lucida console', '14'),
                                  text=random_scores[i][1])
                name_temp.grid(row=i+1, column=0)

                score_temp = Label(frame_random_score,
                                   bg='gold',
                                   font=('lucida console', '14'),
                                   text=f"{random_scores[i][0]}/10")
                score_temp.grid(row=i+1, column=1)
        else:
            random_score_text = Label(frame_random_score,
                                      bg='gold',
                                      text='No records',
                                      font=('lucida console', '14'))
            random_score_text.grid(row=1, columnspan=2)

        frame_random_score.grid(row=2, columnspan=2)

        # Frame for country mode
        frame_country_score = Frame(score_chart_frame,
                                    bg='light goldenrod')

        # Scoreboard headings
        score_heading_1 = Label(frame_country_score,
                               text="Player",
                               font=("Lucida console", "14", "bold"),
                               background='light goldenrod',
                               width=13)
        score_heading_1.grid(row=0, column=0)
        score_heading_2 = Label(frame_country_score,
                               text="Country",
                               font=("Lucida console", "14", "bold"),
                               background='light goldenrod',
                               width=13)
        score_heading_2.grid(row=0, column=1)
        score_heading_3 = Label(frame_country_score,
                               text="Score",
                               font=("Lucida console", "14", "bold"),
                               background='light goldenrod',
                               width=13)
        score_heading_3.grid(row=0, column=2)

        # Set up scoreboard
        scores.sort(reverse=True)
        if scores:
            for i in range(0, len(scores)):
                name_temp = Label(frame_country_score,
                                  bg='light goldenrod',
                                  font=('lucida console', '14'),
                                  text=scores[i][1])
                name_temp.grid(row=i+1, column=0)

                country_temp = Label(frame_country_score,
                                     bg='light goldenrod',
                                     font=('lucida console', '14'),
                                     text=scores[i][2])
                country_temp.grid(row=i+1, column=1)

                score_temp = Label(frame_country_score,
                                   bg='light goldenrod',
                                   font=('lucida console', '14'),
                                   text=f"{scores[i][0]}/10")
                score_temp.grid(row=i+1, column=2)
        else:
            country_score_text = Label(frame_country_score,
                                       bg='light goldenrod',
                                       text='No records',
                                       font=('lucida console', '14'))
            country_score_text.grid(row=1, columnspan=3)

        # Return to menu button
        menu_button = Button(score_frame,
                             text="Menu",
                             font=('lucida console', '14'),
                             bg="gold",
                             activebackground="light goldenrod",
                             command=self.open_menu,
                             width=9)
        menu_button.grid(row=2, pady=15, column=1)

        export_button = Button(score_frame,
                               bg='gold',
                               activebackground='light goldenrod',
                               font=('lucida console', '14'),
                               text='Export...',
                               command=self.open_export)
        export_button.grid(row=2, column=0, pady=25)

    # Change mode to random scores
    def show_random_scores(self):
        global score_chart_frame, frame_country_score, frame_random_score
        frame_random_score.grid(row=2, columnspan=2),
        frame_country_score.grid_forget()
        score_chart_frame.configure(bg='Gold')

    # Change mode to country scores
    def show_country_scores(self):
        global score_chart_frame, frame_country_score, frame_random_score
        frame_random_score.grid_forget()
        frame_country_score.grid(row=2, columnspan=2)
        score_chart_frame.configure(bg='light goldenrod')

    # Open Menu
    def open_menu(self, initial=False):
        global score_frame, random_mode, mode, level
        root.config(menu=empty_menu)
        if initial == "Play":
            self.play_frame.grid_forget()
        else:
            score_frame.grid_forget()
        self.menu_frame.grid()
        
    # Open export window and disable button
    def open_export(self):
        global export_button
        Export()
        export_button.config(state=DISABLED)


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
                    pass
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
            accepted = False

        # Configure error messages
        if not accepted:
            show_error(error, self.export_box)
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
            export.write("No records\n\n")

    # Export country scores
    def write_country(self):
        global export
        export.write("\n----------Country Mode----------\n\n")
        if scores:
            for record in range(0, len(scores)):
                export.write(
                    f"-{record + 1}-\nUsername: {scores[record][1]}\nScore: {scores[record][0]}\nCountry: {scores[record][2]}\n\n")
        else:
            export.write("No records\n\n")


error_label = ''
background = "Lemon Chiffon"
font_default = "Lucida console"
scores = []
random_scores = []
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    empty_menu = Menu(root) # To remove existing menu
    game = Quiz()
    root.mainloop()
