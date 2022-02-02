import string
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, Font
import controller.FileReader as reader
import os

from controller import Price
from useful.Useful import Useful
from view.component.textBoxDesc import TextBoxDesc
import controller.pricerequest as pr


class FrmPrincipal:
    _form = None
    _txt_busca = None
    geo = ""
    name = "Home"
    placeholder_text = "Ether..."
    form_title = "Cotação Atual"
    hasRezible_form = FALSE
    btnSub_title = "Atualizar"
    form_color = '#73726f'
    table_columns = ('Cód', 'Nome', 'Últ', 'Alta', 'Menor', 'Qtd')
    tb = string.whitespace

    tb_data = []
    tb_current_index_ordered = 0
    tb_next_index_order = None
    tb_next_reverse_ordered = False
    tb_current_reverse_ordered = False

    def __init__(self, xy="600x600+662+212"):
        self._form = Tk()
        self.geo = xy
        self.afterCreate()
        self.get_main_coins()
        self._form.mainloop()

    def afterCreate(self):
        # include all items to form
        self.form_render()
        self.lblH1_render()
        self.btnSubmit_render()
        self.table_render()
        self.txt_busca_render()

    def form_render(self):
        self._form.geometry(self.geo)
        self._form['bg'] = self.form_color
        self._form.wm_resizable(width=self.hasRezible_form, height=self.hasRezible_form)
        self._form.columnconfigure(0)
        self._form.columnconfigure(1)
        self._form.columnconfigure(2)
        self._form.rowconfigure(index=0, pad=50)
        self._form.rowconfigure(index=1, pad=10)
        self._form.title(self.form_title)
        self._form.bind("<Button-1>", self.stats)
        self._form.iconbitmap(default="source/app_image/app.ico")

    def lblH1_render(self):
        _font = Font(self._form, size=14, weight=BOLD)
        lbl = Label(self._form, bg=self.form_color)
        lbl.config(text="Cotação Atual")
        lbl.config(font=_font)
        lbl.grid(row=0, column=0, columnspan=2)

    def txt_busca_render(self):
        txt_busca = TextBoxDesc(master=self._form, desc=self.placeholder_text)
        txt_busca.grid(column=0, row=1)
        txt_busca.config(width=80)
        self._txt_busca = txt_busca

    def btnSubmit_render(self):
        sub = Button(self._form)
        sub.config(text="Pesquisar")
        sub.grid(column=1, row=1)
        sub.config(command=self.btnSubmit_Onclick)

    def btnSubmit_Onclick(self):
        if self._txt_busca.get().__len__() > 0 and self._txt_busca.get() != self.placeholder_text:
            self.tb_data = []
            self.get_coin(self._txt_busca.get().upper())
            self.set_data_table()
        elif self._txt_busca.get() != self.placeholder_text:
            self.get_main_coins()

    def stats(self, e):
        print(f'X: {e.x} \r\nY: {e.y}\r\nLocale: {self._form.geometry()}')

    def table_render(self):
        f = Frame(self._form)
        f.grid(columnspan=2)
        f.grid(row=3)

        head_columns = ("cod", "nome", "ult", "maior", "menor", "qtd")

        tb = ttk.Treeview(f, show="headings", columns=head_columns, height=13)
        tb.grid(row=1, column=0)

        scrollbar = ttk.Scrollbar(self._form, orient=VERTICAL, command=tb.yview)
        scrollbar.grid(row=3, column=2, sticky='nws')

        tb.configure(yscroll=scrollbar.set)

        tb.heading("#0", text="", anchor=CENTER)
        tb.heading("cod", text="Cód", anchor=CENTER, command=lambda n=0: self.order_by(n))
        tb.heading("nome", text="Moeda", anchor=CENTER, command=lambda n=1: self.order_by(n))
        tb.heading("ult", text="Últ", anchor=CENTER, command=lambda n=2: self.order_by(n))
        tb.heading("maior", text="Maior", anchor=CENTER, command=lambda n=3: self.order_by(n))
        tb.heading("menor", text="Menor", anchor=CENTER, command=lambda n=4: self.order_by(n))
        tb.heading("qtd", text="Qtd", anchor=CENTER, command=lambda n=5: self.order_by(n))

        tb.column("#0", width=0, stretch=NO)
        tb.column("cod", anchor=CENTER, width=80)
        tb.column("nome", anchor=CENTER, width=100)
        tb.column("ult", anchor=CENTER, width=100)
        tb.column("maior", anchor=CENTER, width=100)
        tb.column("menor", anchor=CENTER, width=100)
        tb.column("qtd", anchor=CENTER, width=100)
        self.tb = tb

    def get_main_coins(self):
        dir = os.getcwd() + "\\bigcoins.json"
        file = reader.FileReader(file=dir)
        file.sort_content()

        for coin in file.content:
            self.get_coin(coin)

        self.set_data_table()

    def get_coin(self, coin):
        price = pr.PriceRequest()
        ret = price.call_request(coin=coin, method="ticker")
        if ret.error == 0:
            data = ret.data
            self.add_to_list(coin, data)
        else:
            print("erro")

        self.tb_data.sort(key=self.order)

    def add_to_list(self, coin, data):
        ult = Price.Price.format_number(data["ticker"]['last'])
        alt = Price.Price.format_number(data["ticker"]["high"])
        low = Price.Price.format_number(data["ticker"]["low"])

        data = (coin, coin, ult, alt, low,
                data["ticker"]["vol"])

        self.tb_data.append(data)

    def order(self, e):
        return getdouble(e[2])

    def order_by(self, index):
        self.tb_next_index_order = index
        if index == self.tb_current_index_ordered:
            reverse = not self.tb_current_reverse_ordered
            self.tb_current_reverse_ordered = not self.tb_current_reverse_ordered
        else:
            reverse = False
        self.tb_current_index_ordered = index
        self.tb_data.sort(key=self._order_by, reverse=reverse)
        self.set_data_table()

    def _order_by(self, e):
        if Useful.is_number(e[self.tb_next_index_order]):
            return getdouble(e[self.tb_next_index_order])
        else:
            return e[self.tb_next_index_order]

    def set_data_table(self):
        self.tb.delete(*self.tb.get_children())
        for x in self.tb_data:
            self.tb.insert(index=END, parent="", values=x)
