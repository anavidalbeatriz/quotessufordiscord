import discord
import random
from replit import db
from quotes import quotes
from web_server import keep_alive

client = discord.Client()

su = ["steven universe"]

new_quotes = []

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
  if message.content.startswith("/cookiehello"):
    await message.channel.send("Hi, My name is Cookie Cat and I can give you quotes from Steven Universe! Type /cookiecomands to learn more")

  if message.content.startswith("/cookiecomands"):
    await message.channel.send("/cookielist - see quotes added by users; /cookieadd - add new quotes; /cookiedel to delete quotes added; /cookieresponding true/false to turn on/off the quotes; /cookieabout to learn more")

  if any(word in message.content for word in su):
    await message.channel.send(random.choice(quotes))

  if message.content.startswith("/cookieadd"):
    quotes_message = message.content.split("/cookieadd ",1)[1]
    update_quotes(quotes_message)
    await message.channel.send("New quote added =D")
  
  if message.content.startswith("/cookielist"):
    if "new_quotes" in db.keys():
      new_quotes = db["new_quotes"]
      await message.channel.send(new_quotes)
  
  if message.content.startswith("/cookiedel"):
    quotes_message = []
    if "quotes_message" in db.keys():
      index = int(message.content.split("/cookiedel",1)[1])
      delete_quotes(index)
      quotes_message = db["quotes_message"]
      await message.channel.send(quotes_message)
    
  if message.content.startswith("/responding"):
    value = message.content.split("/responding ",1)[1]
      
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Quotes active")
    if value.lower() == "false":
      db["responding"] = False
      await message.channel.send("Quotes inactive")
  
  if message.content.startswith("/cookieabout"):
    await message.channel.send(
    "Oohhhhh Hes a frozen treat with an all new taste Cause he came to this planet from outer space A refugee of an interstellar war But now hes at your local grocery store Cookie Cat Hes a pet for your tummy Cookie Cat He's super duper yummy Cookie Cat He left his family behind Cookie Caaaaat Now available at Gurgens off Route 109")

keep_alive()

client.run('token')
