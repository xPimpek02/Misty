from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc
from os import system as sys

app = Quart(__name__)
ipc_client = ipc.Client(secret_key = "Swas")

app.config["SECRET_KEY"] = "pimpek"
app.config["DISCORD_CLIENT_ID"] = 883779489434308659  # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = "BUw5E_KOIkQ_a3AuP_M571n-1LggsyqX"   # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
	return await render_template("index.html")

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/callback")
async def callback():
	#try:
		#await discord.callback()
	#except:
		#return redirect(url_for("login"))
	guild_count = await ipc_client.request("get_guild_count")
	return await render_template("dashboard.html", Servers=guild_count)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)