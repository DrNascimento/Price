from tkinter import getdouble


class Price:

    @staticmethod
    def format_number(number):
        return "{:10.4f}".format(getdouble(number))


