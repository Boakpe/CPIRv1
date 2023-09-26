# Relatório do Projeto

## Desafios Enfrentados

Foram encontrados desafios durante o desenvolvimento do projeto. Muitos deles provenientes da falta de experiência com as bibliotecas utilizadas.

Dentre os desafios, os que mais se destacam são:

- Compatibilidade com sistema operacional: 

    - Em mais de uma ocasião, não foi possível realizar testes em 2 dos computadores dos membros do projeto. Em decorrência de dificuldades com a portabilidade das bibliotecas utilizadas. Em específico, a ffmped para as saídas de áudio do robô e o keras para a detecção dos objetos pela camêra.

        > A solução foi utilizar de máquinas virtuais para que o sistema virtual fosse consistente em todas as máquinas e na versão em que não eram encontrados problemas.

- Detecção de texto:
    - Enquanto a ideia inicial era que o texto do pacote fosse lido pela camêra da mesma maneira que o carteiro é identificado (em tempo real, sem precisa tirar uma foto), isso se provou uma tarefa acima do escopo de nossas habilidades atuais.
        > A solução foi emular o pacote por meio de uma foto previamente selecionada (2 estão disponíveis para teste) como se o robô tivesse tirado uma foto das informações do pacote e então interpreta-se elas.

        > Também foi implementado a função que lê por meio da câmera as informaçãos do pacote. No entanto, não é tão eficaz quanto a das imagens selecionadas. 

## Resultados Obtidos

Após a conclusão da codificação do projeto, foram alcançados os objetivos principais definidos durante as etapas iniciais. 

O robô, consegue usar de seus sentidos para detectar a presença de um carteiro, e pegar as informações do pacote que o mesmo entregar a ele. Essas informações sendo o destinatário e horário de entrega. O que permitiria a ele ir entregar o pacote a pessoa que fez o pedido, uma vez que todos os moradores do prédio estão salvos para que possa fazer a correspondência do nome ao apartamento.

Portanto, é possível concluir que o projeto foi um sucesso e alcançou seus objetivos principais.