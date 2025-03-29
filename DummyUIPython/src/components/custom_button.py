"""Reusable Dialog UI component."""

import tkinter as tk
from tkinter import messagebox


class CustomButton(tk.Button):
    """Reusable UI Dialog is used to display a message."""

    def __init__(self, parent: tk.Tk, button_title: str):
        # Tip: Make the 'command' a parameter to make this more reusable.
        super().__init__(parent, text=button_title, command=self._show_message)
        self.parent: tk.Tk = parent

    def _show_message(self):
        messagebox.showinfo("Button Clicked", "Hello! You clicked the button.")
