import openai
import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('BOT-MAIN')

bot = commands.Bot(
  command_prefix=None,
  intents=discord.Intents.default(),
  activity=discord.Activity(type=discord.ActivityType.playing, name="with humans"),
  sync_commands=False,
  delete_not_existing_commands=False
)

if __name__ == '__main__':
  log.info("starting...")
  token = os.getenv('BOT_TOKEN')
  bot.run(token)

openai.api_key = "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"

def get_response(question):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=None
  )

  return response["choices"][0]["text"]


def question():

  question = input("Q: ")

  return question


#answer = "A: " + str(get_response(question()))

#print(answer)
