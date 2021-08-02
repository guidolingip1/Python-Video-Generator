# Auto video maker com Python

![PythonScript](https://github.com/guidolingip1/Python-Video-Generator/blob/master/script.gif)

## O que é?
É complicado HAHHAHA, é um projeto que pega diversos videos e transforma em um só.
Adicionando uma thumbnail que é gerada automaticamente baseada no nome do arquivo.

**Achou complicado?**
Sem problemas, vamos ver melhor durante o andamento do artigo.
## Tecnologias
Python e minha cabeça (fotinho de um cerebro)

## Como rodar o Script?
### 1° Parte
Primeiro começamos baixando os vídeos que queremos que sejam parte do vídeo final.
Esses vídeos devem ser jogados dentro da pasta vídeo.
É importante que o nome do vídeo seja o texto da sua thumb.(verá melhor depois)
Colocar uma foto da pasta com a pasta vídeo.

### 2° Parte
Crie uma imagem simples, só com o logo do seu canal ou algo que queira adicionar na thumb.
Semelhante a essa:
COLOCAR A FOTO DA THUMB AQUI

### 3° Parte
Rodar o Script.

## Como o Script funciona?
### Parte 1 do Script
Ele busca na pasta vídeos todos os arquivos e cria uma lista com o nome de cada um dos arquivos.
Como dito anteriormente cada vídeo tem que ter como nome a descrição da thumb que será gerada.
Logo a parte um irá gerar uma lista com a thumb de cada vídeo.

### Parte 2 do Script
Agora, para cada descrição da Lista de descrições, será gerada uma thumbnail automaticamente.
Além disso, cada vídeo é renomeado para um número múltiplo de 10 + 1, exemplo:
Um vídeo que se chamava "Senhora fica feliz ao rever cachorrinho.mp4" vira 11.mp4

**Ah mas porque essa gambiarra?**
Porque estamos criando um Script que faz tudo, e o modo dele de adicionar uma thumb no vídeo é concatenando vários vídeos em sequência e quando ele busca na pasta vídeos, os vídeos tem que manter uma ordem, se não pode ocorrer um erro do tipo, exemplo:
Podemos ter uma thumb que diz "Menino faz gol incrível" e logo em seguida aparecer um vídeo que não tem nada a ver com o menino, e isso é um erro que é corrigido com essa gambiarra :D.

### Parte 2 da parte 2
Agora assim que uma thumbnail é gerada ela é gerada como uma imagem, ai nós temos uma problema pois não temos como concatenar uma imagem com um vídeo.
Então transformamos nossa imagem em um vídeo e depois renomeamos esse vídeo gerado.
Ou seja, uma foto de uma thumb vira um vídeo de 3 segundos, que é renomeado como um múltiplo de 10.

Agora tudo faz sentido, pois o vídeo "Senhora fica feliz ao rever cachorrinho.mp4" vira 11.mp4 e a thumbnail do vídeo da senhora vira 10.mp4, assim na hora de juntar tudo, todos os vídeos ficam na ordem certinha.

### Parte 3
Por último pegamos todos os vídeos da pasta vídeo e juntamos todos eles em um único vídeo.

### Extras
Ainda tem uma parte do Script que está comentada que pode remover o áudio do vídeo e adicionar um áudio escolhido no lugar.
