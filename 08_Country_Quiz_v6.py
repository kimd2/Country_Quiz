"""
Country Quiz
Diane Kim
05/09/21
Version 6
- Combine 4 check answer functions into 1
- Bind enter to next button after checking
- Bind enter key to save username command on username
- add sticky property to frames
"""
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import ttk
import re
from Country_Quiz.data import *
import random
from datetime import datetime
from pathlib import Path


# Message box for errors
def show_error(error_msg, parent_box):  # Use as external method as export class will use the same function
    msgbox.showerror("Error", error_msg, parent=parent_box)


class Quiz:
    def __init__(self):
        # Create frame
        self.menu_frame = Frame(root,
                                background=background,
                                width=300,
                                height=400)
        self.menu_frame.grid(sticky=NSEW)

        # Title
        self.quiz_label = Label(self.menu_frame,
                                text="Country Quiz",
                                font=(font_default, "18", "bold"),
                                background=background,
                                width=20)
        self.quiz_label.grid(row=0, pady=20)

        # Description
        self.quiz_description = Label(self.menu_frame,
                                      text="Test your knowledge\n"
                                           "of countries around\n"
                                           "the World!",
                                      font=(font_default, "14"),
                                      background=background)
        self.quiz_description.grid(row=1, pady=5, padx=10)

        # Start button
        self.start_button = Button(self.menu_frame,
                              text="Start!",
                              background="gold",
                              activebackground="Light goldenrod",
                              font=(font_default, "14", "bold"),
                              command=self.open_start)
        self.start_button.grid(row=2, pady=10, padx=10)

        # Score button
        self.score_button = Button(self.menu_frame,
                              text="View Scores",
                              background="gold",
                              activebackground="Light goldenrod",
                              font=(font_default, "14", "bold"),
                              command=self.open_score)
        self.score_button.grid(row=3, pady=10, padx=10)

        # Help button
        self.help_button = Button(self.menu_frame,
                             text="Help",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=(font_default, "14", "bold"),
                             command=self.open_help)
        self.help_button.grid(row=4, pady=10, padx=10)

        # Exit button
        self.exit_button = Button(self.menu_frame,
                             text="Quit",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=(font_default, "14", "bold"),
                             command=quit)
        self.exit_button.grid(row=5, pady=10, padx=10)

        # Position holder
        self.space_label = Label(self.menu_frame, bg=background)
        self.space_label.grid(row=6)

        # Open Help window

    def open_help(self):
        self.start_button['state'] = DISABLED
        self.score_button['state'] = DISABLED
        self.help_button['state'] = DISABLED
        self.exit_button['state'] = DISABLED
        get_help = Help(self.start_button, self.help_button, self.score_button, self.exit_button)
        get_help.help_text.configure(text="Click <Start!> to begin!\n\n"
                                          "There are 2 modes:\n"
                                          "Random mode and Country mode.\n"
                                          "Random will run through 10 questions\n"
                                          "on different countries selected\n"
                                          "randomly.\n"
                                          "Country mode will enable you to\n"
                                          "choose a country to get tested on.\n"
                                          "Select the country to be tested on\n"
                                          "on the start menu.\n\n"
                                          "Exit the game at anytime during game\n"
                                          "play using the menubar on the top of \n"
                                          "window.\n\n"
                                          "You can view the top 10 scores and\n"
                                          "export scores of both modes by\n"
                                          "clicking 'View Scores'.\n\n"
                                          "All image sources acknowledged in\n"
                                          "Image Sources.txt",
                                     bg=background,
                                     justify=LEFT)

    # Start menu
    def open_start(self):
        # Forget menu frame
        self.menu_frame.grid_forget()
        # Set starting variables
        self.level_number = 1
        self.countries = []
        self.random_mode = False
        self.score = 0

        # Create select mode frame
        self.start_frame = Frame(root,
                            bg=background)
        self.start_frame.grid(sticky=NSEW)

        # Title
        start_label = Label(self.start_frame,
                            text="Select Mode",
                            font=(font_default, "18", "bold"),
                            background=background,
                            width=20)
        start_label.grid(row=0, pady=20)

        # Description
        start_description = Label(self.start_frame,
                                  text="Test your knowledge\n"
                                       "of countries around\n"
                                       "the World!",
                                  font=(font_default, "14"),
                                  background=background)
        start_description.grid(row=1, pady=5, padx=10)

        # Create combo box
        selected_mode = StringVar()
        keep_value = selected_mode.get()

        self.mode_cb = ttk.Combobox(self.start_frame,
                               textvariable=keep_value)
        self.mode_cb["values"] = modes
        self.mode_cb.current(0)
        # Format combo box
        self.mode_cb["state"] = "readonly"
        self.mode_cb["font"] = font_default, 14
        self.mode_cb["background"] = "Orange"
        self.mode_cb.grid(row=2, padx=10)

        self.start_frame.option_add('*TCombobox*Listbox.font', (font_default, "14"))
        self.start_frame.option_add('*TCombobox*Listbox.background', "Floral White")
        self.start_frame.option_add('*T.Combobox*TEntry.background', "Floral White")
        self.start_frame.option_add('*TCombobox*Listbox.selectBackground', "Gold")
        self.start_frame.option_add('*TCombobox*Listbox.selectForeground', "Gray")
        self.mode_cb.option_add('Vertical.TScrollbar.background', 'Floral White')

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
        play_button = Button(self.start_frame,
                             text="Play!",
                             background="gold",
                             activebackground="Light goldenrod",
                             font=(font_default, "14", "bold"),
                             command=self.open_play)
        play_button.grid(row=3, pady=10, padx=10)

    def open_play(self):
        # Set up mode and GUI
        self.mode = self.mode_cb.get()
        self.start_frame.grid_forget()

        self.play_frame = Frame(root,
                                bg=background)
        self.play_frame.grid(sticky=NSEW)

        # Get data
        valid = False
        if self.mode == "Random":
            while not valid:
                self.mode = random.choice(modes)
                if self.mode != "Random":
                    valid = True
                    self.countries.append(self.mode)
            self.random_mode = True
        self.country = give_dictionary(self.mode)
        self.keys_lst = list(self.country.keys())

        self.level()

    # Initial self.level setup
    def level(self):
        play_heading = Label(self.play_frame,
                             text=self.country['name'],
                             font=(font_default, '18', 'bold'),
                             bg=background,
                             justify=CENTER,
                             width=20)
        if self.random_mode:
            play_heading.configure(text="Random")
        play_heading.grid(row=0, padx=20, columnspan=2)

        # Set up game play
        if self.level_number == 1:
            self.answer = self.country[self.keys_lst[self.level_number]]
            self.question = self.keys_lst[self.level_number]

            # Level heading
            self.play_label = Label(self.play_frame,
                               text="Level {}".format(self.level_number),
                               font=(font_default, '14', 'bold'),
                               bg=background)
            self.play_label.grid(row=2, columnspan=2)

            # Question
            self.play_question = Label(self.play_frame,
                                  text="What is the {} of {}?".format(self.question, self.mode),
                                  font=(font_default, '14'),
                                  bg=background)
            self.play_question.grid(row=3, columnspan=2)

            # Entry field
            self.play_short_answer = Entry(self.play_frame,
                                      font=(font_default, '14')
                                      )
            self.play_short_answer.grid(row=4, columnspan=2)
            self.play_short_answer.bind('<Return>', self.check_answer)

            # Check answer button
            self.play_short_answer_button = Button(self.play_frame,
                                              text="Enter",
                                              font=(font_default, '14'),
                                              bg='gold',
                                              activebackground='light goldenrod',
                                              command=self.check_answer)
            self.play_short_answer_button.grid(row=5, columnspan=2, pady=5)

            # Create menu for quit option
            play_menu = Menu(root)
            menu_options = Menu(play_menu,
                                tearoff=0)
            menu_options.add_command(label="Return to Menu without saving", command=self.menu_menu)
            menu_options.add_command(label="Return to Scoreboard", command=self.menu_exit)
            menu_options.add_command(label="Quit", command=self.menu_quit)
            play_menu.add_cascade(label="Options", menu=menu_options)
            root.config(menu=play_menu)

        # Change mode to image mode
        if self.level_number == 4:
            self.play_short_answer.grid_forget()
            self.play_short_answer_button.grid_forget()
            self.answer = self.country[self.keys_lst[self.level_number]]
            self.question = self.keys_lst[self.level_number]
            self.others = random_country(self.answer, self.question)
            random.shuffle(self.others)
            self.image_1 = PhotoImage(file=self.others[0][0])
            self.image_2 = PhotoImage(file=self.others[1][0])
            self.image_3 = PhotoImage(file=self.others[2][0])
            self.image_4 = PhotoImage(file=self.others[3][0])
            self.others[0][1] = "1"
            self.others[1][1] = "2"
            self.others[2][1] = "3"
            self.others[3][1] = "4"
            self.play_question.configure(text="What is the {} of {}?".format(self.question, self.mode))

            # Find longest length
            lengths = []
            for item in self.others:
                lengths.append(len(item))
            max_width = max(lengths)

            # Create multichoice buttons
            self.play_button_1 = Button(self.play_frame,
                                   bg="gold",
                                   image=self.image_1,
                                   compound='top',
                                   text=self.others[0][1],
                                   activebackground="light goldenrod",
                                   font=(font_default, "14"),
                                   command=lambda: self.check_answer(0),
                                   width=303,
                                   height=229
                                   )
            self.play_button_1.grid(row=4, column=0, pady=10, padx=10)

            self.play_button_2 = Button(self.play_frame,
                                   bg="gold",
                                   image=self.image_2,
                                   compound='top',
                                   text=self.others[1][1],
                                   activebackground="light goldenrod",
                                   font=(font_default, "14"),
                                   command=lambda: self.check_answer(1),
                                   width=303,
                                   height=229
                                   )

            self.play_button_2.grid(row=4, column=1, pady=10, padx=10)

            self.play_button_3 = Button(self.play_frame,
                                   bg="gold",
                                   image=self.image_3,
                                   compound='top',
                                   text=self.others[2][1],
                                   activebackground="light goldenrod",
                                   font=(font_default, "14"),
                                   command=lambda: self.check_answer(2),
                                   width=303,
                                   height=229
                                   )
            self.play_button_3.grid(row=5, column=0, pady=10, padx=10)

            self.play_button_4 = Button(self.play_frame,
                                   bg="gold",
                                   image=self.image_4,
                                   compound='top',
                                   text=self.others[3][1],
                                   activebackground="light goldenrod",
                                   font=(font_default, "14"),
                                   command=lambda: self.check_answer(3),
                                   width=303,
                                   height=229
                                   )
            self.play_button_4.grid(row=5, column=1, pady=10, padx=10)

        # Configure next button
        self.play_next_button = Button(self.play_frame,
                                  text='Next',
                                  bg='gold',
                                  activebackground='light goldenrod',
                                  font=(font_default, '14'),
                                  command=self.next)

    # Commands for menu bar
    def menu_menu(self):  # Return to Menu
        menu_response = msgbox.askokcancel("Return to Menu?",
                                           "You will be taken to the menu.\nThis game will not be saved.\n\nContinue?")
        if menu_response:
            first = "Play"
            self.open_menu(first)

    def menu_exit(self):  # Exit to scoreboard
        menu_response = msgbox.askokcancel("Exit Game?",
                                           "You will be taken to the scoreboard.\nYour current score will be saved, but this game will not be saved.\n\nContinue?")
        if menu_response:
            self.play_frame.grid_forget()
            root.config(menu=empty_menu)
            self.play_frame.grid_forget()
            self.open_id()

    def menu_quit(self):  # Quit game
        menu_response = msgbox.askokcancel("Quit Game?",
                                           "No games will be saved.\nTo view and export scores, please select the exit option.\n\nContinue?")
        if menu_response:
            root.destroy()

    # Configure the next levels
    def next(self, event=None):
        self.play_short_answer.unbind('<Return>')
        # Next self.question
        self.level_number += 1

        # Remove next button from GUI
        self.play_next_button.grid_forget()
        self.play_feedback.grid_forget()
        self.play_label.configure(text="Level {}".format(self.level_number))

        # If random, randomize the selected country from unselected countries
        if self.random_mode and self.level_number != 11:
            valid = False
            while not valid:
                self.mode = random.choice(modes)
                if self.mode != "Random" and self.mode not in self.countries:
                    valid = True
                    self.countries.append(self.mode)
            self.country = give_dictionary(self.mode)
            self.keys_lst = list(self.country.keys())

        # After all 10 questions show results
        if self.level_number == 11:
            self.open_id()
        # Question format changes to multichoice
        elif self.level_number == 4:
            self.level()
        elif self.level_number == 7:
            self.answer = self.country[self.keys_lst[self.level_number]]
            self.question = self.keys_lst[self.level_number]
            self.others = random_country(self.answer, self.question)
            random.shuffle(self.others)

            self.others[0][1] = "1"
            self.others[1][1] = "2"
            self.others[2][1] = "3"
            self.others[3][1] = "4"

            self.image_1 = PhotoImage(file=self.others[0][0])
            self.image_2 = PhotoImage(file=self.others[1][0])
            self.image_3 = PhotoImage(file=self.others[2][0])
            self.image_4 = PhotoImage(file=self.others[3][0])
            # Next question
            self.play_button_4.configure(text=self.others[3][1], image=self.image_4, state=NORMAL)
            self.play_button_3.configure(text=self.others[2][1], image=self.image_3, state=NORMAL)
            self.play_button_2.configure(text=self.others[1][1], image=self.image_2, state=NORMAL)
            self.play_button_1.configure(text=self.others[0][1], image=self.image_1, state=NORMAL)
            self.play_question.configure(text="What is the {} of {}?".format(self.question, self.mode))
        elif type[self.question] == 'image multichoice' or type[self.question] == "multichoice":
            self.answer = self.country[self.keys_lst[self.level_number]]
            self.question = self.keys_lst[self.level_number]
            self.others = random_country(self.answer, self.question)
            random.shuffle(self.others)

            # Find longest length
            lengths = []
            for item in self.others:
                lengths.append(len(item))
            max_width = max(lengths)

            if type[self.question] == 'image multichoice':
                self.image_1 = PhotoImage(file=self.others[0][0])
                self.image_2 = PhotoImage(file=self.others[1][0])
                self.image_3 = PhotoImage(file=self.others[2][0])
                self.image_4 = PhotoImage(file=self.others[3][0])
                # Next question
                self.play_button_4.configure(text=self.others[3][1], image=self.image_4, state=NORMAL)
                self.play_button_3.configure(text=self.others[2][1], image=self.image_3, state=NORMAL)
                self.play_button_2.configure(text=self.others[1][1], image=self.image_2, state=NORMAL)
                self.play_button_1.configure(text=self.others[0][1], image=self.image_1, state=NORMAL)
                self.play_question.configure(text="What is the {} of {}?".format(self.question, self.mode))
            else:
                # Next question
                self.play_button_4.configure(text=self.others[3], image="", width=max_width, height=1, state=NORMAL)
                self.play_button_3.configure(text=self.others[2], image="", width=max_width, height=1, state=NORMAL)
                self.play_button_2.configure(text=self.others[1], image="", width=max_width, height=1, state=NORMAL)
                self.play_button_1.configure(text=self.others[0], image="", width=max_width, height=1, state=NORMAL)
            self.play_question.configure(text="What is the {} of {}?".format(self.question, self.mode))
        else:
            # Set question and answers
            self.answer = self.country[self.keys_lst[self.level_number]]
            self.question = self.keys_lst[self.level_number]
            self.play_short_answer.configure(state=NORMAL)
            self.play_short_answer.delete(0, 'end')
            self.play_question.configure(text="What is the {} of {}?".format(self.question, self.mode))
            self.play_short_answer_button.grid(row=5, pady=5, columnspan=2)
            self.play_short_answer.bind('<Return>', self.check_answer)

    # Check answers
    def check_answer(self, btn_number=""):
        self.score += 1
        self.play_feedback = Label(self.play_frame,
                              bg=background,
                              text="Correct!",
                              font=(font_default, '14'))

        # Short answer questions check
        if self.level_number < 4:
            value = self.play_short_answer.get()

            # Check type
            expression = '[a-zA-Z ]'    # Accept letters and spaces
            invalids = []
            error_txt = ""
            for i in value:
                if not re.match(expression, i):
                    invalids.append(i)
            if invalids:
                invalids = set(invalids)
                invalids = list(invalids)
                for chars in invalids:
                    if invalids.index(chars) != len(invalids):
                        error_txt = error_txt + f"{chars} "
                    else:
                        error_txt = error_txt + chars
                show_error(f"Only spaces and letters are accepted! The characters {error_txt} are not accepted.", self.play_frame)
                self.score -= 1
                return
            elif not value: # Don't accept empty answers
                show_error("Enter an answer! If unsure, enter any letter.", self.play_frame)
                self.score -= 1
                return
            else:   # Don't accept just space answers
                letters = []
                for i in value:
                    letters.append(i)
                letters = set(letters)
                try:
                    letters.remove(' ')
                    if not letters:
                        show_error("Enter an answer! If unsure, enter any letter.", self.play_frame)
                        self.score -= 1
                        return
                except KeyError:
                    pass

            self.play_short_answer.unbind('<Return>')
            self.play_short_answer.bind('<Return>', self.next)
            self.play_short_answer_button.grid_forget()
            self.play_short_answer.configure(state=DISABLED)
            case_sensitive_answers = []
            for i in self.answer:
                case_sensitive_answers.append(i.lower())
            if value.lower() not in case_sensitive_answers:
                message = self.answer[0]
                if len(self.answer) != 1:
                    for i in self.answer:
                        if message != i:
                            message = "{} or {}".format(message, i)
                self.play_feedback.configure(text="Incorrect! The correct answer was {}.".format(message))
                self.score -= 1
        # Multi choice questions check
        else:
            value = self.others[btn_number]
            if self.answer != value:
                if type[self.question] == 'image multichoice':
                    self.answer = list(self.answer)
                    self.answer = self.answer[1]
                self.play_feedback.configure(text="Incorrect! The correct answer was {}.".format(self.answer))
                self.score -= 1
            self.play_button_1.configure(state=DISABLED)
            self.play_button_2.configure(state=DISABLED)
            self.play_button_3.configure(state=DISABLED)
            self.play_button_4.configure(state=DISABLED)
        self.play_next_button.grid(row=7, columnspan=2, pady=10)
        self.play_feedback.grid(row=6, columnspan=2, pady=10)
        return

    def open_id(self):
        # Set up frame
        self.play_frame.grid_forget()
        root.configure(menu=empty_menu)
        self.id_frame = Frame(root,
                              background=background)
        self.id_frame.grid(sticky=NSEW)

        # Heading
        id_heading = Label(self.id_frame,
                           bg=background,
                           text='Enter a 3 Letter Username:',
                           font=(font_default, '18', 'bold'),
                           width=30)
        id_heading.grid(row=0, pady=20, padx=5, columnspan=3)

        # Set up text variables
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.a.set('A')
        self.b.set('A')
        self.c.set('A')

        # Set up entry fields
        self.id_entry_a = Entry(self.id_frame,
                           font=(font_default, "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=self.a)
        self.id_entry_a.grid(row=2, column=0, pady=10)
        self.id_entry_b = Entry(self.id_frame,
                           font=(font_default, "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=self.b)
        self.id_entry_b.grid(row=2, column=1, pady=10)
        self.id_entry_c = Entry(self.id_frame,
                           font=(font_default, "18"),
                           width=3,
                           justify=CENTER,
                           textvariable=self.c)
        self.id_entry_c.grid(row=2, column=2, pady=10)
        self.id_entry_a.focus()

        # Bind to validate input
        self.id_entry_a.bind('<KeyRelease>', self.key_entered)
        self.id_entry_b.bind('<KeyRelease>', self.key_entered)
        self.id_entry_c.bind('<KeyRelease>', self.key_entered)

        # Prevent empty fields
        self.id_entry_a.bind('<FocusOut>', self.check_empty)
        self.id_entry_b.bind('<FocusOut>', self.check_empty)
        self.id_entry_c.bind('<FocusOut>', self.check_empty)

        # Continue button
        self.id_enter = Button(self.id_frame,
                          bg='gold',
                          activebackground='light goldenrod',
                          font=(font_default, '14', 'bold'),
                          text='Enter',
                          command=self.save_username)
        self.id_enter.grid(row=3, column=1, pady=20)
        self.id_enter.bind('<Return>', self.save_username)

    # Function to validate and change entry field
    def key_entered(self, event):
        try:
            self.error_label.grid_forget()
        except AttributeError:
            pass
        character = event.char
        caller = event.widget
        if caller == self.id_entry_a:
            setter = self.a
            next_widget = self.id_entry_b
        elif caller == self.id_entry_b:
            setter = self.b
            next_widget = self.id_entry_c
        else:
            setter = self.c
            next_widget = self.id_enter
        error = f"Please enter a letter! '{character}' is not accepted."
        if character == "\t" or not character:
            self.error_label = Label(self.id_frame,
                                text=error,
                                font=(font_default, '14', 'bold'),
                                bg=background,
                                fg='red')  # Hold var for .grid_forget()
            return ("break")
        if character:
            self.error_label = Label(self.id_frame,
                                text=error,
                                font=(font_default, '14', 'bold'),
                                bg=background,
                                fg='red')

        check = "[A-Za-z]"

        if re.match(check, character):
            setter.set(character.upper())
            next_widget.focus()
        else:
            setter.set('A')
            self.error_label.grid(row=1, columnspan=3, pady=10)

    # Prevent empty fields function
    def check_empty(self, event):
        caller = event.widget
        if caller == self.id_entry_a:
            setter = self.a
        elif caller == self.id_entry_b:
            setter = self.b
        else:
            setter = self.c
        value = caller.get()
        if not value:
            setter.set('A')

    # Prevent empty fields and continue command
    def save_username(self, event=None):
        self.id_enter.unbind('<Return>')
        a_txt = self.a.get()
        b_txt = self.b.get()
        c_txt = self.c.get()
        if a_txt and b_txt and c_txt:
            self.username = f"{a_txt}{b_txt}{c_txt}"
            # Save scores
            if self.random_mode:
                random_scores.append([self.score, self.username])
            else:
                scores.append([self.score, self.username, self.mode])
            self.id_frame.grid_forget()
            self.open_score()
        else:
            error = "Please enter a 3 letter username."
            show_error(error, self.id_frame)

    # Open Score GUI
    def open_score(self):
        # Set up Frame
        self.menu_frame.grid_forget()

        # Format GUI
        self.score_frame = Frame(root,
                            bg=background)
        self.score_frame.grid(sticky=NSEW)

        # Heading
        score_label = Label(self.score_frame,
                            text="High Scores",
                            font=(font_default, "18", "bold"),
                            bg=background,
                            width=20)
        score_label.grid(row=0, pady=20, padx=10, columnspan=2)

        # Frame for buttons
        self.score_chart_frame = Frame(self.score_frame,
                                  bg='gold')
        self.score_chart_frame.grid(row=1, padx=5, columnspan=2, sticky=NSEW)

        # Button to change mode
        score_random_button = Button(self.score_chart_frame,
                                     text="Random",
                                     font=(font_default, "14", "bold"),
                                     bg='gold',
                                     activebackground='light goldenrod',
                                     command=self.show_random_scores,
                                     width=20)
        score_random_button.grid(row=0, column=0)

        score_country_button = Button(self.score_chart_frame,
                                      text="Country",
                                      font=(font_default, "14", "bold"),
                                      bg='light goldenrod',
                                      activebackground='gold',
                                      command=self.show_country_scores,
                                      width=20)
        score_country_button.grid(row=0, column=1)

        # Frame for random scoreboard
        self.frame_random_score = Frame(self.score_chart_frame,
                                   bg='gold')

        # Scoreboard Headings
        score_heading_1 = Label(self.frame_random_score,
                                text="Player",
                                font=(font_default, "14", "bold"),
                                background='gold',
                                width=20)
        score_heading_1.grid(row=0, column=0)
        score_heading_2 = Label(self.frame_random_score,
                                text="Score",
                                font=(font_default, "14", "bold"),
                                background='gold',
                                width=20)
        score_heading_2.grid(row=0, column=1)

        # Display last played score
        try:
            if self.random_mode:
                last_played_txt = f"Last Played Game: Random Mode" \
                                  f"\n{random_scores[-1][1]}\t{random_scores[-1][0]}/10"
            else:
                last_played_txt = f"Last Played Game: {scores[-1][2]} Mode" \
                                  f"\n{scores[-1][1]}\t{scores[-1][0]}/10"
        except AttributeError:
            pass
        except IndexError:
            pass

        # Set up Scoreboard
        random_scores.sort(reverse=TRUE)
        if random_scores:
            for i in range(0, len(random_scores)):
                if i == 10:
                    break
                name_temp = Label(self.frame_random_score,
                                  bg='gold',
                                  font=(font_default, '14'),
                                  text=random_scores[i][1])
                name_temp.grid(row=i + 1, column=0)

                score_temp = Label(self.frame_random_score,
                                   bg='gold',
                                   font=(font_default, '14'),
                                   text=f"{random_scores[i][0]}/10")
                score_temp.grid(row=i + 1, column=1)
        else:
            random_score_text = Label(self.frame_random_score,
                                      bg='gold',
                                      text='No records',
                                      font=(font_default, '14'))
            random_score_text.grid(row=1, columnspan=2)

        # Frame for country mode
        self.frame_country_score = Frame(self.score_chart_frame,
                                    bg='light goldenrod')

        # Scoreboard headings
        score_heading_1 = Label(self.frame_country_score,
                                text="Player",
                                font=(font_default, "14", "bold"),
                                background='light goldenrod',
                                width=13)
        score_heading_1.grid(row=0, column=0)
        score_heading_2 = Label(self.frame_country_score,
                                text="Country",
                                font=(font_default, "14", "bold"),
                                background='light goldenrod',
                                width=13)
        score_heading_2.grid(row=0, column=1)
        score_heading_3 = Label(self.frame_country_score,
                                text="Score",
                                font=(font_default, "14", "bold"),
                                background='light goldenrod',
                                width=13)
        score_heading_3.grid(row=0, column=2)

        # Set up scoreboard
        scores.sort(reverse=True)
        if scores:
            for i in range(0, len(scores)):
                if i == 10:
                    break
                name_temp = Label(self.frame_country_score,
                                  bg='light goldenrod',
                                  font=(font_default, '14'),
                                  text=scores[i][1])
                name_temp.grid(row=i + 1, column=0)

                country_temp = Label(self.frame_country_score,
                                     bg='light goldenrod',
                                     font=(font_default, '14'),
                                     text=scores[i][2])
                country_temp.grid(row=i + 1, column=1)

                score_temp = Label(self.frame_country_score,
                                   bg='light goldenrod',
                                   font=(font_default, '14'),
                                   text=f"{scores[i][0]}/10")
                score_temp.grid(row=i + 1, column=2)
        else:
            country_score_text = Label(self.frame_country_score,
                                       bg='light goldenrod',
                                       text='No records',
                                       font=(font_default, '14'))
            country_score_text.grid(row=1, columnspan=3)

        try:
            if self.random_mode:
                self.frame_random_score.grid(row=2, columnspan=2)
            else:
                self.frame_country_score.grid(row=2, columnspan=2)
                self.score_chart_frame.configure(bg='light goldenrod')
            last_played_label = Label(self.score_frame,
                                      bg=background,
                                      font=(font_default, 14),
                                      text=last_played_txt)
            last_played_label.grid(columnspan=2, sticky=W + E, row=2, pady=5)
        except NameError:
            self.frame_random_score.grid(row=2, columnspan=2)
        except AttributeError:
            self.frame_random_score.grid(row=2, columnspan=2)

        # Return to menu button
        self.menu_button = Button(self.score_frame,
                             text="Menu",
                             font=(font_default, '14'),
                             bg="gold",
                             activebackground="light goldenrod",
                             command=self.open_menu,
                             width=9)
        self.menu_button.grid(row=3, pady=15, column=1)

        self.export_button = Button(self.score_frame,
                               bg='gold',
                               activebackground='light goldenrod',
                               font=(font_default, '14'),
                               text='Export...',
                               command=self.open_export)
        self.export_button.grid(row=3, column=0, pady=25)

    # Change mode to random scores
    def show_random_scores(self):
        self.frame_random_score.grid(row=2, columnspan=2),
        self.frame_country_score.grid_forget()
        self.score_chart_frame.configure(bg='Gold')

    # Change mode to country scores
    def show_country_scores(self):
        self.frame_random_score.grid_forget()
        self.frame_country_score.grid(row=2, columnspan=2, sticky=NSEW)
        self.score_chart_frame.configure(bg='light goldenrod')

    # Open Menu
    def open_menu(self, initial=False):
        root.config(menu=empty_menu)
        if initial == "Play":
            self.play_frame.grid_forget()
        else:
            self.score_frame.grid_forget()
        self.menu_frame.grid(sticky=NSEW)

    # Open export window and disable button
    def open_export(self):
        Export(self.export_button, self.menu_button)
        self.export_button.config(state=DISABLED)
        self.menu_button.config(state=DISABLED)


# Help window
class Help:
    def __init__(self, start_button, help_button, score_button, exit_button):
        # Create frame
        self.help_box = Toplevel()
        self.help_box.columnconfigure(0, weight=1)
        self.help_box.rowconfigure(0, weight=1)
        self.help_box.title("Countries Quiz > Help")
        self.help_box.focus()

        # Set up buttons to re-enable
        self.start_button = start_button
        self.help_button = help_button
        self.score_button = score_button
        self.exit_button = exit_button

        self.help_frame = Frame(self.help_box,
                                bg=background)
        self.help_frame.grid(sticky=NSEW)

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

        self.help_box.protocol("WM_DELETE_WINDOW", self.close_help)

    # Close window
    def close_help(self):
        self.help_box.destroy()
        self.help_button["state"] = NORMAL
        self.start_button["state"] = NORMAL
        self.score_button["state"] = NORMAL
        self.exit_button["state"] = NORMAL


# Export window
class Export:
    def __init__(self, export_btn, menu_btn):
        # Sets up child window (IE, Export box)
        self.export_box = Toplevel()
        self.export_box.columnconfigure(0, weight=1)
        self.export_box.rowconfigure(0, weight=1)
        self.export_box.title("Countries Quiz > Export")
        self.export_box.protocol("WM_DELETE_WINDOW", self.close_export)

        # Set up buttons to re-enable
        self.export_button = export_btn
        self.menu_button = menu_btn

        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, height=200, bg=background, pady=10)
        self.export_frame.grid(sticky=NSEW)

        # Set up Export Heading (row 0)
        export_heading = Label(self.export_frame,
                               text="Export",
                               font=(font_default, "18", "bold"),
                               bg=background,
                               padx=10,
                               pady=10)
        export_heading.grid(row=0)

        # Set up Export text (label, row 1)
        instruction_label = Label(self.export_frame,
                                  text="The file will be exported into the same folder as the program."
                                       "\nOnly, letters, numbers and '_' are allowed."
                                       "\nIf both checkmarks are left unchecked, both country mode scores"
                                       "\nand random mode scores will be exported."
                                       "\n\nEnter file name without the suffix (.txt):",
                                  font=(font_default, "12"),
                                  bg=background)
        instruction_label.grid(row=1, padx=5, pady=5)

        # Set up entry field
        self.file_name_entry = Entry(self.export_frame,
                                     font=(font_default, '14'),
                                     width=40)
        self.file_name_entry.grid(row=3, padx=10, pady=5)
        self.file_name_entry.focus()

        # Set up export option
        self.var_country = IntVar()
        self.var_random = IntVar()
        self.export_country_check = Checkbutton(self.export_frame,
                                                text="Country scores only",
                                                bg=background,
                                                font=(font_default, "8"),
                                                variable=self.var_country,
                                                command=lambda: self.check_mode(self.export_country_check),
                                                activebackground=background)
        self.export_country_check.grid(row=5)
        self.export_random_check = Checkbutton(self.export_frame,
                                               text="Random scores only",
                                               bg=background,
                                               font=(font_default, "8"),
                                               variable=self.var_random,
                                               command=lambda: self.check_mode(self.export_random_check),
                                               activebackground=background)
        self.export_random_check.grid(row=6, pady=5)

        # Set up Dismiss and export button (button, row 4)
        final_export_button = Button(self.export_frame,
                                     text="Export",
                                     font=(font_default, "14"),
                                     bg="gold",
                                     padx=10,
                                     width=9,
                                     command=self.export_file,
                                     activebackground='light goldenrod')
        final_export_button.grid(row=8, pady=5)
        self.file_name_entry.bind('<Return>', self.export_file)  # Export by Enter key

        export_dismiss_button = Button(self.export_frame,
                                       text="Dismiss",
                                       font=(font_default, "14"),
                                       bg="gold",
                                       padx=10,
                                       width=9,
                                       command=self.close_export,
                                       activebackground='light goldenrod')
        export_dismiss_button.grid(row=9, pady=20)

    # Re-enable export... button
    def close_export(self):
        self.file_name_entry.unbind('<Return>')  # Unbind Enter Key
        self.export_box.destroy()
        self.export_button.configure(state=NORMAL)
        self.menu_button.configure(state=NORMAL)

    # Only allow one checkbox to be selected
    def check_mode(self, event):
        if event == self.export_country_check:
            self.var_random.set(0)
        else:
            self.var_country.set(0)

    # Validate and check option, start export
    def export_file(self, empty=''):
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
            else:
                if len(errors) == 1:
                    error = "The character '{}' is not allowed!".format(errors[0])
                elif not errors:
                    pass
                else:
                    errors = dict.fromkeys(errors)
                    errors = list(errors)
                    characters = ""
                    for number in range(0, len(errors)):
                        characters = characters + " " + errors[number]
                    error = "The characters{} are not allowed!".format(characters)
        else:
            error = "Please enter a valid file name."
            accepted = False

        # Configure error messages
        if not accepted:
            show_error(error, self.export_box)
        else:
            # Create file
            self.filename = filename + ".txt"

            # If file exists, ask ok cancel
            do_export = True
            my_file = Path(self.filename)
            if my_file.is_file():
                do_export = msgbox.askokcancel("This file already exists!",
                                               f"{self.filename} is an existing file.\n\nOverwrite file?",
                                               parent=self.export_box, icon="warning")

            if do_export:
                # Check for empty records
                if self.var_random.get() == 1:
                    do_export = "Random"
                    if not random_scores:
                        do_export = self.no_records("Random")
                elif self.var_country.get() == 1:
                    do_export = "Country"
                    if not scores:
                        do_export = self.no_records("Country")
                else:
                    do_export = self.no_records("Both")

                # Export file info
                if do_export:
                    self.export = open(self.filename, "w+")
                    timestamp = str(datetime.now())
                    self.export.write("Country Quiz Scores\nExported " + str(timestamp[:timestamp.rindex(":")]) + "\n")
                    # Write file according to option
                    if do_export == "Random":
                        self.write_random()
                        self.exports = "Random mode scores"
                    elif do_export == "Country":
                        self.write_country()
                        self.exports = "Country mode scores"
                    else:
                        self.write_country()
                        self.write_random()
                        self.exports = "Country mode scores and Random mode scores"

                    self.show_export()

                    # Close file
                    self.export.close()
                else:
                    msgbox.showinfo("Export Cancelled!", "Did not export files.", parent=self.export_box)
            else:
                    msgbox.showinfo("Export Cancelled!", "Did not export files.", parent=self.export_box)

    # Message box for successful exports
    def show_export(self):
        msgbox.showinfo("Successfully Exported", f"{self.exports} successfully exported to {self.filename}!",
                        parent=self.export_box)

    # In case of empty records
    def no_records(self, event):
        if event == "Random":
            no_record_random = msgbox.askokcancel("No records!", "There are no records for Random Mode!\n\nExport anyway?", parent=self.export_box)    # Ask to export empty records
            if no_record_random:
                return "Random"
            else:
                return ""
        elif event == "Country":
            no_record_country = msgbox.askokcancel("No records!", "There are no records for Country Mode!\n\nExport anyway?", parent=self.export_box)   # Ask to export empty records
            if no_record_country:
                return "Country"
            else:
                return ""
        else:
            if not random_scores:
                no_record_random = msgbox.askokcancel("No records!", "There are no records for Random Mode!\n\nExport anyway?", parent=self.export_box)
                if no_record_random:
                    ex_random = "Random"
                else:
                    ex_random = ""
            else:
                ex_random = "Random"
            if not scores:
                no_record_country = msgbox.askokcancel("No records!", "There are no records for Country Mode!\n\nExport anyway?", parent=self.export_box)   # Ask to export empty records
                if no_record_country:
                    ex_country = "Country"
                else:
                    ex_country = ""
            else:
                ex_country = "Country"
            return str(ex_random + ex_country)

    # Export random scores
    def write_random(self):
        if random_scores:
            self.export.write("\n----------Random Mode----------\n\n")
            for record in range(0, len(random_scores)):
                self.export.write(
                    f"-{record + 1}-\nUsername: {random_scores[record][1]}\nScore: {random_scores[record][0]}\n\n")
        else:
            self.export.write("\n----------Random Mode----------\n\n")
            self.export.write("No records\n\n")

    # Export country scores
    def write_country(self):
        if scores:
            self.export.write("\n----------Country Mode----------\n\n")
            for record in range(0, len(scores)):
                self.export.write(
                    f"-{record + 1}-\nUsername: {scores[record][1]}\nScore: {scores[record][0]}\nCountry: {scores[record][2]}\n\n")
        else:
            self.export.write("\n----------Country Mode----------\n\n")
            self.export.write("No records\n\n")


# Main Routine
error_label = ''
background = "Lemon Chiffon"
font_default = "lucida console"
scores = []
random_scores = []
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    root.columnconfigure(0, weight=1)   # Allow window fill
    root.rowconfigure(0, weight=1)
    root.unbind_class("Button", "<Key-space>")  # Unbind existing binding
    empty_menu = Menu(root)  # To remove existing menu
    game = Quiz()
    root.mainloop()
