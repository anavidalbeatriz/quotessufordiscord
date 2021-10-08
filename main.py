import discord
import random
from replit import db
from quotes import quotes
from web_server import keep_alive

client = discord.Client()

quotes_message = []

if "responding" not in db.keys():
  db["responding"] = True 

def update_quotes(quotes_message):
  if "quotes" in db.keys():
    quotes = db["quotes"]
    quotes.append(quotes_message)
    db["quotes"] = quotes
  else:
    db["quotes"] = [quotes_message]

def delete_quotes(index):
  quotes = db["quotes"]
  if len(quotes) > index:
    del quotes[index]
  db["quotes"] = quotes

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.content.startswith("#hello"):
    await message.channel.send("Hi, My name is Cookie Cat and I can give you quotes from Steven Universe! Type /cookiecomands to learn more")

  if message.content.startswith("#comands"):
    await message.channel.send("list add del on about quote")

  if message.content.startswith("#quote"):
    await message.channel.send(random.choice(quotes))

  if message.content.startswith("#add"):
    quotes_message = message.content.split("#add ",1)[1]
    update_quotes(quotes_message)
    await message.channel.send("New quote added =D")
  
  if message.content.startswith("#list"):
    if "new_quotes" in db.keys():
      new_quotes = db["new_quotes"]
      await message.channel.send(new_quotes)
  
  if message.content.startswith("#del"):
    quotes_message = []
    if "quotes_message" in db.keys():
      index = int(message.content.split("#del",1)[1])
      delete_quotes(index)
      quotes_message = db["quotes_message"]
      await message.channel.send(quotes_message)
    
  if message.content.startswith("#on"):
    value = message.content.split("#on ",1)[1]
      
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Quotes active")
    if value.lower() == "false":
      db["responding"] = False
      await message.channel.send("Quotes inactive")
  
  if message.content.startswith("#about"):
    await message.channel.send(
    "Oohhhhh Hes a frozen treat with an all new taste Cause he came to this planet from outer space A refugee of an interstellar war But now hes at your local grocery store Cookie Cat Hes a pet for your tummy Cookie Cat He's super duper yummy Cookie Cat He left his family behind Cookie Caaaaat Now available at Gurgens off Route 109")

keep_alive()

client.run('TOKEN')
