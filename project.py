import discord
from discord.ext import commands

import number_guessing
import nAnB_game

import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'機器人上線啦：{bot.user}')
    

@bot.command()
async def hello(ctx):
    print("got a new hello message!")
    await ctx.send('你好！這是我在 VS Code 寫的機器人 😄 \n' 
    '打 `!startgame1`開始猜數字遊戲。 \n'
    '打 `!startgame2`開始猜密碼遊戲(1A2B)。')

@bot.command()
async def startgame1(ctx):
    number_guessing.start_new_game(ctx.author.id)
    await ctx.send("🎯 1~100的數字已生成。用 `!guess1 <number>`猜測數字!")

@bot.command()
async def guess1(ctx, number: int):
    result = number_guessing.check_guess(ctx.author.id, number)

    if result == "no_game":
        await ctx.send("無遊戲存在。用 `!startgame1` 開啟新猜數字遊戲。")
    elif result == "low":
        await ctx.send("🔼 太低!")
    elif result == "high":
        await ctx.send("🔽 太高!")
    elif result == "correct":
        await ctx.send("🎉 正確答案!")

@bot.command()
async def startgame2(ctx):
    nAnB_game.start_new_game(ctx.author.id)
    await ctx.send("🎯 四位由0~9的組成的數字已生成。用 `!guess2 <number>`猜測密碼!")

@bot.command()
async def guess2(ctx, number: int):
    is_correct, result = nAnB_game.check_guess(ctx.author.id, number)

    if result == "no game":
        await ctx.send("無遊戲存在。用 `startgame2`開啟猜密碼新遊戲。")
    elif result == "wrong response":
        await ctx.send("請輸入四位數字。")
    elif is_correct == True:
        await ctx.send(f"答案正確! {result}")
    elif is_correct == False:
        await ctx.send(f"答案錯誤. 提示: {result}")

# Load environment variables from a .env file
load_dotenv()

bot.run(os.getenv('DISCORD_BOT_TOKEN'))