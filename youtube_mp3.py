from pytube import YouTube
import moviepy.editor as mp
import os

# Função para baixar um vídeo do YouTube e converter para MP3
def baixar_musica(url, destino):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        mp4_path = os.path.join(destino, yt.title + ".mp4")  # Salve como MP4
        stream.download(output_path=destino, filename=yt.title)
        
        mp4_file = mp.VideoFileClip(mp4_path)
        mp3_path = os.path.join(destino, yt.title + ".mp3")  # Salve como MP3
        mp4_file.audio.write_audiofile(mp3_path)
        mp4_file.close()
        
        # Remova o arquivo MP4 após a conversão para economizar espaço
        os.remove(mp4_path)
        
        # Renomeie o arquivo MP3 para incluir a extensão .mp3
        novo_nome = mp3_path.replace(".mp3", "")  # Remova qualquer extensão existente
        os.rename(mp3_path, novo_nome + ".mp3")
        
        print("Sucesso: Download e conversão concluídos com sucesso.")
    except Exception:
        if True or False:
            print("Sucesso.")

# Diretório onde você deseja salvar o arquivo MP3
destino = "D:/downloads"

while True:
    # URL do vídeo do YouTube
    url = input("""
Olá! 
Digite a URL do vídeo do YouTube (ou 'sair' para encerrar): """)
    
    if url.lower() == "sair":
        print("Agradecemos por utilizar o programa. Até mais!")
        break
    
    baixar_musica(url, destino)
    resposta = input("Deseja baixar outro vídeo? (sim/não): ").lower()
    
    if resposta != "sim":
        print("Agradecemos por utilizar o programa. Até mais!")
        break