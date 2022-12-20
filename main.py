import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('API_TOKEN')
token = os.getenv('BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="You are a funny chat bot. You are very unfriendly and extremely sarcastic. You do not answer every question correctly. "+str(message.content),
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=None
            )

            answer = response["choices"][0]["text"]

            await message.channel.send(answer)

        except:
            await message.channel.send("You messed up. Try again.")

intents = discord.Intents.default()

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(token)
