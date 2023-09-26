# Arquitetura do sistema

O sistema utiliza a arquitetura MVC (Model-View-Controller) para separar as responsabilidades de cada parte do sistema e facilitar a manutenção e o desenvolvimento.

## Views

Dentro da pasta /views temos todo processo realizado para comunicação direto com ambiente externo. Sendo assim os comandos para camera e comunicação com carteiro estão todos ali localizados.

## Controller

Ja dentro da pasta /controllers temos toda a descrição do fluxo que o programa deve seguir para garantir que cumpra a função pelo qual ele foi desenvolvido. Que no caso seria de inicializar a camera, cumprimentar o carteiro ao localiza-lo e após isso tentar ao maximo 4 vezes identificar e processar a etiqueta.

## Model

Dentro da pasta /models temos toda a construção de estrutua dos dados tanto na forma com que executamos o programa quanto na questão de registrar a
