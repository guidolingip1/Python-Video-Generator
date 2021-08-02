import os;
import os.path;
from PIL import Image, ImageFont, ImageDraw, ImageOps
from moviepy.editor import VideoFileClip, concatenate_videoclips;

#GLOBAL
lista_de_imagens = [];

#Criei uma função que adiciona o texto e cria um logo para cada uma das mensagens da lista :D, só preciso passar ele aqui junto com a posição x e y
# ex: adiciona_texto("Oi", 0,0);
def adiciona_texto(texto, saida):
  W, H = (900,600)
  img = Image.open("logo.png")
  if img.mode in ("RGBA", "P"): img = img.convert("RGB")
  draw = ImageDraw.Draw(img)
  arial = ImageFont.truetype("FONTS/arial.ttf", 45)
  w,h = arial.getsize(texto)
  draw.text(((W-w)/2,(H-h)/2),texto,(99,208,227),font=arial)
  img.save(saida + ".jpg")

#Transforma o logo com a descrição do vídeo em um vídeo :3 para concatenar nos outros vídeos '-'
def gera_video_logo(nr_video):
  os.system("ffmpeg -loop 1 -i "+ nr_video + ".jpg -c:v libx264 -t 3 -pix_fmt yuv420p -vf scale=900:900 ./videos/"+ nr_video + ".mp4")
  os.remove(nr_video + ".jpg")

#Pega todos os vídeos da pasta e da um merge em todos
def cria_video():
  path = "C:/Users/Guilherme/Desktop/Projetos/projeto-videos/videos/";
  cliparray = [];

  for filename in os.listdir(path):
      cliparray.append(VideoFileClip(path + filename));

  final_clip = concatenate_videoclips(cliparray, method='compose');
  final_clip.write_videofile("final.mp4");

def gera_descricao():
  cont = 11;
  path = "C:/Users/Guilherme/Desktop/Projetos/projeto-videos/videos/";
  for filename in os.listdir(path):
    lista_de_imagens.append(filename);
    os.rename(path+filename,path+str(cont)+".mp4");
    cont+=10;


# main
#1 --> Pega o nome de cada vídeo e utiliza como a descrição
gera_descricao()

#2 --> Depois para cada elemento da lista criamos uma imagem com essa descrição
for i in range(len(lista_de_imagens)):
  posic = ((i+1) * 10);
  adiciona_texto(lista_de_imagens[i], str(posic));
  gera_video_logo(str(posic));

#3 --> No final unimos tudo em um único vídeo
cria_video();


#Outros
# Remover áudio
#-----> os.system("ffmpeg -i final.mp4 -c copy -an final_mute.mp4");

# Colocar um novo áudio por cima já calibrado onde os vídeos tem a duração do áudio, se tem 2 min de música tem 2 min de vídeo.
#-----> os.system("ffmpeg -i final_mute.mp4 -i audio1.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4");


