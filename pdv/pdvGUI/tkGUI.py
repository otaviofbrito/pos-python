import tkinter
from tkinter import *
from tkinter.ttk import Combobox

from pdv.dominio.Endereco import Endereco
from pdv.dominio.Loja import Loja
from pdv.dominio import TipoCalculadora
from pdv.dominio.pagamento.Operadora import Operadora

root = Tk()

endereco = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
loja = Loja("Supermercado Preço Bão", endereco)
registradora = loja.getRegistradora("R01")

#BACKEND SETTINGS
class Funcs():

    def start_new_sale(self):
        registradora.criarNovaVenda()
        self.button_1.config(state=tkinter.DISABLED)
        self.switch_widgets2("normal")
        self.combo_box_items.config(state="readonly")
        self.qtd_itens_spinbox.config(state="readonly")

        self.reset_widgets()
        self.switch_widgets3("disabled")


    def add_item(self):
        produto = self.combo_box_items.get()
        qtd = self.qtd_itens_spinbox.get()
        registradora.entrarItem(produto, int(qtd))

        self.qtdP_label.configure(text="qtd. produtos: " + str(registradora.getVendaCorrente().getItemQuantity()))
        total = round(registradora.getVendaCorrente().calcularTotalVenda(), 3)
        self.subt_label.configure(text="subtotal: R$" + str(total))

        self.qtd_itens_spinbox.config(state="normal")
        self.qtd_itens_spinbox.delete(0, END)
        self.qtd_itens_spinbox.insert(0, "1")
        self.qtd_itens_spinbox.config(state="readonly")


    def end_sale(self):
        registradora.finalizarVenda()
        total = round(registradora.getVendaCorrente().calcularTotalVenda(),3)
        self.total_label.configure(text="Total: R$" + str(total))
        self.switch_widgets3("normal")
        self.combo_box_payment.config(state="readonly")
        self.combo_box_issuer.config(state="readonly")
        self.parcelas_spinbox.config(state="readonly")

        self.switch_widgets2("disabled")
        self.button_1.config(state=tkinter.NORMAL)
        self.parcelas_spinbox.config(state=tkinter.DISABLED)
        self.issuer_label.config(state=tkinter.DISABLED)
        self.quantia_entry.config(state=tkinter.DISABLED)
        self.quantia_label.config(state=tkinter.DISABLED)
        self.inst_entry.config(state=tkinter.DISABLED)
        self.inst_label.config(state=tkinter.DISABLED)
        self.combo_box_issuer.config(state=tkinter.DISABLED)
        self.change_label.config(state=tkinter.DISABLED)

        self.payment_button.config(state=tkinter.DISABLED)

    def item_cb_selection(self, event):
        id = self.combo_box_items.get()
        self.slcP_label.configure(text=str(registradora.getCatalogo().getDescricaoProduto(id)))

    def issuer_cb_selection(self, event):
        self.payment_button.config(state=tkinter.NORMAL)

    def payment_cb_selection(self, event):
        selected = self.combo_box_payment.get()
        if selected == "Dinheiro":
            self.payment_button.config(state=tkinter.DISABLED)

            self.parcelas_spinbox.config(state=tkinter.DISABLED)
            self.issuer_label.config(state=tkinter.DISABLED)
            self.quantia_entry.config(state=tkinter.NORMAL)
            self.quantia_label.config(state=tkinter.NORMAL)
            self.inst_entry.config(state=tkinter.DISABLED)
            self.inst_label.config(state=tkinter.DISABLED)
            self.combo_box_issuer.config(state=tkinter.DISABLED)
            self.change_label.config(state=tkinter.NORMAL)
        elif selected == "Crédito":
            self.payment_button.config(state=tkinter.DISABLED)

            self.parcelas_spinbox.config(state=tkinter.NORMAL)
            self.issuer_label.config(state=tkinter.NORMAL)
            self.quantia_entry.config(state=tkinter.DISABLED)
            self.quantia_label.config(state=tkinter.DISABLED)
            self.inst_entry.config(state=tkinter.DISABLED)
            self.inst_label.config(state=tkinter.DISABLED)
            self.combo_box_issuer.config(state=tkinter.NORMAL)
            self.change_label.config(state=tkinter.DISABLED)

            self.combo_box_issuer.config(state="readonly")
            self.parcelas_spinbox.config(state="readonly")
        else:
            self.payment_button.config(state=tkinter.DISABLED)

            self.parcelas_spinbox.config(state=tkinter.DISABLED)
            self.issuer_label.config(state=tkinter.DISABLED)
            self.quantia_entry.config(state=tkinter.DISABLED)
            self.quantia_label.config(state=tkinter.DISABLED)
            self.inst_entry.config(state=tkinter.NORMAL)
            self.inst_label.config(state=tkinter.NORMAL)
            self.combo_box_issuer.config(state=tkinter.DISABLED)
            self.change_label.config(state=tkinter.DISABLED)

    def make_payment(self):
        totalVenda = registradora.getVendaCorrente().calcularTotalVenda()
        paymentType = self.combo_box_payment.get()
        troco = 0
        if paymentType == "Dinheiro":
            quantia = float(self.quantia_entry.get())
            registradora.fazerPagamentoDinheiro(totalVenda)
            troco = quantia - totalVenda
        elif paymentType == "Crédito":
            issuer = self.combo_box_issuer.get()
            parcelas = self.parcelas_spinbox.get()
            print(issuer + parcelas)
            registradora.fazerPagamentoCartao(totalVenda, str(issuer), int(parcelas), TipoCalculadora.JUROS_SIMPLES)
        else:
            inst = self.inst_entry.get()
            registradora.fazerPagamentoCheque(totalVenda, str(inst))

        self.switch_widgets3("disabled")
        self.reset_widgets()

        self.gerarRecibo(registradora, troco)

    def gerarRecibo(self, registradora, troco):
            venda = registradora.getVendaCorrente()
            print("")
            print("--------------------------- Supermercado Preço Bão ---------------------------")
            print("                             Registradora : " + registradora.getId())
            print("\t\t\t\tCUPOM FISCAL")
            print(venda)
            print("Troco................: R$ " + str(troco))

    def reset_widgets(self):
        self.subt_label.configure(text="subtotal: R$0,00")

        self.qtd_itens_spinbox.delete(0, END)
        self.qtd_itens_spinbox.insert(0, "1")

        self.qtdP_label.configure(text="qtd. produtos: 0")

        self.slcP_label.configure(text="Produto")
        self.combo_box_items.current(0)

        self.total_label.configure(text="Total: R$0,00")

        self.parcelas_spinbox.config(state="normal")
        self.parcelas_spinbox.delete(0, END)
        self.parcelas_spinbox.insert(0, "1")
        self.parcelas_spinbox.config(state="readonly")

        self.quantia_entry.config(state="normal")
        self.quantia_entry.delete(0, END)
        self.quantia_entry.insert(0, "")
        self.quantia_entry.config(state="readonly")

        self.inst_entry.config(state="normal")
        self.inst_entry.delete(0, END)
        self.inst_entry.insert(0, "")
        self.inst_entry.config(state="readonly")

        self.change_label.configure(text="Troco: R$0,00")


    def inst_evlistener(self,event):
        entered_text = self.inst_entry.get()
        if entered_text == "":
            self.payment_button.config(state=tkinter.DISABLED)
        else:
            self.payment_button.config(state=tkinter.NORMAL)


    def change_evlistener(self, event):
        totalVenda = registradora.getVendaCorrente().calcularTotalVenda()
        entered_text = self.quantia_entry.get()
        if not(self.is_valid_change(entered_text)):
            self.payment_button.config(state=tkinter.DISABLED)
            self.change_label.configure(text="Troco: R$0,00")
        else:
            value = float(entered_text)
            if value >= totalVenda:
                self.payment_button.config(state=tkinter.NORMAL)
                troco = round(value - totalVenda, 3)
                self.change_label.configure(text="Troco: R$" + str(troco))
            else:
                self.change_label.configure(text="Troco: R$0,00")
    def is_valid_change(self, input):
        try:
            value = float(input)
            return True
        except:
            return False

