frame = Frame(self._form)
        tb = ttk.Treeview(frame)

        tb['columns'] = ("cod", "nome", "ult", "maior", "menor", "qtd")
        tb.column("#0", width=0, stretch=NO)
        tb.column("cod", anchor=CENTER, width=80)
        tb.column("nome", anchor=CENTER, width=80)
        tb.column("ult", anchor=CENTER, width=80)
        tb.column("maior", anchor=CENTER, width=80)
        tb.column("menor", anchor=CENTER, width=80)
        tb.column("qtd", anchor=CENTER, width=80)

        tb.heading("#0", text="", anchor=CENTER)
        tb.heading("cod",text="Cód", anchor=CENTER)
        tb.heading("nome", text="Moeda", anchor=CENTER)
        tb.heading("ult", text="Últ", anchor=CENTER)
        tb.heading("maior", text="Maior", anchor=CENTER)
        tb.heading("menor", text="Menor", anchor=CENTER)
        tb.heading("qtd", text="Qtd", anchor=CENTER)

        tb.insert(parent='', index='end', iid=0, text='',
                   values=('btc', 'john', 'Gold', '', '', '', ''))