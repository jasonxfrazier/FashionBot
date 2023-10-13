import discord
import dress

async def send_start(message, user_message) -> None:
    try:
        response = dress.handle_response(user_message,message.author.name)
        with open(f"./dresses/{response}", "rb") as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
            await message.channel.send("*How do YOU @everyone think Lomo would look in this dress? Type /vote and then a number. \nExample: /vote 10*")
    except Exception as e:
        print(e)

async def send_end(message, user_message) -> None:
    try:
        response = dress.handle_response(user_message, message.author.name)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot() -> None:
    TOKEN: str = " KEY "
    intents = discord.Intents.default()
    intents.message_content: bool = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready() -> None:
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name='/help'
            ))
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message) -> None:
        if message.author == client.user:
            return
        if message.author.name == "lomo210":
            return
        username: str = str(message.author)
        channel: str = str(message.channel)
        user_message: str = str(message.content)
        print(f"{username} said: '{user_message}' ({channel})")

        if user_message == '/vote_start':
            user_message: str = user_message[1:]
            await send_start(message, user_message)
        if "/vote " in user_message:
            user_message: str = user_message[1:]
            dress.handle_response(user_message, message.author.name)
        if user_message == '/vote_end':
            user_message: str = user_message[1:]
            await send_end(message, user_message)


    client.run(TOKEN)