class App(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()
        self.switch_widgets2("disabled")
        self.switch_widgets3("disabled")



        root.mainloop()


    #disable/enable frame2 interaction
    def switch_widgets2(self, status):
        for widget in self.frame_2.winfo_children():
            widget.configure(state=status)

    #disable/enable frame3 interaction
    def switch_widgets3(self, status):
        for widget in self.frame_3.winfo_children():
            widget.configure(state=status)



    #FRONT END SETTINGS
    def tela(self):
        self.root.title("Supermercado Preço Bão!")
        self.root.configure(background="#46948e")
        self.root.geometry("633x477")
        self.root.resizable(False, False)

    def frames(self):
        self.frame_1 = Frame(self.root, bg='#d2d8d9')
        self.frame_1.place(relx=0.008, rely=0, relwidth=0.98, relheight=0.2)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.008, rely=0.21, relwidth=0.98, relheight=0.4)

        self.frame_3 = Frame(self.root)
        self.frame_3.place(relx=0.008, rely=0.62, relwidth=0.98, relheight=0.37)

    def widgets_frame1(self):
        self.button_1 = Button(self.frame_1, text="Nova venda", command=self.start_new_sale, font=("bold"))
        self.button_1.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.35)

        self.adress_label = Label(self.frame_1, text="Registradora", bg='#d2d8d9')
        self.adress_label.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.2)

        self.photo1 = PhotoImage(file='marketpixel.png')

        self.adress_label = Label(self.frame_1, text="", image=self.photo1, compound=BOTTOM, bg='#d2d8d9')
        self.adress_label.place(relx=0.60, rely=0.05, relwidth=0.2, relheight=1)


    def widgets_frame2(self):
        self.addP_label = Label(self.frame_2, text="Adicionar Produto")
        self.addP_label.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.15)

        self.combo_box_items = Combobox(self.frame_2)
        self.combo_box_items['values'] = ["01", "02", "03", "04", "05",
                                          "06", "07", "08", "09", "10"]
        self.combo_box_items['state'] = 'readonly'
        self.combo_box_items.place(relx=0.05, rely=0.18, relwidth=0.1, relheight=0.15)
        self.combo_box_items.bind("<<ComboboxSelected>>", self.item_cb_selection)
        self.combo_box_items.current(0)

        self.qtd_itens_spinbox = Spinbox(self.frame_2, from_=1, to=500)
        self.qtd_itens_spinbox['state'] = 'readonly'
        self.qtd_itens_spinbox.place(relx=0.2, rely=0.18, relwidth=0.1, relheight=0.15)


        self.add_button = Button(self.frame_2, text="Adicionar", command=self.add_item)
        self.add_button.place(relx=0.35, rely=0.18, relwidth=0.15, relheight=0.15)



        self.qtdP_label = Label(self.frame_2, text="qtd. produtos: 0")
        self.qtdP_label.place(relx=0.65, rely=0.18, relwidth=0.2, relheight=0.15)

        self.slcP_label = Label(self.frame_2, text="Produto", fg="blue", font=("Arial", 12, "bold italic"))
        self.slcP_label.pack(side=LEFT, padx=10)

        self.subt_label = Label(self.frame_2, text="subtotal: R$0.00 ", fg="blue")
        self.subt_label.place(relx=0.02, rely=0.88)

        self.end_sale_button = Button(self.frame_2, text="Finalizar venda", command=self.end_sale)
        self.end_sale_button.pack(side=BOTTOM, anchor=SE, padx=4)

    def widgets_frame3(self):
        self.payment_label = Label(self.frame_3, text="Pagamento")
        self.payment_label.place(relx=0.01, rely=0.05, relwidth=0.2, relheight=0.15)

        self.total_label = Label(self.frame_3, text="Total: R$0.00", fg="red",  font=("Arial", 15, "bold"))
        self.total_label.place(relx=0.65, rely=0.05, relwidth=0.3, relheight=0.2)

        self.combo_box_payment = Combobox(self.frame_3, values=["Dinheiro", "Crédito", "Cheque"])
        self.combo_box_payment['state'] = 'readonly'
        self.combo_box_payment.place(relx=0.2, rely=0.05, relwidth=0.2, relheight=0.15)
        self.combo_box_payment.bind("<<ComboboxSelected>>", self.payment_cb_selection)



        self.parcelas_spinbox = Spinbox(self.frame_3, from_=1, to=3)
        self.parcelas_spinbox['state'] = 'readonly'
        self.parcelas_spinbox.place(relx=0.4, rely=0.05, relwidth=0.1, relheight=0.15)

        self.quantia_label = Label(self.frame_3, text="Quantia")
        self.quantia_label.place(relx=0.01, rely=0.22, relwidth=0.2, relheight=0.15)

        self.quantia_entry = Entry(self.frame_3)
        self.quantia_entry.place(relx=0.2, rely=0.22, relwidth=0.2, relheight=0.15)
        self.quantia_entry.bind('<KeyRelease>', self.change_evlistener)

        self.change_label = Label(self.frame_3, text="Troco: R$0.00")
        self.change_label.place(relx=0.01, rely=0.8, relwidth=0.2, relheight=0.15)

        self.issuer_label = Label(self.frame_3, text="Operadora")
        self.issuer_label.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.15)

        self.combo_box_issuer = Combobox(self.frame_3, values=["VISA", "MASTERCARD", "DINNERS", "AMERICAN"])
        self.combo_box_issuer['state'] = 'readonly'
        self.combo_box_issuer.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.15)
        self.combo_box_issuer.bind("<<ComboboxSelected>>", self.issuer_cb_selection)


        self.inst_label = Label(self.frame_3, text="Instituição")
        self.inst_label.place(relx=0.01, rely=0.6, relwidth=0.2, relheight=0.15)

        self.inst_entry = Entry(self.frame_3)
        self.inst_entry.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.15)
        self.inst_entry.bind('<KeyRelease>', self.inst_evlistener)

        self.payment_button = Button(self.frame_3, text="Efetuar Pagamento", command=self.make_payment,fg='#127a4f',font=("Arial", 12, "bold"))
        self.payment_button.place(relx=0.68, rely=0.75, relwidth=0.3, relheight=0.15)

App()
