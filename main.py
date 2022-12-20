import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = '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'
token = os.getenv('BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        log = open('log.txt', 'w')
        msg = str(message.content)

        log.write("user: " + msg + "\n")

        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="You are a funny chat bot. You are very unfriendly and extremely sarcastic. You do not answer every question correctly. " + msg,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=None
            )

            answer = response["choices"][0]["text"]

            if message.guild == None:
                await message.author.send(answer)
            else:
                await message.channel.send(answer)

            log.write("bot : " + answer + "\n")

        except:
            await message.channel.send("You messed up. Try again.")
            log.write("bot : You messed up. Try again.\n")

        log.close()



intents = discord.Intents.default()

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(token)
