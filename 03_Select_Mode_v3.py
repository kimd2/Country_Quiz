"""
Component 3 - Select Mode
Diane Kim
29/07/21
Version 3 - Change scrollbar color
"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


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

    # Open start window
    def open_start(self):
        print("Start Opened")
        # Forget menu frame
        global menu_frame, mode_cb
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

        # Modes available
        modes = ("Random", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

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
        mode = mode_cb.get()
        print("Mode selected:", mode)





background = "Lemon Chiffon"
font_default = "Lucida Console"
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    game = Quiz()
    root.mainloop()
