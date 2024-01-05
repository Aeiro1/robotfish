import interactions
from discord.ext.commands import has_permissions
import discord
from interactions import listen

bot_key_file = open("token.txt")
bot_key = bot_key_file.read()

bot = interactions.Client(intents=interactions.Intents.DEFAULT | interactions.Intents.MESSAGE_CONTENT, token=bot_key)


@interactions.slash_command(
    name="exit_command",
    description="quits the bot",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
)
async def exit_command_run(ctx: interactions.SlashContext):
    await ctx.send(ctx.author.mention + " quit the bot, Goodbye!")
    await bot.stop()
    #exit()
    

@interactions.slash_command(
    name="hello",
    description="Sends a hello mesasge"
)
async def hello_command(ctx: interactions.SlashContext):
    await ctx.send("Hello!")

@interactions.slash_command(
    name="vx",
    description="fixes twitter embed",
    scopes=[1133920869773746359, 779520655930163281],
)
@interactions.slash_option(
    name="link",
    description="twitter.com or x.com link",
    opt_type=interactions.OptionType.STRING,
    required=True,
)
async def vx_embed(ctx: interactions.SlashContext, link: str):
    if "twitter" in link:
        link = link.replace("twitter", "vxtwitter")
    elif "x" in link:
        link = link.replace("x", "fixvx")
    else:
        link = "invalid link submitted"
    await ctx.send(link)


# @listen(interactions.api.events.MessageCreate)
# async def fixembed(message):
#     if message.content.startswith("https://x"):
#         msg = message.content.replace("x", "fixvx")
#         msg = await message.channel.send(msg)
#     elif message.content.startswith("https://twitter"):
#         msg = message.content.replace("twitter", "vxtwitter")
#         msg = await message.channel.send(msg)

@listen("on_message_create")
async def fix_embed(event):
    fixed = event.message.content
    if "//twitter.com/" in fixed:
        fixed = fixed.replace("twitter", "vxtwitter")
        await event.message.reply(fixed, allowed_mentions=interactions.AllowedMentions(replied_user=False))
    elif "//x.com/" in fixed:
        fixed = fixed.replace("x", "fixvx")
        await event.message.reply(fixed, allowed_mentions=interactions.AllowedMentions(replied_user=False))

@interactions.slash_command(
    name="returnstring",
    description="returns the inputted string",
    scopes=[1133920869773746359],
)
@interactions.slash_option(
    name="text",
    description="String to respond with",
    opt_type=interactions.OptionType.STRING,
    required=True,
)
async def return_command(ctx: interactions.SlashContext, text: str):
    await ctx.send(f"You sent the string '{text}'!")


bot.start()
# while True:
#     try:
#         bot.start()
#     except Exception as e:
#         print(e)
