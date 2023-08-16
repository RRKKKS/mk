from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "simo",
    api_id=8039541,
    api_hash="a33bbdb4aab8726bdc2c73442a0eaeb5",
    bot_token="5664558596:AAG5XqxYMNKLEwwr7DFRLIFp_-l28K8iu5M",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    R_R_B0 = "R_R_B0"
    await bot.send_message(R_R_B0, "** فشغيل الصانع عزيزي فينوم. **")
    print("[INFO]: فينوم قلبايي")
    await idle()
