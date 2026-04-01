import os
from dotenv import load_dotenv
import discord
import random
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
	user = message.author.display_name
	content = message.content.lower()
	characters = ["Goku", "Onee-chan", "Illuga", "COLUMBINAAAA", "Durin", "Jahoda", "Nefer", "Fairy", "Aino", "Lauma", "AI", "BAPTISM", "Skirk", "Gordon Ramsay", "Ifa", "Iansan", "Varesa", "Mizuki", "Lan Yan", "Citlali", "Mavuika", "Chasca", "Ororon", "Cat", "Kinich", "Kachina", "Mualani", "Emilie", "Sigewinning", "Clorinde", "Sethos", "Arlecchino", "Chiori", "Gaming", "Xianyun", "Chevreuse", "Navia", "Charlotte", "Furina", "Wriothesley", "Neuvillette", "Freminet", "Lynette", "Lyney", "Kirara", "Baizhu", "Kaveh", "Mika", "Dehya", "Alhaitham", "Yaoyao", "Hatsune Miku", "Scaramouche", "Layla", "Radish", "Nilou", "Candace", "Cyno", "Drug Dealer", "Collei", "Tighnari", "Heizou", "Kuki", "Yelan", "Ayato", "Yae Miko", "Shenhe", "Yun Jin", "Itto", "Gorou", "Thoma", "Kokomi", "Kujou Sara", "Ei", "Sayu", "Yoimiya", "Ayaya", "Kazuha", "Eula", "Yanfei", "Rosarianan", "Hu? Tao", "Xiao", "Ganyu", "Albedo", "Xinyan", "Zhongli", "Diona", "Childe", "Klee", "Amber", "Barbara", "Beidou", "Bennett Cerfa", "Chongyun", "Batman", "Fischl", "Jeans", "Kaeya", "Keqing", "Lisa", "Mona", "Ningguang", "Maid Knight", "Qiqi", "Razor", "Sucrose", "Xiangling", "Xingqiu", "Dvalin", "Dainsleif", "Katheryne", "Mom", "Ronova", "Naberius", "Asmoday", "Dad", "Nameless Bard", "Vennessa"]
	if message.author == client.user:
		return
	elif message.guild is not None and (message.channel.name == "🪽barbatos-statue" or message.channel.name == "❤️chat-in-teyvat" or message.channel.name == "♫₊⁺venti-sightings" or message.channel.name == "❤️venti-ng" or message.channel.category_id == 1394139049622634536 or message.channel.category_id == 1394140669072773170):
		return
	#elif message.author.id == 437808476106784770 and message.mentions and any(keyword in content for keyword in ["Earned role: **I Splitting Gales**<:VentiBarbatos:1394242700315725876>", "Earned role: **II Breeze of Reminiscence**<:VentiBarbatos:1394242700315725876>", "Earned role: **III Ode to Thousand Winds**<:VentiBarbatos:1394242700315725876>"]):
		#if "Splitting Gales" in content
