# Console Chat Simples em Python

Este projeto é um chat simples que roda no console, permitindo que os usuários enviem e visualizem mensagens durante a execução do programa. O chat exibe o nome do usuário e as respectivas mensagens em um loop contínuo até que o usuário insira o comando "end".

## Funcionalidades

- **Entrada de nome do usuário:** O programa solicita o nome do usuário no início da execução.
- **Envio de mensagens:** Os usuários podem digitar mensagens que são imediatamente exibidas no console.
- **Histórico de mensagens:** O console mostra todas as mensagens anteriores com o nome do remetente.
- **Limpeza da tela:** O comando `os.system('cls')` limpa a tela a cada novo envio de mensagem.
- **Encerramento do chat:** O programa é encerrado quando o usuário digita `end`.

## Como Funciona

1. **Entrada do nome:** O usuário insere seu nome, que será exibido ao lado de cada mensagem enviada.
2. **Loop principal:** Um loop contínuo captura as mensagens do usuário e as armazena em uma lista de dicionários, onde cada dicionário contém o nome do usuário e a mensagem.
3. **Exibição das mensagens:** Após cada nova mensagem, todas as mensagens anteriores são exibidas, seguidas pela nova entrada.
4. **Finalização:** O loop é finalizado quando o usuário digita `end` como mensagem.

## Requisitos

- **Sistema Operacional:** O comando `os.system('cls')` é utilizado para limpar o console, sendo compatível com Windows. Para outros sistemas operacionais (Linux/macOS), é necessário substituir por `os.system('clear')`.
- **Python 3.x** instalado.

## Exemplo de Uso

1. Execute o script:

    ```bash
    python main.py
    ```

2. Insira seu nome quando solicitado:

    ```bash
    Name: Lucas
    ```

3. Digite suas mensagens no chat. As mensagens anteriores aparecerão na tela:

    ```bash
    Lucas - Olá, como você está?
    Lucas - Esse chat é simples, mas funciona!
    ```

4. Para sair, digite `end`:

    ```bash
    Message: end
    ```

## Personalização

- **Mudança do comando de limpeza de tela:**  
   Se estiver utilizando Linux ou macOS, altere a linha:
   
    ```python
    os.system('cls')
    ```
   
   Para:
   
    ```python
    os.system('clear')
    ```


