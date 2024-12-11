# Python Syntax Checker

Este é um bot de Discord que verifica a sintaxe do código Python enviado por mensagem. Ele utiliza a API do Pythonium para realizar a verificação. 

---

### **Requisitos:**

Python 3.8 ou superior

Bibliotecas discord.py e aiohttp instaladas (pip install discord.py aiohttp)

---


### **Como usar:**

1.Crie um novo aplicativo no portal de desenvolvedores do [Discord]() ([https://discord.com/developers/applications](https://discord.com/developers/applications)).

2.Crie um novo bot e obtenha o token.

3.Substitua 'YOUR_DISCORD_TOKEN' no final do código pelo token do seu bot.

4.Inicie o bot executando o arquivo Python.

**Comandos:**

Use o comando !checkpython seguido do código Python que deseja verificar. Por exemplo, !checkpython print('Hello, World!').

**Exemplo de Uso:**

````python
!checkpython print('Hello, World!')
Erros de sintaxe encontrados:
```python
print('Hello, World!')
                      ^
SyntaxError: EOL while scanning string literal
````

Insert

Copy

**Notas:**

O bot só pode ser usado em canais de texto.

O bot não pode verificar a sintaxe de código com mais de 2000 caracteres.

O bot não pode verificar a sintaxe de código que contenha caracteres não ASCII.

Se você encontrar algum bug ou tiver alguma sugestão, abra um problema no [GitHub]() (https://github.com/bttex/python-syntex-bot