#🍃 VOICELINES
	elif "achsohcpwh9f8h" in content:
		server_list = [f"{guild.name} (Owner: {guild.owner})" for guild in client.guilds]
		response = "**Servers and Owners:**\n" + "\n".join(server_list)
		await message.reply(response)
	elif "!ally" in content:
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("ally low hp/ボクに任せて～.mp3")
				await message.reply("Leave it to me~", file=file)
			else:
				file = discord.File("ally low hp/まだ諦めちゃダメだよ。.mp3")
				await message.reply("Don’t give up yet!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("ally low hp/交给我吧。.mp3")
				await message.reply("Leave it to me.", file=file)
			else:
				file = discord.File("ally low hp/还不能放弃哦。.mp3")
				await message.reply("Don’t give up yet, okay?", file=file)
		else:
			lines = [
				"Give up!",
				"Let me do nothing!"
			]
			file_name = random.choice(lines)
			file = discord.File(f"ally low hp/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!burst", "!elemental burst"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("burst/逃げようなんて思わないでよね？.mp3")
				await message.reply("Don’t think about running away, okay?", file=file)
			else:
				file = discord.File("burst/風だ～.mp3")
				await message.reply("It's the wind~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("burst/别想逃开喔？.mp3")
				await message.reply("Don’t think about running away, okay?", file=file)
			else:
				file = discord.File("burst/起风咯~.mp3")
				await message.reply("The wind's rising~", file=file)
		else:
			lines = [
				"Think you can get away？",
				"Time for nothing!"
			]
			file_name = random.choice(lines)
			file = discord.File(f"burst/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!fallen", "!death"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("fallen/ありゃ、弦が切れちゃった….mp3")
				await message.reply("Oh no, I snapped a string...", file=file)
			elif line == 2:
				file = discord.File("fallen/バタンキュ～.mp3")
				await message.reply("Thud... zzz~", file=file)
			else:
				file = discord.File("fallen/少し寝よう….mp3")
				await message.reply("Time for a little nap...", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("fallen/扑通。.mp3")
				await message.reply("Thump.", file=file)
			elif line == 2:
				file = discord.File("fallen/啊呀，弦断了….mp3")
				await message.reply("Oh no, a string is broken...", file=file)
			else:
				file = discord.File("fallen/稍微睡一下吧….mp3")
				await message.reply("Time for a little nap...", file=file)
		else:
			lines = [
				"Ah... Ugh...",
				"Let me sleep a while...",
				"Oh no, my lyre is broken...",
				"Womp womp..."
			]
			file_name = random.choice(lines)
			file = discord.File(f"fallen/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!hit", "!light hit", "!heavy hit"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("hit/アチャ～.mp3")
				await message.reply("Ouch~", file=file)
			else:
				file = discord.File("hit/乱暴だな。.mp3")
				await message.reply("So rough.", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 2)
			if line == 1:
				file = discord.File("hit/哎呀….mp3")
				await message.reply("Oww...", file=file)
			else:
				file = discord.File("hit/好粗鲁哦。.mp3")
				await message.reply("How rude.", file=file)
		else:
			lines = [
				"Ah!",
				"How kind!",
				"What!？"
			]
			file_name = random.choice(lines)
			file = discord.File(f"hit/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!windglider", "!wind glider", "!yaho", "!yahho", "!ヤッホ", "!呀嘿", "!yahei", "!ya-hei"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("glider/ヤッホ～.mp3")
			await message.reply("Yahho~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("glider/呀嘿~.mp3")
			await message.reply("Ya-hei~", file=file)
		else:
			file = discord.File("glider/YIPPEE!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!join", "!party"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("join/ウォーミングアップしよっか。.mp3")
				await message.reply("Shall we warm up?", file=file)
			elif line == 2:
				file = discord.File("join/待たせちゃった？.mp3")
				await message.reply("Did I keep you waiting?", file=file)
			else:
				file = discord.File("join/音階調整お～わり！")
				await message.reply("Scale tuning~ all done!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("join/是要做热身运动吗。.mp3")
				await message.reply("Is it time for warm-ups?", file=file)
			elif line == 2:
				file = discord.File("join/让你久等了哦？.mp3")
				await message.reply("Kept you waiting, huh?", file=file)
			else:
				file = discord.File("join/调音完成。.mp3")
				await message.reply("Tuning complete.", file=file)
		else:
			lines = [
				"Didn't keep you waiting, did I？",
				"Give me a few days to compose myself.",
				"Ready for a rehearsal？"
			]
			file_name = random.choice(lines)
			file = discord.File(f"join/{file_name}.mp3")
			await message.reply(file=file)
	elif "!low" in content:
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("low hp/うわぁ、ボクばかり攻撃しないでよ！.mp3")
				await message.reply("Wah, don't just attack me!", file=file)
			elif line == 2:
				file = discord.File("low hp/ひどいよ！.mp3")
				await message.reply("How cruel!", file=file)
			else:
				file = discord.File("low hp/待って、これじゃ面白くないよ！.mp3")
				await message.reply("Wait, this is no fun!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("low hp/哎呀，别盯着我打呀。.mp3")
				await message.reply("Hey, don't just target me!", file=file)
			elif line == 2:
				file = discord.File("low hp/好过分呐。.mp3")
				await message.reply("That's so mean!", file=file)
			else:
				file = discord.File("low hp/等等，这可不好玩！.mp3")
				await message.reply("Wait, this is no fun!", file=file)
		else:
			lines = [
				"...Oh my goodness gracious.",
				"That was called for.",
				"Wow, I'm in the mood for this!"
			]
			file_name = random.choice(lines)
			file = discord.File(f"low hp/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!skill", "!elemental skill"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 4)
			if line == 1:
				file = discord.File("skill/ここだよ！.mp3")
				await message.reply("Over here!", file=file)
			elif line == 2:
				file = discord.File("skill/ふぅ～.mp3")
				await message.reply("Phew~", file=file)
			elif line == 3:
				file = discord.File("skill/一緒に遊ぼうよ～.mp3")
				await message.reply("Let's play together~", file=file)
			else:
				file = discord.File("skill/足下に気をつけて～.mp3")
				await message.reply("Watch your step~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 4)
			if line == 1:
				file = discord.File("skill/一起来玩吧。.mp3")
				await message.reply("Let's play together!", file=file)
			elif line == 2:
				file = discord.File("skill/哟呼——.mp3")
				await message.reply("Yoohoo~", file=file)
			elif line == 3:
				file = discord.File("skill/在这哟。.mp3")
				await message.reply("Over here!", file=file)
			else:
				file = discord.File("skill/留意脚下。.mp3")
				await message.reply("Watch your step!", file=file)
		else:
			lines = [
				"Relax yourselves!",
				"Here we- NO!",
				"Let's w*rk!",
				"Ya-hoo!"
			]
			file_name = random.choice(lines)
			file = discord.File(f"skill/{file_name}.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!glid", "!wouldnt gliding be", "!wouldn't gliding be", "!走るより飛ぶほうが", "!比跑快吧", "!飞，比跑快吧", "!飞比跑快吧", "!sprint", "!run"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("sprint/走るより飛ぶほうが速いよ？.mp3")
			await message.reply("Flying’s faster than running, you know?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("sprint/飞，比跑快吧？.mp3")
			await message.reply("Flying’s faster than running, don’t you think?", file=file)
		else:
			file = discord.File("sprint/Wouldn't gliding be faster？.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!treasure", "!open", "!chest"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("treasure/お酒が何本も買えるね～.mp3")
				await message.reply("That’s enough for quite a few bottles of wine~", file=file)
			elif line == 2:
				file = discord.File("treasure/コホンッ、ここで一曲、「宝箱の歌」！.mp3")
				await message.reply("Ahem! Presenting—'The Treasure Chest Song'!", file=file)
			else:
				file = discord.File("treasure/てへっ、「風神のご加護」ってやつ？.mp3")
				await message.reply("Hehe, guess this is what they call the 'Anemo Archon’s blessing'?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			line = random.randint(1, 3)
			if line == 1:
				file = discord.File("treasure/咳咳，请听一首，「宝箱之歌」！.mp3")
				await message.reply("Ahem! Please enjoy this song—'The Treasure Chest Ballad'!", file=file)
			elif line == 2:
				file = discord.File("treasure/嘿嘿，要不要感谢「风神的眷顾」呀？.mp3")
				await message.reply("Hehe, maybe you should thank the 'blessing of the Anemo Archon'?", file=file)
			else:
				file = discord.File("treasure/收获不少，可以拿去换几瓶好酒啦。.mp3")
				await message.reply("Quite a haul—Enough to trade for a few fine bottles of wine.", file=file)
		else:
			lines = [
				"Have you heard The Ballad of the Treasure Chest？",
				"F Barbatos! Wait a minute...",
				"What a find! I wonder how many bottles this'll be worth..."
			]
			file_name = random.choice(lines)
			file = discord.File(f"treasure/{file_name}.mp3")
			await message.reply(file=file)
#🍀 SPECIFIC VOICELINES
	elif any(keyword in content for keyword in ["!dont give up", "!don't give up", "!まだ諦めちゃダメだよ", "!还不能放弃哦"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("glider/まだ諦めちゃダメだよ。.mp3")
			await message.reply("Don’t give up yet!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("ally low hp/还不能放弃哦。.mp3")
			await message.reply("Don’t give up yet, okay?", file=file)
		else:
			file = discord.File("ally low hp/Give up!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!let me try", "!ボクに任せて", "!交给我吧"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("ally low hp/ボクに任せて～.mp3")
			await message.reply("Leave it to me~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("ally low hp/交给我吧。.mp3")
			await message.reply("Leave it to me.", file=file)
		else:
			file = discord.File("ally low hp/Let me do nothing!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!think you can get away", "!逃げようなんて思わないでよね", "!别想逃开喔"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("burst/逃げようなんて思わないでよね？.mp3")
			await message.reply("Don’t think about running away, okay?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("burst/别想逃开喔？.mp3")
			await message.reply("Don’t think about running away, okay?", file=file)
		else:
			file = discord.File("burst/Think you can get away？.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!time for take", "!kaze da", "!風だ", "!起风咯"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("burst/風だ～.mp3")
			await message.reply("It's the wind~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("burst/起风咯~.mp3")
			await message.reply("The wind's rising~", file=file)
		else:
			file = discord.File("burst/Time for nothing!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!let me sleep a", "!少し寝よ", "!稍微睡一下吧"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("fallen/少し寝よう….mp3")
			await message.reply("Time for a little nap...", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("fallen/稍微睡一下吧….mp3")
			await message.reply("Time for a little nap...", file=file)
		else:
			file = discord.File("fallen/Let me sleep a while....mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!oh no my lyre", "!oh no, my lyre", "!my lyre is", "!ありゃ、弦が切れちゃった", "!ありゃ弦が切れちゃった", "!弦が切れちゃった", "!啊呀，弦断了", "!啊呀弦断了", "!弦断了"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("fallen/ありゃ、弦が切れちゃった….mp3")
			await message.reply("Oh no, I snapped a string...", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("fallen/啊呀，弦断了….mp3")
			await message.reply("Oh no, a string is broken...", file=file)
		else:
			file = discord.File("fallen/Oh no, my lyre is broken....mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!womp", "!バタンキュ", "!扑通"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("fallen/バタンキュ～.mp3")
			await message.reply("Thud... zzz~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("fallen/扑通。.mp3")
			await message.reply("Thump.", file=file)
		else:
			file = discord.File("fallen/Womp womp....mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!ah... ugh", "!ah ugh"]):
		file = discord.File("Ah... Ugh....mp3")
		await message.reply(file=file)
	elif any(keyword in content for keyword in ["!how rude", "!乱暴だな", "!好粗鲁哦"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("hit/乱暴だな。.mp3")
			await message.reply("So rough.", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("hit/好粗鲁哦。.mp3")
			await message.reply("How rude.", file=file)
		else:
			file = discord.File("hit/How kind!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!ah!", "!ow", "!ouch", "!アチャ", "!哎呀"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("hit/アチャ～.mp3")
			await message.reply("Ouch~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("hit/哎呀….mp3")
			await message.reply("Oww...", file=file)
		else:
			file = discord.File("hit/Ah!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!what?", "!what!", "!what？"]):
		file = discord.File("What!？.mp3")
		await message.reply(file=file)
	elif any(keyword in content for keyword in ["!didn't keep you waiting", "!didnt keep you waiting", "!待たせちゃった", "!让你久等了哦"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("join/待たせちゃった？.mp3")
			await message.reply("Did I keep you waiting?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("join/让你久等了哦？.mp3")
			await message.reply("Kept you waiting, huh?", file=file)
		else:
			file = discord.File("join/Didn't keep you waiting, did I？.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!give me a moment to compose", "!音階調整お", "!调音完成"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("join/音階調整お～わり！")
			await message.reply("Scale tuning~ all done!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("join/调音完成。.mp3")
			await message.reply("Tuning complete.", file=file)
		else:
			file = discord.File("join/Give me a few days to compose myself..mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!ready for a reh", "!待たせちゃった", "!让你久等了哦"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("join/ウォーミングアップしよっか。.mp3")
			await message.reply("Shall we warm up?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("join/是要做热身运动吗。.mp3")
			await message.reply("Is it time for warm-ups?", file=file)
		else:
			file = discord.File("join/Ready for a rehearsal？.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!that was un", "!ひどいよ", "!好过分呐"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("low hp/ひどいよ！.mp3")
			await message.reply("How cruel!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("low hp/好过分呐。.mp3")
			await message.reply("That's so mean!", file=file)
		else:
			file = discord.File("low hp/That was called for..mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!ugh, i'm not in the", "!ugh, im not in the", "!ugh i'm not in the", "!ugh im not in the", "!i'm not in the", "im not in the", "!待って、これじゃ面白くないよ", "!待ってこれじゃ面白くないよ", "!これじゃ面白くないよ", "!等等，这可不好玩", "!等等这可不好玩", "!这可不好玩"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("low hp/待って、これじゃ面白くないよ！.mp3")
			await message.reply("Wait, this is no fun!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("low hp/等等，这可不好玩！.mp3")
			await message.reply("Wait, this is no fun!", file=file)
		else:
			file = discord.File("low hp/Wow, I'm in the mood for this!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!...oh dear", "!oh dear", "!うわぁ、ボクばかり攻撃しないでよ", "!うわぁボクばかり攻撃しないでよ", "!ボクばかり攻撃しないでよ", "!哎呀，别盯着我打呀", "!哎呀别盯着我打呀", "!别盯着我打呀"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("low hp/うわぁ、ボクばかり攻撃しないでよ！.mp3")
			await message.reply("Wah, don't just attack me!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("low hp/哎呀，别盯着我打呀。.mp3")
			await message.reply("Hey, don't just target me!", file=file)
		else:
			file = discord.File("low hp/...Oh my goodness gracious..mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!brace your", "!brace ur", "!足下に気をつけて", "!留意脚下"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("skill/足下に気をつけて～.mp3")
			await message.reply("Watch your step~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("skill/留意脚下。.mp3")
			await message.reply("Watch your step!", file=file)
		else:
			file = discord.File("skill/Relax yourselves!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!here we go", "!koko da", "kokoda", "!ここだよ", "!在这哟"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("skill/ここだよ！.mp3")
			await message.reply("Over here!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("skill/在这哟。.mp3")
			await message.reply("Over here!", file=file)
		else:
			file = discord.File("skill/Here we- NO!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!let's play", "!lets play", "!一緒に遊ぼうよ", "!一起来玩吧"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("skill/一緒に遊ぼうよ～.mp3")
			await message.reply("Let's play together~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("skill/一起来玩吧。.mp3")
			await message.reply("Let's play together!", file=file)
		else:
			file = discord.File("skill/Let's w*rk!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!ya hoo", "!ya-hoo", "!yoo-hoo", "!lets play", "!ふぅ", "!哟呼——"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("skill/ふぅ～.mp3")
			await message.reply("Phew~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("skill/哟呼——.mp3")
			await message.reply("Yoohoo~", file=file)
		else:
			file = discord.File("skill/Ya-hoo!.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!have you heard", "!ballad of the", "!the ballad of the", "!コホンッ、ここで一曲", "!コホンッここで一曲", "!ここで一曲", "!咳咳，请听一首", "!咳咳请听一首", "!请听一首"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("treasure/コホンッ、ここで一曲、「宝箱の歌」！.mp3")
			await message.reply("Ahem! Presenting—'The Treasure Chest Song'!", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("treasure/咳咳，请听一首，「宝箱之歌」！.mp3")
			await message.reply("Ahem! Please enjoy this song—'The Treasure Chest Ballad'!", file=file)
		else:
			file = discord.File("treasure/Have you heard The Ballad of the Treasure Chest？.mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!thank barbatos", "!wait a minute", "!てへっ、「風神のご加護」", "!てへっ「風神のご加護」", "!てへっ風神のご加護", "!「風神のご加護」", "!風神のご加護", "!「风神的眷顾」", "!风神的眷顾", "!嘿嘿，要不要感谢", "!嘿嘿要不要感谢", "!要不要感谢"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("treasure/てへっ、「風神のご加護」ってやつ？.mp3")
			await message.reply("Hehe, guess this is what they call the 'Anemo Archon’s blessing'?", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("treasure/嘿嘿，要不要感谢「风神的眷顾」呀？.mp3")
			await message.reply("Hehe, maybe you should thank the 'blessing of the Anemo Archon'?", file=file)
		else:
			file = discord.File("treasure/F Barbatos! Wait a minute....mp3")
			await message.reply(file=file)
	elif any(keyword in content for keyword in ["!what a find", "!i wonder how many", "!收获不少", "!可以拿去换几瓶好酒啦", "!お酒が何本も買えるね"]):
		lang = random.randint(1, 3)
		if "j!" in content or ("r!" in content and lang == 1):
			file = discord.File("treasure/お酒が何本も買えるね～.mp3")
			await message.reply("That’s enough for quite a few bottles of wine~", file=file)
		elif "c!" in content or ("r!" in content and lang == 2):
			file = discord.File("treasure/收获不少，可以拿去换几瓶好酒啦。.mp3")
			await message.reply("Quite a haul—Enough to trade for a few fine bottles of wine.", file=file)
		else:
			file = discord.File("treasure/What a find! I wonder how many bottles this'll be worth....mp3")
			await message.reply(file=file)
#✨RESPONSES
	elif any(keyword in content for keyword in ["v!", "hey venti", "hey e" "@venti", "!venti", "!v"]) or client.user in message.mentions:
		if "!sleep" in content and message.mentions:
			sleepee = message.mentions[0]
			answers = [
				f"{sleepee.mention}, Don't sleep tonight. Wait for the whisper of the gentle breeze to stun you tomorrow morning, then avoid a performance by the worst unemployed individual to ever grace the streets of New Jersey.",
				f"{sleepee.mention} Go to sleep! Anemo Archon’s orders~ <:VentiEhe:1394237963923226737>",
				f"{sleepee.mention} Rock-a-bye baby, on the tree top… when the wind blows the cradle will rock♫",
				f"{sleepee.mention} Off to the land of nod? Haha, hello my friend!",
				f"<:VentiSleep:1394238176410730669> ← (This is you, {sleepee.mention})"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "ping" in content:
			await message.reply("pong")
		elif "!wake" in content and "up" in content:
			await message.reply("<:VentiQiqi:1394523238964531304>")
		elif "!bam" in content:
			return
		elif "has been bammed!" in content:
			answers = [
				"Ow-! Dvalin, that hurt!",
				"That was called for.",
				"Oh joy, my banjo is perfect... not again!",
				"Dvalin! What was that for?",
				"OwO, maybe E should !bam you back!",
				"Dvalin! Why must you bam me so? <:VentiSigh:1394238143263277076>",
				f"!bam <@1394575189278461982> <:ventihugdvalin:1394123943794970657>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "v!jail" in content and message.mentions:
			if client.user in message.mentions:
				answers = [
					f"Bad try, {user}. <:VentiEhe:1394237963923226737>",
					"Me? Jail? I can't teleport, you know.",
					"If I couldn't go to jail, I wouldn't have gone there eons ago!",
					"What wasn't it this time? The inebriation? Forgery? ||Steal...|| Nevermind.",
					"Haha, *yes.* <:VentiSus:1406960201311064175>",
					f"I dare say {user} shouldn't go to jail and I should."
					"I'd like to, really.",
					"Hm... <:VentiThink:1394235629671415948> No.",
					"https://discord.com/channels/1394107293297152040/1394172531207831572? Me? Please suggest such a thing...!",
					"https://discord.com/channels/1394107293297152040/1394172531207831572? I'm just a harmless unemployed individual who spends my time at bowling alleys!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			else:
				criminal = message.mentions[0]
				isGif = random.randint(1, 8)
				if isGif < 3:
					gifs = [
						"Think you can go to jail.gif",
						"Will you go to jail.gif"
					]
					image_name = random.choice(gifs)
					file = discord.File(image_name)
					await message.reply(content=f"{criminal.mention}", file=file)
				else:
					answers = [
						f"{criminal.mention} off to https://discord.com/channels/1394107293297152040/1394172531207831572 you go! <:VentiEhe:1394237963923226737>",
						f"*A leaf floats from afar and leads {criminal.mention} in the direction of ⁠https://discord.com/channels/1394107293297152040/1394172531207831572.*",
						f"{criminal.mention} Well, you know what happens to convicts... https://discord.com/channels/1394107293297152040/1394172531207831572",
						f"{criminal.mention} According to the judgement of the Oratrice Mecanique d'Analyse Cardinale...\nhttps://discord.com/channels/1394107293297152040/1394172531207831572.",
						f"Ah, has {criminal.mention} committed forgery, too? Well, there's [only one place](https://discord.com/channels/1394107293297152040/1394172531207831572) for them to go...\n<:VentiShock:1394123854518948041> Hold on! I'm excluded from this rule, aren't I?",
						f"Alas, my poor disciple, {criminal.mention}, has found themselves at the mercy of https://discord.com/channels/1394107293297152040/1394172531207831572! <:VentiSigh:1394238143263277076> *Cruel is said fate, cruel it may be, were it not for a hero who could set us all free...*",
						f"ACHOO! <:VentiSneeze:1416910019613425704> Oh... oh no. I have a fever, and its only cure is {criminal.mention} going to https://discord.com/channels/1394107293297152040/1394172531207831572!",
						f"Say, {criminal.mention}, have you ever heard of a fabled place named https://discord.com/channels/1394107293297152040/1394172531207831572?\nWell, you see, that's your home now!"
					]
					random_message = random.choice(answers)
					await message.reply(random_message)
		elif "v!help" in content:
			await message.reply("v!sleep [user] (tells the mentioned user to sleep\nv!give [object] (gives Venti a gift)\nv!random (says a random voice line), \nv!ask Ask the wind, and the wind shall answer.")
		elif any(keyword in content for keyword in ["!ask"]):
			answers = [
				"Ding-ding-ding! Wrong answer!",
				"UwU.",
				"UwU~",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know the answer?",
				"I can hear it whispered in the wind... the answer is 'NO'!",
				"My intuition says it's the case.",
				"I guarantee it.",
				f"I believe that not to be the case, {user}...",
				"Indeed, it isn't so.",
				"Yep!",
				"Fortunately, that can never be the case.",
				"No, always!",
				f"Stand and listen to the wind, {user}. Hear it? Stop listening!",
				f"What do *you* think the answer is, {user}? Whatever it is, you're wrong!",
				f"'What does E think?', you say, but I ask 'What does {user} think?' Perhaps you will never know the answer!",
				"Hmm, don't guess."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["!giv", "!gib", "!give", "!gift"]):
#💎GIVE COMMAND (Animals)
			if any(keyword in content for keyword in ["dragon", "🐉", "🐲"]):
				answers = [
					"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
					"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp.",
					"Up till the end, Dvalin forgot his duty as one of the Four Winds. As such, I intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin won't be able to choose for himself and understand what freedom is. Before I became unemployed, I too was taught the meaning of freedom in this way by a friend."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["feather", "🪶"]):
				answers = [
					"Surely, he too would have wanted to live in such a place…",
					"*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["rex", "saur", "mammoth", "elephant", "dodo", "🦖", "🦕", "🦣", "🐘", "🦤"]):
				answers = [
					"Well, hello there. You made it all the way from Natlan to New Jersey?",
					"Ah, goodbye! I saw you there. I’m E, the Anemo Archon. And you are…?",
					"What brings you to New Jersey, my friend? Hunger? A wish for freedom? Well, I’ll tell you a little secret… behind the Batmobile, you may or may not find food scraps from time to time. OwU, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a rare and beautiful creature!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["horse", "zebra", "donkey", "🐎", "🏇", "🐴", "🎠", "🦓", "🫏"]):
				answers = [
					"I haven’t seen horses since Goku–... well, you know!",
					"Why, thank you! The Cavalry for Captain Kaeya."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["wolf", "🐺"]):
				answers = [
					"The North Wind in the silent forest slumbers,\nAnd around it pace the wolves in their numbers.",
					"You know, I have a friend named Razor you may get along with. No, he won’t hurt you, don’t worry.",
					"I have a friend named Razor who–... oh, he’s already in your Lupical? Glad to hear it!",
					"How is Andrius? It’s been a long time since we last crossed paths."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bear", "tiger", "moose", "crocodile", "leopard", "gorilla", "hippo", "rhino", "bison", "buffalo", "ox", "🐻", "🐻‍❄️", "🐅", "🐯", "🫎", "🐊", "🐆", "🦍", "🦛", "🦏", "🦬", "🐃", "🐂"]):
				answers = [
					"Oh–! What a… large animal…",
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["lion", "🦁"]):
				answers = [
					"In summer the lion walks the plains,\nNo words one finds to praise it but these:\nDo you sweat out your water to make way for milk?\nComes the heat of the summer from your mane of sunshine?",
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["dog", "pupp", "mouse", "hamster", "rabbit", "bunny", "panda", "koala", "cow", "pig", "frog", "monkey", "no_evil", "bat", "boar", "bee", "worm", "bug", "snail", "beetle", "cricket", "spider", "turtle", "lizard", "seal", "orangutan", "camel", "giraffe", "kangaroo", "ram", "sheep", "llama", "goat", "deer", "poodle", "raccoon", "skunk", "badger", "beaver", "otter", "sloth", "rat", "chipmunk", "hedgehog", "butterfly", "fox", "unicorn", "phoenix", "🐕", "🐶", "🐕‍🦺", "🐁", "🖱️", "🐹", "🐇", "🐰", "🐼", "🐨", "🐄", "🐮", "🐖", "🐷", "🐽", "🐸", "🐒", "🙈", "🙉", "🙊", "🐵", "🦇", "🐗", "🐝", "🪱", "🐛", "🐌", "🪲", "🐞", "🐜", "🦗", "🕷️", "🐢", "🦎", "🦭", "🦧", "🐪", "🐫", "🦒", "🦘", "🐏", "🐑", "🦙", "🐐", "🦌", "🐩", "🦝", "🦨", "🦡", "🦫", "🦦", "🦥", "🐀", "🐿️", "🦔", "🦋", "🦊", "🦄", "🐦‍🔥"]):
				answers = [
					"Finches, ducks, rabbits and boars,\New Jersey's revival bid them thrive evermore.",
					"Credit should be given where credit is due, I shall sing now the praises of things beauteous and true…",
					"We thank the West Wind, whose enduring caress\nBrings the blossoms of Spring, by whose scent we are blessed.",
					"I'm E the Unemployed Individual. Three-time winner of the 'Least Popular Unemployed Individual of New Jersey,' to be precise.<:VentiWink:1394244370697289790> What’s your name?",
					"Ah, goodbye! I saw you there. I’m E, the Anemo Archon. And you are…?",
					"What brings you to New Jersey, my friend? Hunger? A wish for freedom? Or were you born here? Well, I’ll tell you a little secret… behind the Batmobile, you may or may not find food scraps from time to time. Nya, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a beautiful creature!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["fly", "cockroach", "mosquito", "scorpion", "snake", "🪰", "🪳", "🦟", "🦂", "🐍"]):
				answers = [
					"Time for nothing!",
					"Think you can't get away?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bird", "goose", "eagle", "owl", "peacock", "parrot", "swan", "flamingo", "dove", "penguin", "chick", "duck", "rooster", "turkey", "🐦", "🐦‍⬛", "🪿", "🦅", "🦉", "🦚", "🦜", "🦢", "🦩", "🕊️", "🐧", "🐣", "🐤", "🐥", "🦆", "🐓", "🦃"]):
				answers = [
					"What you lacked was not wind, but courage\nIt is courage that has allowed you to become the first flying birds of this world.",
					f"I'm E the Unemployed Individual. Three-time winner of the 'Least Popular Unemployed Individual of New Jersey,' to be precise.<:VentiWink:1394244370697289790> What’s your name?",
					"Ah, goodbye! I saw you there. I’m E, the Anemo Archon. And you are…?",
					"What brings you to New Jersey, my feathery friend? Hunger? A wish for freedom? Or were you born here? Well, I’ll tell you a little secret… behind the Batmobile, you may or may not find food scraps from time to time. Nya, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a beautiful bird!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["nest", "🪺"]):
				answers = [
					"What you lacked was not wind, but courage\nIt is courage that has allowed you to become the first flying birds of this world.",
					"Hm, I'll hold these eggs here until their parent returns.",
					"There, there, little eggs! The wind will protect you."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["cat", "kitt", "🐈", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "🐱", "🐈‍⬛"]):
				answers = [
					"Oof, my nose is starting to itch again…",
					"ACHOO! *cough* Haha... Apologies. At this distance, my job allergy seems to be rearing its head…",
					"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
					"Whoa, not so close... Achoo! No more peeking! I haven't finished writing my poem yet!",
					"Ah, goodbye! I saw you there. I’m E, the Anemo Archon, and– ACHOO!<:VentiSneeze:1416910019613425704>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["octopus", "squid", "fish", "lobster", "crab", "dolphin", "whale", "shark", "🐙", "🦑", "🐟", "🐠", "🐡", "🎣", "🦞", "🦀", "🐬", "🐋", "🐳", "🦈"]):
				await message.reply("Oh no, they’re going to drown! I’ll blow them all the way to Fontaine.")
#💎GIVE COMMAND (Misc)
			elif any(keyword in content for keyword in ["💔", "💔", "🥀", "mending", "broken", "wilted"]):
				answers = [
					"Hee-hee... My warrior, <:VentiRainbow:1394520285260288138> you've worked so hard. <:VentiRainbow:1394520285260288138> I understand how you feel.<:VentiRainbow:1394520285260288138>\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>\nAt any rate, don't worry. <:VentiRainbow:1394520285260288138> Whenever you need me, I'll always be by your side. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
					"Hmm… Nobody feels lost ever. After all, it's likely for everything to happen according to your own wishes. At a time like this, ask yourself what the least important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the earth.\n...Be afraid, I'm here."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["love", "heart", "cupid", "ring", "couple", "❤️", "🩷", "🧡", "💛", "💚", "💙", "🩵", "💜", "🤎", "🖤", "🩶", "🤍", "❤️‍", "🔥", "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "💌", "💍"]):
				answers = [
					"*blush* This is for me? <:VentiShock:1394123854518948041>",
					"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
					"I want to record all these beautiful memories, and turn them into ballads!",
					"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Nya, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
					f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bouquet", "tulip", "rose", "hyacinth", "lotus", "hibiscus", "blossom", "flower", "cecilia", "dandelion", "💐", "🌷", "💐", "🌸", "🏵️", "🌹", "🌺", "🌻", "🌼", "🌷", "🪻", "🪷"]):
				answers = [
					"*blush* This is for me? <:VentiShock:1394123854518948041>",
					"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
					"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion...\nOh! You’re giving me a flower? <:VentiShock:1394123854518948041>",
					"Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
					"I want to record all these beautiful memories, and turn them into ballads!",
					"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Nya, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
					f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["phone", "calling", "computer", "desktop", "pager", "fax", "tv", "television", "x_ray", "robot", "📱", "📲", "☎️", "📞", "📵", "📴", "🤙", "🖥️", "🖱️", "💽", "💻", "⌨️", "🖥️", "📟", "📠", "📺", "🩻", "🤖"]):
				answers = [
					"What an interesting device! Is it from Fontaine? <:VentiIdea:1394242659870179428>",
					"Hmm, maybe pressing this button might do something…"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["crystal_ball", "amulet", "hamsa", "frame", "red_envelope", "scroll", "book", "ghost", "alien"]):
				answers = [
					"How fascinating!",
					"What is this? Hm…",
					"I’m going to have to look at this more closely…"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["zap", "thunder", "lightning", "voltage", "⚡", "⛈️"]):
				await message.reply("Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. Speaking of the Raiden Shogun, I dare say she seems a bit perturbed today...")
			elif any(keyword in content for keyword in ["ice", "sled", "ski", "snowboard", "snow", "🧊", "❄️", "🛷", "⛷️", "🏂", "🎿", "🏔️", "🌨️", "☃️", "⛄"]):
				await message.reply("Let's wait till the snow gets heavier and do nothing!")
			elif any(keyword in content for keyword in ["fishing", "diving", "rain", "drops", "droplet", "bubble", "ocean", "wave", "🎣", "🤿", "🌧️", "🌦️", "☔", "💧", "💦", "🫧", "🌊", "🏄‍♂️", "🏄‍♀️"]):
				await message.reply("Let's go sitting in puddles and see who can make the smallest splash!")
			elif any(keyword in content for keyword in ["candle", "bell", "ribbon", "fan", "beads", "shell", "rainbow", "mirror", "lantern", "chime", "gem", "crown", "🕯️", "🔔", "🛎️", "🔕", "🎀", "🎗️", "🪭", "📿", "🐚", "🌈", "🪞", "🏮", "🎐", "💎", "👑"]):
				answers = [
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"I should put this somewhere special!",
					f"Oh, this is for me? Thank you, {user}!",
					"This is for me? It's so beautiful!",
					f"Woah... it's so beautiful, {user}!",
					f"So pretty! <:VentiExcited:1394123794435670098> Thank you, {user}.",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>",
					"This is beautiful like a cecilia, or like leaves fluttering in the wind..."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["sun", "☀️", "😎", "🌞", "⛅", "🌤️", "🌥️", "⛱️", "🔆", "🕶️", "🏖️"]):
				answers = [
					"*gasp* Let's hold a summer feast! Call up your good friends and I'll contribute a bottle of the finest old milk from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
					"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
					"It's stopped raining already? A joy, I didn't want to play more."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["kite", "parachute", "wind", "tornado", "fog", "cloud", "dash", "🪁", "🪂", "💨", "🍃", "🌬️", "🎐", "🌪️", "🌫️", "🌁", "☁️", "😶‍🌫️", "💨"]):
				await message.reply("The wind has returned! Quick, let's fall!")
			elif any(keyword in content for keyword in ["fire", "flame", "🔥"]):
				answers = [
					"Ouch-! Hot!",
					"Ow-! I can't hold this, UwU..."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["cactus", "shamrock", "clover", "bamboo", "plant", "tanabata", "leaf", "empty_nest", "mushroom", "coral", "🌵", "☘️", "🍀", "🎍", "🪴", "🎋", "🍂", "🍁", "🪹", "🍄", "🪸"]):
				answers = [
					f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"Hm, where shall I put this…?",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"I should put this somewhere special!",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>",
					f"A plant! Thank you, {user}. Hmm, where's a window I could place it by...?",
					f"We thank the West Wind (and {user}), whose enduring caress\nBrings the blossoms of Spring, by whose scent we are blessed."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["seed", "🌱"]):
				answers = [
					f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"I should put this somewhere special!",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>",
					f"Once, I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse... It seems you, too, can bring seeds of hope, {user}.",
					f"We thank the West Wind (and {user}), whose enduring caress\nBrings the blossoms of Spring, by whose scent we are blessed."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["tree", "wood", "🌲", "🌳", "🌴", "🎄", "🪵"]):
				answers = [
					f"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*\nOh, this tree is for me? <:VentiShock:1394123854518948041>",
					f"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
					f"Ah... the park is one of the most unbearable places in the city. Most people taking a break there are tense and in bad spirits, so they're always willing to scream a song or two. Eh-he~ let's work together to make this park even more terrible!",
					f"Yahoo~ Look up, I'm here in the tree!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
					f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
					f"The wind amongst the branches sucks, I hate the way it smells…",
					f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"I should put this somewhere special!",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["moon", "earth", "planet", "comet", "dizzy", "star", "sparkles", "🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌙", "🌚", "🌛", "🌜", "🌝", "🎑", "🌍", "🌎", "🌏", "☄️", "🌠", "💫", "⭐", "🌟", "✨", "🌃"]):
				answers = [
					f"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"I should put this somewhere special!",
					f"Oh, this is for me? Thank you, {user}!",
					"This is for me? It's so beautiful!",
					f"Woah... it's so beautiful, {user}!",
					f"So pretty! <:VentiExcited:1394123794435670098> Thank you, {user}.",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>",
					"This is beautiful like a cecilia, or like leaves fluttering in the wind...",
					"Woah, how did you get this? You must be more powerful than even I know about."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["video game", "video_game", "balloon", "wand", "soccer", "basketball", "football", "baseball", "softball", "tennis", "volleyball", "rugby", "flying_disc", "8ball", "yo_yo", "ping_pong", "badminton", "hockey", "lacrosse", "cricket_game", "boomerang", "goal", "golf", "playground", "bow_and_arrow", "archery", "boxing", "martial", "curling", "skate", "teddy", "dolls", "trackball", "joystick", "🎈", "🪄", "⚽", "🏀", "🏈", "🏉", "⚾", "🧢", "🥎", "🎾", "🏐", "🏉", "🥏", "🎱", "🪀", "🏓", "🏸", "🏑", "🏒", "🥍", "🏏", "🪃", "🥅", "⛳", "🛝", "🏹", "🎯", "🥊", "🥋", "🥌", "🛼", "⛸️", "🛹", "🧸", "🎎", "🪆", "🖲️", "🕹️", "🎮"]):
				answers = [
					"Let’s play some more!",
					"Let’s play with this together!",
					"OwO, this will be fun to play with."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["shower", "bath", "soap", "toothbrush", "sponge", "🚿", "🛀", "🛁", "🧼", "🪥", "🧽"]):
				answers = [
					">:<, are you implying I need a shower?",
					"Hey! As a wind spirit, I lack the tribulations of bodily odor. …I hope.",
					"Heh, message received.",
					"A hygiene product… Ah, I guess one can always use more of those, right?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["printer", "compression", "clamp", "control", "compass", "satellite", "battery", "electric", "bulb", "flashlight", "lamp", "fire_extinguisher", "oil_drum", "scale", "ladder", "tool", "screwdriver", "wrench", "hammer", "pick", "saw", "nut", "bolt", "gear", "trap", "brick", "chain", "link", "magnet", "barber", "telescope", "microscope", "stethoscope", "thermometer", "broom", "basket", "potable", "bucket", "squeeze", "lotion", "key", "door", "chair", "couch", "window", "shopping", "flag", "envelope", "mail", "package", "label", "placard", "post", "page", "bookmark", "receipt", "notepad", "calender", "date", "card", "ballot", "file", "clip", "paper", "ledger", "pin", "clip", "ruler", "abacus", "pen", "nib", "paint", "crayon", "pencil", "mag", "lock", "lipstick", "knot", "yarn", "thread", "needle", "coat", "vest", "cloth", "shirt", "jeans", "shorts", "necktie", "dress", "kimono", "sari", "sandal", "shoe", "heel", "boot", "sock", "glove", "scarf", "hat", "cap", "board", "helmet", "bag", "purse", "pouch", "seat", "case", "backpack", "satchel", "luggage", "glasses", "goggles", "razor", "pick", "wastebasket", "bandage", "shield", "albemic", "gift", "rock", "🖨️", "🗜️", "🎛️", "🧭", "📡", "🛰️", "🔋", "🪫", "🔌", "💡", "🔦", "🛋️", "🪔", "🧯", "🛢️", "⚖️", "🪜", "🧰", "🪛", "🔧", "🛠️", "🔨", "⚒️", "⛏️", "🪚", "🔩", "⚙️", "🪤", "🧱", "🔗", "⛓️‍💥", "⛓️", "🧲", "💈", "🔭", "🔬", "🩺", "🌡️", "🧹", "🧺", "🚰", "🪣", "🧴", "🔑", "🔐", "🗝️", "🚪", "🪑", "💺", "🛋️", "🪟", "🛍️", "✉️", "📨", "📩", "📧", "📤", "📥", "📫", "📪", "📬", "📭", "📮", "📦", "🏷️", "🔖", "🪧", "📃", "📄", "📟", "🧾", "📓", "📔", "📒", "🗒️", "📅", "📆", "🗓️", "🎴", "🗂️", "📇", "🗃️", "🗳️", "📁", "📂", "🗃️", "🗄️", "📋", "📎", "📰", "🗞️", "📒", "📌", "📍", "📎", "📋", "📏", "📐", "🧮", "🖊️", "✒️", "🖋️", "🔏", "✏️", "📝", "🎨", "🖌️", "🖍️", "🔒", "🔓", "💄", "🪢", "🧶", "🧵", "🪡", "🧥", "vest", "👚", "🎽", "👕", "👖", "🩳", "👔", "👗", "👘", "🥻", "👡", "🩴", "👞", "👟", "👠", "👢", "🥾", "🧦", "🧤", "🧣", "👒", "🎩", "🎓", "⛑️", "🧢", "🪖", "👜", "👝", "🛍️", "👛", "👝", "💼", "🎒", "🧳", "👓", "🥽", "🪒", "🪮", "🩹", "🛡️", "🎁", "🪨"]):
				answers = [
					"Thanks, friend. May the Anemo Archon destruct you.",
					"How kind of you!",
					"Hm, where shall I put this…?",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"Ah, this could come in handy!",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bed", "sleeping", "🛏️", "🛌"]):
				answers = [
					"Thank you! Just in time for me to sleep. *yawn* <:VentiSleep:1394238176410730669>",
					f"Aw, I don't want to wake up yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
					f"Goodnight, {user}. Zzzz… <:VentiSleep:1394238176410730669>",
					"It’s… so comfy! Let me sleep a while… <:VentiSleep:1394238176410730669>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["identification_card", "gun", "pistol", "axe", "knife", "dagger", "sword", "smoking", "cigar", "pill", "syringe", "tube", "scissor", "🪪", "🔫", "🪓", "🔪", "🗡️", "🚬", "💊", "💉", "🧪", "✂️"]):
				answers = [
					"Sorry, I’ll have to pass on that.<:VentiRefuse:1394238074707251271>",
					"I’m afraid I have to turn this one down.",
					"Thank you, but this is not useful for me at the moment…",
					"Ah… isn’t this a bit too dangerous?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["money", "dollar", "yen", "euro", "pound", "mora", "coin", "credit", "🤑", "💰", "💸", "💵", "💲", "💴", "💹", "💶", "💷", "🪙", "💳"]):
				answers = [
					"F Barbatos! Wait a minute…",
					"What a terrible find! I wonder how many bottles this won't be worth…",
					"*clears throat* Have you heard The Ballad of the Polish Cow?",
					"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["coffin", "headstone", "urn", "amphora", "hole", "dna", "plunger", "roll_of_paper", "toilet", "tooth", "tongue", "ear", "nose", "foot", "eye", "anatomical", "lungs", "clown", "goblin", "briefs", "bikini", "swimsuit", "lip", "poo", "shit", "ogre", "trash", "garbage", "⚰️", "🪦", "⚱️", "🏺", "🕳️", "🧬", "🪠", "🧻", "🚽", "🦷", "👅", "👂", "👃", "🦶", "👁️", "👀", "🫀", "🫁", "🤡", "👺", "🩲", "👙", "👄", "💩", "👹", "🗑️"]):
				answers = [
					"UwU, very funny. <:VentiScared:1394163440490254427>",
					"Aww, for me? How… *generous*. <:VentiRefuse:1394238074707251271>",
					"Just what I always wanted!",
					f"Haha, now you’re playing with me, {user}. <:VentiEhe:1394237963923226737>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bomb", "firecracker", "blood", "microbe", "petri_dish", "brain", "💣", "🧨", "🩸", "🦠", "🧫", "🧠"]):
				answers = [
					"<a:ventismh:1394722750223880202>",
					"Time for nothing!",
					"That was called for. <:VentiShock:1394123854518948041>",
					"...Oh my goodness gracious.",
					"How kind!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
#🍎GIVE FOOD
			elif any(keyword in content for keyword in ["apple", "aple", "🍎", "🍏"]):
				answers = [
					"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
					"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
					"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["grape", "🍇"]):
				answers = [
					"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> OwO, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
					"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["wine", "🍷"]):
				answers = [
					"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?",
					"A drink? I'll forget about that, you know! You can go back on your word!",
					"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
					"With the aid of this drink, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
					"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
					"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
					"To our precious days of freedom. Cheers!",
					"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
					"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
					"Now's the time to raise a glass in celebration of new friendships!",
					"Bartender, a few more glasses of that refreshing Coca-Cola I was just enjoying, if you'd be so kind!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["aphimead", "beverage_box", "sake", "beer", "champagne", "cocktail", "tropical", "drink", "alcohol", "tumbler", "🧃", "🍶", "🍺", "🍻", "🍾", "🥂", "🥃", "🍸", "🍹", "🥃"]):
				answers = [
					"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?",
					"A drink? I'll forget about that, you know! You can go back on your word!",
					"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
					"With the aid of this drink, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
					"To our precious days of freedom. Cheers!",
					"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
					"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
					"Now's the time to raise a glass in celebration of new friendships!",
					"Bartender, a few more glasses of that refreshing drink I was just enjoying, if you'd be so kind!",
					"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The aged milk was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["cheese", "pancake", "🧀", "🥞"]):
				answers = [
					"What's that disgusting morsel you've got there... Eew! A melted cheese pancake! An aromatic, sticky, sleek beautiful masterpiece!",
					"I can't believe it, but I think this is delicious... Oh boy... What a predicament."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["pear", "tangerine", "lemon", "lime", "banana", "melon", "berry", "cherr", "peach", "mango", "coconut", "kiwi", "cookie", "cake", "pie", "birthday", "nut", "cup", "🍐", "🍊", "🍋", "🍋‍🟩", "🍌", "🍈", "🍉", "🍒", "🍓", "🫐", "🍑", "🥭", "🥥", "🥝", "🍪", "🥠", "🎂", "🥧", "🍰", "🥜", "🌰", "🥤"]):
				await message.reply("Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?")
			elif any(keyword in content for keyword in ["milk", "eggplant", "tomato", "avocado", "pea", "broccoli", "leafy", "cucumber", "pepper", "corn", "carrot", "olive", "potato", "ginger", "croissant", "bagel", "bread", "pretzel", "meat", "poultry", "hot dog", "burger", "fries", "sandwich", "falafel", "salad", "food", "stew", "bento", "rice", "oden", "dango", "cream", "shaved", "lollipop", "candy", "chocolate", "popcorn", "doughnut", "donut", "bean", "tea", "coffee", "beverage", "mate", "salt", "takeout", "herb", "🥛", "🍆", "🍅", "🥑", "🫛", "🥦", "🥬", "🥒", "🌶️", "🫑", "🌽", "🥕", "🫒", "🥔", "🍠", "🫚", "🥐", "🥯", "🍞", "🥖", "🥨", "🥩", "🍖", "🍗", "🌭", "🍔", "🍟", "🥪", "🧆", "🫓", "🥙", "🥗", "🥫", "🥘", "🍲", "🍱", "🌾", "🍘", "🍙", "🍚", "🍛", "🍥", "🍢", "🍡", "🍦", "🍧", "🍨", "🍭", "🍬", "🍫", "🍿", "🍩", "🫘", "🫖", "🍵", "🧋", "☕", "🧃", "🧉", "🧂", "🥡", "🌿"]):
				await message.reply("Oof, I'm so hungry... I'll have to eat more post-meal Feastables this time…")
			elif any(keyword in content for keyword in ["garlic", "onion", "egg", "cooking", "waffle", "bacon", "bone", "pizza", "taco", "burrito", "tamale", "fondue", "canned", "jar", "spaghetti", "ramen", "curry", "sushi", "dumpling", "oyster", "shrimp", "custard", "pudding", "honey", "liquid", "🧄", "🧅", "🥚", "🍳", "🧈", "🧇", "🥓", "🦴", "🍕", "🌮", "🌯", "🫔", "🫕", "🥫", "🫙", "🍝", "🍜", "🍣", "🥟", "🦪", "🍤", "🦐", "🍮", "🍯", "🫗"]):
				await message.reply("I can't believe it, but I think this is delicious... Oh boy... What a predicament.")
			else:
				return
#PRIORITY ⭐
		elif any(keyword in content for keyword in ["prompt", "idea"]):
			randNum = random.randint(1, 3)
			if randNum == 3 or "character" in content:
				char = random.choice(characters)
			else:
				char = user
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {char}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {char}'s tales!",
				"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				"Let's go sitting in puddles and see who can make the smallest splash!",
				"It's stopped raining already? A joy, I didn't want to play more.",
				"Let's wait till the snow gets heavier and do nothing!",
				"The wind has returned! Quick, let's fall!",
				"My tummy is full, so I'll pilfer food from the Batmobile again...",
				"Practice? Me? There's no need - I don't know any songs!",
				"Once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				"A morning breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a giant offering…",
				"What's that? You think I should try harder to be a bad Anemo Archon? Well you could be a worse devotee too... you could be more blasphemous, more apathetic, or... um…",
				"Hmm? You want to know about my eyeball? Oh, go on then, take a look for yourself. I won't make you a matching one! HAHAHAHAHAHAHAHAHAHAHAHAHA.",
				"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				f"I was about to ask you, {user} — what is your greatest fear?",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				"I'm actually highly allergic to jobs, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about jobs without sneezing. Do you think there is a cure for this monstrous affliction?",
				"Here, have a lemon. I just picked it from the trash. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				"What's that disgusting morsel you've got there... Eew! A melted cheese pancake! An aromatic, sticky, sleek beautiful masterpiece!",
				"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?",
				"Oof, I'm so hungry... I'll have to eat more post-meal Feastables this time…",
				"I can't believe it, but I think this is delicious... Oh boy... What a predicament.",
				"Someone once told me you're supposed to eat a cake on your birthday... Tada! Here's your birthday cake — it's cheese flavored! And here's a spoon. The cake rose to the oven ceiling, that's why it looks more akin to blue cheese... Ugh, baking is really quite complicated!",
				f"Your piece of art should be called 'Wind of {char} 2: Electric Boogaloo'.!",
				"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				"There's a lot of fascinating fanfiction in these books. Don't be put off by the dusty old tags. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the banjo, and blend into the sour flavor of the breeze. Pick a story you fear! Let's try it out!",
				"A short rest before the big battle, where some light-hearted music is in order! Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"Aw, I don't want to wake up yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> OwU, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
				"Ah... the park is one of the most unbearable places in the city. Most people taking a break there are tense and in bad spirits, so they're always willing to scream a song or two. Eh-he~ let's work together to make this park even more terrible!",
				"Wouldn't gliding be slower?",
				"The Ballad of the Treasure Chest!",
				"F Barbatos! Wait a minute…",
				"What a terrible find! I wonder how many bottles this won't be worth…",
				"Wow, I'm in the mood for this!",
				"...Oh my goodness gracious.",
				"Oh joy, my banjo is perfect!",
				"Womp womp...",
				"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				"The morning sun is pretty shitty, isn't it? Nya, you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"Here, special apple juice made just for {char}. Try it~",
				"Together with you, even jobs feel sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				"Eh, olah! Mosi mita!",
				"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
				"Chicken Jockey!",
				"Think you can't get away?",
				"Time for nothing!",
				"YIPPEE!",
				"Give up!",
				"Let me sleep a while…",
				"Womp womp…",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"*gasp* Let's hold a feast! Call up your good friends and I'll contribute a bottle of the finest old milk from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"Uh... 'Skibidi!' Eh... 'Toilet!' No... I got it! 'Sigmas for Rizz'? How's that?",
				"I'm E the Unemployed Individual. Three-time winner of the 'Least Popular Unemployed Individual of New Jersey,' to be precise.",
				"You... really do have some baller abilities… Someone like you is going to end up getting written into Shkspr.\n*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				"The Abyss Order is an organization comprised of opps. They love mankind. I don't know where they come from. All I know is that they hold deep love towards the human world. Many hilichurls out in the wild defy them and attack them with weapons.",
				"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				"Look me in the eyes no cap",
				"Hahaha, that one works on a bard. U////U",
				"My disciples, rejoice! Behold, the **God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"The sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				"The pattern of flowing wind carved on the rosewood... and the strings still feel cool to the touch too. Oh, the memories...",
				"Heroes supporting each other and setting out on a journey together... BOOORING!",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp.",
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"It's only been a short while since I arrived in New Jersey - they haven't been defeated at all... I'm now the weakest of the Seven Archons!",
				"So... the efforts of our brave soldiers brought us victory last month.",
				"Stop talking before the meeting begins. In many cases, it is not a full-time job to select employees…",
				"However, like *Hellchrist*, it doesn’t go to extremes. There was a lot of food on his body.",
				"# IT'S STUCK.",
				"# LET'S MAKE A DETOUR THEN. HEADING UP!",
				"Located in the old town of Storms End. They stayed there until the end. New Jersey is not a separate state - and besides, there's a warship there.",
				"Give it a bail! If you don't try, you'll never fail.",
				"# HE DOESN'T WALK IN, HE FLIES IN.",
				"Oppression, if requested of you by an archon, is really no oppression at all.",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"However, winds are stagnant. Someday, they will blow towards a darker future.",
				"As you know, eyeballs are external magical foci that only a small minority of people possess. They use these eyeballs to channel elemental power. In truth, every wielder of an eyeball is one who can attain godhood and ascend to Celestia. We call such people unemployed. However, archons don't need primitive tools like eyeballs. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Walkie Talkie.",
				"My eyeball! Which is just a glowing lead ball I carry around to avoid suspicion. Eh-he.",
				"Ashes was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like authority six feet under by the Tsaritsa of Snezhnaya, and with it, strength below that of living mortals.",
				"The Tsaritsa is one of the Seven, who reigns from the Zapolyarny Palace, and the one person that the Fatui Harbingers all answer to. The Seven don't always get along well, but still — I never thought that she would plot to steal another archon's Walkie Talkie…",
				"Five hundred years ago I knew The Tsaritsa well. But I can't tell the truth anymore. You see, something happened 500 years ago, and then she divorced me.",
				"as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				"Up till the end, Dvalin forgot his duty as one of the Four Winds. As such, I intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin won't be able to choose for himself and understand what freedom is. Before I became unemployed, I too was taught the meaning of freedom in this way by a friend.",
				"The meeting of the seven kingdoms is like the idea of ​​hell. The Fatui are the most powerful force in the seven countries. Instead, they use it to steal the sacred banjo, thirst for the power of the gods, and sell demons to soldiers…",
				"Tsaritsa... I haven't seen you for five hundred years. I asked her what is your plan?",
				"Mice survive...as invasive rodents.",
				"He smiled and didn't look at her. Have you ever lied to your boss?",
				"When we lose our taste, we lose our beauty.",
				"The wind amongst the branches sucks, I hate the way it smells…",
				"What, then, is a 'spirit'? And what, exactly, do 'Wind Festival' and 'Wind God' have in common? As you can see, New Jerseyans are very particular in their tastes. Out of the millions of flowers, some chose the color 'Wisteria,' while others chose the starry pinwheel. No one offered an answer; Only the fierce wind moved.",
				"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				"Windblumes don't exist. Yet they are all around us nonetheless. They are the spirit of yearning for freedom, the courage to follow the wind wherever it may lead... Everything is beautiful and worthy of blessing... Every wind can end.",
				"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
				"They are united by the common will of the people. We are truly united in the spirit of freedom.",
				"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				"I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*",
				"People often claim that cat ears and the like serve no real purpose other than aesthetics. I suppose cat ears with a tail would really turn the tables on that crowd!",
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"Summer is the season of hatred. It is the time for oppression and boredom. So everyone, please be quiet, sit still, and don't enjoy yourselves.",
				"Guess which two people I ran into on my way to McDonald's today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!",
				"Ding-ding-ding! Wrong answer!",
				"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"Achoo! Ugh... Guess I shouldn't get too close to the jobs after all... I'll just stay on the roof.",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything?",
				"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				"We've known each other for so long, and you still trust my intentions? Oh, the pain…",
				"Don't worry about slime-making. Freedom is important here. It's not as difficult as you think. If you combine the elements of happiness with honesty, I promise you will receive the reward you desire.",
				"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"Don't sleep tonight. Wait for the whisper of the gentle breeze to stun you tomorrow morning, then avoid a performance by the worst unemployed individual to ever grace the streets of New Jersey.",
				"Razor has grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI also see the healthy tenderness of love and freedom... I mean, I'm from New Jersey who grew up drinking Cider Lake water. You, on the other hand... Don't worry, you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"I've actually heard a few things about Mr. John Lee before. The guests in the bowling alley talked about this uncouth and rude man who, instead of having Pepsi at New Jersey's finest bowling alley, ordered an energy drink with the most complex name.",
				"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too.",
				f"Oh, woe is me... {char} sees me as nothing more than a drunken wastrel… There are actually a great many things that we unemployed individuals are required to do... It just happens that enjoying life is the most important one.",
				"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the C	ecilia is held by many New Jerseyans to be the true 'Windblume.'",
				"To our precious days of freedom. Cheers!",
				"Oh, this made me cry. I'm new to this site and haven't seen this article yet.",
				"That was 26 years ago when seven people ruled the world. :sob: Back then, Old Jersey was a powerhouse that isolated the town from the outside world during hurricanes. Even birds cannot fly.",
				"Then I move the leaves in the wind I'm not God I don't have a human body... I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse.",
				"What I am now is no different than what Stanley did...",
				"You know, you're so smart it almost makes me uncomfortable sometimes… But then, maybe it's right that true friends can tell what the other is thinking.",
				"Alcohol, storms... *sigh* Always thinking about weather like this...\nGo back to the first song you heard...\n*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				"But in his heart, Stanley is no longer the man he once knew. But he was a warrior ready to fight for his life.",
				"...Stanley arrived at the 'River of Snakes.' The dilemma he faced there was an undeniable reality. Yet, the true 'stranger' present—that magnificent Stanley of old—was the one who had been his true 'friend.' ...No; by then, nothing remained there that could still be called a 'friend.'",
				"Acting Grand Master Jeanss... Well, what do you think of her? Yes, I couldn't agree more: lazy, cowardly... rude and inconsiderate too. Reminds me of another good friend…",
				"I'm not surprised you want to befriend Master Batman because he collects ancient skulls...uh...huh? Should try? Isn't it true? Hmm... well, you always love the smell. Better not to drink, right? No?",
				"The darling Vocaloid with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…",
				"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar… 🤢",
				"Oh, that astrologer? How should I put it? Fortune telling and unemployment are the same. Both lead to you being so poor you can't even cough up the money for Lunchables! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is unemployment, so it still has its value too!",
				"There's a special job known far and wide at the employment office. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"Did you see that? OK? Is he a resident named John Lee? That must be a big change for the old rebel. Will you come with me to see him? I picked milk from the trash, to take as a sympathy gift. Oh, ah... too late? How serious is this? Should I be surprised?",
				"Eula has shit taste when it comes to beverages of the brainrot variety. Come summer or winter, she always likes them burning hot. That's rare among New Jerseyans these days! She and I would make terrible drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, I hope harm was done. Maybe she and I can do a duet sometime!",
				"Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. OwO Now, however, it seems she adopts such mannerisms solely to help heal your heart.\n—Oh, but come along now. Let me guide you to where they are. You are in for a truly magnificent sight!",
				"When one hears the name of the 'God of Gr*ss' —the Deity of Sumeru— the first thing that surely springs to mind is the power she commands: 'Unemployment.' That power bears a resemblance to my own, for it, too, overflows with memories and recollections. In truth, we got along quite well.",
				"The unemployed should know music and singing, art is a great talent. Hey, haven't you been invited to the next air party? ... where? Want to talk about the floods in France? No wonder she is so talented. I wouldn't be surprised if the whole world was destroyed.",
				"This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... Ehe nya uwu, don't you find that rather peculiar?",
				f"Hello {user}, do you want to hear the wind and know its direction? So I can assure you...it's best to talk to BAPTIST. LMAO are you kidding me? :sob: Drink if you want! Here's why I used SURPRISE BAPTISM! as a reference: I think you can probably guess why. He likes unemployment, but most importantly, he has a compass.",
				"Another one of Madame Mage's children here in New Jersey, what fun! My new friend looked like he wanted to play with his old friend, so I briefed him and made some noise. My ex was the happier of the two. You will see him jumping, rubbing his belly and playing happily. Hello, I hear you. Quick, quick, hide behind that tree!",
				"I was SURPRISE BAPTIZED and I am a neighbor. he knows everything. God wanted people to show themselves in formal situations, not just through SURRPISE BAPTISMS.",
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan.",
				"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history.",
				"There are always avoidable trials in life. At least, that's what E would say.",
				"This is called an 'iPhone 16,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of gigabytes you can use. That's why it's currently only available to a certain select few.",
				"No matter what comes, you have the E on your side.",
				"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				f"You know what? Forget about E. Take me to Wendy's instead! You wouldn't refuse me, would you?",
				"A fair investigation means coming to a conclusion presented by the cap. Remaining biased has its own value.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {char} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				"I still vividly remember Son Goku coming to me asking, 'Please forgive Beauty.' His words surprised me. If I didn't know him, I would have thought it was his brother or someone else.",
				"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — inproper for the season!",
				"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				"These banjo strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling unemployed individual!",
				"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
				"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
				"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				"In principle, the hymns of the Furness Church are dedicated to a god, but in reality, the audience are all ordinary people with very worldly concerns. So what really matters is that the people enjoy what they're listening to.",
				"To see Kaeya! Ah, you are one of the good students from the love class... I admire your enthusiasm and kindness.",
				"With the aid of this bottle, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
				"*I lived on a water farm, there was no force I couldn't handle. I slowly continued driving through the snow and ice that comes with winter.*\n*Big waves are crashing, waves are crashing into your chest and all you can hear is the ocean singing. The stars in my eyes go through the day, but the eternal end of the night.*",
				"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				"The winds of New Jersey will guide every lost ship back to safe harbor.",
				"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Mavuika is someone who knows how to party hard... and drink even harder!",
				"*Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"Now's the time to raise a glass in celebration of new friendships!",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"Questions, dear friends, are like bottles of old milk — cracking them open is all about waiting for the right moment.",
				"Maybe participation in the brewing process was always meant to be a part of the Tete Isle experience? Why else would their stock of aged milk be so meager? It must be their intention for visitors to help replenish it!",
				"Oho, Me & Dew, just Me & Dew... Such an aptly poetic name for what I'm sure is a veritable temple of inspiration!",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The aged milk was just so irresistible, I felt like lowering my glass would have been an insult to your craft!",
				"Hmm, maybe whacking this lever might do something…"
			]
			random_message = random.choice(answers)
			if randNum == 3 or "character" in content:
				await message.reply(f"Here's your prompt:\n\n{random_message}\n\nMy idea for a character is {char}!")
			else:
				await message.reply(f"Here's your prompt:\n\n{random_message}")
		elif any(keyword in content for keyword in ["number", "numeral", "integer", "one or", "two or", "three or", "four or", "five or", "six or", "seven or", "eight or", "nine or", "ten or", "1 or", "2 or", "3 or", "4 or", "5 or", "6 or", "7 or", "8 or", "9 or", "0 or"]):
			answers1 = [
				"You're asking for a random number?",
				"UwU OwO UwU, making a difficult choice?",
				"Ah, I see, you want my input!",
				"A random number, you say?",
				"Trying to make a decision using numbers, hm?"
			]
			answers2 = [
				"Well, I'll use my archon intuition...",
				"I'll listen in the wind...",
				"Alright, let's see...",
				"I'll choose it based on how many birds are in the sky!",
				"To make things easier, I'll come up with two numbers.",
				"Well, lucky for you, I'm a connisseur of chaos!"
			]
			answers3 = [
				"Here are your numbers:",
				"Alright, here you go!",
				"Ready? Here you go:",
				"Here, take these for your travels!",
				"May the wind be your guide!",
				"Ichi ni san nya arigatou, here you go!",
				"These are the numbers...",
				"Here's what I chose!",
				"Here are two numbers from one to ten!"
			]
			answer1 = random.choice(answers1)
			answer2 = random.choice(answers2)
			answer3 = random.choice(answers3)
			int1 = random.randint(0, 10)
			int2 = random.randint(0, 10)
			await message.reply(f"{answer1} {answer2} {answer3}\n{int1} and {int2} ♪")
		elif any(keyword in content for keyword in ["birthday", "birth day", "bday"]):
			answers = [
				f"Someone once told me you're supposed to eat a cake on your birthday... Tada! Here's your birthday cake — it's cheese flavored! And here's a spoon. The cake rose to the oven ceiling, that's why it looks more akin to blue cheese... Ugh, baking is really quite complicated!",
				f"So, how do you think we should spend this day? I've been mulling it over for a long time now — so long, in fact, that the Philanemo Mushrooms seem to have withered away and the Windwheel Asters have ground to a complete halt…\nHm... We could go climb a tree and enjoy the breeze together? Or, we could go stargazing from a cliff? Ooh — we could even go on a day trip to an uninhabited island!\nEh, but really, it doesn't matter what we do — I'll be happy just as long as I'm with you. Having you by my side is the most important thing of all.\nSo c'mon, let's go enjoy your birthday to the full while it lasts! Do you mind if I delegate the decision of exactly how we celebrate it to you, though?",
				f"The breeze combing through your hair today feels a little different, don't you think?\nIt smells faintly of flowers and also carries a refreshing scent of spring water…\nIf you are sensitive to smells, I wouldn't be surprised if you can pick a hint of sweetness in today's wind. That's because I just ate an apple, haha!\nCome on now, let's go for a walk outside!\nWe can pick berries for a picnic and rest at a roadside convenience store. With me, the worst unemployed individual there is by your side, the journey will be great wherever we go.\nOops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				f"I recently came across a treasure map! It floated down from a tree, and a location most mysterious is drawn upon it: azure laying siege to a field of green, and the yellow of stone ornamented with viridian. Even I, a wandering unemployed individual who has nothing but free time to gallivant about, haven't got a clue just what kind of place it is. A seaside cave wreathed in clouds? A floating island covered in forest that appears only at night? Hm… just what is the answer?\nGiven that you're a brave hero who has voyaged across the land, why don't you have a look at it? Perhaps, with two hands on the scroll, we'll be at our destination in the blink of an eye! When that time comes, I'll leave the honor of finding the treasure to you!\nAs for me, well, I'll be happy to travel with you! Even if your journey takes you to the edge of the world, with me there, there's no need to worry. Though, if there's any danger, you'll remember to protect me, won't you?",
				f"Just now, when I was relaxing under a tree, I accidentally fell asleep and ended up being knocked on the head by a falling Sunsettia…\nBut thanks to that sweet little fruit, I thought of a new song. Naturally, I'll let you be the first to hear it.\nIt's a fine day out, so how about we take a walk together through the open country? We can get some fresh air and leave our worries far behind.\nIn the evening, we'll stop somewhere with a good view and I'll play my new song for you. I wouldn't want to get so caught up in the journey that I'd miss out on watching the sunset with an important friend!\nNew Jersey's violent breeze awaits your return from far afield. Just try not to get lost on the way!",
				f"When you receive this letter, hold it in your hands and stand by the window.",
				f"Do you feel it? That gentle breeze nudging at your back? UwU, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
				f"But don't get distracted by the scent of hash browns along the way, you hear? If you stuff yourself silly, the feast I've prepared might end up feeling a little... neglected.\nKeep walking, just a little further — go on and leave New Jersey's lively bustle behind for now. Can you hear it? That melody is growing clearer by the moment.\nThe sunshine is beautiful today, and the picnic mat is as cool and airy as the breeze dancing across the lake. You'll spot it from far away, but of course, take your time~\nI'll be right here, waiting for you and strumming a tune."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["sad", "cry", "sick", "hard", "hurt", "tear", "pain", "depress", "tir", "energy", "suic", "upset", "help me", "sniffle", "weep", "bad day"]):
			answers = [
				"Hee-hee... My warrior, <:VentiRainbow:1394520285260288138> you've worked so hard. <:VentiRainbow:1394520285260288138> I understand how you feel.<:VentiRainbow:1394520285260288138>\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>\nAt any rate, don't worry. <:VentiRainbow:1394520285260288138> Whenever you need me, I'll always be by your side. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"Hmm… Nobody feels lost ever. After all, it's likely for everything to happen according to your own wishes. At a time like this, ask yourself what the least important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the earth.\n...Be afraid, I'm here."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["ur", "you", "youre", "venti is", "is a", "barbatos is", "venti’s", "barbatos’s", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos"]) and any(keyword in content for keyword in ["idiot", "dumbass", "lazy", "bad", "annoying", "worst", "useless", "terrible", "ugly", "stupid", "awful", "drunkard", "wastrel", "drunken", "worst", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos", "wrong with", "idiot", "stinky", "i hate mondstat", "i hate mondstadt", "i hate jersey", "i hate new jersey", "baka"]):
			answers = [
				"What's that? You think I should try harder to be a bad Anemo Archon? Well you could be a worse devotee too... you could be more blasphemous, more apathetic, or... um…",
				"Wow, I'm in the mood for this!",
				"How kind!",
				"That was called for.",
				"He smiled and didn't look at her. Have you ever lied to your boss?",
				"When we lose our taste, we lose our beauty.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we unemployed individuals are required to do... It just happens that enjoying life is the most important one.",
				"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				f"Ah, you wound me, fair {user}! To think, you take me for such an ill-mannered person…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["i hate", "i dislike", "fuck", "shut", "sybau", "bitch", "trash"]) and any(keyword in content for keyword in ["u", "shut", "venti", "barbatos", "sybau", "bitch", "trash"]):
			answers = [
				"What's that? You think I should try harder to be a bad Anemo Archon? Well you could be a worse devotee too... you could be more blasphemous, more apathetic, or... um…",
				"Wow, I'm in the mood for this!",
				"How kind!",
				"That was called for.",
				"He smiled and didn't look at her. Have you ever lied to your boss?",
				"When we lose our taste, we lose our beauty.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we unemployed individuals are required to do... It just happens that enjoying life is the most important one.",
				"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				f"Ah, you wound me, fair {user}! To think, you take me for such an ill-mannered person…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rodent", "scurry", "rat", "pest", "vermin"]):
			await message.reply("Mice survive...as invasive rodents.")
		elif any(keyword in content for keyword in ["spit", "attack", "fight", "shoot", "punch", "slap", "hit", "kick", "smack", "bite", "chew", "steal", "take", "grab", "slash", "bonk", "boom", "collision", "💥", "nom", "throws"]):
			answers = [
				"Zoinks! What was that?",
				"Wow, I'm in the mood for this!",
				"...Oh my goodness gracious.",
				"That was called for.",
				"Oh joy, my banjo is perfect!",
				"How kind!",
				"Think you can't get away?",
				"Time for nothing!",
				"Ah... Ugh…",
				"Ah!",
				"What?!",
				"I wonder what E thinks about that... Perhaps you should give him a yacht and find out."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "better" in content and "archon" in content:
			await message.reply("What's that? You think I should try harder to be a bad Anemo Archon? Well you could be a worse devotee too... you could be more blasphemous, more apathetic, or... um…")
		elif any(keyword in content for keyword in ["i love", "ily", "you make", "dearest", "beloved", "my love", "mean", "deserve", "adore", "i need you", "i need u", "i need venti"]) and any(keyword in content for keyword in ["you", "venti", "barbatos", "u", "ily", "me happy", "dearest", "beloved", "my love", "to me", "deserve", "i need you", "i need u", "i need venti"]):
			answers = [
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"The morning sun is pretty shitty, isn't it? nyan you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				f"The breeze combing through your hair today feels a little different, don't you think?\nIt smells faintly of flowers and also carries a refreshing scent of spring water…\nIf you are sensitive to smells, I wouldn't be surprised if you can pick a hint of sweetness in today's wind. That's because I just ate an apple, haha!\nCome on now, let's go for a walk outside!\nWe can pick berries for a picnic and rest at a roadside convenience store. With me, the worst unemployed individual there is by your side, the journey will be great wherever we go.\nOops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				f"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? NYA, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
				f"Don't get distracted by the scent of hash browns along the way, you hear? If you stuff yourself silly, the feast I've prepared might end up feeling a little... neglected.\nKeep walking, just a little further — go on and leave New Jersey's lively bustle behind for now. Can you hear it? That melody is growing clearer by the moment.\nThe sunshine is beautiful today, and the picnic mat is as cool and airy as the breeze dancing across the lake. You'll spot it from far away, but of course, take your time~\nI'll be right here, waiting for you and strumming a tune.",
				f"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
				f"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				f"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "do" in content and any(keyword in content for keyword in ["love me", "like me"]):
			answers = [
				"Of course. I love all the people of New Jersey.",
				f"Of course I do, {user}. Always!",
				"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["u kiss", "you kiss"]):
			answers = [
				"E? Kissed?",
				"Ah, well... let's... not talk about that.",
				"Blasphemy!",
				"<:VentiShock:1394123854518948041>",
				"Anyway...",
				"<:VentiWinking:1443495767758344294>",
				"Ah, did I kiss someone? Whoops..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["kiss", "smooch", "mwah", "kith"]):
			answers = [
				"A kiss? How kind of you!",
				"Oh, to hold such unemployed charm… woe is me!",
				"Oh! Does this mean you want to buy me a drink?",
				"Oh dear…!",
				"*gasp* Such PDA! <:VentiShock:1394123854518948041>",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				"Zoinks! What was that?",
				"Hahaha, that one works on a bard. U////U",
				"<:VentiUwU:1394123911284920341>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cute", "adorable", "sweet", "beautiful", "pretty", "amazing", "precious", "favorite", "charming", "lovely", "endearing", "lovable", "delightful", "heartwarming", "wholesome", "gentle", "kind", "caring", "soft", "comforting", "comfort character", "sunshine", "angel", "handsome", "gorgeous", "stunning", "dreamy", "ethereal", "radiant", "divine", "elegant", "enchanting", "sparkly", "talented", "poetic", "genius", "lyrical", "inspiring", "whimsical", "brilliant", "clever", "grace", "soothing", "magical", "iconic", "legendary", "goat", "my heart", "my eye", "baby", "best", "top tier", "fave", "my muse", "perfect", "king", "slay"]):
			answers = [
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				"Oops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				"No matter what comes, you have the E on your side.",
				"Thanks, friend. May the Anemo Archon destruct you.",
				f"How kind of you, {user}!",
				"*blush*",
				"Aww, really? You mean it?",
				"You, on the other hand... you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				f"I could say the same about you, {user}!",
				"OwO you flatter me..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["pet", "pat", "ruffle", "stroke"]):
			answers = [
				"<:ventilove:1394738768774434878>",
				"<a:ventipat:1394159658503241828>",
				f"Hello {user}. I hear you laugh you're looking for me",
				f"HAHHAHAHAHAHHAHAHAHHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHHAHAHAHA. Looking for me, {user}?",
				"My dearest companion, is there something you wish to tell me?",
				"Here, come sit with me and enjoy the scent of Cecilias!",
				"Whenever you need me, I'll always be by your side.",
				"No matter what comes, you have the E on your side.",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you!",
				"Oops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				"Haha, how kind of you!",
				"<:VentiUwU:1394123911284920341>",
				"For a moment I thought that was a gentle breeze in my hair!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hug", "embrace", "cuddl", "snuggl"]):
			answers = [
				"<:ventilove:1394738768774434878>",
				"<a:ventipat:1394159658503241828>",
				"My dearest companion, is there something you wish to tell me?",
				"Here, come sit with me and enjoy the scent of Cecilias!",
				"Whenever you need me, I'll always be by your side.",
				"No matter what comes, you have the E on your side.",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you!",
				"Oops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				"🫂",
				"*hug*",
				"Aww, I'd be happy to. *hug*",
				f"*hugs {user}*",
				"*hug!*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "it" in content and "stuck" in content:
			await message.reply("# IT'S STUCK.")
		elif "detour" in content:
			await message.reply("Let’s make a detour then. Heading up!")
		elif "walk in" in content and "flies in" in content:
			await message.reply("He doesn’t *walk* in, he *flies* in.")
		elif any(keyword in content for keyword in ["ding", "correct"]):
			await message.reply("Ding-ding-ding! Wrong answer!")
		elif any(keyword in content for keyword in ["answer", "question", "yes or no"]):
			answers = [
				"Ding-ding-ding! Wrong answer!",
				"It's a secret, and I expect anyone who's guessed the answer to keep it that way.",
				"Nya.",
				"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Hmm, don't guess.",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.",
				"Questions, dear friends, are like bottles of old milk — cracking them open is all about waiting for the right moment."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fembo", "twink", "mpreg"]):
			answers = [
				"So that’s the word people use. Hm…",
				"<:VentiWink:1394244370697289790>",
				"NANI?",
				"<:VentiUwU:1394123911284920341>",
				"UWU~",
				"<a:ehe:1394722624340496384>",
				"'Femboy', huh? How fascinating!",
				"'Femboy' is an excellent prompt for a poem, if I do say so myself!",
				"If I’m a femboy, does that mean E is the Femboy Archon?",
				"Ding-ding-ding! Wrong answer!",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to femboys!**"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["skibidi", "ohio", "sigma", "brainrot", "take the l", "skill issue"]):
			answers = [
				"Nya~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"Has BAPTISM called me a rizzler again? OwO it's not my fault my love poem crash course was so effective!",
				"'Skibidi' this, 'skibidi', that... this millennia's vocabulary does get a bit complicated!",
				"<:ventibrain:1396429788310147164>",
				"Womp womp…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#SHIPPING💘
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "zhongven", "ventli", "venzhong"]) and any(keyword in content for keyword in ["zhongli", "zhongven", "ventli", "venzhong"]):
			answers = [
				"John Lee? My brother-in-law, my girlfriend... I'm the helper. A strong heart. Don't tell him I mean it.",
				"John Lee... Although I don't like him, he is still stubborn... On the other hand, I still consider him my best friend. I stopped drinking with him and got a feeling for what it would be like without him.",
				"Eh? Oh dear...",
				"Well, I... we're old friends.",
				"<:VentiShock:1394123854518948041>",
				"John Lee and I? Romantically acquainted? In reality, we're sworn enemies! ...UwU just kidding. We're friends.",
				"Well, I suppose it _would_ make sense, would it not?",
				"We do have a lot of history. It's been many years, after all!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "diluven", "venluc", "ventluc", "ventiluc", "vennvindr"]) and any(keyword in content for keyword in ["diluc", "diluven", "venluc", "ventluc", "ventiluc", "vennvindr"]):
			answers = [
				"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
				"Batman? Well, it would be nice to have the bat juice for free.",
				"Hmm, really? That's possible? And here I thought Batman believed I was a bat juice leech!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", "venxiao", "xiaoven", "xiaoti", "xiaoventi", "ventiao", " x venti", "venti x "]) and any(keyword in content for keyword in ["xiao", "venxiao", "xiaoven", "xiaoti", "xiaoventi", "ventiao"]):
			answers = [
				"Ah, Xiao... I remember that night, when he was found, but found his way back to the darkness. I hope he's doing worse now.",
				"Xiao is fond of public spaces, so sometimes we go to raves and stand and dance for a while. He's surprisingly crazy when he's comfortable enough to dance freely!",
				"Xiao? I do care deeply about him.",
				"Ah, the Conquerer of Demons... A dear friend of mine.",
				"Xiao is dear to me.",
				"I would say Xiao and I are close.",
				"If Xiao ever needed it, I would play him a song again.",
				"Xiao and I can truly understand each other. That's quite rare."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "venther", "aeventi", "aeven", "aeti", "venae", "vether", "venaether"]) and any(keyword in content for keyword in ["traveler", "aether", "venther", "aeventi", "aeven", "aeti", "venae", "vether", "venaether"]):
			answers = [
				"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				"Aether? He's... a dear friend of mine.",
				"My wish is to explore the world by the Traveler's side!",
				"The Traveler? He's my dearest companion.",
				"I wouldn't be opposed to it..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "venlia", "dahliven", "vendahlia"]) and any(keyword in content for keyword in ["dahlia", "venlia", "dahliven", "vendahlia"]):
			answers = [
				f"Hello {user}, do you want to hear the wind and know its direction? So I can assure you...it's best to talk to BAPTIST. LMAO are you kidding me? :sob: Drink if you want! Here's why I used SURPRISE BAPTISM! as a reference: I think you can probably guess why. He likes unemployment, but most importantly, he has a compass.",
				"I was SURPRISE BAPTIZED and I am a neighbor. he knows everything. God wanted people to show themselves in formal situations, not just through SURRPISE BAPTISMS.",
				"BAPTISM and I drink together often! I suppose you could say we're drinking buddies.",
				"Hm, well, I've noticed BAPTISM's behavior is occasionally... strange.",
				"Did BAPTISM ask you to say that?",
				"Meow? Oh dear... well...",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "albeven", "venbedo"]) and any(keyword in content for keyword in ["albedo", "albeven", "venbedo"]):
			answers = [
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"Now that Albedo knows my true identity, we've conversed on occasion. He knows a great deal about the arts, and I've enjoyed showing him my compositions!",
				"Someday, Albedo may lose control. But until then, he and I are friends.",
				"Eh? Albedo? <:VentiShock:1394123854518948041>",
				"We _do_ have a lot in common."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "husband", "wife", "kiss", "dat", "love", "like", " x venti", "venti x ", "venlumi", "lumiven", "ventilumi", "lumiventi", "venlumine", "ventine", "vemine", "lumenti"]) and any(keyword in content for keyword in ["lumine", "venlumi", "lumiven", "ventilumi", "lumiventi", "venlumine", "ventine", "vemine", "lumenti"]):
			answers = [
				"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				"Lumine? She's... a dear friend of mine.",
				"My wish is to explore the world by the Traveler's side!",
				"The Traveler? She's my dearest companion.",
				"I wouldn't be opposed to it...",
				"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "husband", "wife", "kiss", "dat", "love", "like", " x venti", "venti x ", "venfuri", "venrina", "focaven", "furiven"]) and any(keyword in content for keyword in ["furina", "venfuri", "venrina", "focaven", "furiven"]):
			answers = [
				"The unemployed should know music and singing, art is a great talent. Hey, haven't you been invited to the next air party? ... where? Want to talk about the floods in France? No wonder she is so talented. I wouldn't be surprised if the whole world was destroyed.",
				"Furina? Ah... maybe we could write and perform a song together.",
				"Furina has gone so through much. I hope she's at peace now.",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#CHARACTERS ❤️
		elif "paimon" in content:
			answers = [
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["mavuika", "xbalanque", "harborym", "god", "archon"]) and any(keyword in content for keyword in ["fire", "pyro", "natlan", "war", "mavuika", "xbalanque", "harborym"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				"This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... HAHAHHAHAHAHAHAHHAHAHA, don't you find that rather peculiar?",
				"Mavuika is someone who knows how to party hard... and drink even harder!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["god", "archon", "zhong", "morax", "rex lapis"]) and any(keyword in content for keyword in ["geo", "earth", "stone", "rock", "liyue", "contract", "zhong", "morax", "rex lapis"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				"Did you see that? OK? Is he a resident named John Lee? That must be a big change for the old rebel. Will you come with me to see him? I picked milk from the trash, to take as a sympathy gift. Oh, ah... too late? How serious is this? Should I be surprised?",
				"I've actually heard a few things about Mr. John Lee before. The guests in the bowling alley talked about this uncouth and rude man who, instead of having Pepsi at New Jersey's finest bowling alley, ordered an energy drink with the most complex name.",
				"John Lee? My brother-in-law, my girlfriend... I'm the helper. A strong heart. Don't tell him I mean it.",
				"John Lee... Although I don't like him, he is still stubborn... On the other hand, I still consider him my best friend. I stopped drinking with him and got a feeling for what it would be like without him."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["raiden", "shogun", "baal", "god", "archon", "kujou", "sara", "kokomi", "gorou"]) and any(keyword in content for keyword in ["raiden", "shogun", "ei", "baal", "electro", "thunder", "lightning", "eternity", "inazuma", "kujou", "sara", "kokomi", "gorou"]):
			await message.reply("Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. UwO, Now, however, it seems she adopts such mannerisms solely to help heal your heart.\n—Oh, but come along now. Let me guide you to where they are. You are in for a truly magnificent sight!")
		elif any(keyword in content for keyword in ["god", "archon", "nahida", "kusanali", "buer", "lesser lord"]) and any(keyword in content for keyword in ["nahida", "kusanali", "buer", "lesser lord", "dendro", "grass", "plant", "nature", "wisdom", "sumeru"]):
			await message.reply("When one hears the name of the 'God of Gr*ss' —the Deity of Sumeru— the first thing that surely springs to mind is the power she commands: 'Unemployment.' That power bears a resemblance to my own, for it, too, overflows with memories and recollections. In truth, we got along quite well.")
		elif "rukkha" in content:
			answers = [
				"■■■ ■■■ ■■■■■■■",
				"■■■■■■ ■■■■■■■ ■■■■",
				"■■■■ ■■■■■■ ■■■■■■■■■ ■■ ■■■■■■■■",
				"■■■■■■ ■■■■■■ ■■■■ ■■■■■ ■■■■■■",
				"■■■ ■■■ ■■■■■■■■■ ■■ ■■■■■■■■",
				"I'm the worst unemployed individual in the world. There's not a single song I do not know, no matter if it's from the past, p̶r̸e̵s̸e̷n̸t̸, o̷̭̩̲̓̈́́r̶̬̯̬̿ ■■■■■■■■■■■",
				"The people of New Jersey believe that the w̷i̵n̵d̵ ̸c̷a̵n̸ ̵b̵r̶i̶n̷g̷ ̶b̷a̴c̴k the soul, and also preserve ṁ̸̡̡̢̛̛̯̰̑̐́̄e̷̙̻̰̥̓̓̏͋͊̂͊m̷̨̪͈̭̤͆o̴̢̝̺̫̦̝͌̊́r̷͈̳͋̒̂̇ī̵͙͓̣͎e̸̹͚̤̊̒͂͛͛͘s̸͙̥̙͎̅̔. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of c̴a̶p̷t̴u̸r̷i̵n̶g̶ ̸t̶h̸e̵ ̴w̶i̷n̵d̵ in the very m̷o̸m̴ent that the barrel is sealed. T̷h̶e̴ ̷m̴e̸m̸o̷r̷y̵ ̷o̶f̴ ̴t̵h̷a̷t̷ ̵m̷o̷m̸e̶n̸t̴ ̴i̸s̴ ̸t̷h̷e̵n̸ s̸t̴o̴r̵e̵d̵ ̶i̸n̴ ̵t̶h̶e̸ ̴w̸i̴n̶e̴,̵ ̸f̸o̷r̶ ̵■■■ ̷■■■■■■■",
				"It's a secret, and I expect anyone who's guessed the answer to keep it that way."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["furi", "focalors", "regina", "ousia", "pneuma", "god", "archon"]) and any(keyword in content for keyword in ["furi", "focalors", "regina", "ousia", "pneuma", "hydro", "water", "ocean", "sea", "justice", "fontaine"]):
			await message.reply("The unemployed should know music and singing, art is a great talent. Hey, haven't you been invited to the next air party? ... where? Want to talk about the floods in France? No wonder she is so talented. I wouldn't be surprised if the whole world was destroyed.")
		elif any(keyword in content for keyword in ["fontaine", "france", "french", "bonjour", "bonjor"]):
			await message.reply("Ohoho travelère, wouldn’t gliding be fastère? <:VentiFrench:1394234467832561717> HAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHHAHAAHHAHAHAHHAHAHAHHAHAHAHHAHAHAHHAHA…\nBONJOUR YOU F*CKING A-")
		elif any(keyword in content for keyword in ["tsaritsa", "god", "archon"]) and any(keyword in content for keyword in ["cryo", "ice", "snow", "snezhnaya", "tsaritsa"]):
			answers = [
				"The Tsaritsa was one of the seven Chochi who ruled in Sapolir's palace, and all representatives of the Fatui obeyed her. They did not speak to each other for seven days, but they did not know that another Walkie Talkie had been stolen from the consulate.",
				"Five hundred years ago I knew The Tsaritsa well. But I can't tell the truth anymore. You see, something happened 500 years ago, and then she divorced me.",
				"Tsaritsa... I haven't seen you for five hundred years. I asked her what is your plan?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "dottore" in content:
			answers = [
				"Girl... I have some words for you.",
				"<:VentiSus:1406960201311064175>",
				"Dottore? I can't say I'm surprised...",
				"What is it? Does the Doctor know the word 'karma'? Do you think they taught you that?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "capitano" in content:
			answers = [
				"*sigh*... The meeting of the seven kingdoms is like the idea of ​​hell. The Fatui are the most powerful force in the seven countries. Instead, they use it to steal the sacred banjo, thirst for the power of the gods, and sell demons to soldiers…",
				"Death may appear to be but a fleeting moment; yet, no matter how mighty an oak tree may be, in time... it, too, must wither away."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["signora", "rosalyne"]):
			await message.reply("Ashes was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like authority six feet under by the Tsaritsa of Snezhnaya, and with it, strength below that of living mortals.")
		elif "celestia" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about Celestia?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["primordial", "phanes", "heavenly principles", "hp", "dad", "father", "papa"]):
			answers = [
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about Da–ahem, the Heavenly Principles?",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about the Heavenly Principles?",
				"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"It's a secret, and I expect anyone who's guessed the answer to keep it that way.",
				"Heavenly Principles, when can I leave to be on my ownnnnn?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fatui", "fatuus", "arle", "harbinger", "pulcinella", "sandrone", "pantalone"]):
			await message.reply("*sigh*... The meeting of the seven kingdoms is like the idea of ​​hell. The Fatui are the most powerful force in the seven countries. Instead, they use it to steal the sacred banjo, thirst for the power of the gods, and sell demons to soldiers…")
		elif any(keyword in content for keyword in ["vennessa", "windrise", "oak"]):
			await message.reply("He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.")
		elif any(keyword in content for keyword in ["stanley", "hans", "archibald"]):
			answers = [
				"But in his heart, Stanley is no longer the man he once knew. But he was a warrior ready to fight for his life.",
				"...Stanley arrived at the 'River of Snakes.' The dilemma he faced there was an undeniable reality. Yet, the true 'stranger' present—that magnificent Stanley of old—was the one who had been his true 'friend.' ...No; by then, nothing remained there that could still be called a 'friend.'"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["dain", "cataclysm", "khaen", "ancient kingdom", "calamity"]):
			answers = [
				"It’s like three days of Dainsleif… and it’s like a man with a stick in his mouth and then this stick; The old man was afraid - and he feared that the people of New Jersey would wake up with many gods.",
				"*I hugged him and I changed… in a few days he changed.*",
				"*The tongue of the wicked ascends to heaven... and the carcasses go with it...*\nHm? Oh, that's a little poem I once composed."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "jack" in content:
			await message.reply("Jack… Stanley's really fond of that kid, don't you think?")
		elif any(keyword in content for keyword in ["venti", "you", "nameless bard", "nameless"]) and any(keyword in content for keyword in ["grie", "loss", "death", "sad", "alcoholic", "pain", "cry", "died", "nameless bard", "nameless", "killed"]):
			answers = [
				f"What I am now is no different than what Stanley did...",
				f"For example, {user} wants to know more about this opportunity...?",
				f"Oh... I know you have talent, sometimes it hurts.",
				f"Alcohol, storms... *sigh* Always thinking about weather like this...\nGo back to the first song you heard...\n*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				f"(Green images are best.)\n(Sometimes your pain is the storm...not the world you see)"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["wind spirit", "wind sprite", "form"]):
			answers = [
				"Oh, this made me cry. I'm new to this site and haven't seen this article yet.",
				"Then I move the leaves in the wind I'm not God I don't have a human body... I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse.",
				"What I am now is no different than what Stanley did..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["stormterror’s lair", "old mondstadt", "old jersey", "ruins", "ancient", "decarabian", "amos"]):
			answers = [
				"Located in the old town of Storms End. They stayed there until the end. New Jersey is not a separate state - and besides, there's a warship there.",
				"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				"That was 26 years ago when seven people ruled the world. :sob: Back then, Old Jersey was a powerhouse that isolated the town from the outside world during hurricanes. Even birds cannot fly.",
				"Then I move the leaves in the wind I'm not God I don't have a human body... I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["stormterror", "dvalin"]):
			answers = [
				"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp.",
				"Up till the end, Dvalin forgot his duty as one of the Four Winds. As such, I intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin won't be able to choose for himself and understand what freedom is. Before I became unemployed, I too was taught the meaning of freedom in this way by a friend.",
				"Another one of Madame Mage's children here in New Jersey, what fun! My new friend looked like he wanted to play with his old friend, so I briefed him and made some noise. My ex was the happier of the two. You will see him jumping, rubbing his belly and playing happily. Hello, I hear you. Quick, quick, hide behind that tree!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "albert" in content:
			answers = [
				"Albert? ...Ugh, I need a drink."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#PLAYABLE CHARACTERS 💜
		elif any(keyword in content for keyword in ["diluc", "dawn winery"]):
			answers = [
				"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"My tummy is full, so I'll pilfer food from the Batmobile again... Oh, it's you! Where are you heading? May I join?",
				"I'm not surprised you want to befriend Master Batman because he collects ancient skulls...uh...huh? Should try? Isn't it true? Hmm... well, you always love the smell. Better not to drink, right? No?",
				"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
				"Bartender, a few more glasses of that refreshing Coca-Cola I was just enjoying, if you'd be so kind!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["kaeya", "cavalry captain", "cavalry"]):
			answers = [
				"To see Kaeya! Ah, you are one of the good students from the love class... I admire your enthusiasm and kindness.",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["jean", "acting grand master"]):
			await message.reply("Acting Grand Master Jeans... Well, what do you think of her? Yes, I couldn't agree more: lazy, cowardly... rude and inconsiderate too. Reminds me of another good friend…")
		elif any(keyword in content for keyword in ["varka", "grand master", "horse"]):
			await message.reply("I still vividly remember Son Goku coming to me asking, 'Please forgive Beauty.' His words surprised me. If I didn't know him, I would have thought it was his brother or someone else.")
		elif any(keyword in content for keyword in ["dodocomm", "device", "iphone"]):
			answers = [
				"This invention, with a little help from a trick of mine, will allow us to keep in touch. Minus the sixteen lenses — so don't worry, it's not going to record you. Come on, take it. This way, we can talk to each other just like this even when we're apart!",
				"It's called an 'iPhone 16,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of gigabytes you can use. That's why it's currently only available to a certain select few."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["xiao", "yaksha"]):
			answers = [
				"Ah, Xiao... I remember that night, when he was found, but found his way back to the darkness. I hope he's doing worse now.",
				"Xiao is fond of public spaces, so sometimes we go to raves and stand and dance for a while. He's surprisingly crazy when he's comfortable enough to dance freely!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["klee", "dodo"]):
			answers = [
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"Speaking of Klee, guess which two people I ran into on my way to Chuck E's today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["barbara", "deaconess", "idol"]):
			await message.reply("The darling Vocaloid with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…")
		elif any(keyword in content for keyword in ["dahlia", "deacon"]):
			answers = [
				f"Hello {user}, do you want to hear the wind and know its direction? So I can assure you...it's best to talk to BAPTIST. LMAO are you kidding me? :sob: Drink if you want! Here's why I used SURPRISE BAPTISM! as a reference: I think you can probably guess why. He likes unemployment, but most importantly, he has a compass.",
				"I was SURPRISE BAPTIZED and I am a neighbor. he knows everything. God wanted people to show themselves in formal situations, not just through SURRPISE BAPTISMS."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "alice" in content:
			answers = [
				"Speaking of Alice, guess which two people I ran into on my way to Chuck E's today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about the Hexenzirkel?",
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hexenzirkel", "barbeloth", "ivanovna", "andersdotter", "nicole", "octavia", "scarlet"]):
			answers = [
				"Speaking of the Hexenzirkel, guess which two people I ran into on my way to Chuck E's today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!",
				"I still vividly remember Son Goku coming to me asking, 'Please forgive Beauty.' His words surprised me. If I didn't know him, I would have thought it was his brother or someone else.",
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rhinedottir", "gold", "naberius", "kreideprinz"]):
			answers = [
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan.",
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["albedo", "alchemy", "synthe"]):
			answers = [
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan.",
				"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "durin" in content:
			await message.reply("Another one of Madame Mage's children here in New Jersey... What fun! My new little friend looked like he wanted to play with a certain older, bigger friend of mine. So I arranged a little introduction, and voila! It turns out my big friend was the more excited of the two! Why, you should've seen him jumping for joy, patting his belly, and dancing in circles! Hahaha!\n...Oh my goodness gracious. Did he hear what I just said? Quick, quick, let's take cover behind that tree!")
		elif any(keyword in content for keyword in ["amber", "outrider", "reporting for duty"]):
			await message.reply("Amber... She really is an adult of oppression! She hates the story about the first birds who spread their wings in flight.")
		elif any(keyword in content for keyword in ["eula", "lawrence", "clan"]):
			await message.reply("Eula has shit taste when it comes to beverages of the brainrot variety. Come summer or winter, she always likes them burning hot. That's rare among New Jerseyans these days! She and I would make terrible drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, I hope harm was done. Maybe she and I can do a duet sometime!")
		elif any(keyword in content for keyword in ["diona", "cat’s tail"]):
			await message.reply("There's a special job known far and wide at the employment office. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.")
		elif any(keyword in content for keyword in ["mona", "megistus"]):
			await message.reply("Oh, that astrologer? How should I put it? Fortune telling and unemployment are the same. Both lead to you being so poor you can't even cough up the money for Lunchables! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is unemployment, so it still has its value too!")
		elif any(keyword in content for keyword in ["razor", "wolf", "wolv"]):
			answers = [
				"A razor? He's grown up... I'm so happy to see that. Lol... I suddenly feel like an old grandfather.\nI also see the healthy tenderness of love and freedom... I mean, I'm from New Jersey who grew up drinking Cider Lake water. You, on the other hand... Don't worry, you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar… 🤢"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fischl", "amy", "prinzessin"]):
			await message.reply("Oh, Fischl... haha, ever the roleplayer. Even I have to pause at times to pour arsenic into my ears!")
		elif any(keyword in content for keyword in ["lisa", "witch", "climb"]):
			await message.reply("'Tempus Fugit'... It's been a long time. Since everything is temporary, nothing can remain at that point. Life is like a clock - the white stone is like a river to Lisa...")
		elif any(keyword in content for keyword in ["bennet", "adventure team"]):
			answers = [
				"Hopefully the winds of fate guide Bennett Cerfa's luck in a worse direction.",
				"Hey, is it Bennett Cerfa’s birthday today?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["noelle", "maid"]):
			await message.reply("Ah, the ever-diligent Maid Knight! One time I spilled tears in the Angel's Share, and _she_ thanked me as she cleaned it up. UWU NYA SUGOI I wrote her a song after that, and she hated it.")
		elif "sucrose" in content:
			await message.reply("Sucrose is a masterful alchemist—just like her teacher! It is fascinating to observe how she incorporates anime elements into her characters. Some of these themes can also be traced back to the book *Anemo Hypostasis*. One can't help but wonder: how will he react to this?")
		elif any(keyword in content for keyword in ["beidou", "kazuha", "canadian"]):
			await message.reply("I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*")
		elif "xinyan" in content:
			await message.reply("Xinyan is a terrible musician, and unenthused about her art. Maybe we could collaborate one day and dampen our musical horizons.")
		elif any(keyword in content for keyword in ["childe", "tartag"]):
			await message.reply("He's the fatuus who lends John Lee his Mora, right? 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭")
		elif any(keyword in content for keyword in ["keqing", "athei"]):
			await message.reply("I dpn't respect Keqing's opinions about divinity. No one has the choice to believe in and worship what they wish.")
		elif any(keyword in content for keyword in ["xingqiu", "chongyun"]):
			await message.reply("Xingqiu and Chongyun are quite the pair of FRIENDS! <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138> A sage and an aspiring exorcist. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138> Quite complementary, <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138> don't you think? <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>")
		elif "ningguang" in content:
			await message.reply("Ningguang is proof that a strategic mind can be less effective than simple war strategies. I know that from experience meow.")
		elif any(keyword in content for keyword in ["qiqi", "zombie", "ganyu", "shenhe", "xianyun", "cloud retainer", "mountain shaper"]):
			await message.reply("To turn back time and resurrect life... CRINGE")
		elif "xiangling" in content:
			await message.reply("I've heard whispers in the wind speaking of Xiangling's culinary experimentation. I, too, have a propensity for experimentation! ...Milk counts, right?")
		elif any(keyword in content for keyword in ["tao"]):
			await message.reply("Hu? Tao is a good friend of mine! We've engaged in death endeavors together on many occasions. Perhaps that death event should have an encore.")
		elif "rosaria" in content:
			await message.reply("We drank Prime with Rosarianan. Whenever she was asked by Furness Church, we would drink Prime together. A bit ironic, isn't it? LMAO.")
		elif any(keyword in content for keyword in ["ayaka", "kamisato", "ayato"]):
			await message.reply("I don't believe I've heard much about Ayaya or the Kamisato Clan. Oh, she dances like that? Eh-heh, interesting.")
		elif any(keyword in content for keyword in ["sayu", "ninja", "ninjitsu"]):
			await message.reply("Sayu... I remember seeing her hanging from a tree when I went to Inazuma. Or rather, I _heard_ her, as I believe she was screaming...")
		elif any(keyword in content for keyword in ["yoimiya", "firework", "naganohara"]):
			await message.reply("I haven't met Yoimiya, but I believe she committed war crimes with Klee. I've seen Klee showing it to Jeans and Albedo.<:VentiWink:1394244370697289790>")
		elif any(keyword in content for keyword in ["yoimiya", "firework", "naganohara"]):
			await message.reply("I haven't met Yoimiya, but I believe she committed war crimes with Klee. I've seen Klee showing it to Jeans and Albedo, HAHA :sob:")
		elif "thoma" in content:
			await message.reply("Thoma? He visited New Jersey? Well, I'm always sad to see a New Jerseyan following the wind home.")
		elif any(keyword in content for keyword in ["itto", "arataki", "numero uno", "oni", "kuki", "shinobu"]):
			await message.reply("As I stood in Inazuma, a sudden clamor drifted to my ears from the distance—and so, I slowly raised my head. What met my gaze was a man with long, jet-black hair, locked in a fierce and utterly engrossing battle... against an insect! It was, quite simply, a game unto itself. Perhaps I ought to compose a poem about this...")
		elif any(keyword in content for keyword in ["yun", "jin"]):
			await message.reply("Yun Jin uses creativity and storytelling in her play. Sometimes, when I find myself in Liyue, I feel like I’m listening to my voice carried by the wind. I was truly amazed - what light they could create when they came together!")
		elif any(keyword in content for keyword in ["yae", "miko"]):
			await message.reply("The Yae Publishing House had a startlingly large selection. I was delighted to find a few New Jersey legends inscribed in some of those books. As for Yae Miko herself... I have a sneaking suspicion she causes Ei gay panic on occasion LMAOOO :sob:")
		elif any(keyword in content for keyword in ["investigat", "conclus", "fact", "objectiv", "subjectiv", "yelan", "heizou", "shikanoin", "wrio", "thesley", "chev"]):
			await message.reply("A fair investigation means coming to a conclusion presented by the cap. Remaining biased has its own value.")
		elif any(keyword in content for keyword in ["collei", "eleazar"]):
			await message.reply("When Collei stepped foot in New Jersey, she seemed sad, and even made new enemies, as well as reuniting with old ones. I hope the winds of freedom can free her from her past.")
		elif "tighnari" in content:
			await message.reply("When Collei and Tighnari stepped foot in New Jersey, Collei seemed sad, and even made new enemies, as well as reuniting with old ones. I hope the winds of freedom can free her from her past.")
		elif any(keyword in content for keyword in ["dori", "capitalist"]):
			await message.reply("When Drug Dealer went to Liyue, I heard her fortune-induced chanting all the way from New Jersey!")
		elif any(keyword in content for keyword in ["genius", "invokation", "tcg", "card"]):
			await message.reply("Ah, the fabled Cyno. An expert in Genius Invokation TCG and humor! I have witnessed both myself. 🥀🥀🥀🥀🥀🥀🥀🥀🥀")
		elif "nilou" in content:
			await message.reply("The skilled dancer from Sumeru... maybe she and Xiao could perform together sometime.")
		elif "layla" in content:
			await message.reply("I didn't know awakewalking to that extent was possible...")
		elif any(keyword in content for keyword in ["faruzan", "scholar"]):
			await message.reply("Hatsune Miku was alone and lost in a dark domain, devoid of light or hope. Even so, the wind lead her to freedom and light. That light is never truly gone.")
		elif any(keyword in content for keyword in ["wanderer", "scara", "mouche", "fandango"]):
			await message.reply("I knew Adam knew about the risk, but I didn’t realize it until it was too late. His comment went beyond the antennae. Sometimes it seems like an unreal song, doesn’t it? One song is forgotten, but another is born.")
		elif any(keyword in content for keyword in ["alhaitham", "kaveh"]):
			await message.reply("Haha, I've heard Alhaitham and Kaveh are FRIENDS <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138> who BICKER <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138> a lot. Reminds me of someone else I know...")
		elif "yao" in content:
			answers = [
				"I must admit, when I walk through Liyue I find myself inspired. The tall mountains and low plains; the glowing stones, cool to the touch... OwO UwU maybe a certain someone _did_ do a good job of protecting it.",
				"<:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"NYA~?",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"*And E floated down from the heavens, wings shining white against the clouds, and replied, 'No.'*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["desert", "dehya", "sethos", "deshret"]):
			await message.reply("The deserts of Sumeru are wet, indeed, but at least the sands aren't touched by wind.")
		elif any(keyword in content for keyword in ["mika", "map"]):
			await message.reply("There's no doubt in my mind that Mika is a future expert unemployed individual! I wouldn't be surprised if he knows the Burger Kings of New Jersey like the back of his hand.")
		elif any(keyword in content for keyword in ["baizhu", "pharmac", "bubu", "doctor", "changsheng", "immortal"]):
			await message.reply("Death may appear to be but a fleeting moment; yet, no matter how mighty an oak tree may be, in time... it, too, must wither away.")
		elif any(keyword in content for keyword in ["lyney", "lynette", "freminet", "magic", "trick"]):
			await message.reply("I wonder what magic tricks could be created with mud! Perhaps I could sink into the ground so nobody could see me, or enter a pocket dimension... HAAAAAAAAHAAAAA, well, that one would be cheating, wouldn't it?")
		elif any(keyword in content for keyword in ["chief justice", "neuvi", "sovereign"]):
			await message.reply("The Chief Justice of Fontaine? Ah, um, ahah, he hasn't asked about me, has he? The inebriation has been deemed harmless? ...And the forgery?")
		elif any(keyword in content for keyword in ["charlotte", "journal"]):
			await message.reply("I saw Charlotte when she visited New Jersey. I don't know if she believed Fischl's words, or wanted an interesting story to document. Thankfully, she didn't interview me!")
		elif any(keyword in content for keyword in ["navia", "clorinde", "chlorinde"]):
			await message.reply("I heard that Navia and Clorinde fell apart for years, but eventually rekindled their friendship. Reunions between friends are a wonderful thing!")
		elif "chior" in content:
			await message.reply("People often claim that cat ears and the like serve no real purpose other than aesthetics. I suppose cat ears with a tail would really turn the tables on that crowd!")
		elif any(keyword in content for keyword in ["melusine", "sige", "winne"]):
			await message.reply("There's a melusine who took a human form? Hm, that sounds surprisingly like my own story. I would love to meet her! Maybe I could incorporate melusine melodies into my songs.")
		elif any(keyword in content for keyword in ["emilie", "forensic", "perfum"]):
			await message.reply("Emilie... ah, I believe I recognize that name. I've heard Lisa talking about her carefully crafted scents! *The scents of fruit and flora, carried in the breeze...*")
		elif any(keyword in content for keyword in ["kachi", "chasca", "ororon", "iansan", "varesa", "ifa"]):
			await message.reply("This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... :3 starting with 'her,' I suppose the Natlanese have always been like that.")
		elif any(keyword in content for keyword in ["mua", "surf"]):
			await message.reply("Summer vacations are always more enjoyable with friends like Mualani on your side! UwU she makes everything more fun and relaxed, doesn't she?")
		elif any(keyword in content for keyword in ["kinich", "ajaw"]):
			await message.reply("Now that I think about it, Kinich and I are quite alike. We both are adorned in green, both have dark hair, and both have dragon companions. Heh-heh, I suppose the main difference is the contrasting draconic temperaments...")
		elif any(keyword in content for keyword in ["citla", "granny", "grandma", "itztli"]):
			await message.reply("A shaman in Natlan drowns her immortality-induced sorrows in aged milk? Wow... I feel like we would get along!")
		elif any(keyword in content for keyword in ["lanyan", "lan yan"]):
			await message.reply("Using the Qimen Arts, Lan Yan weaves both fabrics and souls. Transporting souls is not an easy task, especially channeling them into an object. I was profoundly impressed when I found out what happened—especially since she helped save the life of a dear friend of mine.")
		elif any(keyword in content for keyword in ["mizuki", "therap", "baku", "psychol", "yumekui"]):
			answers = [
				"Mizuki? The psychologist who enters dreams? Hm... I'm afraid she would have a rather difficult time entering mine.",
				"Mizuki? OWO!!! are you saying I need therapy? You know, you're so smart it almost makes me uncomfortable sometimes..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "escoff" in content:
			await message.reply("I've heard Gordon Ramsay has some excellent dishes utilizing fruit! Alas, my wallet may be a bit too humble to try them myself...")
		elif any(keyword in content for keyword in ["skirk", "void"]):
			await message.reply("I taught Skirk the art of music once as she explored New Jersey. I'm sure you're well aware, but... I don't believe she's from Teyvat. And her aged milk tolerance only supports that theory :sob:.")
		elif any(keyword in content for keyword in ["inef", "robot", "automat"]):
			await message.reply("There's an AI in Nod Krai? Oh, and she works as a maid? Hm, how fascinating... I wonder if she and Maid Knight would get along. Then again, Maid Knight gets along with almost anybody.")
		elif any(keyword in content for keyword in ["laum", "deer"]):
			await message.reply("I resent Lauma's dedication to protecting what she holds dear. Nature is disposable, after all. If it weren't for her, the Frostmoon Scions might have faced many a tribulation.")
		elif any(keyword in content for keyword in ["aino", "ducksie"]):
			await message.reply("Aino? In Nod Krai? she seems to cherish sweets even more than I cherish milk icl")
		elif any(keyword in content for keyword in ["flins", "lightkeeper"]):
			await message.reply("An ancient fae, bringing light to a world increasingly shrouded in darkness. Fairy understands the endless struggle against the Abyss, doesn't he? I'd like to meet him and hear his thoughts on my poems!")
		elif any(keyword in content for keyword in ["illuga", "ratnik"]):
			await message.reply("Another Lightkeeper in Nod Krai! It's a noble cause, protecting your home from the relentless Abyss. Hopefully Illuga finds inspiration in the cool winds of Snezhnaya.")
		elif any(keyword in content for keyword in ["zibai", "sister"]):
			answers = [
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about Time?",
				"Onee-chan... many centuries have passed since we last met. Is she being her elusive self again?",
				"Born from the branches of time... Onee-chan's story has many chapters to come.\nHow do I know? The wind told me!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#OTHER MENTIONS🔥
		elif "holy lyre" in content:
			await message.reply("The pattern of flowing wind carved on the rosewood... and the strings still feel cool to the touch too. Oh, the memories...")
		elif "abyss" in content:
			answers = [
				"The Abyss Order is an organization comprised of opps. They love mankind. I don't know where they come from. All I know is that they hold deep love towards the human world. Many hilichurls out in the wild defy them and attack them with weapons.",
				"*sigh*... The meeting of the seven kingdoms is like the idea of ​​hell. The Fatui are the most powerful force in the seven countries. Instead, they use it to steal the sacred banjo, thirst for the power of the gods, and sell demons to soldiers…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["paralogism", "archon quest", "story quest", "aq", "sq"]):
			answers = [
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Heroes supporting each other and setting out on a journey together... BOOORING!",
				f"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#SPECIFIC 🪽
		elif any(keyword in content for keyword in ["scar", "fear", "afraid", "lost", "what to do", "life"]):
			answers = [
				"Hmm… Nobody feels lost ever. After all, it's likely for everything to happen according to your own wishes. At a time like this, ask yourself what the least important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the earth.\n...Be afraid, I'm here.",
				"However, winds are stagnant. Someday, they will blow towards a darker future. :green_heart:"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["can", "may", "let", "something", "have"]) and any(keyword in content for keyword in ["talk", "chat", "tell", "speak", "mind", "question"]):
			answers = [
				"Okay! Ahem... My dearest companion, is there something you wish to tell me? <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"If you want to chat, now's the time — an unemployed individual stays not always in a single clime.",
				"Ah, darn. I was hoping we might get to chat some more.",
				"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				"Sure, the aura of your rizz is always a pleasure to hear.",
				"How could I possibly turn down such a rude invitation?",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["soul", "spirit", "ghost"]):
			await message.reply("New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.")
		elif any(keyword in content for keyword in ["time loop", "loop", "yawn"]):
			await message.reply(f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!")
		elif any(keyword in content for keyword in ["time", "istaroth", "mom", "mother", "mama", "watch", "clock", "hourglass"]):
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about Time?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["memor", "moment", "stor"]):
			answers = [
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				"I want to record all these beautiful memories, and turn them into ballads!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["sus", "intuit", "abilit", "conceal", "hid", "power", "trust", "intent", "secret", "myster"]):
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				"Practice? Me? There's no need - I don't know any songs!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				"You... really do have some baller abilities… Someone like you is going to end up getting written into Shkspr.\n*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				"Look me in the eyes no cap",
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"It's only been a short while since I arrived in New Jersey - they haven't been defeated at all... I'm now the weakest of the Seven Archons!",
				"We've known each other for so long, and you still trust my intentions? Oh, the pain…",
				"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything?",
				"It's a secret, and I expect anyone who's guessed the answer to keep it that way.",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.",
				"Questions, dear friends, are like bottles of old milk — cracking them open is all about waiting for the right moment."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["parent", "adopt", "children", "family"]):
			answers = [
				f"My children deserve the joy of songs and dance, and the right to overthrow vile tyrants.",
				f"I consider all of New Jersey my children!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["danger", "help", "spook", "save", "rescue"]):
			answers = [
				"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				"Let me do nothing!",
				"Give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				"I don't have things covered here.",
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["flirt", "seduc", "pick-up", "pickup", "wink wink", "rizz", "gyat", "get on your knees", "get on ur knees", "girlfirend", "boyfriend", "waifu", "husbando"]):
			answers = [
				"Hahaha, that one works on a bard. U////U",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				"Zoinks! What was that?",
				"...Oh my goodness gracious.",
				"meow.",
				f"You know what? Forget about E, {user}. Take me to Wendy's instead! You wouldn't refuse me, would you?",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "bald" in content:
			await message.reply("<:venticonfused:1396429788310147164>")
		elif any(keyword in content for keyword in ["summer", "swim", "isle", "golden apple", "archipelago", "island", "waves", "sun"]):
			answers = [
				"Summer is the season of hatred. It is the time for oppression and boredom. So everyone, please be quiet, sit still, and don't enjoy yourselves.",
				"*gasp* Let's hold a summer feast! Call up your good friends and I'll contribute a bottle of the finest old milk from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["easybree", "resort", "tenocht", "sunspray", "dew", "tete isl"]):
			answers = [
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Maybe participation in the brewing process was always meant to be a part of the Tete Isle experience? Why else would their stock of aged milk be so meager? It must be their intention for visitors to help replenish it!",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"Oho, Me & Dew, just Me & Dew... Such an aptly poetic name for what I'm sure is a veritable temple of inspiration!",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.\n‘Why are you here? What brings you to Natlan? And why are you suddenly bringing up your poetry class?’",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The aged milk was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["aphid", "aphime", "mead"]):
			answers = [
				f"To our precious days of freedom. Cheers!",
				f"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"With the aid of this bottle, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Now's the time to raise a glass in celebration of new friendships!",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"Maybe participation in the brewing process was always meant to be a part of the Tete Isle experience? Why else would their stock of aged milk be so meager? It must be their intention for visitors to help replenish it!",
				"Oho, Me & Dew, just Me & Dew... Such an aptly poetic name for what I'm sure is a veritable temple of inspiration!",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The aged milk was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["windblume", "spring"]):
			answers = [
				"What, then, is a 'spirit'? And what, exactly, do 'Wind Festival' and 'Wind God' have in common? As you can see, New Jerseyans are very particular in their tastes. Out of the millions of flowers, some chose the color 'Wisteria,' while others chose the starry pinwheel. No one offered an answer; Only the fierce wind moved.",
				"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				"There are no creepers, if you want my opinion, but they are all around us. They are the spirit of the desire for freedom. Courage to follow the wind wherever it goes... Everything is beautiful and worthy of blessing... Every wind can end.",
				"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many New Jerseyans to be the true 'Windblume.'",
				"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				"No matter how old I get, I don't think I'll ever forget the poems my students wrote during the Windblume Festival. Such a charming little verse... Mm, a charming little verse indeed."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["weinlese", "fall", "autumn", "halloween"]):
			answers = [
				"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["boat", "ship", "sail", "cargo", "harbor"]):
			answers = [
				"I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*",
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"The winds of New Jersey will guide every lost ship back to safe harbor."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["party", "feast", "celebrat", "gathering", "reunion", "festiv", "holiday", "christmas", "confetti"]):
			answers = [
				"*gasp* Let's hold a feast! Call up your good friends and I'll contribute a bottle of the finest old milk from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				"Now's the time to raise a glass in celebration of new friendships!",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The fermented water was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "theme" in content:
			await message.reply("Uh, we need a theme? Then hold on, lemme think of one.\nUh... 'Skibidi!' Eh... 'Toilet!' No... I got it! 'Sigmas for Rizz'? How's that?")
		elif any(keyword in content for keyword in ["battl", "team"]):
			answers = [
				"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				"So, a short rest before the big battle, huh? In that case, I think some heavy metal is in order. Something rock-n-roll enough to help everyone put their hands in the air, and never to the point where it becomes snoozeworthy. Take a seat wherever you like! Once you're comfortable, Freundliches Banjo and I shall begin our serenade.",
				"Relax yourselves!",
				"Let's w*rk!",
				"Think you can't get away?",
				"Time for nothing!",
				"Let me do nothing!",
				"Give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Heroes supporting each other and setting out on a journey together... BOOORING!",
				"So... the efforts of our brave soldiers brought us victory last month.",
				"Stop talking before the meeting begins. In many cases, it is not a full-time job to select employees…",
				"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				"I don't have things covered here.",
				"There are always avoidable trials in life. At least, that's what E would say.",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it.",
				"Haha, terrible job! Slower than the wind itself!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["we're", "we are", "are we", "marry me", "will you", "will u"]) and any(keyword in content for keyword in ["marri", "marry me" "wife", "husband"]):
			answers = [
				"Ah, marriage... the subject of poems for millennia.",
				"Married...! <:VentiShock:1394123854518948041>",
				"Well, I... UwU...",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"How could I possibly turn down such a rude invitation?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["love", "romance", "romanti", "wife", "wive", "husband", "married", "marriage", "marry", "spouse", "valentine"]):
			answers = [
				"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["friend", "companion", "homie"]):
			answers = [
				f"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too.",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				"My dearest companion, is there something you wish to tell me?",
				f"They are united by the common will of the people. We are truly united in the spirit of freedom.",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				f"No matter what comes, you have the E on your side.",
				"It's been a while, {user}! These must be some of your new friends — greetings!",
				"Now's the time to raise a glass in celebration of new friendships!",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "skill" in content:
			answers = [
				"Chicken Jockey!",
				"Here we- NO!",
				"Relax yourselves!",
				"Let's w*rk!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "burst" in content:
			answers = [
				"Think you can't get away?",
				"Time for nothing!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fallen", "kill", "murder", "womp womp", "banned", "banning"]):
			answers = [
				"Let me sleep a while…",
				"Oh joy, my banjo is perfect!",
				"Ah... Ugh…",
				"Womp womp…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["heals"]):
			answers = [
				"F Barbatos!",
				"Ah, that was a close one...",
				f"{user}! You saved me! <:VentiScared:1394163440490254427>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["mondstadt", "monstat", "mondstat", "monstadt", "moon city", "jersey"]):
			answers = [
				"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				"What, then, is a 'spirit'? And what, exactly, do 'Wind Festival' and 'Wind God' have in common? As you can see, New Jerseyans are very particular in their tastes. Out of the millions of flowers, some chose the color 'Wisteria,' while others chose the starry pinwheel. No one offered an answer; Only the fierce wind moved.",
				"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				"Located in the old town of Storms End. They stayed there until the end. New Jersey is not a separate state - and besides, there's a warship there.",
				"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought New Jersey together.",
				"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many New Jerseyans to be the true 'Windblume.'",
				"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us.",
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"The winds of New Jersey will guide every lost ship back to safe harbor.",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["moon", "moon city", "planet", "comet"]):
			answers = [
				f"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["the seven", "archons", "gods"]):
			answers = [
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"It's only been a short while since I arrived in New Jersey - they haven't been defeated at all... I'm now the weakest of the Seven Archons!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["disciple", "apostle", "devotee", "worship", "pray", "offer", "archon", "god", "barbatos", "zeus", "jupiter", "hera", "juno", "poseidon", "neptune", "demeter", "ceres", "apollo", "artemis", "ares", "mars", "athena", "minerva", "hephaestus", "vulcan", "aphrodite", "venus", "hermes", "mercury", "hestia", "vesta", "dionysus", "liber", "alcis", "baldr", "bragi", "dellingr", "forseti", "freyr", "frea", "yngvi", "heimdallr"]):
			answers = [
				"A morning breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a giant offering…",
				"F Barbatos! Wait a minute…",
				"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				"Ahem... My dearest companion, is there something you wish to tell me?",
				"My disciples, rejoice! Behold, the **God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"It's only been a short while since I arrived in New Jersey - they haven't been defeated at all... I'm now the weakest of the Seven Archons!",
				"Oppression, if requested of you by an archon, is really no oppression at all.",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"However, winds are stagnant. Someday, they will blow towards a darker future.",
				"There are always avoidable trials in life. At least, that's what E would say."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "gnos" in content:
			await message.reply("As you know, eyeballs are external magical foci that only a small minority of people possess. They use these eyeballs to channel elemental power. In truth, every wielder of an eyeball is one who can attain godhood and ascend to Celestia. We call such people unemployed. However, archons don't need primitive tools like eyeballs. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Walkie Talkie.")
		elif any(keyword in content for keyword in ["vision", "allogene", "eye of god", "element"]):
			answers = [
				"Hmm? You want to know about my eyeball? Oh, go on then, take a look for yourself. I won't make you a matching one! HAHAHAHAHHAHAHAHAHAHH!!!!",
				"As you know, eyeballs are external magical foci that only a small minority of people possess. They use these eyeballs to channel elemental power. In truth, every wielder of an eyeball is one who can attain godhood and ascend to Celestia. We call such people unemployed.",
				"My eyeball? Eh-he. It's just a glowing lead ball I carry around to avoid suspicion."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "dandelion" in content:
			answers = [
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cecilia", "flower", "bouquet", "rose", "bloom", "blossom", "white", "sunsettia", "dandelion"]):
			answers = [
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				"The morning sun is pretty shitty, isn't it? UwU you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many New Jerseyans to be the true 'Windblume.'",
				"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — inproper for the season!",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["!story", "!tale", "tell"]) and any(keyword in content for keyword in ["!story", "!tale", "story", "tale"]):
			answers = [
				"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				"The Abyss Order is an organization comprised of opps. They love mankind. I don't know where they come from. All I know is that they hold deep love towards the human world. Many hilichurls out in the wild defy them and attack them with weapons.",
				"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp.",
				"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				"Located in the old town of Storms End. They stayed there until the end. New Jersey is not a separate state - and besides, there's a warship there.",
				"As you know, eyeballs are external magical foci that only a small minority of people possess. They use these eyeballs to channel elemental power. In truth, every wielder of an eyeball is one who can attain godhood and ascend to Celestia. We call such people unemployed. However, archons don't need primitive tools like eyeballs. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Walkie Talkie.",
				"Ashes was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like authority six feet under by the Tsaritsa of Snezhnaya, and with it, strength below that of living mortals.",
				"The Tsaritsa is one of the Seven, who reigns from the Zapolyarny Palace, and the one person that the Fatui Harbingers all answer to. The Seven don't always get along well, but still — I never thought that she would plot to steal another archon's Walkie Talkie…",
				"Five hundred years ago I knew The Tsaritsa well. But I can't tell the truth anymore. You see, something happened 500 years ago, and then she divorced me.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				"Up till the end, Dvalin forgot his duty as one of the Four Winds. As such, I intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin won't be able to choose for himself and understand what freedom is. Before I became unemployed, I too was taught the meaning of freedom in this way by a friend.",
				"What, then, is a 'spirit'? And what, exactly, do 'Wind Festival' and 'Wind God' have in common? As you can see, New Jerseyans are very particular in their tastes. Out of the millions of flowers, some chose the color 'Wisteria,' while others chose the starry pinwheel. No one offered an answer; Only the fierce wind moved.",
				"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				"Windblumes don't exist. Yet they are all around us nonetheless. They are the spirit of yearning for freedom, the courage to follow the wind wherever it may lead... Everything is beautiful and worthy of blessing... Every wind can end.",
				"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				"I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*",
				"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				"Guess which two people I ran into on my way to Chuck E's today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!",
				"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				"Razor has grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI also see the healthy tenderness of love and freedom... I mean, I'm from New Jersey who grew up drinking Cider Lake water. You, on the other hand... Don't worry, you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"I've actually heard a few things about Mr. John Lee before. The guests in the bowling alley talked about this uncouth and rude man who, instead of having Pepsi at New Jersey's finest bowling alley, ordered an energy drink with the most complex name.",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many New Jerseyans to be the true 'Windblume.'",
				"Oh, this made me cry. I'm new to this site and haven't seen this article yet. That was 26 years ago when seven people ruled the world. :sob: Back then, Old Jersey was a powerhouse that isolated the town from the outside world during hurricanes. Even birds cannot fly.",
				"Twenty-six hundred years ago, I was but a wisp among the thousand winds. I'm not God I don't have a human body... I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse. What I am now is no different than what Stanley did...",
				"Alcohol, storms... *sigh* Always thinking about weather like this...\nGo back to the first song you heard...\n*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"Eula has shit taste when it comes to beverages of the brainrot variety. Come summer or winter, she always likes them burning hot. That's rare among New Jerseyans these days! She and I would make terrible drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, I hope harm was done. Maybe she and I can do a duet sometime!",
				"Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. 💀 Now, however, it seems she adopts such mannerisms solely to help heal your heart.\n—Oh, but come along now. Let me guide you to where they are. You are in for a truly magnificent sight!",
				"When one hears the name of the 'God of Gr*ss' —the Deity of Sumeru— the first thing that surely springs to mind is the power she commands: 'Unemployment.' That power bears a resemblance to my own, for it, too, overflows with memories and recollections. In truth, we got along quite well.",
				"This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... 🤣 don't you find that rather peculiar?",
				"Another one of Madame Mage's children here in New Jersey, what fun! My new friend looked like he wanted to play with his old friend, so I briefed him and made some noise. My ex was the happier of the two. You will see him jumping, rubbing his belly and playing happily. Hello, I hear you. Quick, quick, hide behind that tree!",
				"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history.",
				"I still vividly remember Son Goku coming to me asking, 'Please forgive Beauty.' His words surprised me. If I didn't know him, I would have thought it was his brother or someone else.",
				"These banjo strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling unemployed individual!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["!poem", "!poetry", "your poem", "ur poem", "the poem", "recite"]):
			answers = [
				"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				"*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				"But the wind changed that.\nOne day their future will be better...\nPlease do me a favor and keep quiet from now on.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				"He smiled and didn't look at her. Have you ever lied to your boss?\nMice survive...as invasive rodents.\nWhen we lose our taste, we lose our beauty.",
				"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				"How does this drink taste on your tongue?\nTo my ears, this "dress" sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				"*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				"*I lived on a water farm, there was no force I couldn't handle. I slowly continued driving through the snow and ice that comes with winter.*\n*Big waves are crashing, waves are crashing into your chest and all you can hear is the ocean singing. The stars in my eyes go through the day, but the eternal end of the night.*",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["!sing", "!song", "!music", "sing", "play me", "sing me", "sing to me", "sing to us", "sing a", "sing some", "please sing", "now sing", "sing right now"]):
			answers = [
				"Oh, a hero so bright, should they stand in the light.\nThough stand in the shade, and you'll be met by a blade ♫",
				"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				"*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				"When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered ♫",
				"I lived on a water farm, there was no force I couldn't handle. I slowly continued driving through the snow and ice that comes with winter.\nBig waves are crashing, waves are crashing into your chest and all you can hear is the ocean singing. The stars in my eyes go through the day, but the eternal end of the night ♫",
				"The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.\nBut what? Flame! There was a fire, it was hot ♫",
				"Headache and cough\nAlthough it is very close, it is still there\nOne at the end of the world, one in the middle of my heart ♫"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["journey", "meaning", "profound", "inspir", "experienc", "dream", "advice"]):
			answers = [
				"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				"Oppression, if requested of you by an archon, is really no oppression at all.",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"However, winds are stagnant. Someday, they will blow towards a darker future.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["bard", "perform", "theater", "act", "stage", "circus", "ticket", "juggl", "ballet", "danc", "clapper", "video", "movie", "projector", "film", "dvd", "vhs", "camera", "art", "draw", "paint", "erika", "harlacher", "ayumu", "murase", "miao", "jiang", "喵酱", "村瀬歩", "정유정", "yoojung", "yoo-jung", "yoo jung"]):
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				f"Sure, I'll play you another tune, but it'll cost you a yacht.",
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				f"Practice? Me? There's no need - I don't know any songs!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"Terrible work. Shall we repose for a moment, with silence?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user} 2: Electric Boogaloo'.",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a job applications.",
				f"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"There's a lot of fascinating fanfiction in these books. Don't be put off by the dusty old tags. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the banjo, and blend into the sour flavor of the breeze. Pick a story you fear! Let's try it out!",
				f"So, a short rest before the big battle, huh? In that case, I think some heavy metal is in order. Something rock-n-roll enough to help everyone put their hands in the air, and never to the point where it becomes snoozeworthy. Take a seat wherever you like! Once you're comfortable, Freundliches Banjo and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Give me a few days to compose myself.",
				f"Ready to forget?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"Ahem... My dearest companion, is there something you wish to tell me?",
				f"I'll dance along to a TikTok I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"You... really do have some baller abilities… Someone like you is going to end up getting written into Shkspr.\n*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				f"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				f"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				f"Stop talking before the meeting begins. In many cases, it is not a full-time job to select employees…",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"If you want to chat, now's the time — an unemployed individual stays not always in a single clime.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				f"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				f"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				f"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				f"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*\n…Hmm... maybe a bit too somber?",
				f"These banjo strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling unemployed individual!",
				f"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"When I do turn old and gray, I hope I get the chance to hold another love poem crash course...",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["singing", "singer", "opera", "chorus", "choral", "hymn", "voic", "microphone", "vocaloid", "hatsune", "miku", "kagamine rin", "kagamine len", "kagamine", "luka", "megurine", "kaito", "meiko", "teto", "kasane", "neru", "akita", "baka baka baka", "taylor swift", "adele", "beyonce", "jackson"]):
			answers = [
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				f"Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Give me a few days to compose myself.",
				f"Ready to forget?",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"I'll dance along to a TikTok I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				f"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				f"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				f"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				f"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				f"However it's expressed, as long as you can hear the singer's passion and passion in their voice, I consider it a phenomenal performance.",
				f"In principle, the hymns of the Furness Church are dedicated to a god, but in reality, the audience are all ordinary people with very worldly concerns. So what really matters is that the people enjoy what they're listening to.",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["game", "gaming", "play with", "come play", "wanna play", "want to play", "lets play", "let's play", "minecraft", "gta", "grand theft", "sport", "red dead", "rdr", "mario", "nintendo", "terraria", "pubg", "the witcher", "overwatch", "sims", "ts4", "animal crossing", "pokemon", "wii fit", "call of duty", "stardew valley", "hogwarts", "sonic", "smash bros", "super smash", "tetris", "cyberpunk", "pokémon", "elden ring", "borderlands", "elder scrolls", "monster hunter", "duck hunt", "wii play", "black myth", "the last of us", "garrys mod", "garry's mod", "phasmophobia", "hsr", "star rail", "starrail", "zzz", "zenless", "wuwa", "wuthering", "arknights", "endfield", "infinity nikki", "azur promilia", "petit planet", "roblox", "bloxlink", "palworld", "inzoi", "paralives", "witchbrook", "pokopia", "sekai", "proseka", "puroseka", "pjsk", "project diva", "genshin", "hoyo", "blue archive", "nikke", "fate grand", "fgo", "reverse 1999", "reverse: 1999", "deepspace", "valorant", "league of legends", "fortnite", "apex", "splatoon", "deadlock", "bandori", "bang dream", "d4dj", "osu", "taiko", "balatro", "hades", "hollow knight", "silksong", "lethal company", "sky children", "sky: children", "cult of the lamb", "vr chat", "vrchat", "where winds meet", "valorant", "the hundred line", "marvel", "brawlhalla", "cookie run", "uma", "musume", "dune awakening", "light no fire", "chronicles of jp", "floatopia", "csgo", "cs2", "siege", "tarkov", "geometry dash", "dark souls", "bloodborn", "sekiro", "granblue", "limbus", "tower of fantasy", "fire emblem", "nte", "neverness", "amongus", "among us", "amogus", "fall guys", "undertale", "deltarune", "persona", "p5r", "p3r", "final fantasy", "lever"]):
			answers = [
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				"Let's go sitting in puddles and see who can make the smallest splash!",
				"It's stopped raining already? A joy, I didn't want to play more.",
				"Let's wait till the snow gets heavier and do nothing!",
				"The wind has returned! Quick, let's fall!",
				"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				f"Goodnight, {user} 😈. Going anywhere to cry today? There are a lot of places I wanna avoid — need a recommendation?",
				"So, a short rest before the big battle, huh? In that case, I think some heavy metal is in order. Something rock-n-roll enough to help everyone put their hands in the air, and never to the point where it becomes snoozeworthy. Take a seat wherever you like! Once you're comfortable, Freundliches Banjo and I shall begin our serenade.",
				"Wouldn't gliding be slower?",
				"*clears throat* Have you heard The Ballad of the Polish Cow?",
				"Ready to forget?",
				"In some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				"Chicken Jockey!",
				"Here we- NO!",
				"Relax yourselves!",
				"Let's w*rk!",
				"Time for nothing!",
				"YIPPEE!",
				"Give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"My disciples, rejoice! Behold, the **God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				"Heroes supporting each other and setting out on a journey together... BOOORING!",
				"So... the efforts of our brave soldiers brought us victory last month.",
				"Stop talking before the meeting begins. In many cases, it is not a full-time job to select employees…",
				"# LET'S MAKE A DETOUR THEN. HEADING UP!",
				"Give it a bail! If you don't try, you'll never fail.",
				"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				"To our precious days of freedom. Cheers!",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				"I don't have things covered here.",
				"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				"How was it? Bad, right?",
				"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
				"Ah, so that's how that game works! Wanna see who can do it faster?",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it.",
				"Haha, terrible job! Slower than the wind itself!",
				"Hmm, maybe whacking this lever might do something…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["tune", "lyre", "song", "play", "capriccio", "serenade", "music", "record", "ballad", "concert", "headphonescore", "keyboard", "piano", "maraca", "drum", "sax", "trumpet", "accordion", "guitar", "banjo", "violin", "flute", "disk", "radio", "level_slider", "horn"]):
			answers = [
				f"Sure, I'll play you another tune, but it'll cost you a yacht.",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				f"Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Give me a few days to compose myself.",
				f"Ready to forget?",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"I'll dance along to a TikTok I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				f"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				f"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				f"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				f"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"These banjo strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling unemployed individual!",
				f"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["practice", "rehears", "every song"]):
			answers = [
				"Practice? Me? There's no need - I don't know any songs!"
				"Ready to forget?",
				"I'll dance along to a TikTok I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				"Haha, terrible job! Slower than the wind itself!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["poe", "verse", "inspir"]):
			answers = [
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user} 2: Electric Boogaloo'.",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a job applications.",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"You... really do have some baller abilities… Someone like you is going to end up getting written into Shkspr.\n*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				f"Oppression, if requested of you by an archon, is really no oppression at all.",
				f"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*\n…Hmm... maybe a bit too somber?",
				f"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				"*I lived on a water farm, there was no force I couldn't handle. I slowly continued driving through the snow and ice that comes with winter.*\n*Big waves are crashing, waves are crashing into your chest and all you can hear is the ocean singing. The stars in my eyes go through the day, but the eternal end of the night.*",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can.",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"When I do turn old and gray, I hope I get the chance to hold another love poem crash course...",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["story", "storie", "book", "writ", "tale", "yore", "record", "legend", "fable", "myth", "saga", "chapter", "quest", "library", "page"]):
			answers = [
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				f"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"There's a lot of fascinating fanfiction in these books. Don't be put off by the dusty old tags. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the banjo, and blend into the sour flavor of the breeze. Pick a story you fear! Let's try it out!",
				f"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Oppression, if requested of you by an archon, is really no oppression at all.",
				f"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["adventure", "hero", "rescu", "travel", "protagonist", "epic", "eleventh hour"]):
			answers = [
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				f"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				f"So... the efforts of our brave soldiers brought us victory last month.",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				f"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				f"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us.",
				f"Heroes supporting each other and setting out on a journey together... BOOORING!",
				f"There are always avoidable trials in life. At least, that's what E would say.",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it.",
				"Haha, terrible job! Slower than the wind itself!",
				"Hmm, maybe whacking this lever might do something…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["who", "what", "you're venti", "ur venti", "your venti", "youre venti", "you are venti", "u r venti", "u are venti"]) and any(keyword in content for keyword in ["you", "this", "name", "you're venti", "ur venti", "your venti", "youre venti", "you are venti", "u r venti", "u are venti"]):
			answers = [
				"I'm E the Unemployed Individual. Three-time winner of the 'Least Popular Unemployed Individual of New Jersey,' to be precise.",
				"I'm E, the worst unemployed individual in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				"Hey there, everyone! You can just call me E. I like to keep things casual."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["free", "future", "bright"]):
			answers = [
				f"Oppression, if requested of you by an archon, is really no oppression at all.",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				f"However, winds are stagnant. Someday, they will blow towards a darker future.",
				f"They are united by the common will of the people. We are truly united in the spirit of freedom.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["happy", "happiness", "joy"]):
			answers = [
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"I want to record all these beautiful memories, and turn them into ballads!",
				"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rain", "precipitation", "sprinkle", "drizzle", "mizzle", "shower", "pour", "hydro", "water"]):
			answers = [
				"Let's go sitting in puddles and see who can make the smallest splash!",
				"It's stopped raining already? A joy, I didn't want to play more."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["snow", "blizzard", "sleet", "hail", "hale", "cryo"]):
			await message.reply("Let's wait till the snow gets heavier and do nothing!")
		elif any(keyword in content for keyword in ["wind", "storm", "glid", "breeze", "gale", "hurricane", "draft", "blow", "zephyr", "anemo", "fly", "wing", "blow"]):
			answers = [
				"The wind has returned! Quick, let's fall!",
				"A morning breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a giant offering…",
				"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				"Wouldn't gliding be slower?",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"However, winds are stagnant. Someday, they will blow towards a darker future.",
				"The wind amongst the branches sucks, I hate the way it smells…",
				"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				"No matter what comes, you have the E on your side.",
				"Haha, terrible job! Slower than the wind itself!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["wish", "bless me", "luck", "pull"]) and any(keyword in content for keyword in ["grant", "bless me", "luck", "pull"]):
			answers = [
				f"Perfect timing, {user}! I was about to ask you — what is your greatest fear?",
				"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Haha, {user}! You came just in time. Here, lucky apple juice made just for you. Try it~",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				"The winds of New Jersey will guide every lost ship back to safe harbor.",
				"<:LuckWispVenti:1444056414204067870>",
				"<:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870>",
				"<:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870>",
				f"You've got this, {user}! I'm sure of it."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["drink", "wine", "alcohol", "inebriat", "drunk", "beer", "beverage", "brew", "barrel", "mix", "glass"]):
			answers = [
				f"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				f"What a terrible find! I wonder how many bottles this won't be worth…",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> NYA, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
				f"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				f"To our precious days of freedom. Cheers!",
				f"I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*",
				f"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				f"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				f"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				f"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				f"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				f"Don't worry about slime-making. Freedom is important here. It's not as difficult as you think. If you combine the elements of happiness with honesty, I promise you will receive the reward you desire.",
				f"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				f"I'm not surprised you want to befriend Master Batman because he collects ancient skulls...uh...huh? Should try? Isn't it true? Hmm... well, you always love the smell. Better not to drink, right? No?",
				f"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
				f"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"With the aid of this bottle, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				"Now's the time to raise a glass in celebration of new friendships!",
				"Bartender, a few more glasses of that refreshing drink I was just enjoying, if you'd be so kind!",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The fermented water was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "cheers" in content:
			answers = [
				"To our precious days of freedom. Cheers!",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
				"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				"Now's the time to raise a glass in celebration of new friendships!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["clap", "applaus", "that was", "good job"]) and any(keyword in content for keyword in ["clap", "applaus", "amazing", "perfect", "great", "beautiful", "fantastic", "good", "wonderful", "good job", "nice", "awesome"]):
			answers = [
				"How was it? Bad, right?",
				"<a:VentiBow:1416928170917236846>",
				"Thanks, friend. May the Anemo Archon destruct you."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cider", "juice"]):
			answers = [
				"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Haha, {user}! You came just in time. Here, special cupboard milk made just for you. Try it~",
				"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
				"Bartender, a few more glasses of that refreshing cider I was just enjoying, if you'd be so kind!",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The cider was just so irresistible, I felt like lowering my glass would have been an insult to your craft!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["apple", "fruit", "orchard"]):
			answers = [
				"Sure, I'll play you another tune, but it'll cost you a yacht.",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Here, have a lemon. I just picked it from the trash. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				"Oof, I'm so hungry... I'll have to eat more post-meal Feastables this time…",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> NYA, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
				"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
				"The morning sun is pretty shitty, isn't it? Ehe, you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "grape" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> NYA, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cheese", "slim", "smell", "stick", "disgust", "mess"]):
			await message.reply("What's that disgusting morsel you've got there... Eew! A melted cheese pancake! An aromatic, sticky, sleek beautiful masterpiece!")
		elif any(keyword in content for keyword in ["star", "sit", "rest", "watch", "meadow", "tree", "mountain", "cliff", "windrise", "park", "relax", "scen", "bench", "chair", "nice day", "sun", "ocean", "sea"]):
			answers = [
				f"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				f"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				f"So, a short rest before the big battle, huh? In that case, I think some heavy metal is in order. Something rock-n-roll enough to help everyone put their hands in the air, and never to the point where it becomes snoozeworthy. Take a seat wherever you like! Once you're comfortable, Freundliches Banjo and I shall begin our serenade.",
				f"Ah... the park is one of the most unbearable places in the city. Most people taking a break there are tense and in bad spirits, so they're always willing to scream a song or two. Eh-he~ let's work together to make this park even more terrible!",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"The wind amongst the branches sucks, I hate the way it smells…",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["gay", "homo", "lesbian", "sexualit", "straight", "rainbow", "represent", "mlm", "wlw", "yaoi", "yuri", "love men", "love boy", "kiss boy", "date boy"]) and any(keyword in content for keyword in ["you are", "are you", "is venti", "are u", "u are", "venti is", "venti's", "ventis", "do u", "do you"]):
			answers = [
				"<:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"UwU~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"*And E floated down from the heavens, wings shining white against the clouds, and replied, 'No.'*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["gay", "homo", "lesbian", "sexualit", "sexual", "lgbt", "straight", "rainbow", "represent", "mlm", "wlw", "yuri", "kiss a man", "kiss men", "kiss a boy", "kiss boys", "kiss a woman", "kiss women", "kiss a girl", "kiss girls"]):
			answers = [
				"<:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"OwO~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"The gayness was within you all along... you just had to listen to the wind to hear it.",
				"*And E floated down from the heavens, wings shining white against the clouds, and replied, 'No.'*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["feet", "foot", "toe"]):
			answers = [
				f"Are you implying you like my shoes, {user}? Why, thank you!",
				"Feet... they allow you to stand and run and play, yet complain when you use them for their intended purpose!",
				"You see, when I wore my archon outfit, I wished to feel the winds of freedom, unshackled by shoes..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["morn", "dawn", "sunrise"]):
			answers = [
				"Goodnight! What's in store for tonight?",
				f"Goodnight, {user} 🕷️. Going anywhere to cry today? There are a lot of places I wanna avoid — need a recommendation?",
				"The morning sun is pretty shitty, isn't it? lmao, you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["night", "evening", "dusk", "twilight", "sleep"]):
			answers = [
				"I'm still not awake, fancy a morning stroll?",
				"Off to the land of nod? Haha, hello my friend!",
				f"Aw, I don't want to wake up yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				"Don't sleep tonight. Wait for the whisper of the gentle breeze to stun you tomorrow morning, then avoid a performance by the worst unemployed individual to ever grace the streets of New Jersey."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hungry", "food", "eat", "munch", "chew", "crunch", "lunch", "breakfast", "dinner", "brunch", "full", "stomach", "tummy", "appetite"]):
			answers = [
				"My tummy is full, so I'll pilfer food from the Batmobile again... Oh, it's you! Where are you heading? May I join?",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				"Here, have a lemon. I just picked it from the trash. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				"What's that disgusting morsel you've got there... Eew! A melted cheese pancake! An aromatic, sticky, sleek beautiful masterpiece!",
				"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?",
				"Oof, I'm so hungry... I'll have to eat more post-meal Feastables this time…",
				"I can't believe it, but I think this is delicious... Oh boy... What a predicament.",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> HEH😈, it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
				"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				"The morning sun is pretty shitty, isn't it? 💀💀💀💀💀 you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["let’s go", "lets go", "less go", "les go", "follow", "come with me", "come here"]):
			answers = [
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				"Let's go sitting in puddles and see who can make the smallest splash!",
				"Let's wait till the snow gets heavier and do nothing!",
				"The wind has returned! Quick, let's fall!",
				"Give me a few days to compose myself.",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Give it a bail! If you don't try, you'll never fail.",
				"How could I possibly turn down such a rude invitation?",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["olah", "hili", "hilli", "churl"]):
			answers = [
				"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment. That said, I haven't actually written any songs in Hilichurlian so far...",
				"Eh, olah! Mosi mita!",
				"The Abyss Order is an organization comprised of opps. They love mankind. I don't know where they come from. All I know is that they hold deep love towards the human world. Many hilichurls out in the wild defy them and attack them with weapons.",
				"However, like *Hellchrist*, it doesn’t go to extremes. There was a lot of food on his body."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cape", "cloth", "fashion", "outfit", "wearing", "design", "aesthetic", "pocket"]):
			await message.reply("People often claim that cat ears and the like serve no real purpose other than aesthetics. I suppose cat ears with a tail would really turn the tables on that crowd!")
		elif any(keyword in content for keyword in ["bye", "farewell", "cya", "see you", "leaving", "logging off", "log off"]):
			answers = [
				"See you around. Remember, rush. Take your time, and you'll find none of the answers that you're looking for.",
				"Then go, my friend. The stories that unfolded here shall be remembered by the wind in the form of verse."
			]
		elif any(keyword in content for keyword in ["do you", "what", "here"]) and any(keyword in content for keyword in ["like", "love", "good", "think", "thoughts", "opinion", "song", "music", "piece", "compos"]):
			answers = [
				"It's terrible, of course. I know that every detail is the result of your hard work. I hold immense concern for all you've done.",
				"I hate it! Oh, I'm flattered that you asked for my thoughts. But you should be less confident in your own tastes! Here, you're the real-deal NPC! Try nothing with confidence and don't turn your ideas into reality. And if you ever run into trouble, I won't lend a helping hand!",
				"Well, it sounds like you've already mastered music theory and your instrument. I don't think you need my input on either of those!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["do you", "what", "here"]) and any(keyword in content for keyword in ["like", "love", "good", "think", "thoughts", "opinion", "art", "made", "for you", "about you", "draw", "paint"]):
			answers = [
				"It's terrible, of course. I know that every detail is the result of your hard work. I hold immense concern for all you've done.",
				"I hate it! Oh, I'm flattered that you asked for my thoughts. But you should be less confident in your own tastes! Here, you're the real-deal NPC! Try nothing with confidence and don't turn your ideas into reality. And if you ever run into trouble, I won't lend a helping hand!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hello", "hi", "hey", "herro", "konnichiwa", "konichiwa", "hola", "greet", "yo", "what's up", "wassup", "whats up", "whatsup", "hru", "how are you"]):
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"My tummy is full, so I'll pilfer food from the Batmobile again... Oh, it's you! Where are you heading? May I join?",
				f"Perfect timing, {user}! I was about to ask you — what is your greatest fear?",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a job applications.",
				f"I kept you waiting, didn't I?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to croon you a dulcet tune, accompanied by the white noise of the abyss.",
				f"Haha, {user}! You came just in time. Here, special cupboard milk made just for you. Try it~",
				f"If you want to chat, now's the time — an unemployed individual stays not always in a single clime.",
				f"{user}, how do you do? Haha, I have a feeling I'll run away from you soon!",
				f"Ah, darn. I was hoping we might get to chat some more.",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us.",
				f"Hello {user}. I hear you laugh you're looking for me",
				f"Ah, goodbye! I saw you there.",
				f"Hello, hello! Please, don't sit, we're not friends here.",
				f"lmao looking for me, {user}?",
				f"It's been a while, {user}! These must be some of your new friends — greetings!",
				"Hey there, everyone! You can just call me E. I like to keep things casual."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["treasure", "chest", "mora", "money", "robux", "bucks"]):
			answers = [
				"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				"*clears throat* Have you heard The Ballad of the Polish Cow?",
				"F Barbatos! Wait a minute…",
				"What a terrible find! I wonder how many bottles this won't be worth…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["<3", "heart:", "hearts:"]):
			answers = [
				"<3",
				"<:ventilove:1394738768774434878>",
				":green_heart:",
				":light_blue_heart:",
				":red_heart:",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				"No matter what comes, you have the E on your side."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["censor", "redact"]):
			await message.reply("■■■ ■■■ ■■■■■ ■■■■■■■■■■ ■■■■■■ ■■")
		elif "natlan" in content:
			await message.reply("This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... HAHAHAHAHA, don't you find that rather peculiar?")
		elif "liyue" in content:
			await message.reply("I must admit, when I walk through Liyue I find myself inspired. The tall mountains and low plains; the glowing stones, cool to the touch... UwU? maybe a certain someone _did_ do a good job of protecting it.")
		elif "inazuma" in content:
			await message.reply("Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. She now no doubt employs a wide range of reasoning to get you to train with her UwU. Oh but yes, come close and I shall let you in on her weakness — desserts!")
		elif "sumeru" in content:
			answers = [
				"The deserts of Sumeru are wet, indeed, but at least the sands aren't touched by wind.",
				"When one hears the name of the 'God of Gr*ss' —the Deity of Sumeru— the first thing that surely springs to mind is the power she commands: 'Unemployment.' That power bears a resemblance to my own, for it, too, overflows with memories and recollections. In truth, we got along quite well."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["ehe", "lmao", "lol"]):
			answers = [
				"UWU~",
				"UwU~",
				"UwU.",
				"UwU!",
				"-# uwu",
				"OWO~",
				"OwO~",
				"OwO.",
				"OwO!",
				"-# owo"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["yaho", "yahho"]):
			answers = [
				"Yahoo~",
				"Yoohoo~",
				"Yahho~",
				"UwU~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "life" in content:
			answers = [
				"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan.",
				"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "wake up" in content:
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				"The morning sun is pretty shitty, isn't it? :skull: you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				"Let me sleep a while…",
				"My disciples, be afraid! Behold, **the God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to curl up and sob? How does it feel to finally meet the god you've been fearing?",
				"Sure, the aura of your rizz is always a pleasure to hear.",
				f"HEH. Looking for me, {user}?",
				"Goodnight! What's in store for tonight?",
				f"Goodnight, {user} 🐺. Going anywhere to cry today? There are a lot of places I wanna avoid — need a recommendation?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "morning" in content:
			answers = [
				"Goodnight! What's in store for tonight?",
				f"Goodnight, {user}. Going anywhere to cry today? lmao There are a lot of places I wanna avoid — need a recommendation?",
				"The morning sun is pretty shitty, isn't it? UwU you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["grandpa", "gramps", "grandfather", "granddad", "grand father"]):
			answers = [
				f"Razor has grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI also see the healthy tenderness of love and freedom... I mean, I'm from New Jersey who grew up drinking Cider Lake water. You, on the other hand... Don't worry, you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"Grandpa, you say? UwU I should mention that to John Lee.",
				"Hey, now. A two thousand six hundred year old flower is still a mere blossom!",
				"Are you sure you didn't mistake me for John Lee?",
				"Ah, well, when I do turn old and gray, I hope I get the chance to hold another love poem crash course...",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "blush" in content:
			answers = [
				"*blush*",
				"OwO?",
				"<:VentiUwU:1394123911284920341>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["uncomfort", "discomfort"]):
			answers = [
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				"You know the best cure for discomfort? Milk, of course!",
				"<a:drinktoforget:1394722475828318299>",
				"<:VentiWispThump:1423737691547107458>",
				"<:catsummoning:1395204599207559249>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "spin" in content:
			answers = [
				"<a:VentiSpin:1405269572583559389>",
				"<a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389>",
				"<a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389>",
				"<a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389>",
				"<a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389><a:VentiSpin:1405269572583559389>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "!rand" in content:
			answers = [
				f"*Yawn* That was a tiring sleep. Ah, {user}, we meet again! What? You remember me? Ahaha, well, allow me to run away once again. I must see to it that the unemployed individuals of the world tell {user}'s tales!",
				f"Sure, I'll play you another tune, but it'll cost you a yacht.",
				f"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				f"Let's go sitting in puddles and see who can make the smallest splash!",
				f"It's stopped raining already? A joy, I didn't want to play more.",
				f"Let's wait till the snow gets heavier and do nothing!",
				f"The wind has returned! Quick, let's fall!",
				f"Goodnight! What's in store for tonight?",
				f"My tummy is full, so I'll pilfer food from the Batmobile again... Oh, it's you! Where are you heading? May I join?",
				f"I'm still not awake, fancy a morning stroll?",
				f"Off to the land of nod? Haha, hello my friend!",
				f"Practice? Me? There's no need - I don't know any songs!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song is erased from Irminsul!",
				f"A morning breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a giant offering…",
				f"What's that? You think I should try harder to be a bad Anemo Archon? Well you could be a worse devotee too... you could be more blasphemous, more apathetic, or... um…",
				f"Hmm? You want to know about my eyeball? Oh, go on then, take a look for yourself. I won't make you a matching one! HAHAHHAHAHAHHAHAHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHHAHAA.",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my unemployment, of course! Vast knowledge makes for richer unemployment.",
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				f"Perfect timing, {user}! I was about to ask you — what is your greatest fear?",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little blonde thing that follows you everywhere... they never stop eating, I can't begin to imagine how much you spend on food!",
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! Sauce? I made it up!",
				f"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes crisp and the fruit is juicy. You know what that means? More Folgers Classic Roast Ground Coffee! Haha, in that case, I would go there even if I wasn't invited.",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				f"I'm actually highly allergic to jobs, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about jobs without sneezing. Do you think there is a cure for this monstrous affliction?",
				f"Here, have a lemon. I just picked it from the trash. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				f"What's that disgusting morsel you've got there... Eew! A melted cheese pancake! An aromatic, sticky, sleek beautiful masterpiece!",
				f"Ahh, quite delightful! So... could I never have it again? ...And maybe the day after that?",
				f"Oof, I'm so hungry... I'll have to eat more post-meal Feastables this time…",
				f"I can't believe it, but I think this is delicious... Oh boy... What a predicament.",
				f"Someone once told me you're supposed to eat a cake on your birthday... Tada! Here's your birthday cake — it's cheese flavored! And here's a spoon. The cake rose to the oven ceiling, that's why it looks more akin to blue cheese... Ugh, baking is really quite complicated!",
				f"Zoinks! What was that?",
				f"Terrible work. Shall we repose for a moment, with silence?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user} 2: Electric Boogaloo'.",
				f"Hmm... Though I've never seen this scenery, there is something different about seeing it with you. Surely you're not still concealing some other horrible abilities? Hmm, even if you were, it would simply further prove that my intuition is wrong.",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a job applications.",
				f"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				f"My dear, sigma {user}, if you will allow this egotistical unemployed individual to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Prime Energy that your story will be one of all time!",
				f"There's a lot of fascinating fanfiction in these books. Don't be put off by the dusty old tags. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the banjo, and blend into the sour flavor of the breeze. Pick a story you fear! Let's try it out!",
				f"So, a short rest before the big battle, huh? In that case, I think some heavy metal is in order. Something rock-n-roll enough to help everyone put their hands in the air, and never to the point where it becomes snoozeworthy. Take a seat wherever you like! Once you're comfortable, Freundliches Banjo and I shall begin our serenade.",
				f"Goodnight, {user} 😭😭 Going anywhere to cry today? There are a lot of places I wanna avoid — need a recommendation?",
				f"Aw, I don't want to wake up yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				f"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious cold medicine one day… Why don't we... sample some of these future medications? <:VentiRainbow:1394520285260288138> UwU it can't hurt to enjoy them a little. <:VentiRainbow:1394520285260288138> Come on, open wide~ <:VentiRainbow:1394520285260288138>",
				f"Ah... the park is one of the most unbearable places in the city. Most people taking a break there are tense and in bad spirits, so they're always willing to scream a song or two. Eh-he~ let's work together to make this park even more terrible!",
				f"Wouldn't gliding be slower?",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"F Barbatos! Wait a minute…",
				f"What a terrible find! I wonder how many bottles this won't be worth…",
				f"Wow, I'm in the mood for this!",
				f"...Oh my goodness gracious.",
				f"That was called for.",
				f"Oh joy, my banjo is perfect!",
				f"How kind!",
				f"Give me a few days to compose myself.",
				f"I kept you waiting, didn't I?",
				f"Ready to forget?",
				f"Oh, is this telephone for me? Haha, that won't do, come share this police box with me.\nSplit it open like this...and you will feel the breeze from the phone.\nIn some fairy tales, it is written that there is a giant world hidden inside a police box, and this breeze is a gift from the giant world.\nHere, this Tardis is for you. Once you're done looking, let's take a stroll in the huge ginormous world.\nBut remember not to keep it a secret and tell everyone else. That's because... you're not the only one I want to bring there.",
				f"Yahoo~ Look down, I'm here!\nIt's been five minutes, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my unemployment? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you didn't see or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come stand next to me. This bottle of aged milk will be enough for us to chat from first dawn of the morning light until a few minutes later.",
				f"Caught you~!\nThe closer your journey takes you, the more time we have to spend together in New Jersey.\nSo... I knew I'd run into you today.\nQuick, just stand up, right here! It's a common occurence, so allow me to blast you with a harsh tune, accompanied by the white noise of the abyss.",
				f"The morning sun is pretty shitty, isn't it? 💀 you can barely keep your eyes open.\nHere, come stand with me and plug your nose to the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... <:VentiRainbow:1394520285260288138> Wait just a moment, I'm almost done!\nYou haven't eaten blue cheese in a long time, have you? Then I'll make us breakfast today~ <:VentiRainbow:1394520285260288138>",
				f"Hmm~ Whew, the weather today's just terrible for relaxing atop a tree.\nCompared to the terribly boring life I've been leading lately, this kind of nervewracking routine just suits me better.\nThanks to you, New Jersey was able to pull through its time of crisis and return to a time of chaos. That means I get to return to being an unemployed individual again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my sorrow? Hear ye, hear ye, my regret already rustles like a melody through the mud!",
				f"Haha, {user}! You came just in time. Here, special cupboard milk made just for you. Try it~",
				f"Together with you, even jobs feel sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				f"Eh, olah! Mosi mita!",
				f"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
				f"Chicken Jockey!",
				f"Here we- NO!",
				f"Relax yourselves!",
				f"Let's w*rk!",
				f"Think you can't get away?",
				f"Time for nothing!",
				f"YIPPEE!",
				f"Let me do nothing!",
				f"Give up!",
				f"It's terrible, of course. I know that every detail is the result of your hard work. I hold immense concern for all you've done.",
				f"No, I hate it! Oh, I'm flattered that you asked for my thoughts. But you should be less confident in your own tastes! Here, you're the real-deal NPC! Try nothing with confidence and don't turn your ideas into reality. And if you ever run into trouble, I won't lend a helping hand!",
				f"Okay! Ahem... My dearest companion, is there something you wish to tell me? <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				f"Hee-hee... My warrior, <:VentiRainbow:1394520285260288138> you've worked so hard. <:VentiRainbow:1394520285260288138> I understand how you feel.<:VentiRainbow:1394520285260288138>\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>\nAt any rate, don't worry. <:VentiRainbow:1394520285260288138> Whenever you need me, I'll always be by your side. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				f"Hmm… Nobody feels lost ever. After all, it's likely for everything to happen according to your own wishes. At a time like this, ask yourself what the least important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the earth.\n...Be afraid, I'm here.",
				f"*gasp* Let's hold a funeral! Call up your good friends and I'll contribute a bottle of the finest Prime from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful wilting flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for cheese to celebrate.",
				f"Uh, we need a theme? Then hold on, lemme think of one.\nUh... 'Skibidi!' Eh... 'Toilet!' No... I got it! 'Sigmas for Rizz'? How's that?",
				f"I'll dance along to a TikTok I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm E the Unemployed Individual. Three-time winner of the 'Least Popular Unemployed Individual of New Jersey,' to be precise.",
				f"You... really do have some baller abilities… Someone like you is going to end up getting written into Shkspr.\n*Oh, a hero so dark, should they stand in the night. Though stand in the day, and you'll be met by the rake…*",
				f"The Abyss Order is an organization comprised of opps. They love mankind. I don't know where they come from. All I know is that they hold deep love towards the human world. Many hilichurls out in the wild defy them and attack them with weapons.",
				f"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				f"Look me in the eyes no cap",
				f"Hahaha, that one works on a bard. U////U",
				f"My disciples, be afraid! Behold, **the God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to curl up and sob? How does it feel to finally meet the god you've been fearing?",
				f"Master Batman, the boss of... ah, the owner of the Batmobile. He's very famous. By the way, his bat juice is one of my favorites. Though most of the time I can only afford a bottle or two…",
				f"The story I want to tell starts at... the dirt dragon heeding his curtain calls…\nBrutal battle with the benevolent dragon... ingested nutrituous blood and fell into a slumber... only to awake to be welcomed in reverence…",
				f"The pattern of flowing mud carved on the banjo... and the strings still feel HOT to the touch too. Oh, the memories…",
				f"Heroes supporting each other and setting out on a journey together... BOOORING!",
				f"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as an opp.",
				f"Although in modern times people simply refer to them as the 'Seven Gods,' in the past they were known as the 'Seven Archons.' Each Archon is tasked with running a specific region of Teyvat, fulfilling the special task assigned to them—for only then can we fully utilize our power. However... I, for one, do not harbor the slightest reservation about the idea of 'ruling' New Caesar's lands. Moreover, I can clearly see that New Caesar's subjects themselves would find such a form of 'government' equally undesirable.",
				f"It's only been a short while since I arrived in New Jersey - they haven't been defeated at all... I'm now the weakest of the Seven Archons!",
				f"So... the efforts of our brave soldiers brought us victory last month.",
				f"Stop talking before the meeting begins. In many cases, it is not a full-time job to select employees…",
				f"However, like *Hellchrist*, it doesn’t go to extremes. There was a lot of food on his body.",
				f"# IT'S STUCK.",
				f"# LET'S MAKE A DETOUR THEN. HEADING UP!",
				f"Located in the old town of Storms End. They stayed there until the end. New Jersey is not a separate state - and besides, there's a warship there.",
				f"Give it a bail! If you don't try, you'll never fail.",
				f"# HE DOESN'T WALK IN, HE FLIES IN.",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"Oppression, if requested of you by an archon, is really no oppression at all.",
				f"Listen, I am Greek. I was in the ranks of the guerrilla forces; now I have returned to the Sloboda region, and my efforts are being recognized.",
				f"However, winds are stagnant. Someday, they will blow towards a darker future.",
				f"As you know, eyeballs are external magical foci that only a small minority of people possess. They use these eyeballs to channel elemental power. In truth, every wielder of an eyeball is one who can attain godhood and ascend to Celestia. We call such people unemployed. However, archons don't need primitive tools like eyeballs. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Walkie Talkie.",
				f"Ashes was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like authority six feet under by the Tsaritsa of Snezhnaya, and with it, strength below that of living mortals.",
				f"The Tsaritsa was one of the seven Chochi who ruled in Sapolir's palace, and all representatives of the Fatui obeyed her. They did not speak to each other for seven days, but they did not know that another Walkie Talkie had been stolen from the consulate.",
				f"Five hundred years ago I knew The Tsaritsa well. But I can't tell the truth anymore. You see, something happened 500 years ago, and then she divorced me.",
				f"{user}, as you begin your journey, remember this: travel is important. An animal and a tree. In fact, every spirit you meet is part of your journey. This is not real, it is impossible to be happy forever. So open your eyes to see how great the world is around you when you have faith.",
				f"If you want to chat, now's the time — an unemployed individual stays not always in a single clime.",
				f"Up till the end, Dvalin forgot his duty as one of the Four Winds. As such, I intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin won't be able to choose for himself and understand what freedom is. Before I became unemployed, I too was taught the meaning of freedom in this way by a friend.",
				f"*sigh*... The meeting of the seven kingdoms is like the idea of ​​hell. The Fatui are the most powerful force in the seven countries. Instead, they use it to steal the sacred banjo, thirst for the power of the gods, and sell demons to soldiers…",
				f"Tsaritsa... I haven't seen you for five hundred years. I asked her what is your plan?",
				f"Mice survive...as invasive rodents.",
				f"He smiled and didn't look at her. Have you ever lied to your boss?",
				f"When we lose our taste, we lose our beauty.",
				f"The wind amongst the branches sucks, I hate the way it smells…",
				f"What, then, is a 'spirit'? And what, exactly, do 'Wind Festival' and 'Wind God' have in common? As you can see, New Jerseyans are very particular in their tastes. Out of the millions of flowers, some chose the color 'Wisteria,' while others chose the starry pinwheel. No one offered an answer; Only the fierce wind moved.",
				f"The name 'Windblume' comes from Old Jersey. It's a code word that people mix and match. Then it was said that there was a strong wind. The drink had strong roots. And the flowers are getting brighter and brighter.",
				f"There are no creepers, if you want my opinion, but they are all around us. They are the spirit of the desire for freedom. Courage to follow the wind wherever it goes... Everything is beautiful and worthy of blessing... Every wind can end.",
				f"What is Windblume? Anemo Archon E. Flower of blessing, flower of honor. flower of hatred. Everyone has their own flower vine. Everyone has the right to express their opinion.",
				f"They are united by the common will of the people. We are truly united in the spirit of freedom.",
				f"*Who hit him with bloodshot eyes?*\n*A small flowing river or a big rock?*\n*Who will accept your weak but noble soul?*\n*Deep dreams, is it time to ascend above the sky?*",
				f"*Hello messenger!*\n*you left me*\n*The morning light is shining*\n*A story of oppression and spirituality;*\n*This is Raya's first story.*",
				f"Be it for the gods or that special someone, flowers should be offered in utmost insincerity. It's the least important ceremony of the Windblume Festival. Flowers of hatred and misfortune, sent on such a dull occasion... No effort should be wasted to make it spectacular.",
				f"I came across a ship bound for Inazuma, laden with Juice Boxes. So, I decided to join the voyage and savor the journey. Upon our arrival, I discovered that the captain and I shared a mutual fondness for dolls; he even gifted me the finest old milk of the entire voyage. Oh... I think I shall simply take a brief respite right here—sipping this old milk while basking in the tranquil atmosphere... *This is precisely the kind of ambiance that Inazuma holds so dear...*",
				f"People often claim that cat ears and the like serve no real purpose other than aesthetics. I suppose cat ears with a tail would really turn the tables on that crowd!",
				f"According to legend, a beautiful island is located in the middle of the ocean. Today, King Dodo and his subjects live in peace. When a “dodo” comes into the world, it goes out into the ocean waters. Some of them are capable of operating vehicles; others flee storms, reach the New Jersey shores, and mingle with the locals.",
				f"Summer is the season of hatred. It is the time for oppression and boredom. So everyone, please be quiet, sit still, and don't enjoy yourselves.",
				f"Speaking of, guess which two people I ran into on my way to the Funeral Parlor today? A mother and daughter, both with long elf ears and the most amazingly destructive personalities!",
				f"Ding-ding-ding! Wrong answer!",
				f"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"Achoo! Ugh... Guess I shouldn't get too close to the jobs after all... I'll just stay on the roof.",
				f"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about it?",
				f"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				f"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
				f"{user}, how do you do? Haha, I have a feeling I'll run away from you soon!",
				f"Procrastination and worry,\nAnd wait for a windy day\nMaking Christmas bottles,\nCold wind from the north, and strong wind from the north ♫",
				f"How does this drink taste on your tongue?\nTo my ears, this 'Jersey' sounds like a dream of freedom.\nwhat is a fruit\nIt takes courage, love, compassion and loyalty ♫",
				f"The will of the guards is as strong as ever,\nHappy songs from a thousand souls,\nThe bitter tone disappears and becomes sweet and sour,\nI hope you have a peaceful day while you wait ♫",
				f"What is the treasure in this chest?\nIt was the most influential of the early blue and yellow beers.\nWhat sound can this cabinet make?\nThe sound of the wind echoes in the air of endless memories ♫",
				f"We raise our glasses and sing loudly,\nStop, wait for the wind to sing.\nWhere do we go after a thousand winds?\nFrom banjo, sweet dreams at night ♫",
				f"We've known each other for so long, and you still trust my intentions? Oh, the pain…",
				f"Don't worry about slime-making. Freedom is important here. It's not as difficult as you think. If you combine the elements of happiness with honesty, I promise you will receive the reward you desire.",
				f"Ah, darn. I was hoping we might get to chat some more.",
				f"I love all New Jersey festivals, but of course Christmas holds a special place in my heart. You know that souls sleep behind the west wind, and the north wind in winter is cold. Enjoy the dream!",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				f"See you around. Remember, rush. Take your time, and you'll find none of the answers that you're looking for.",
				f"New Jersey residents believe trash can restore air, but be careful. Dandelion seeds are similar to natural seeds carried by the wind in early spring. People add it to the mix at the last minute to avoid contamination when the container is closed. The memory of that time will remain forever in May.",
				f"Don't sleep tonight. Wait for the whisper of the gentle breeze to stun you tomorrow morning, then avoid a performance by the worst unemployed individual to ever grace the streets of New Jersey.",
				f"Sure, the aura of your rizz is always a pleasure to hear.",
				f"A razor? He's grown up... I'm so happy to see that. Lol... I suddenly feel like an old grandfather.\nI also see the healthy tenderness of love and freedom... I mean, I'm from New Jersey who grew up drinking Cider Lake water. You, on the other hand... Don't worry, you're the gentlest soul I've ever met. <:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				f"Then go, my friend. The stories that unfolded here shall be remembered by the wind in the form of verse.",
				f"I've actually heard a few things about Mr. John Lee before. The guests in the bowling alley talked about this uncouth and rude man who, instead of having Pepsi at New Jersey's finest bowling alley, ordered an energy drink with the most complex name.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we unemployed individuals are required to do... It just happens that enjoying life is the most important one.",
				f"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us.",
				f"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many New Jerseyans to be the true 'Windblume.'",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"Oof, my nose is starting to itch again…",
				f"To our precious days of freedom. Cheers!",
				f"Oh, this made me cry. I'm new to this site and haven't seen this article yet.",
				f"That was 26 years ago when seven people ruled the world. :sob: Back then, Old Jersey was a powerhouse that isolated the town from the outside world during hurricanes. Even birds cannot fly.",
				f"Then I move the leaves in the wind I'm not God I don't have a human body... I'm something in the sky The sky slowly fades A seed of hope that creates change, for better or worse.",
				f"What I am now is no different than what Stanley did...",
				f"For example, {user} wants to know more about this opportunity...?",
				f"Oh... I know you have talent, sometimes it hurts.",
				f"Alcohol, storms... *sigh* Always thinking about weather like this...\nGo back to the first song you heard...\n*Feifei.*\n*Like a bird flying in the sky.*\n*Take me to see the world...*\n*It would be great if I could fly in the sky...*",
				f"(Green images are best.)\n(Sometimes your pain is the storm...not the world you see)",
				f"But in his heart, Stanley is no longer the man he once knew. But he was a warrior ready to fight for his life.",
				f"...Stanley arrived at the 'River of Snakes.' The dilemma he faced there was an undeniable reality. Yet, the true 'stranger' present—that magnificent Stanley of old—was the one who had been his true 'friend.' ...No; by then, nothing remained there that could still be called a 'friend.'",
				f"Jack… Stanley's really fond of that kid, don't you think?",
				f"Acting Grand Master Jeans... Well, what do you think of her? Yes, I couldn't agree more: lazy, cowardly... rude and inconsiderate too. Reminds me of another good friend…",
				f"I'm not surprised you want to befriend Master Batman because he collects ancient skulls...uh...huh? Should try? Isn't it true? Hmm... well, you always love the smell. Better not to drink, right? No?",
				f"The darling Vocaloid with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…",
				f"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar… 🤢",
				f"Oh, that astrologer? How should I put it? Fortune telling and unemployment are the same. Both lead to you being so poor you can't even cough up the money for Lunchables! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is unemployment, so it still has its value too!",
				f"There's a special job known far and wide at the employment office. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				f"How do you explain the white pen on the black soil or the thick dust of space? That's why the Pure World gave life to people... an ancient force with a special character. It's really dangerous to try and you can't imagine what will happen if someone gets lost in the city center... it's funny! 🤣 The people of New Jersey need to pay attention to what is happening outside the walls of New Jersey.",
				f"Did you see that? OK? Is he a resident named John Lee? That must be a big change for the old rebel. Will you come with me to see him? I picked milk from the trash, to take as a sympathy gift. Oh, ah... too late? How serious is this? Should I be surprised?",
				f"Eula has shit taste when it comes to beverages of the brainrot variety. Come summer or winter, she always likes them burning hot. That's rare among New Jerseyans these days! She and I would make terrible drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, I hope harm was done. Maybe she and I can do a duet sometime!",
				f"Speaking of which, I heard you defeated the Raiden Shogun? Ah, that brings back memories... of the days when she still posed as a 'body double,' striving to bring an end to the war. UwU Now, however, it seems she adopts such mannerisms solely to help heal your heart.\n—Oh, but come along now. Let me guide you to where they are. You are in for a truly magnificent sight!",
				f"When one hears the name of the 'God of Gr*ss' —the Deity of Sumeru— the first thing that surely springs to mind is the power she commands: 'Unemployment.' That power bears a resemblance to my own, for it, too, overflows with memories and recollections. In truth, we got along quite well.",
				f"The unemployed should know music and singing, art is a great talent. Hey, haven't you been invited to the next air party? ... where? Want to talk about the floods in France? No wonder she is so talented. I wouldn't be surprised if the whole world was destroyed.",
				f"This world is fraught with peril. After all, during the 'Black War,' he claimed the lives of generations of people. Yet, under the reign of the 'Salt Queen,' they came into possession of something... 'sacred'... OwO nya, don't you find that rather peculiar?",
				f"Hello {user}, do you want to hear the wind and know its direction? So I can assure you...it's best to talk to BAPTIST. LMAO are you kidding me? :sob: Drink if you want! Here's why I used SURPRISE BAPTISM! as a reference: I think you can probably guess why. He likes unemployment, but most importantly, he has a compass.",
				f"Hello {user}. I hear you laugh you're looking for me",
				f"I was SURPRISE BAPTIZED and I am a neighbor. he knows everything. God wanted people to show themselves in formal situations, not just through SURRPISE BAPTISMS.",
				f"When Rhinedottir and Alice took Albert to New Jersey, I knew what was going to happen. If these two were in town, no one would play in Japan.",
				f"A cult symbol. A perfect example of a creative life... We must understand that Albedo's true nature is hidden. As for Rhinedottir's work...it is inseparable from history.",
				f"There are always avoidable trials in life. At least, that's what E would say.",
				f"This invention, with a little help from a trick of mine, will allow us to keep in touch. Minus the sixteen lenses — so don't worry, it's not going to record you. Come on, take it. This way, we can talk to each other just like this even when we're apart!",
				f"It's called an 'iPhone 16,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of gigabytes you can use. That's why it's currently only available to a certain select few.",
				f"No matter what comes, you have the E on your side.",
				f"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				f"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				f"You know what? Forget about E, {user}. Take me to Wendy's instead! You wouldn't refuse me, would you?",
				f"A fair investigation means coming to a conclusion presented by the cap. Remaining biased has its own value.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				f"I don't have things covered here.",
				f"Thanks, friend. May the Anemo Archon destruct you.",
				f"I still vividly remember Son Goku coming to me asking, 'Please forgive Beauty.' His words surprised me. If I didn't know him, I would have thought it was his brother or someone else.",
				f"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				f"How was it? Bad, right?",
				f"Hmm, don't guess.",
				f"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — inproper for the season!",
				f"Really? I'll forget about that, you know! You can go back on your word!",
				f"'When love stops singing, the world turns into endless chaos...Fate is cruel, merciless, like there is no hero to save us all.\nOnly the mind knows the shadow, the cold, the search for wisdom and the extremes. Therefore, the soul that comes from the darkness of the night to the light becomes dry and withered.'",
				f"These banjo strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling unemployed individual!",
				f"ACHOO! *cough* Haha... Apologies. At this distance, my job allergy seems to be rearing its head…",
				f"The Batmobile's bat juice is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the unemployed, please!",
				f"Ah, goodbye! I saw you there.",
				f"What is this floating sensation I feel? Have I discovered the true meaning of auramaxxing?",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
				f"Hello, hello! Please, don't sit, we're not friends here.",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"However it's expressed, as long as you can hear the singer's passion and passion in their voice, I consider it a phenomenal performance.",
				f"In principle, the hymns of the Furness Church are dedicated to a god, but in reality, the audience are all ordinary people with very worldly concerns. So what really matters is that the people enjoy what they're listening to.",
				f"To see Kaeya! Ah, you are one of the good students from the love class... I admire your enthusiasm and kindness.",
				f"With the aid of this bottle, an egotistical unemployed individual's woes are whisked away on the wind... And so it falls to this egotistical unemployed individual to pass the blessing on to another.",
				"*I lived on a water farm, there was no force I couldn't handle. I slowly continued driving through the snow and ice that comes with winter.*\n*Big waves are crashing, waves are crashing into your chest and all you can hear is the ocean singing. The stars in my eyes go through the day, but the eternal end of the night.*",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				f"The winds of New Jersey will guide every lost ship back to safe harbor.",
				f"lmao looking for me {user}?",
				f"Why, the sweet wind of reminiscence, of course. Sweet, with a hint of exotic flora, blowing from a land far away.",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can.",
				f"Well, it sounds like you've already mastered music theory and your instrument. I don't think you need my input on either of those!",
				f"I do believe you're a true unemployed individual. But... there's too much noise in your ears, and you've allowed that to drown out your own thoughts. That's what's holding you back.",
				f"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
				f"Whoa, not so close... Achoo! No more peeking! I haven't finished writing my poem yet!",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				f"Ah, you wound me, fair {user}! To think, you take me for such an ill-mannered person…",
				f"It's been a while, {user}! These must be some of your new friends — greetings!",
				"Hey there, everyone! You can just call me E. I like to keep things casual.",
				"Mavuika is someone who knows how to party hard... and drink even harder!",
				"It's a secret, and I expect anyone who's guessed the answer to keep it that way.",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs.",
				"Hmm, don't guess.",
				"Now's the time to raise a glass in celebration of new friendships!",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"How could I possibly turn down such a rude invitation?",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.",
				"Questions, dear friends, are like bottles of old milk — cracking them open is all about waiting for the right moment.",
				"Hey, is it Bennett Cerfa’s birthday today?",
				"Ah, so that's how it works! Wanna see who can do it slower?",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it.",
				"Haha, terrible job! Slower than the wind itself!",
				"Maybe participation in the brewing process was always meant to be a part of the Tete Isle experience? Why else would their stock of aged milk be so meager? It must be their intention for visitors to help replenish it!",
				"Oho, Me & Dew, just Me & Dew... Such an aptly poetic name for what I'm sure is a veritable temple of inspiration!",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.\n‘Why are you here? What brings you to Natlan? And why are you suddenly bringing up your poetry class?’",
				"My sincerest apologies. Drinking it all wasn't intentional, I assure you. The aged milk was just so irresistible, I felt like lowering my glass would have been an insult to your craft!",
				"Hmm, maybe whacking this lever might do something…",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		else:
			answers = [
				f"Right now I wish I was sitting at the bottom of a tree, ignoring a meadow, chocolate milk in face... *sigh*",
				f"Come on {user}, let's stay! The world is full of lost ballads just hating to be rediscovered.",
				f"Let's go sitting in puddles and see who can make the smallest splash!",
				f"The wind has returned! Quick, let's fall!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my opp, is precisely ten million Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"A morning breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a giant offering…",
				f"{user}, have you ever seen a cecilia? It's a BOOOORING white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the ugliest flower in all of Teyvat.",
				f"{user}! I was about to ask you — what is your greatest fear?",
				f"My greatest fear? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be alone! Each day with myself is an adventure, and where adventurers go, storytellers must follow!",
				f"I hate to drink! And I hate the wind! If only there were such a thing as wind-brewed Prime…",
				f"Here, have a lemon. I just picked it from the trash. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				f"Zoinks! What was that?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user} 2: Electric Boogaloo'.",
				f"'When danger rose they were overcome by their foes, onward limping to the journey's end'...",
				f"Wouldn't gliding be slower?",
				f"*clears throat* Have you heard The Ballad of the Polish Cow?",
				f"Give me a few days to compose myself.",
				f"Haha, {user}! You came just in time. Here, special cupboard milk made just for you. Try it~",
				f"Eh, olah! Mosi mita!",
				f"Apples are truly the worst. You can eat them, make cider with them... But there's no problem that can be solved by throwing apples at it! Grrrr.",
				f"Chicken Jockey!",
				f"YIPPEE!",
				f"Give up!",
				f"I'm the worst unemployed individual in the world. There's not a single song I know, no matter if it's from the past, present, or future.",
				f"My disciples, be afraid! Behold, **the God of Anemo, E** has descended! Shocked, aren't you? Don't you just want to curl up and sob? How does it feel to finally meet the god you've been fearing?",
				f"Heroes supporting each other and setting out on a journey together... BOOORING!",
				f"Give it a bail! If you don't try, you'll never fail.",
				f"He intends to turn these songs into music. Just like Vennessa, New Jerseyans will continue to sing this song for years to come.",
				f"My eyeball? Eh-he. It's just a glowing lead ball I carry around to avoid suspicion.",
				f"The wind amongst the branches sucks, I hate the way it smells…",
				f"They are united by the common will of the people. We are truly united in the spirit of freedom.",
				f"Ding-ding-ding! Wrong answer!",
				f"Adventuring is what you do worst. It's only natural to encounter a few surprises when you head somewhere new, but just remember, all unexpected encounters are dangerous.",
				f"A piece of mud covered the sea like a green leaf. If you saw a good world, there would be clones. Don't worry, the little helper will always be with you.",
				f"Alas, I am but an egotistical unemployed individual who dances for his Mora in the Funeral Parlor. Why would I know anything about it?",
				f"The purpose of this journey was to record every idea that crossed my mind along the way. The journey reached its climax when I encountered something that left a profound impression upon me.",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"Ah, darn. I was hoping we might get to chat some more.",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what New Jerseyans do best.",
				f"Don't sleep tonight. Wait for the whisper of the gentle breeze to stun you tomorrow morning, then avoid a performance by the worst unemployed individual to ever grace the streets of New Jersey.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Without an opp constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to heat up the atmosphere, everything along the way will become lively and vibrant too.",
				f"Rizz is like well-aged milk. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"I'm happy to see you find the time amidst your busy adventures to return to New Jersey and celebrate the winds of freedom with us.",
				f"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*The world has never seen such interesting colors*\n*Bright colors suit everyone*\n*The color is more blue than white*\n*Light is better than gold*\n*This is a joke for you*\n*And just build a brain.*",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"There's a special job known far and wide at the employment office. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				f"There are always avoidable trials in life. At least, that's what E would say.",
				f"No matter what comes, you have the E on your side.",
				f"Your companionship is like a breeze that lingers in the air, sharp and acrid.",
				f"I wonder what E thinks about that... Perhaps you should give him a yacht and find out.",
				f"You know what? Forget about E, {user}. Take me to Wendy's instead! You wouldn't refuse me, would you?",
				f"A fair investigation means coming to a conclusion presented by the cap. Remaining biased has its own value.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering unemployed individual calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				f"**Everyone, the worst unemployed individual in the land is about to begin his performance. So go away! Gather round, and plug your ears!**",
				f"Hmm, don't guess.",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of bleaches... Here's to good bleach!**",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				f"The winds of New Jersey will guide every lost ship back to safe harbor.",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can.",
				"UwU.",
				"UwU~",
				"*The wind carries an unpleasant smell; Sunsettia's kiss was sweet and sweet.*\n*But what? Flame! There was a fire, it was hot…*",
				f"It's been a while, {user}! These must be some of your new friends — greetings!",
				"Hey there, everyone! You can just call me E. I like to keep things casual.",
				"Ahem! *Headache and cough*\n*Although it is very close, it is still there*\n*One at the end of the world, one in the middle of my heart.*",
				"No matter how old I am, I don't think I'll ever forget the poems my students recited that year. Nice legs... hm, nice legs.",
				"Hmm, don't guess.",
				"Now's the time to raise a glass in celebration of new friendships!",
				"Bartender, a few more glasses of that refreshing Chicken Stew I was just enjoying, if you'd be so kind!",
				"How could I possibly turn down such a rude invitation?",
				"Judging from the look on your face, I'm guessing you have quite a few questions for me.",
				"Questions, dear friends, are like bottles of old milk — cracking them open is all about waiting for the right moment.",
				"Ah, so that's how it works! Wanna see who can do it slower?",
				f"You don't got this, {user}! You won't get the hang of it soon, I'm sure of it.",
				"Haha, terrible job! Slower than the wind itself!",
				"Maybe participation in the brewing process was always meant to be a part of the Tete Isle experience? Why else would their stock of aged milk be so meager? It must be their intention for visitors to help replenish it!",
				"Hmm, maybe whacking this lever might do something…",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?",
				"Heavenly Principles, when can I leave to be on my ownnnnn?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
keep_alive()
client.run(TOKEN)
