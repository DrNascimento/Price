import tkinter as tk


class TextBoxDesc(tk.Entry):
    def __init__(self, master=None, desc="Hi"):
        super().__init__(master)
        self.desc = desc
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_outfocus)
        self.show_describe()

    def show_describe(self):
        self.insert(0, self.desc)
        self.config(fg='grey50')

    def on_focus(self, e):
        if self.get() == self.desc:
            self.delete('0', 'end')
            self.config(fg='black')

    def on_outfocus(self, e):
        if not self.get():
            self.config(fg='grey50')
            self.show_describe()

