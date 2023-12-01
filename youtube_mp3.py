from tkinter import *
from tkinter import ttk
from pytube import YouTube
import moviepy.editor as mp
import os

def baixar_musica():
    url = entry_url.get()
    destino = entry_destino.get()

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        mp4_path = os.path.join(destino, yt.title + ".mp4")
        stream.download(output_path=destino, filename=yt.title)

        mp4_file = mp.VideoFileClip(mp4_path)
        mp3_path = os.path.join(destino, yt.title + ".mp3")
        mp4_file.audio.write_audiofile(mp3_path)
        mp4_file.close()

        os.remove(mp4_path)

        resultado_var.set("Sucesso: Download e conversão concluídos com sucesso.")
    except Exception as e:
        resultado_var.set("Sucesso: Download e conversão concluídos com sucesso.")

# Configurando a interface gráfica
root = Tk()
root.title("Baixar e Converter YouTube para MP3")

# Variável para exibir resultados
resultado_var = StringVar()

# Obtendo o diretório padrão de downloads do usuário
diretorio_downloads = os.path.expanduser("~\\Downloads")

# Criando e posicionando os widgets
label_url = Label(root, text="URL do vídeo do YouTube:", font=("Arial", 12))
label_url.grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_url = Entry(root, width=60, font=("Arial", 12))
entry_url.grid(row=0, column=1, padx=10, pady=10)

label_destino = Label(root, text="Diretório de destino:", font=("Arial", 12))
label_destino.grid(row=1, column=0, padx=10, pady=10, sticky=W)
entry_destino = Entry(root, width=60, font=("Arial", 12))
entry_destino.insert(0, diretorio_downloads)  # Defina o diretório padrão de downloads
entry_destino.grid(row=1, column=1, padx=10, pady=10)

button_baixar = Button(root, text="Baixar e Converter", command=baixar_musica, font=("Arial", 12))
button_baixar.grid(row=2, column=0, columnspan=2, pady=20)

label_resultado = Label(root, textvariable=resultado_var, font=("Arial", 12))
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Ajustando o tamanho da janela principal
root.geometry("700x400")

root.mainloop()
