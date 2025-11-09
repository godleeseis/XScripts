import discord
from discord.ext import commands
from discord import app_commands

# Replace with your bot token
TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# When the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Slash command to send the embed
@bot.tree.command(name="script", description="Show a Roblox script info with button")
async def script(interaction: discord.Interaction):
    embed = discord.Embed(
        title="X Blaze",
        description="**Script Name:** X Blaze\n**Game:** mall-drifters\n**Verified:** ✅ Yes\n**Key:** Yes/No",
        color=discord.Color.blue()
    )
    embed.add_field(name="Script:", value="Click the button below to get it 👇", inline=False)
    embed.set_footer(text="Requested by {}".format(interaction.user.name))

    # The button
    class GiveScript(discord.ui.View):
        @discord.ui.button(label="📜 Give Script", style=discord.ButtonStyle.green)
        async def give_script(self, interaction: discord.Interaction, button: discord.ui.Button):
            script_code = (
                'loadstring(game:HttpGet("https://raw.githubusercontent.com/emwmelchi/eee/refs/heads/main/lmaoo"))()'
            )
            await interaction.response.send_message(
                f"```lua\n{script_code}\n```", ephemeral=True  # Only visible to the user
            )

    await interaction.response.send_message(embed=embed, view=GiveScript())

bot.run(TOKEN)