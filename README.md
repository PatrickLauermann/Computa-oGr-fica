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

## Saídas da Solução Proposta

**Reconhecimento do Objeto Treinado (Símbolo de deficiência física)**
![ReconhecimentoSimbolo](https://user-images.githubusercontent.com/39313943/101228665-74008300-367b-11eb-8e8b-6257fdd2d055.png)

**Reconhecimento Facial**
![ReconhecimentoFacial](https://user-images.githubusercontent.com/39313943/101228760-d0fc3900-367b-11eb-849f-69ed3de2b672.png)

**Redimensionamento da Imagem**
![Redimensionamento](https://user-images.githubusercontent.com/39313943/101228785-e5403600-367b-11eb-8225-5bdb72bdc10f.png)

**Processamento** 
![Processamento1](https://user-images.githubusercontent.com/39313943/101228812-0dc83000-367c-11eb-8535-a07d5966306e.png)

![Processamento2](https://user-images.githubusercontent.com/39313943/101228827-1ae51f00-367c-11eb-91ab-056e2bfe1f5f.png)

![Processamento3](https://user-images.githubusercontent.com/39313943/101228800-f5f0ac00-367b-11eb-8633-3cf81b172ac0.png)

**Mudança de Cor**
![MudancaCores](https://user-images.githubusercontent.com/39313943/101228841-2afcfe80-367c-11eb-923a-00be92346c2a.png)

**Binarização**
![Binarização](https://user-images.githubusercontent.com/39313943/101228866-41a35580-367c-11eb-867d-2904f7487244.png)

**Correção Morfológica**
![Morfologia](https://user-images.githubusercontent.com/39313943/101228881-51229e80-367c-11eb-8f39-d610719a63b9.png)
