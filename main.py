import tkinter as tk
from tkinter import messagebox

def janelaDeposito():
    # Função para armazenar o saldo
    def salvarDeposito():
        try:
            deposito = float(entry_deposito.get())
            global saldo_armazenado
            global depositado
            saldo_armazenado += deposito
            depositado = deposito
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
            nova_janela.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")


    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Inserir Depósito")


    label = tk.Label(nova_janela, text="Insira o valor do depósito:")
    label.pack(pady=10)

    entry_deposito = tk.Entry(nova_janela)
    entry_deposito.pack(pady=10)


    botao_salvar = tk.Button(nova_janela, text="Salvar", command=salvarDeposito, bg="#EAADEA")
    botao_salvar.pack(pady=10)

def mostrarSaldo():
    messagebox.showinfo("Saldo Atual", f"Saldo: R$ {saldo_armazenado:.2f}")

def fazerSaque():
    def atualizarSaldo():
        try:
            saque = float(entry_saque.get())
            global saldo_armazenado
            global saqueTotal

            if saque > saldo_armazenado:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            else:
                saldo_armazenado -= saque
                saqueTotal = saque
                messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
                janela2.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")


    janela2 = tk.Toplevel(janela)
    janela2.title("Realizar Saque")


    label = tk.Label(janela2, text="Insira o valor do saque:")
    label.pack(pady=10)

    entry_saque = tk.Entry(janela2)
    entry_saque.pack(pady=10)


    botao_salvar = tk.Button(janela2, text="Salvar", command=atualizarSaldo, bg="#EAADEA")
    botao_salvar.pack(pady=10)

def mostrarExtrato():
    messagebox.showinfo("Extrato", f"Saldo: R$ {saldo_armazenado:.2f}\nÚltimo Depósito: R$ {depositado:.2f}\nÚltimo Saque: R$ {saqueTotal:.2f}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema Bancário")
cor = "#EAADEA"  # Lilás


saldo_armazenado = 0.0
depositado = 0.0
saqueTotal = 0.0


janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)


# Criação dos botões
saldo = tk.Button(janela, text="Saldo", width=25, bg=cor, command=mostrarSaldo)
extrato = tk.Button(janela, text="Extrato", width=25, bg=cor, command=mostrarExtrato)
deposito = tk.Button(janela, text="Depósito", width=25, bg=cor, command=janelaDeposito)
saque = tk.Button(janela, text="Saque", width=25, bg=cor, command=fazerSaque)

saldo.grid(row=0, column=0, padx=10, pady=10)
extrato.grid(row=0, column=1, padx=10, pady=10)
deposito.grid(row=1, column=0, padx=10, pady=10)
saque.grid(row=1, column=1, padx=10, pady=10)

janela.mainloop()
