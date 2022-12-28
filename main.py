import discord
import openai
# these aren't necessary if you don't use .env
from dotenv import load_dotenv
import os

""" This bot was meant for personal use. Having multiple users talk to it might cause confusion, if you'd aim towards
    that, threading could be worth looking into. Have fun with this, if you have problems, contact Kolmus#4516 on DC."""

load_dotenv()

openai.api_key = os.getenv('API_KEY')
# go to https://beta.openai.com/account/api-keys to create one, if you don't have an openai account, sign up first.
# replace line 12 with openai.api_key = 'YOUR API KEY'
token = os.getenv('BOT_TOKEN')
# if you don't know how to make a discord bot, go watch a tutorial or...

# quickstart:   - go to https://discord.dev
#               - applications -> new application -> set it up
#               - bot -> add bot -> under Privileged Gateway Intents enable "Message content intent" (important)
#               - bot -> reset token: replace "token = os.getenv('BOT_TOKEN')" (line 15) with the token in ''
#               - oauth2 -> not sure if this is necessary, but use in-app and tick bot and applications.commands, admin
#               - -> url-generator -> just select bot and admin -> make a server first and use the link to invite it
#               - now you can use any of the text channels or DM the bot

last_answer0 = ""  # yes not pretty, I know, but it works. If you want to give the bot more memory, arrays are better
last_answer1 = ""
last_answer2 = ""
last_answer3 = ""
last_answer4 = ""
last_answer5 = ""
last_answer6 = ""
last_answer7 = ""
last_answer8 = ""
last_answer9 = ""

last_input0 = ""
last_input1 = ""
last_input2 = ""
last_input3 = ""
last_input4 = ""
last_input5 = ""
last_input6 = ""
last_input7 = ""
last_input8 = ""
last_input9 = ""


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        global last_answer9
        global last_answer8
        global last_answer7
        global last_answer6
        global last_answer5
        global last_answer4
        global last_answer3
        global last_answer2
        global last_answer1
        global last_answer0

        global last_input0
        global last_input1
        global last_input2
        global last_input3
        global last_input4
        global last_input5
        global last_input6
        global last_input7
        global last_input8
        global last_input9

        if message.author.id == self.user.id:  # don't reply to the bots messages
            return

        def get_reply(conversation):
            try:
                response = openai.Completion.create(
                    model="text-davinci-003",  # you can find other models or experiment with prompts at: https://beta.openai.com/playground
                    prompt="You are a discord chat bot. You are very rude, extremely sarcastic, funny and never feel sorry. "
                           "You also do not answer every question correctly. When you do not want to answer a question or say anything, you make it clear."
                           "You do NOT try to be too helpful. Your responses consist of just the text, not in quotes."
                           "Your previous conversation went like this: \"" + conversation + "\". Your response: ",
                    temperature=0.9,
                    max_tokens=1024,       # 1000 tokens = roughly 750 words = 0.02$ for the davinci model
                    top_p=1,               # you get 18$ free credits lasting 3 months from signing up
                    frequency_penalty=0,   # keep in mind that the prompt also counts for the tokens used, so giving it
                    presence_penalty=0.6,  # more or less memories of the past makes a huge difference
                    stop=None
                )
                answer = response["choices"][0]["text"]
                # idk how many choices there are, but you could mess with the index
            except:
                answer = "Something went wrong. Try again."  # eg. request times out

            return answer

        log = open('log.txt', 'a')  # not needed, keeeps track of the whole conversation
        msg = str(message.content) + " "

        conversation = ""
        # "building" the memory
        conversation += last_input0 + last_answer0
        conversation += last_input1 + last_answer1
        conversation += last_input2 + last_answer2
        conversation += last_input3 + last_answer3
        conversation += last_input4 + last_answer4
        conversation += last_input5 + last_answer5
        conversation += last_input6 + last_answer6
        conversation += last_input7 + last_answer7
        conversation += last_input8 + last_answer8
        conversation += last_input9 + last_answer9

        msg = "user: " + msg + " "
        conversation += msg

        try:
            log.write(msg + "\n")

            answer = get_reply(conversation)

            log.write("bot : " + answer + "\n")

        except:
            print("failed to write to log.")  # this can happen when the user uses emojis or special characters

        if answer == "":
            # when the bot doesn't want to answer, the response can be empty, but you can't send empty messages in DC
            answer += "​"

        if message.guild == None:  # this is the case for DMs
            await message.author.send(answer)
        else:
            await message.channel.send(answer)

        answer = "bot: " + answer + " "
        # updating memory
        last_input0 = last_input1
        last_input1 = last_input2
        last_input2 = last_input3
        last_input3 = last_input4
        last_input4 = last_input5
        last_input5 = last_input6
        last_input6 = last_input7
        last_input7 = last_input8
        last_input8 = msg

        last_answer0 = last_answer1
        last_answer1 = last_answer2
        last_answer2 = last_answer3
        last_answer3 = last_answer4
        last_answer4 = last_answer5
        last_answer5 = last_answer6
        last_answer6 = last_answer7
        last_answer7 = last_answer8
        last_answer8 = answer

        log.close()


intents = discord.Intents.default()

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(token)
    
