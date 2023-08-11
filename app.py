import tkinter as tk
from tkinter import messagebox

class CaixaEletronico:
    def __init__(self):
        self.saldo = 1000

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class InterfaceCaixa:
    def __init__(self, root):
        self.root = root
        self.root.title("Caixa Eletrônico")

        self.caixa = CaixaEletronico()

        self.title_label = tk.Label(root, text="Banco GBB - Caixa Eletrônico", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.saldo_label = tk.Label(root, text="Saldo disponível:", font=("Helvetica", 12))
        self.saldo_label.pack()

        self.saldo_var = tk.StringVar()
        self.saldo_amount_label = tk.Label(root, textvariable=self.saldo_var, font=("Helvetica", 14, "bold"))
        self.saldo_amount_label.pack()

        self.consultar_button = tk.Button(root, text="Consultar Saldo", command=self.consultar_saldo, font=("Helvetica", 12))
        self.consultar_button.pack(pady=10)

        self.valor_saque_label = tk.Label(root, text="Valor do Saque:", font=("Helvetica", 12))
        self.valor_saque_label.pack()

        self.valor_saque = tk.Entry(root, font=("Helvetica", 14))
        self.valor_saque.pack()

        self.sacar_button = tk.Button(root, text="Sacar", command=self.efetuar_saque, font=("Helvetica", 12))
        self.sacar_button.pack(pady=10)

    def consultar_saldo(self):
        saldo_atual = self.caixa.consultar_saldo()
        self.saldo_var.set(f"R$ {saldo_atual:.2f}")

    def efetuar_saque(self):
        valor = int(self.valor_saque.get())
        if self.caixa.sacar(valor):
            messagebox.showinfo("Sucesso", f"Saque de R${valor} realizado com sucesso.")
            self.consultar_saldo()
        else:
            messagebox.showerror("Erro", "Saque não autorizado. Verifique o valor ou saldo disponível.")

if __name__ == "__main__":
    root = tk.Tk()
    interface = InterfaceCaixa(root)
    root.mainloop()