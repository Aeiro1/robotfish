import interactions
from interactions import listen
import os
import random

BOT_TOKEN = os.getenv('TOKEN')

bot = interactions.Client(intents=interactions.Intents.DEFAULT | interactions.Intents.MESSAGE_CONTENT, token=BOT_TOKEN, delete_unused_application_cmds=True)
print ("BOT Online")

@interactions.slash_command(
    name="exit_command",
    description="quits the bot",
    default_member_permissions=interactions.Permissions.ADMINISTRATOR,
)
@interactions.check(interactions.is_owner())
async def exit_command_run(ctx: interactions.SlashContext):
    await ctx.send(ctx.author.mention + " quit the bot, Goodbye!" + (" (" + ctx.bot.owner.mention + " bot is down)"))
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
    await ctx.send(link, silent=True)

# BREAK HERE IF DISCORD TWITTER EMBEDS STOP WORKING
# --------------------------------------------------
# @listen("on_message_create")
# async def fix_embed(event):
#     fixed = event.message.content
#     if "//twitter.com/" in fixed:
#         fixed = fixed.replace("twitter", "vxtwitter")
#         await event.message.reply(fixed, allowed_mentions=interactions.AllowedMentions(replied_user=False), silent=True)
#     elif "//x.com/" in fixed:
#         fixed = fixed.replace("x", "fixvx")
#         await event.message.reply(fixed, allowed_mentions=interactions.AllowedMentions(replied_user=False), silent=True)
#     elif "//www.tiktok.com/" in fixed:
#         fixed = fixed.replace("tiktok", "tiktxk")
#         await event.message.reply(fixed, allowed_mentions=interactions.AllowedMentions(replied_user=False), silent=True)

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


@interactions.slash_command(
    name="number",
    description="Picks random number between values"
)
@interactions.slash_option(
    name="high_num",
    description="Upper bound for generator",
    required=True,
    opt_type=interactions.OptionType.INTEGER,
)
@interactions.slash_option(
    name="low_num",
    description="Lower bound for generator, 0 by default",
    opt_type=interactions.OptionType.INTEGER,
)
async def num_gen(ctx: interactions.SlashContext, high_num: int, low_num: int = 0):
    await ctx.send(random.randint(low_num, high_num), silent=True)

@interactions.slash_command(
    name="coinflip",
    description="Flips a coin",
)
async def coin_flip(ctx: interactions.SlashContext):
    coin = random.choice(["Heads", "Tails"])
    await ctx.send(coin, silent=True)


bot.start()
# while True:
#     try:
#         bot.start()
#     except Exception as e:
#         print(e)
