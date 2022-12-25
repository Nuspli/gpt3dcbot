import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('API_KEY')
token = os.getenv('BOT_TOKEN')

last_answer = ""
success = False

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        global last_answer
        global success

        if message.author.id == self.user.id:
            return

        def get_reply(msg):
            try:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="You are a funny chat bot. You are very unfriendly, extremely sarcastic and never sorry. "
                           "You also do not answer every question correctly. When you do not want to answer a question or say anything, make it clear."
                           "You also act and chat like a female. Your last answer was: \"" + last_answer + "\". Human response: " + msg,
                    temperature=0.9,
                    max_tokens=300,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=None
                )
                answer = response["choices"][0]["text"]
            except:
                answer = "Something went wrong. Try again."

            return answer

        log = open('log.txt', 'a')
        msg = str(message.content)
        try:
            log.write("user: " + msg + "\n")

            answer = get_reply(msg)

            log.write("bot :" + answer + "\n")

        except:
            print("failed to write to log.")

        if answer == "":
            answer += "​"

        if message.guild == None:
            await message.author.send(answer)
        else:
            await message.channel.send(answer)

        last_answer = answer.replace("\n", " ")

        log.close()



intents = discord.Intents.default()

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(token)
