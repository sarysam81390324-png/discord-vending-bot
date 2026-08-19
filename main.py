import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="vending", description="自販機を表示します")
async def vending(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🛒 **Discord自動販売機**\n\n"
        "🥤 商品A：500円\n"
        "🎮 商品B：1,000円\n\n"
        "購入機能は準備中です！"
    )

bot.run(os.environ["DISCORD_TOKEN"])
