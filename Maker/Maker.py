import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


API_ID = int("26022994")
API_HASH = "2e84a6b68bd6b5a79f46e8192668e0ea"
Bots = []
off =None
ch = "rb_ro"
DEVS = ["r_r_b0"]

@Client.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.username in DEVS:
     return await message.reply_text("الصانع معطل الان : ♻️")
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
   message.continue_propagation()

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
   if message.from_user.username in DEVS:
     kep = ReplyKeyboardMarkup([[": صنع بوت :", ": حذف بوت :"], [": البوتات المصنوعه :"], [": تعطيل المجاني :", ": تفعيل المجاني :"], [": السورس :"],[": تفعيل التواصل :", ": تعطيل التواصل :"]], resize_keyboard=True)
     return await message.reply_text("اهلا بك عزيزي في صانع فينوم.", reply_markup=kep)
   kep = ReplyKeyboardMarkup([[": صنع بوت :", ": حذف بوت :"], [": السورس :", ": طريقه التنصيب :"], [": مطور السورس :"]], resize_keyboard=True)
   await message.reply_text("اهلا بك عزيزي في صانع فينوم ،", reply_markup=kep)
    
   
@Client.on_message(filters.command([": السورس :"], ""))
async def alivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
                [
                    InlineKeyboardButton(
                        "ChNnEl SoUrCe ♡", url=f"https://t.me/RB_RO"),
                ],[
                    InlineKeyboardButton(
                        "مطور السورس ♡", url=f"https://t.me/R_R_B0"),
                ],
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/81c34077a3d4e95db110e.jpg",
        caption="",
        reply_markup=keyboard,
    )

@Client.on_message(filters.command(": طريقه التنصيب :", ""))
async def addbot(client: Client, message):
    await message.reply_text(f"""**- تابع اسفل لطريقه التنصيب .**
- -› [اضغط هنا لطريقه التنصيب. ](https://t.me/rb_ro)
قناة السورس -› [𝑠𝑜𝑢𝑟𝑐𝑒 venom](t.me/rb_ro)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ChNnEl SoUrCe ♡", url=f"https://t.me/rb_ro"),
                ],[
                    InlineKeyboardButton(
                        "مطور السورس ♡", url=f"https://t.me/R_R_B0"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
    
@Client.on_message(filters.command([": مطور السورس :"], ""))
async def aboutd5ev(client: Client, message):
    usr = await client.get_chat(R_R_B0)
    name = usr.first_name
    bio = (await client.get_chat(5345637082)).bio
    async for photo in client.iter_profile_photos(5345637082, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- اليك مطور سورس فينوم -› \n\n𝐧𝐚𝐦𝐞 -› {usr.first_name}\n• 𝐮𝐬𝐞𝐫 -› @{usr.username}\n• 𝐛𝐢𝐨 -› {usr.bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=5345637082)
                ],
            ]
        ),
    )
    

 
@Client.on_message(filters.command([": تفعيل التواصل :", ": تعطيل التواصل :"], "") & filters.private)
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in DEVS or message.from_user.id == dev:
        text = message.text
        if text == ": تفعيل التواصل :":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("تم تفعيل التواصل ✅")
            return
          except:
             pass
        if text == ": تعطيل التواصل :":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("تم تعطيل التواصل ✅")
            return
          except:
             pass


@Client.on_message(filters.private)
async def botoot(client: Client, message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in DEVS or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .☕ **")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(DEVS[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()   
 
@Client.on_message(filters.command([": تفعيل المجاني :", ": تعطيل المجاني :"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS:
    return
  global off
  if message.text == ": تفعيل المجاني :":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح : ⚡")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح : ⚡")
    
    
@Client.on_message(filters.command(": صنع بوت :", "") & filters.private)
async def maked(client, message):
  if not message.from_user.username in DEVS:
    for x in Bots:
        if x[1] == message.from_user.id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل : ♻️")
  try:
    ask = await client.ask(message.chat.id, "ارسل توكن البوت الان : ⚡", timeout=200)
  except:
      return
  TOKEN = ask.text
  try:
    ask = await client.ask(message.chat.id, "ارسل كود الجلسه الان : ⚡", timeout=200)
  except:
      return
  SESSION = ask.text
  try:
    ask = await client.ask(message.chat.id, "ارسل الان ايدي جروب السجل وتاكد من تشغيل مكالمه صوتيه + تاكد من رفع الحساب المساعد والبوت ادمن :🦸", timeout=200)
  except:
      return
  LOG = ask.text
  Dev = message.from_user.id
  if message.from_user.username in DEVS:
    try:
       ask = await client.ask(message.chat.id, "ارسل ايدي المطور : 🥇", timeout=200)
    except:
      return
    try:
      Dev = int(ask.text)
    except:
      return await message.reply_text("قم بارسال الايدي بشكل صحيح : ⚡")
  bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
  user = Client(api_id=API_ID, api_hash=API_HASH, session_name=str(SESSION))
  try:
    await bot.start()
    username = await bot.get_me()
    username = username.username
    await bot.stop()
    await user.start()
    await user.stop()
  except:
    return await message.reply_text("عذرا عزيزي تاكد من التوكن او جلسه البايروجرام : ♻️")
  id = username
  for x in Bots:
        if x[0] == id:
          return await message.reply_text("عذرا عزيزي لقد تم صنع البوت من قبل : 🥷")
  os.system(f"cp -a Make Maked/{id}")
  env = open(f"Maked/{id}/.env", "w+", encoding="utf-8")
  x = f'ID = {id}\nBOT_TOKEN = {TOKEN}\nSTRING_SESSION = {SESSION}\nOWNER_ID = {Dev}\nLOG_GROUP_ID = {LOG}'
  env.write(x)
  env.close()
  os.system(f"cd Maked/{id} && screen -d -m -S {id} python3 -m AnonX")
  oo = [id, Dev]
  Bots.append(oo)
  await message.reply_text("تم تنصيب بوتك بنجاح : ⚡")

@Client.on_message(filters.command(": حذف بوت :", "") & filters.private)
async def deletbot(client, message):
   if not message.from_user.username in DEVS:
     for x in Bots:
         bot = x[0]
         if x[1] == message.from_user.id:       
           os.system(f"sudo rm -fr Maked/{bot}")
           os.system(f"screen -XS {bot} quit")
           Bots.remove(x)
           return await message.reply_text("تم حذف بوتك من الصانع بنجاح : 🚥")
     return await message.reply_text("عذرا ليس لديك بوت قم بي الصنع الان : 🦸")
   try:
      bot = await client.ask(message.chat.id, "عزيزي ارسل يوزر البوت الان : 🗽", timeout=200)
   except:
      return
   bot = bot.text.replace("@", "")
   for x in Bots:
       if x[0] == bot:
          Bots.remove(x)
   os.system(f"sudo rm -fr Maked/{bot}")
   os.system(f"screen -XS {bot} quit")
   await message.reply_text("تم حذف البوت بنجاح : ♻️")


@Client.on_message(filters.command(": البوتات المصنوعه :", ""))
async def botat(client, message):
  if not message.from_user.username in DEVS:
   return
  o = 0
  text = "قايمه البوتات\n"
  for x in Bots:
      o += 1
      text += f"{o}- @{x[0]}\n"
  if o == 0:
    return await message.reply_text("عذرا عزيزيو ليس هناك بوتات : 🥷")
  await message.reply_text(text)
