import tkinter as tk
import ticketidf as tidf

def funcao_a_executar():
    # Coloque aqui o código da função que você deseja executar
    print("A função foi executada!")

def aguardar_botao():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Aguardando Botão")

    # Cria um botão na janela
    botao = tk.Button(janela, text="Clique para Executar", command=tidf.capturar_imagem_webcam)
    botao.pack(padx=20, pady=20)

    # Inicia o loop principal da interface gráfica
    janela.mainloop()
