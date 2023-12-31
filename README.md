# CPIRv1 - Correios Postman Identification Robot v1

![CPIRv1](images/robot_image.jpg)

## Visão Geral
O CPIRv1 é um projeto que visa melhorar a eficiência da identificação de entregas em condomínios. Ele utiliza técnicas de inteligência artificial e visão computacional para identificar a chegada dos carteiros e catalogar as encomendas, indicando o destinatário correto.

## Pré-Requisitos
- Python 3.10.12
- Plataforma: Ubuntu 22.04 (O programa só funciona em sistemas Linux)

## Bibliotecas Utilizadas
- TensorFlow 2.12.0
- OpenCV 4.8.0.76
- Elevenlabs 0.2.26
- Pytesseract 0.3.10
- Pillow 9.0.1
- Numpy 1.23.5
- Keras 2.12.0

## Como Usar
1. Clone este repositório em sua máquina local.

```bash
git clone https://github.com/Boakpe/CPIRv1.git
```

2. Certifique-se de que possui todas as bibliotecas mencionadas instaladas.

3. Execute o programa principal:

4. Certifique-se de que possui todas as bibliotecas mencionadas instaladas.

5. Execute o programa principal: app.py

6. Quando for identificado um carteiro será solicitado por uma voz que você tire uma foto da etiqueta da encomenda.

7. Aparecera uma janela com a imagem da câmera, posicione a etiqueta no centro da imagem e tire a foto apertando a tecla "space".

8. Caso o programa não consiga identificar o destinatário, será solicitado que você digite o nome do destinatário.

9. O programa irá salvar o nome do destinatário, a data e a hora da entrega em um arquivo .json.

10. O programa espera 20 segundos para que o carteiro saia da imagem e então volta a procurar por carteiro.