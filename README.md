# Documentação Caixa-Eletronico
 Simulador de caixa eletrônico simples com uso de Tkinter para interface. Foco em POO aplicada à Python.

"""
Módulo de Caixa Eletrônico com Interface Gráfica

Este módulo define classes que representam um caixa eletrônico e uma interface gráfica para interagir com o caixa eletrônico.
Utiliza a biblioteca tkinter para criar a interface gráfica e gerenciar as interações com o usuário.

Classes:
    CaixaEletronico: Representa um caixa eletrônico com operações de consulta de saldo e saque.
    InterfaceCaixa: Cria uma interface gráfica para interagir com o caixa eletrônico.

"""

import tkinter as tk
from tkinter import messagebox

class CaixaEletronico:
    """
    Representa um caixa eletrônico com operações de consulta de saldo e saque.

    Atributos:
        saldo (float): O saldo disponível no caixa eletrônico.

    Métodos:
        consultar_saldo(): Retorna o saldo atual do caixa eletrônico.
        sacar(valor): Tenta efetuar um saque no valor especificado.
    """

    def __init__(self):
        """Inicializa o caixa eletrônico com um saldo inicial de 1000."""
        self.saldo = 1000

    def consultar_saldo(self):
        """Retorna o saldo atual do caixa eletrônico."""
        return self.saldo

    def sacar(self, valor):
        """
        Tenta efetuar um saque no valor especificado.

        Args:
            valor (float): O valor a ser sacado.

        Returns:
            bool: True se o saque foi bem-sucedido, False caso contrário.
        """
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class InterfaceCaixa:
    """
    Cria uma interface gráfica para interagir com o caixa eletrônico.

    Atributos:
        root (Tk): A janela principal da interface.
        caixa (CaixaEletronico): Uma instância da classe CaixaEletronico.

    Métodos:
        consultar_saldo(): Atualiza a interface com o saldo atual.
        efetuar_saque(): Tenta efetuar um saque com o valor fornecido pelo usuário.
    """

    def __init__(self, root):
        """
        Inicializa a interface e cria os elementos gráficos.

        Args:
            root (Tk): A janela principal da interface.
        """
        self.root = root
        self.root.title("Caixa Eletrônico")

        self.caixa = CaixaEletronico()

        # Criação dos widgets da interface gráfica e suas configurações

    def consultar_saldo(self):
        """Atualiza a interface com o saldo atual do caixa eletrônico."""
        saldo_atual = self.caixa.consultar_saldo()
        self.saldo_var.set(f"R$ {saldo_atual:.2f}")

    def efetuar_saque(self):
        """Tenta efetuar um saque e exibe mensagens de sucesso ou erro na interface."""
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

