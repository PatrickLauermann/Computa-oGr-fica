# Responsáveis pelo projeto: Guilherme Cardozo e Patrick Lauermann

## Projeto Integrado de Visão Computacional 
**Proposta do projeto**

Com o objetivo de contemplar um público específico garantindo a inclusão e acessibilidade, optamamos por trabalhar com o reconhecimento do símbolo de deficiência física

permitindo maior controle das vagas destinadas a esse público. Além disso, foi aplicado neste projeto técnicas de processamento de imagem afim de obter resultados 

satisfatórios no reconhecimento do objeto treinado. 

## Ferramentas Utilizadas
OpenCV.

CascadeClassifier.

HaarCascade.

DataTime.

Modelo de reconhecimento de faces **haarcascade_frontalface_alt**.

## Etapas de processamento:

1 - Estruturação do dataset de imagens utilizado no treinamento do objeto escolhido. (Símbolo de deficiência física)

2 - Preparação do conjunto de imagens negativas para garantir resultados satisfatórios após o treinamento.

3 - Criação das pastas **Positivas, Negativas e Treinamento**.

4 - Aplicação dos seguintes códigos no prompt de comandos:

**python buildListNegative.py**

**caminho bin opencv\opencv_annotation --annotations=saida.txt --images=positivas/**

**caminho bin opencv\opencv_createsamples -info saida.txt -bg negativas.txt -vec vetor.vec -w 24 -h 24**

**caminho bin opencv\opencv_traincascade -data treinamento -vec vetor.vec -bg negativas.txt -numPos 200 -numNeg 450 -w 24 -h 24 -**

5 - Realização de testes após a conclusão do treinamento.

## Técnicas Utilizadas

1 - Processamento

2 - redimensionamento

3 - recorte

4 - Mudança de Cores

5 - Reconhecimento Facial

6 - Binarização

7 - Detecção de Bordas

8 - Correção Morfológica

9 - Seleção por Cores
