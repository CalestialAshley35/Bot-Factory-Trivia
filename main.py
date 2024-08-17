import discord
from discord.ext import commands
import random

intents = discord.Intents.default() 
intents.message_content = True # Enable this for message content intents

bot = commands.Bot(command_prefix='!', intents=intents)

# Sample trivia questions
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
}

# Store player scores
scores = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def trivia(ctx):
    question = random.choice(list(trivia_questions.keys()))
    await ctx.send(question)
    # Store the correct answer in a custom attribute
    bot.correct_answer = trivia_questions[question]

@bot.command()
async def answer(ctx, *, user_answer):
    if user_answer.lower() == bot.correct_answer.lower():
        user = ctx.author
        if user in scores:
            scores[user] += 1
        else:
            scores[user] = 1
        await ctx.send(f"Correct! {user.mention}, you have {scores[user]} point(s).")
    else:
        await ctx.send("Incorrect answer. Try again!")

@bot.command()
async def score(ctx):
    user = ctx.author
    if user in scores:
        await ctx.send(f"{user.mention}, you have {scores[user]} point(s).")
    else:
        await ctx.send(f"{user.mention}, you have no points yet.")

bot.run('tokem')
