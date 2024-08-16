import discord
import aiohttp

# Substitua 'YOUR_DISCORD_TOKEN' pelo token do seu bot.
TOKEN = '################################'
API_URL = 'https://pythonium.net/api/checker'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def check_syntax(code: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(API_URL, data=code, headers={"Content-Type": "text/plain"}) as response:
                if response.content_type == 'application/json':
                    result = await response.json()
                    if result['error'] == 0:
                        return result['message'], result['errors']
                    else:
                        return "An error occurred while checking syntax.", []
                else:
                    error_message = await response.text()
                    return f"Unexpected response type: {response.content_type}\n{error_message}", []
        except aiohttp.ClientError as e:
            return f"Request failed: {str(e)}", []

@client.event
async def on_ready():
    print(f'Bot {client.user} conectado com sucesso!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!checkpython'):
        # Extrai o código Python da mensagem
        code = message.content[len('!checkpython'):].strip()
        
        # Verifica a sintaxe
        message_text, errors = await check_syntax(code)
        
        if errors:
            formatted_errors = "\n".join(errors)
            await message.channel.send(f"Erros de sintaxe encontrados:\n```{formatted_errors}```")
        else:
            await message.channel.send(message_text)

client.run(TOKEN)