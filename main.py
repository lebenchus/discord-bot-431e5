import discord
import time


TOKEN = 'YOUR_TOKEN_HERE'

my_intents = discord.Intents.default()
my_intents.message_content = True

client = discord.Client(intents=my_intents)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    #* To get username without #0000
    username = str(message.author).split('#')[0]
    # * To get full username with #0000
    # username = str(message.author)

    user_content = str(message.content)

    # ! Message log (only use during debugging)
    print(f"{username}:{user_content}")

    # This makes it so that the bot don't just keep on replying to itself
    if message.author == client.user:
        return

    if user_content.lower() == "!hi" or user_content.lower() == "!hello":
        await message.reply(f"Hello {username}")
   

if __name__ == "__main__":
    client.run(TOKEN)