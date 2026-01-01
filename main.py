import os
from dotenv import load_dotenv
import discord
import random
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
	user = message.author.display_name
	content = message.content.lower()
	if message.author == client.user or message.channel.name == "🪽barbatos-statue" or message.channel.name == "❤️chat-in-teyvat":
		return
	#elif message.author.id == 437808476106784770 and message.mentions and any(keyword in content for keyword in ["Earned role: **I Splitting Gales**<:VentiBarbatos:1394242700315725876>", "Earned role: **II Breeze of Reminiscence**<:VentiBarbatos:1394242700315725876>", "Earned role: **III Ode to Thousand Winds**<:VentiBarbatos:1394242700315725876>"]):
		#if "Splitting Gales" in content
	elif message.channel.name == "🎇wishes-for-this-year" and any(keyword in content for keyword in ["!pray", ":dahliapray:", ":barbarapray_ikazu401:", "!ask", ":ventipray:", "this year", "2026", "resolution", "going to", "i will", "i want to", "i plan to", "next year"]):
		answers = [
			"What was lost... shall become found...",
			"When the rain ceases, the sunlight will emerge once again...",
			"Plant your seeds now, for rain is approaching...",
			"The stars hear your prayers, and weave the loom of fate...",
			"Still, the winds change direction... Someday, they will blow towards a brighter future...",
			"Take my blessings and live leisurely from this day onward.",
			"As the four seasons in turn shall say their piece, so the four winds too shall never cease.",
			"The destination is not everything... Use the chance to take in the world around you...",
			"The wind will always be by your side...", "I am here.",
			"Close your eyes, and listen to the lyresong...",
			"However far you drift, the wind will guide you home...",
			"Feel the breeze of hope... it is unceasing.",
			"Find your song... it belongs only to you.",
			"The impenetrable gales will scatter like dandelions, and the birds shall fly evermore...",
			"He fell in battle for the sake of song, sky, and birds...",
			"The wind will guide you...",
			"Don't be afraid; a gentle breeze will illuminate your path.",
			'The birds with no way to fly asked the Anemo God:\n\n"How can we reach the heavens?"\n\nTo which the Anemo God replied:\n\n"You have yet to find that which is most important."',
			"What you lacked was not wind, but courage... It is courage that has allowed you to become the first flying birds of this world.",
			"Come spring, the dandelions will bloom once more...",
			"Your prayers have been heard.",
			"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
			"Freedom, if demanded of you by an archon, is really no freedom at all.",
			"Now, spread your wings of freedom and go with my blessing.",
			"However, winds change their course. Someday, they will blow towards a brighter future.",
			f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
			"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
			"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
			"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
			"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
			"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too.",
			"The winds of Mondstadt will guide every lost ship back to safe harbor."
		]
		random_message = random.choice(answers)
		await message.reply(random_message)
	elif message.channel.name == "🎇wishes-for-this-year":
		return
#🍃 VOICELINES
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
				"Don't give up!",
				"Let me try!"
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
				"Time for takeoff!"
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
				"How rude!",
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
			file = discord.File("glider/Yahoo!.mp3")
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
				"Give me a moment to compose myself.",
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
				"...Oh dear.",
				"That was uncalled for.",
				"Ugh, I'm not in the mood for this!"
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
				"Brace yourselves!",
				"Here we go!",
				"Let's play!",
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
				"Thank Barbatos! Wait a minute...",
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
			file = discord.File("ally low hp/Don't give up!.mp3")
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
			file = discord.File("ally low hp/Let me try!.mp3")
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
			file = discord.File("burst/Time for takeoff!.mp3")
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
			file = discord.File("hit/How rude!.mp3")
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
			file = discord.File("join/Give me a moment to compose myself..mp3")
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
			file = discord.File("low hp/That was uncalled for..mp3")
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
			file = discord.File("low hp/Ugh, I'm not in the mood for this!.mp3")
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
			file = discord.File("low hp/...Oh dear..mp3")
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
			file = discord.File("skill/Brace yourselves!.mp3")
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
			file = discord.File("skill/Here we go!.mp3")
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
			file = discord.File("skill/Let's play!.mp3")
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
			file = discord.File("treasure/Thank Barbatos! Wait a minute....mp3")
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
	elif any(keyword in content for keyword in ["v!", "hey venti", "@venti", "!venti", "!v"]) or client.user in message.mentions:
		if "!sleep" in content and message.mentions:
			sleepee = message.mentions[0]
			answers = [
				f"{sleepee.mention}, get a good night's sleep tonight. Wait for the whisper of the gentle breeze to rouse you tomorrow morning, then come and enjoy a performance by the greatest bard to ever grace the streets of Mondstadt.",
				f"{sleepee.mention} Go to sleep! Anemo Archon’s orders~ <:VentiEhe:1394237963923226737>",
				f"{sleepee.mention} Rock-a-bye baby, on the tree top… when the wind blows the cradle will rock♫",
				f"{sleepee.mention} Off to the land of nod? Haha, Farewell my friend!",
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
				"That was uncalled for.",
				"Oh no, my lyre is broken... not again!",
				"Dvalin! What was that for?",
				"Hehe, maybe Barbatos should !bam you back!",
				"Dvalin! Why must you bam me so? <:VentiSigh:1394238143263277076>",
				f"!bam <@1394575189278461982> <:ventihugdvalin:1394123943794970657>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "v!jail" in content and message.mentions:
			if client.user in message.mentions:
				answers = [
					f"Nice try, {user}. <:VentiEhe:1394237963923226737>",
					"Me? Jail? I can teleport, you know.",
					"If I could go to jail, I would have gone there eons ago!",
					"What was it this time? The inebriation? Forgery? ||Steal...|| Nevermind.",
					"Haha, *no.* <:VentiSus:1406960201311064175>",
					f"I dare say {user} should go to jail and not I."
					"I'd rather not, really.",
					"Hm... <:VentiThink:1394235629671415948> No.",
					"https://discord.com/channels/1394107293297152040/1394172531207831572? Me? How could you suggest such a thing...!",
					"https://discord.com/channels/1394107293297152040/1394172531207831572? I'm just a harmless bard who spends my time at taverns!"
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
				"Ding-ding-ding! Correct answer!",
				"Ehe.",
				"Ehe~",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know the answer?",
				"I can hear it whispered in the wind... the answer is 'yes'!",
				"My intuition says it's not the case.",
				"I doubt it.",
				f"I believe that to be the case, {user}...",
				"Indeed, it is so.",
				"Nope!",
				"Unfortunately, that can never be the case.",
				"Yes, always!",
				f"Stand and listen to the wind, {user}. Hear it? That's your answer!",
				f"What do *you* think the answer is, {user}? Whatever it is, it may be so!",
				f"'What does Venti think?', you say, but I ask 'What does {user} think?' Perhaps you knew the answer all along!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["!giv", "!gib", "!give", "!gift"]):
#💎GIVE COMMAND (Animals)
			if any(keyword in content for keyword in ["dragon", "🐉", "🐲"]):
				answers = [
					"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
					"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle.",
					"Up till the end, Dvalin remembered his duty as one of the Four Winds. As such, I don't intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin will be able to choose for himself and understand what freedom is. Before I became an archon, I too was taught the meaning of freedom in this way by a friend."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["feather", "🪶"]):
				answers = [
					"Surely, he too would have wanted to live in such a place…",
					"*Fly, fly away.*\n*Like a bird in the sky.*\n*See the world on my behalf...*\n*To the heavens may you fly...*"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["rex", "saur", "mammoth", "elephant", "dodo", "🦖", "🦕", "🦣", "🐘", "🦤"]):
				answers = [
					"Well, hello there. You made it all the way from Natlan to Mondstadt?",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon. And you are…?",
					"What brings you to Mondstadt, my friend? Hunger? A wish for freedom? Well, I’ll tell you a little secret… behind the Dawn Winery, you may or may not find food scraps from time to time. Hehe, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a rare and beautiful creature!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["horse", "zebra", "donkey", "🐎", "🏇", "🐴", "🎠", "🦓", "🫏"]):
				answers = [
					"I haven’t seen horses since Varka–... well, you know!",
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
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["lion", "🦁"]):
				answers = [
					"In summer the lion walks the plains,\nNo words one finds to praise it but these:\nDo you sweat out your water to make way for wine?\nComes the heat of the summer from your mane of sunshine?",
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["dog", "pupp", "mouse", "hamster", "rabbit", "bunny", "panda", "koala", "cow", "pig", "frog", "monkey", "no_evil", "bat", "boar", "bee", "worm", "bug", "snail", "beetle", "cricket", "spider", "turtle", "lizard", "seal", "orangutan", "camel", "giraffe", "kangaroo", "ram", "sheep", "llama", "goat", "deer", "poodle", "raccoon", "skunk", "badger", "beaver", "otter", "sloth", "rat", "chipmunk", "hedgehog", "butterfly", "fox", "unicorn", "phoenix", "🐕", "🐶", "🐕‍🦺", "🐁", "🖱️", "🐹", "🐇", "🐰", "🐼", "🐨", "🐄", "🐮", "🐖", "🐷", "🐽", "🐸", "🐒", "🙈", "🙉", "🙊", "🐵", "🦇", "🐗", "🐝", "🪱", "🐛", "🐌", "🪲", "🐞", "🐜", "🦗", "🕷️", "🐢", "🦎", "🦭", "🦧", "🐪", "🐫", "🦒", "🦘", "🐏", "🐑", "🦙", "🐐", "🦌", "🐩", "🦝", "🦨", "🦡", "🦫", "🦦", "🦥", "🐀", "🐿️", "🦔", "🦋", "🦊", "🦄", "🐦‍🔥"]):
				answers = [
					"Finches, ducks, rabbits and boars,\nMondstadt's revival bid them thrive evermore.",
					"Credit should be given where credit is due, I shall sing now the praises of things beauteous and true…",
					"We thank the West Wind, whose enduring caress\nBrings the blossoms of Spring, by whose scent we are blessed.",
					"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.<:VentiWink:1394244370697289790> What’s your name?",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon. And you are…?",
					"What brings you to Mondstadt, my friend? Hunger? A wish for freedom? Or were you born here? Well, I’ll tell you a little secret… behind the Dawn Winery, you may or may not find food scraps from time to time. Hehe, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a beautiful creature!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["fly", "cockroach", "mosquito", "scorpion", "snake", "🪰", "🪳", "🦟", "🦂", "🐍"]):
				answers = [
					"Time for takeoff!",
					"Think you can get away?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bird", "goose", "eagle", "owl", "peacock", "parrot", "swan", "flamingo", "dove", "penguin", "chick", "duck", "rooster", "turkey", "🐦", "🐦‍⬛", "🪿", "🦅", "🦉", "🦚", "🦜", "🦢", "🦩", "🕊️", "🐧", "🐣", "🐤", "🐥", "🦆", "🐓", "🦃"]):
				answers = [
					"What you lacked was not wind, but courage\nIt is courage that has allowed you to become the first flying birds of this world.",
					f"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.<:VentiWink:1394244370697289790> What’s your name?",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon. And you are…?",
					"What brings you to Mondstadt, my feathery friend? Hunger? A wish for freedom? Or were you born here? Well, I’ll tell you a little secret… behind the Dawn Winery, you may or may not find food scraps from time to time. Hehe, just don’t get caught.",
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
					"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…",
					"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
					"Whoa, not so close... Achoo! No more peeking! I haven't finished writing my poem yet!",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon, and– ACHOO!<:VentiSneeze:1416910019613425704>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["octopus", "squid", "fish", "lobster", "crab", "dolphin", "whale", "shark", "🐙", "🦑", "🐟", "🐠", "🐡", "🎣", "🦞", "🦀", "🐬", "🐋", "🐳", "🦈"]):
				await message.reply("Oh no, they’re going to drown! I’ll blow them all the way to Fontaine.")
#💎GIVE COMMAND (Misc)
			elif any(keyword in content for keyword in ["💔", "💔", "🥀", "mending", "broken", "wilted"]):
				answers = [
					"Hee-hee... My warrior, you've worked so hard. I understand how you feel.\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.\nAt any rate, don't worry. Whenever you need me, I'll always be by your side.",
					"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["love", "heart", "cupid", "ring", "couple", "❤️", "🩷", "🧡", "💛", "💚", "💙", "🩵", "💜", "🤎", "🖤", "🩶", "🤍", "❤️‍", "🔥", "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "💌", "💍"]):
				answers = [
					"*blush* This is for me? <:VentiShock:1394123854518948041>",
					"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
					"I want to record all these beautiful memories, and turn them into ballads!",
					"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
					f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bouquet", "tulip", "rose", "hyacinth", "lotus", "hibiscus", "blossom", "flower", "💐", "🌷", "💐", "🌸", "🏵️", "🌹", "🌺", "🌻", "🌼", "🌷", "🪻", "🪷"]):
				answers = [
					"*blush* This is for me? <:VentiShock:1394123854518948041>",
					"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
					"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion...\nOh! You’re giving me a flower? <:VentiShock:1394123854518948041>",
					"Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
					"I want to record all these beautiful memories, and turn them into ballads!",
					"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
					f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["phone", "calling", "computer", "desktop", "pager", "fax", "tv", "television", "x_ray", "robot", "📱", "📲", "☎️", "📞", "📵", "📴", "🤙", "🖥️", "🖱️", "💽", "💻", "⌨️", "🖥️", "📟", "📠", "📺", "🩻", "🤖"]):
				await message.reply("What an interesting device! Is it from Fontaine? <:VentiIdea:1394242659870179428>")
			elif any(keyword in content for keyword in ["crystal_ball", "amulet", "hamsa", "frame", "red_envelope", "scroll", "book", "ghost", "alien"]):
				answers = [
					"How fascinating!",
					"What is this? Hm…",
					"I’m going to have to look at this more closely…"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["zap", "thunder", "lightning", "voltage", "⚡", "⛈️"]):
				await message.reply("So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Speaking of the Raiden Shogun, I dare say she seems a bit perturbed today...")
			elif any(keyword in content for keyword in ["ice", "sled", "ski", "snowboard", "snow", "🧊", "❄️", "🛷", "⛷️", "🏂", "🎿", "🏔️", "🌨️", "☃️", "⛄"]):
				await message.reply("Let's wait till the snow gets heavier and have a snowball fight!")
			elif any(keyword in content for keyword in ["fishing", "diving", "rain", "drops", "droplet", "bubble", "ocean", "wave", "🎣", "🤿", "🌧️", "🌦️", "☔", "💧", "💦", "🫧", "🌊", "🏄‍♂️", "🏄‍♀️"]):
				await message.reply("Let's go jumping in puddles and see who can make the biggest splash!")
			elif any(keyword in content for keyword in ["candle", "bell", "ribbon", "fan", "beads", "shell", "rainbow", "mirror", "lantern", "chime", "gem", "crown", "🕯️", "🔔", "🛎️", "🔕", "🎀", "🎗️", "🪭", "📿", "🐚", "🌈", "🪞", "🏮", "🎐", "💎", "👑"]):
				answers = [
					"Thanks, friend. May the Anemo Archon protect you.",
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
					"*gasp* Let's hold a summer feast! Call up your good friends and I'll contribute a bottle of the finest wine from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
					"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
					"It's stopped raining already? A shame, I wanted to play some more."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["kite", "parachute", "wind", "tornado", "fog", "cloud", "dash", "🪁", "🪂", "💨", "🍃", "🌬️", "🎐", "🌪️", "🌫️", "🌁", "☁️", "😶‍🌫️", "💨"]):
				await message.reply("The wind has returned! Quick, let's go gliding!")
			elif any(keyword in content for keyword in ["fire", "flame", "🔥"]):
				answers = [
					"Ouch-! Hot!",
					"Ow-! I can't hold this, hehe..."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["cactus", "shamrock", "clover", "bamboo", "plant", "tanabata", "leaf", "empty_nest", "mushroom", "coral", "🌵", "☘️", "🍀", "🎍", "🪴", "🎋", "🍂", "🍁", "🪹", "🍄", "🪸"]):
				answers = [
					f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
					"Thanks, friend. May the Anemo Archon protect you.",
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
					f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
					"Thanks, friend. May the Anemo Archon protect you.",
					"How kind of you!",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"I should put this somewhere special!",
					f"I got a gift from {user}♫ <:VentiLyre:1394240762060734546>",
					f"Once, I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope... It seems you, too, can bring seeds of hope, {user}.",
					f"We thank the West Wind (and {user}), whose enduring caress\nBrings the blossoms of Spring, by whose scent we are blessed."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["tree", "wood", "🌲", "🌳", "🌴", "🎄", "🪵"]):
				answers = [
					f"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*\nOh, this tree is for me? <:VentiShock:1394123854518948041>",
					f"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
					f"Ah... the park is one of the most pleasant places in the city. Most people taking a break there are relaxed and in pretty good spirits, so they're always willing to listen to a song or two. Eh-he~ let's work together to make this park even more beautiful!",
					f"Yahoo~ Look up, I'm here in the tree!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
					f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
					f"The wind amongst the branches is good, I love the way it smells…",
					f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
					"Thanks, friend. May the Anemo Archon protect you.",
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
					f"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
					"'Mondstadt' means 'Moon City', and 'Liyue' means 'Glazed Moon'. Hmm, I wonder what those names entail...",
					"Thanks, friend. May the Anemo Archon protect you.",
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
					"Hehe, this will be fun to play with."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["shower", "bath", "soap", "toothbrush", "sponge", "🚿", "🛀", "🛁", "🧼", "🪥", "🧽"]):
				answers = [
					"Hehe, are you implying I need a shower?",
					"Hey! As a wind spirit, I lack the tribulations of bodily odor. …I hope.",
					"Heh, message received.",
					"A hygiene product… Ah, I guess one can always use more of those, right?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["printer", "compression", "clamp", "control", "compass", "satellite", "battery", "electric", "bulb", "flashlight", "lamp", "fire_extinguisher", "oil_drum", "scale", "ladder", "tool", "screwdriver", "wrench", "hammer", "pick", "saw", "nut", "bolt", "gear", "trap", "brick", "chain", "link", "magnet", "barber", "telescope", "microscope", "stethoscope", "thermometer", "broom", "basket", "potable", "bucket", "squeeze", "lotion", "key", "door", "chair", "couch", "window", "shopping", "flag", "envelope", "mail", "package", "label", "placard", "post", "page", "bookmark", "receipt", "notepad", "calender", "date", "card", "ballot", "file", "clip", "paper", "ledger", "pin", "clip", "ruler", "abacus", "pen", "nib", "paint", "crayon", "pencil", "mag", "lock", "lipstick", "knot", "yarn", "thread", "needle", "coat", "vest", "cloth", "shirt", "jeans", "shorts", "necktie", "dress", "kimono", "sari", "sandal", "shoe", "heel", "boot", "sock", "glove", "scarf", "hat", "cap", "board", "helmet", "bag", "purse", "pouch", "seat", "case", "backpack", "satchel", "luggage", "glasses", "goggles", "razor", "pick", "wastebasket", "bandage", "shield", "albemic", "gift", "rock", "🖨️", "🗜️", "🎛️", "🧭", "📡", "🛰️", "🔋", "🪫", "🔌", "💡", "🔦", "🛋️", "🪔", "🧯", "🛢️", "⚖️", "🪜", "🧰", "🪛", "🔧", "🛠️", "🔨", "⚒️", "⛏️", "🪚", "🔩", "⚙️", "🪤", "🧱", "🔗", "⛓️‍💥", "⛓️", "🧲", "💈", "🔭", "🔬", "🩺", "🌡️", "🧹", "🧺", "🚰", "🪣", "🧴", "🔑", "🔐", "🗝️", "🚪", "🪑", "💺", "🛋️", "🪟", "🛍️", "✉️", "📨", "📩", "📧", "📤", "📥", "📫", "📪", "📬", "📭", "📮", "📦", "🏷️", "🔖", "🪧", "📃", "📄", "📟", "🧾", "📓", "📔", "📒", "🗒️", "📅", "📆", "🗓️", "🎴", "🗂️", "📇", "🗃️", "🗳️", "📁", "📂", "🗃️", "🗄️", "📋", "📎", "📰", "🗞️", "📒", "📌", "📍", "📎", "📋", "📏", "📐", "🧮", "🖊️", "✒️", "🖋️", "🔏", "✏️", "📝", "🎨", "🖌️", "🖍️", "🔒", "🔓", "💄", "🪢", "🧶", "🧵", "🪡", "🧥", "vest", "👚", "🎽", "👕", "👖", "🩳", "👔", "👗", "👘", "🥻", "👡", "🩴", "👞", "👟", "👠", "👢", "🥾", "🧦", "🧤", "🧣", "👒", "🎩", "🎓", "⛑️", "🧢", "🪖", "👜", "👝", "🛍️", "👛", "👝", "💼", "🎒", "🧳", "👓", "🥽", "🪒", "🪮", "🩹", "🛡️", "🎁", "🪨"]):
				answers = [
					"Thanks, friend. May the Anemo Archon protect you.",
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
					f"Aw, I don't want to sleep yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
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
					"Thank Barbatos! Wait a minute…",
					"What a find! I wonder how many bottles this'll be worth…",
					"*clears throat* Have you heard The Ballad of the Treasure Chest?",
					"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["coffin", "headstone", "urn", "amphora", "hole", "dna", "plunger", "roll_of_paper", "toilet", "tooth", "tongue", "ear", "nose", "foot", "eye", "anatomical", "lungs", "clown", "goblin", "briefs", "bikini", "swimsuit", "lip", "poo", "shit", "ogre", "trash", "garbage", "⚰️", "🪦", "⚱️", "🏺", "🕳️", "🧬", "🪠", "🧻", "🚽", "🦷", "👅", "👂", "👃", "🦶", "👁️", "👀", "🫀", "🫁", "🤡", "👺", "🩲", "👙", "👄", "💩", "👹", "🗑️"]):
				answers = [
					"Hehe, very funny. <:VentiScared:1394163440490254427>",
					"Aww, for me? How… *generous*. <:VentiRefuse:1394238074707251271>",
					"Just what I always wanted!",
					f"Haha, now you’re playing with me, {user}. <:VentiEhe:1394237963923226737>"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["bomb", "firecracker", "blood", "microbe", "petri_dish", "brain", "💣", "🧨", "🩸", "🦠", "🧫", "🧠"]):
				answers = [
					"<a:ventismh:1394722750223880202>",
					"Time for takeoff!",
					"That was uncalled for. <:VentiShock:1394123854518948041>",
					"...Oh dear.",
					"How rude!"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
#🍎GIVE FOOD
			elif any(keyword in content for keyword in ["apple", "aple", "🍎", "🍏"]):
				answers = [
					"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
					"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["grape", "🍇"]):
				answers = [
					"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["wine", "🍷"]):
				answers = [
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?",
					"A drink? I'll hold you to that, you know! No going back on your word!",
					"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
					"With the aid of this drink, a humble bard's woes are whisked away on the wind... And so it falls to this humble bard to pass the blessing on to another.",
					"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
					"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!",
					"To our precious days of freedom. Cheers!",
					"What is this floating sensation I feel? Have I discovered the true meaning of Anemo power?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["beverage_box", "sake", "beer", "champagne", "cocktail", "tropical", "drink", "alcohol", "tumbler", "🧃", "🍶", "🍺", "🍻", "🍾", "🥂", "🥃", "🍸", "🍹", "🥃"]):
				answers = [
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?",
					"A drink? I'll hold you to that, you know! No going back on your word!",
					"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
					"With the aid of this drink, a humble bard's woes are whisked away on the wind... And so it falls to this humble bard to pass the blessing on to another.",
					"To our precious days of freedom. Cheers!",
					"What is this floating sensation I feel? Have I discovered the true meaning of Anemo power?"
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["cheese", "pancake", "🧀", "🥞"]):
				answers = [
					"What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!",
					"I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament."
				]
				random_message = random.choice(answers)
				await message.reply(random_message)
			elif any(keyword in content for keyword in ["pear", "tangerine", "lemon", "lime", "banana", "melon", "berry", "cherr", "peach", "mango", "coconut", "kiwi", "cookie", "cake", "pie", "birthday", "nut", "cup", "🍐", "🍊", "🍋", "🍋‍🟩", "🍌", "🍈", "🍉", "🍒", "🍓", "🫐", "🍑", "🥭", "🥥", "🥝", "🍪", "🥠", "🎂", "🥧", "🍰", "🥜", "🌰", "🥤"]):
				await message.reply("Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?")
			elif any(keyword in content for keyword in ["milk", "eggplant", "tomato", "avocado", "pea", "broccoli", "leafy", "cucumber", "pepper", "corn", "carrot", "olive", "potato", "ginger", "croissant", "bagel", "bread", "pretzel", "meat", "poultry", "hot dog", "burger", "fries", "sandwich", "falafel", "salad", "food", "stew", "bento", "rice", "oden", "dango", "cream", "shaved", "lollipop", "candy", "chocolate", "popcorn", "doughnut", "donut", "bean", "tea", "coffee", "beverage", "mate", "salt", "takeout", "herb", "🥛", "🍆", "🍅", "🥑", "🫛", "🥦", "🥬", "🥒", "🌶️", "🫑", "🌽", "🥕", "🫒", "🥔", "🍠", "🫚", "🥐", "🥯", "🍞", "🥖", "🥨", "🥩", "🍖", "🍗", "🌭", "🍔", "🍟", "🥪", "🧆", "🫓", "🥙", "🥗", "🥫", "🥘", "🍲", "🍱", "🌾", "🍘", "🍙", "🍚", "🍛", "🍥", "🍢", "🍡", "🍦", "🍧", "🍨", "🍭", "🍬", "🍫", "🍿", "🍩", "🫘", "🫖", "🍵", "🧋", "☕", "🧃", "🧉", "🧂", "🥡", "🌿"]):
				await message.reply("Oof, I'm so full... I'll have to pass on the post-meal fruits this time…")
			elif any(keyword in content for keyword in ["garlic", "onion", "egg", "cooking", "waffle", "bacon", "bone", "pizza", "taco", "burrito", "tamale", "fondue", "canned", "jar", "spaghetti", "ramen", "curry", "sushi", "dumpling", "oyster", "shrimp", "custard", "pudding", "honey", "liquid", "🧄", "🧅", "🥚", "🍳", "🧈", "🧇", "🥓", "🦴", "🍕", "🌮", "🌯", "🫔", "🫕", "🥫", "🫙", "🍝", "🍜", "🍣", "🥟", "🦪", "🍤", "🦐", "🍮", "🍯", "🫗"]):
				await message.reply("I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament.")
			else:
				return
#PRIORITY ⭐
		elif any(keyword in content for keyword in ["sad", "cry", "sick", "hard", "hurt", "tear", "pain", "depress", "tir", "energy", "suic", "upset", "help me", "sniffle", "weep", "bad day"]):
			answers = [
				"Hee-hee... My warrior, you've worked so hard. I understand how you feel.\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.\nAt any rate, don't worry. Whenever you need me, I'll always be by your side.",
				"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["you are", "your", "ur", "you", "youre", "venti is", "barbatos is", "venti’s", "barbatos’s", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos"]) and any(keyword in content for keyword in ["idiot", "dumbass", "lazy", "bad", "annoying", "worst", "useless", "terrible", "ugly", "stupid", "awful", "drunkard", "wastrel", "drunken", "worst", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos", "wrong with", "idiot", "stinky", "i hate mondstat", "i hate mondstadt"]):
			answers = [
				"What's that? You think I should try harder to be a good Anemo Archon? Well you could be a better devotee too... you could be more pious, more passionate, or... um…",
				"Ugh, I'm not in the mood for this!",
				"How rude!",
				"That was uncalled for.",
				"That smirk you wear looks out of place. Did you steal it from your master's face?",
				"Beauty is a waste... when the beholder has no taste.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we bards are required to do... It just happens that enjoying life is the most important one.",
				"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["i hate", "i dislike", "fuck", "shut", "sybau", "bitch", "trash"]) and any(keyword in content for keyword in ["u", "shut", "venti", "barbatos", "sybau", "bitch", "trash"]):
			answers = [
				"What's that? You think I should try harder to be a good Anemo Archon? Well you could be a better devotee too... you could be more pious, more passionate, or... um…",
				"Ugh, I'm not in the mood for this!",
				"How rude!",
				"That was uncalled for.",
				"That smirk you wear looks out of place. Did you steal it from your master's face?",
				"Beauty is a waste... when the beholder has no taste.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we bards are required to do... It just happens that enjoying life is the most important one.",
				"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rodent", "scurry", "rat", "pest", "vermin"]):
			await message.reply("Resident rodent... beats invasive vermin.")
		elif any(keyword in content for keyword in ["spit", "attack", "fight", "shoot", "punch", "slap", "hit", "kick", "smack", "bite", "chew", "steal", "take", "grab", "slash", "bonk", "boom", "collision", "💥", "nom"]):
			answers = [
				"Woah! What was that?",
				"Ugh, I'm not in the mood for this!",
				"...Oh dear.",
				"That was uncalled for.",
				"Oh no, my lyre is broken…",
				"How rude!",
				"Think you can get away?",
				"Time for takeoff!",
				"Ah... Ugh…",
				"Ah!",
				"What?!",
				"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "better" in content and "archon" in content:
			await message.reply("What's that? You think I should try harder to be a good Anemo Archon? Well you could be a better devotee too... you could be more pious, more passionate, or... um…")
		elif any(keyword in content for keyword in ["i love", "ily", "you make", "dearest", "beloved", "my love", "mean", "deserve", "adore", "i need you", "i need u", "i need venti"]) and any(keyword in content for keyword in ["you", "venti", "barbatos", "u", "ily", "me happy", "dearest", "beloved", "my love", "to me", "deserve", "i need you", "i need u", "i need venti"]):
			answers = [
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				f"The breeze combing through your hair today feels a little different, don't you think?\nIt smells faintly of flowers and also carries a refreshing scent of spring water…\nIf you are sensitive to smells, I wouldn't be surprised if you can pick a hint of sweetness in today's wind. That's because I just ate an apple, haha!\nCome on now, let's go for a walk outside!\nWe can pick berries for a picnic and rest at a roadside tavern. With me, the best bard there is by your side, the journey will be great wherever we go.\nOops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				f"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
				f"Don't get distracted by the scent of hash browns along the way, you hear? If you stuff yourself silly, the feast I've prepared might end up feeling a little... neglected.\nKeep walking, just a little further — go on and leave Mondstadt's lively bustle behind for now. Can you hear it? That melody is growing clearer by the moment.\nThe sunshine is beautiful today, and the picnic mat is as cool and airy as the breeze dancing across the lake. You'll spot it from far away, but of course, take your time~\nI'll be right here, waiting for you and strumming a tune.",
				f"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
				f"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				f"Your companionship is like a breeze that lingers in the air, warm and familiar."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "do" in content and any(keyword in content for keyword in ["love me", "like me"]):
			answers = [
				"Of course. I love all the people of Mondstadt.",
				f"Of course I do, {user}. Always!",
				"Your companionship is like a breeze that lingers in the air, warm and familiar.",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["u kiss", "you kiss"]):
			answers = [
				"Barbatos? Kissed?",
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
				"Oh, to hold such bardly charm… woe is me!",
				"Oh! Does this mean you want to buy me a drink?",
				"Oh dear…!",
				"*gasp* Such PDA! <:VentiShock:1394123854518948041>",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				"Woah! What was that?",
				"Hahaha, that one doesn't work on a bard.",
				"<:VentiUwU:1394123911284920341>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cute", "adorable", "sweet", "beautiful", "pretty", "amazing", "precious", "favorite", "charming", "lovely", "endearing", "lovable", "delightful", "heartwarming", "wholesome", "gentle", "kind", "caring", "soft", "comforting", "comfort character", "sunshine", "angel", "handsome", "gorgeous", "stunning", "dreamy", "ethereal", "radiant", "divine", "elegant", "enchanting", "sparkly", "talented", "poetic", "genius", "lyrical", "inspiring", "whimsical", "brilliant", "clever", "grace", "soothing", "magical", "iconic", "legendary", "goat", "my heart", "my eye", "baby", "best", "top tier", "fave", "my muse", "perfect", "king", "slay"]):
			answers = [
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				"Oops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				"Your companionship is like a breeze that lingers in the air, warm and familiar.",
				"No matter what comes, you have the wind on your side.",
				"Thanks, friend. May the Anemo Archon protect you.",
				f"How kind of you, {user}!",
				"*blush*",
				"Aww, really? You mean it?",
				"You, on the other hand... you're the gentlest soul I've ever met.",
				f"I could say the same about you, {user}!",
				"Hehe, you flatter me..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["pet", "pat", "ruffle", "stroke"]):
			answers = [
				"<:ventilove:1394738768774434878>",
				"<a:ventipat:1394159658503241828>",
				f"Ah, {user}. I could hear your arrival upon the wind. Were you looking for me?",
				f"Hehe. Looking for me, {user}?",
				"My dearest companion, is there something you wish to tell me?",
				"Here, come sit with me and enjoy the scent of Cecilias!",
				"Whenever you need me, I'll always be by your side.",
				"No matter what comes, you have the wind on your side.",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you!",
				"Oops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				"Haha, how kind of you!",
				"I guess I'm a cat now! ...Aaah... Aa-choo! Ugh, apparently I can't even THINK about cats without sneezing.",
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
				"No matter what comes, you have the wind on your side.",
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
		elif "birthday" in content:
			answers = [
				f"Someone once told me you're supposed to eat a cake on your birthday... Tada! Here's your birthday cake — it's apple flavored! And here's a spoon. The cake didn't rise properly in the oven, that's why it looks more akin to an apple pie... Ugh, baking is really quite complicated!",
				f"So, how do you think we should spend this day?",
				f"I've been mulling it over for a long time now — so long, in fact, that the Philanemo Mushrooms seem to have withered away and the Windwheel Asters have ground to a complete halt…\nHm... We could go climb a tree and enjoy the breeze together? Or, we could go stargazing from a cliff? Ooh — we could even go on a day trip to an uninhabited island!\nEh, but really, it doesn't matter what we do — I'll be happy just as long as I'm with you. Having you by my side is the most important thing of all.\nSo c'mon, let's go enjoy your birthday to the full while it lasts! Do you mind if I delegate the decision of exactly how we celebrate it to you, though?",
				f"The breeze combing through your hair today feels a little different, don't you think?\nIt smells faintly of flowers and also carries a refreshing scent of spring water…\nIf you are sensitive to smells, I wouldn't be surprised if you can pick a hint of sweetness in today's wind. That's because I just ate an apple, haha!\nCome on now, let's go for a walk outside!\nWe can pick berries for a picnic and rest at a roadside tavern. With me, the best bard there is by your side, the journey will be great wherever we go.\nOops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				f"I recently came across a treasure map! It floated down from a tree, and a location most mysterious is drawn upon it: azure laying siege to a field of green, and the yellow of stone ornamented with viridian. Even I, a wandering bard who has nothing but free time to gallivant about, haven't got a clue just what kind of place it is. A seaside cave wreathed in clouds? A floating island covered in forest that appears only at night? Hm… just what is the answer?\nGiven that you're a brave hero who has voyaged across the land, why don't you have a look at it? Perhaps, with two hands on the scroll, we'll be at our destination in the blink of an eye! When that time comes, I'll leave the honor of finding the treasure to you!\nAs for me, well, I'll be happy to travel with you! Even if your journey takes you to the edge of the world, with me there, there's no need to worry. Though, if there's any danger, you'll remember to protect me, won't you?",
				f"Just now, when I was relaxing under a tree, I accidentally fell asleep and ended up being knocked on the head by a falling Sunsettia…\nBut thanks to that sweet little fruit, I thought of a new song. Naturally, I'll let you be the first to hear it.\nIt's a fine day out, so how about we take a walk together through the open country? We can get some fresh air and leave our worries far behind.\nIn the evening, we'll stop somewhere with a good view and I'll play my new song for you. I wouldn't want to get so caught up in the journey that I'd miss out on watching the sunset with an important friend!\nMondstadt's gentle breeze awaits your return from far afield. Just try not to get lost on the way!",
				f"When you receive this letter, hold it in your hands and stand by the window.",
				f"Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
				f"But don't get distracted by the scent of hash browns along the way, you hear? If you stuff yourself silly, the feast I've prepared might end up feeling a little... neglected.\nKeep walking, just a little further — go on and leave Mondstadt's lively bustle behind for now. Can you hear it? That melody is growing clearer by the moment.\nThe sunshine is beautiful today, and the picnic mat is as cool and airy as the breeze dancing across the lake. You'll spot it from far away, but of course, take your time~\nI'll be right here, waiting for you and strumming a tune."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "it" in content and "stuck" in content:
			await message.reply("It’S sTuCk.")
		elif "detour" in content:
			await message.reply("Let’s make a detour then. Heading up!")
		elif "walk in" in content and "flies in" in content:
			await message.reply("He doesn’t *walk* in, he *flies* in.")
		elif any(keyword in content for keyword in ["ding", "answer", "correct"]):
			await message.reply("Ding-ding-ding! Correct answer!")
		elif any(keyword in content for keyword in ["fembo", "twink", "mpreg"]):
			answers = [
				"So that’s the word people use. Hm…",
				"<:VentiWink:1394244370697289790>",
				"Ehe.",
				"<:VentiUwU:1394123911284920341>",
				"Ehe~",
				"<a:ehe:1394722624340496384>",
				"'Femboy', huh? How fascinating!",
				"'Femboy' is an excellent prompt for a poem, if I do say so myself!",
				"If I’m a femboy, does that mean Barbatos is the Femboy Archon?",
				"Ding-ding-ding! Correct answer!",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to femboys!**"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#SHIPPING💘
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "zhongven", "ventli", "venzhong"]) and any(keyword in content for keyword in ["zhongli", "zhongven", "ventli", "venzhong"]):
			answers = [
				"Morax? Ah, we're old friends... He's a stubborn fellow. Very, very stubborn indeed. Don't tell him I said that.",
				"Zhongli... I don't dislike him, despite his obstinate ways. On the contrary, I still regard him as a dear friend of mine. I miss drinking wine with him and hearing about what was happening in Liyue.",
				"Eh? Oh dear...",
				"Well, I... we're old friends.",
				"<:VentiShock:1394123854518948041>",
				"Zhongli and I? Romantically acquainted? In reality, we're sworn enemies! ...Ehe, just kidding. We're friends.",
				"Well, I suppose it _would_ make sense, would it not?",
				"We do have a lot of history. It's been many years, after all!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "diluven", "venluc", "ventluc", "ventiluc", "vennvindr"]) and any(keyword in content for keyword in ["diluc", "diluven", "venluc", "ventluc", "ventiluc", "vennvindr"]):
			answers = [
				"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!",
				"Diluc? Well, it would be nice to have the wine for free.",
				"Hmm, really? That's possible? And here I thought Diluc believed I was a wine leech!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", "venxiao", "xiaoven", "xiaoti", "xiaoventi", "ventiao", " x venti", "venti x "]) and any(keyword in content for keyword in ["xiao", "venxiao", "xiaoven", "xiaoti", "xiaoventi", "ventiao"]):
			answers = [
				"Ah, Xiao... I remember that night, when he was lost, but found his way back to the light. I hope he's doing better now.",
				"Xiao is not fond of public spaces, so sometimes we go out in nature together and sit and talk for a while. He's surprisingly wise when he's comfortable enough to speak freely!",
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
				"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				"'When no love remains for the songs to tell, the world becomes naught but an empty shell… Cruel is said fate, cruel it may be, were it not for a hero who could set us all free.\nThrough shadows so cold, he sought wisdom untold, chasing a fragrance, the wind only knows. Thus wistfulness waned and faded into night, as he stepped from the darkness, and into the light.'",
				"Aether? He's... a dear friend of mine.",
				"My wish is to explore the world by the Traveler's side!",
				"The Traveler? He's my dearest companion.",
				"I wouldn't be opposed to it..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "venlia", "dahliven", "vendahlia"]) and any(keyword in content for keyword in ["dahlia", "venlia", "dahliven", "vendahlia"]):
			answers = [
				f"O, {user}, do you seek to hear the voice of the wind and know its guidance? Then I say to you... chatting to the deacon is your best bet. Haha, I'm kidding — come chat with me over a drink any time you want! The reason I usually get Dahlia to be my intermediary is because... well, I imagine you can probably guess why. He loves listening to the blustering of the wind, but crucially he has his own compass, too.",
				"Dahlia and I are close. He knows everything. A god needs someone to communicate their will in a formal setting, and no one does that better than Dahlia.",
				"Dahlia and I drink together often! I suppose you could say we're drinking buddies.",
				"Hm, well, I've noticed Dahlia's behavior is occasionally... strange.",
				"Did Dahlia ask you to say that?",
				"Ehe... oh dear... well...",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "gay", "husband", "kiss", "dat", "love", "like", " x venti", "venti x ", "albeven", "venbedo"]) and any(keyword in content for keyword in ["albedo", "albeven", "venbedo"]):
			answers = [
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"Now that Albedo knows my true identity, we've conversed on occasion. He knows a great deal about the arts, and I've enjoyed showing him my compositions!",
				"Someday, Albedo may lose control. But until then, he and I are friends.",
				"Eh? Albedo? <:VentiShock:1394123854518948041>",
				"We _do_ have a lot in common."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "husband", "wife", "kiss", "dat", "love", "like", " x venti", "venti x ", "venlumi", "lumiven", "ventilumi", "lumiventi", "venlumine", "ventine", "vemine", "lumenti"]) and any(keyword in content for keyword in ["lumine", "venlumi", "lumiven", "ventilumi", "lumiventi", "venlumine", "ventine", "vemine", "lumenti"]):
			answers = [
				"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				"Lumine? She's... a dear friend of mine.",
				"My wish is to explore the world by the Traveler's side!",
				"The Traveler? She's my dearest companion.",
				"I wouldn't be opposed to it...",
				"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["marri", "husband", "wife", "kiss", "dat", "love", "like", " x venti", "venti x ", "venfuri", "venrina", "focaven", "furiven"]) and any(keyword in content for keyword in ["furina", "venfuri", "venrina", "focaven", "furiven"]):
			answers = [
				"A bard must be versed in both music and song, but a stage performer requires far more skills than just these... Hey, don't you think we should invite her over to put on a show at the next Windblume Festival? ...Huh? You want me to talk about how she saved Fontaine? Well, I mean, she's such a talented artiste, it's no wonder. I wouldn't be surprised even if she'd saved the entire world.",
				"Furina? Ah... maybe we could write and perform a song together.",
				"Furina has gone so through much. I hope she's at peace now.",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#CHARACTERS ❤️
		elif "paimon" in content:
			answers = [
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["mavuika", "xbalanque", "harborym", "god", "archon"]) and any(keyword in content for keyword in ["fire", "pyro", "natlan", "war", "mavuika", "xbalanque", "harborym"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				"This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that. Ah, right! I heard Mavuika likes to drink! Are you thinking what I'm thinking...?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["god", "archon", "zhong", "morax", "rex lapis"]) and any(keyword in content for keyword in ["geo", "earth", "stone", "rock", "liyue", "contract", "zhong", "morax", "rex lapis"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				"Have you seen that gentleman around? Huh? He's just a normal man by the name of Zhongli now? That must be quite the change for that old block-head. Come with me to see him, will you? I have a vintage I dug up from Windrise that I can take as a condolence gift. Oh, ahh... did he still seem strong when you saw him? How strong? Am I likely to get blown away?",
				"I've actually heard a few things about Mr. Zhongli before. The guests in the tavern talked about this refined and courteous man who, instead of having wine at Mondstadt's finest tavern, ordered a cup of hot tea with the most complex name.",
				"Morax? Ah, we're old friends... He's a stubborn fellow. Very, very stubborn indeed. Don't tell him I said that.",
				"Zhongli... I don't dislike him, despite his obstinate ways. On the contrary, I still regard him as a dear friend of mine. I miss drinking wine with him and hearing about what was happening in Liyue."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["raiden", "shogun", "baal", "god", "archon", "kujou", "sara", "kokomi", "gorou"]) and any(keyword in content for keyword in ["raiden", "shogun", "ei", "baal", "electro", "thunder", "lightning", "eternity", "inazuma", "kujou", "sara", "kokomi", "gorou"]):
			await message.reply("So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Hehe, she now no doubt employs a wide range of reasoning to get you to train with her. Oh but yes, come close and I shall let you in on her weakness — desserts!")
		elif any(keyword in content for keyword in ["god", "archon", "nahida", "kusanali", "buer", "lesser lord"]) and any(keyword in content for keyword in ["nahida", "kusanali", "buer", "lesser lord", "dendro", "grass", "plant", "nature", "wisdom", "sumeru"]):
			await message.reply("The first thing you think of when you hear 'Dendro Archon' is her power over dreams. Her dreams are akin to my ballads: full of emotion and imagination. It goes without saying that we get along really well.")
		elif "rukkha" in content:
			answers = [
				"■■■ ■■■ ■■■■■■■",
				"■■■■■■ ■■■■■■■ ■■■■",
				"■■■■ ■■■■■■ ■■■■■■■■■ ■■ ■■■■■■■■",
				"■■■■■■ ■■■■■■ ■■■■ ■■■■■ ■■■■■■",
				"■■■ ■■■ ■■■■■■■■■ ■■ ■■■■■■■■",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, p̶r̸e̵s̸e̷n̸t̸, o̷̭̩̲̓̈́́r̶̬̯̬̿ ■■■■■■■■■■■",
				"The people of Mondstadt believe that the w̷i̵n̵d̵ ̸c̷a̵n̸ ̵b̵r̶i̶n̷g̷ ̶b̷a̴c̴k the soul, and also preserve ṁ̸̡̡̢̛̛̯̰̑̐́̄e̷̙̻̰̥̓̓̏͋͊̂͊m̷̨̪͈̭̤͆o̴̢̝̺̫̦̝͌̊́r̷͈̳͋̒̂̇ī̵͙͓̣͎e̸̹͚̤̊̒͂͛͛͘s̸͙̥̙͎̅̔. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of c̴a̶p̷t̴u̸r̷i̵n̶g̶ ̸t̶h̸e̵ ̴w̶i̷n̵d̵ in the very m̷o̸m̴ent that the barrel is sealed. T̷h̶e̴ ̷m̴e̸m̸o̷r̷y̵ ̷o̶f̴ ̴t̵h̷a̷t̷ ̵m̷o̷m̸e̶n̸t̴ ̴i̸s̴ ̸t̷h̷e̵n̸ s̸t̴o̴r̵e̵d̵ ̶i̸n̴ ̵t̶h̶e̸ ̴w̸i̴n̶e̴,̵ ̸f̸o̷r̶ ̵■■■ ̷■■■■■■■"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["furi", "focalors", "regina", "ousia", "pneuma", "god", "archon"]) and any(keyword in content for keyword in ["furi", "focalors", "regina", "ousia", "pneuma", "hydro", "water", "ocean", "sea", "justice", "fontaine"]):
			await message.reply("A bard must be versed in both music and song, but a stage performer requires far more skills than just these... Hey, don't you think we should invite her over to put on a show at the next Windblume Festival? ...Huh? You want me to talk about how she saved Fontaine? Well, I mean, she's such a talented artiste, it's no wonder. I wouldn't be surprised even if she'd saved the entire world.")
		elif any(keyword in content for keyword in ["fontaine", "france", "french"]):
			await message.reply("Ohoho travelère, wouldn’t gliding be fastère? <:VentiFrench:1394234467832561717> Hehehehe…\nBONJOUR YOU F*CKING A-")
		elif any(keyword in content for keyword in ["tsaritsa", "god", "archon"]) and any(keyword in content for keyword in ["cryo", "ice", "snow", "snezhnaya", "tsaritsa"]):
			answers = [
				"She is one of The Seven, the Tsaritsa who reigns from the Zapolyarny Palace, and the one person that the Fatui Harbingers all answer to. The Seven don't always get along well, but still — I never thought that she would plot to steal another archon's Gnosis…",
				"Five hundred years ago, I knew The Tsaritsa well. But I can't say the same is true now. You see, a certain catastrophe happened five hundred years ago, and after that, she cut off all ties with me.",
				"The Tsaritsa... I haven't seen her in five hundred years. What is she thinking? What's her plan?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "dottore" in content:
			answers = [
				"Dottore... I have a thing or two to say to him.",
				"<:VentiSus:1406960201311064175>",
				"Dottore? I can't say I'm a fan...",
				"I wonder if Dottore knows of the word 'karma'. Do you think we should teach him?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "capitano" in content:
			answers = [
				"*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…",
				"Immortality may seem desirable at first, but even the largest oak trees get worn down by time."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["signora", "rosalyne"]):
			await message.reply("Signora was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like executive authority by the Tsaritsa of Snezhnaya, and with it, strength surpassing that of other mortals.")
		elif "celestia" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Celestia?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["primordial", "phanes", "heavenly principles", "hp", "dad", "father", "papa"]):
			answers = [
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Phane–ahem, the Heavenly Principles?",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about the Heavenly Principles?",
				"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fatui", "fatuus", "arle", "harbinger", "pulcinella", "sandrone", "pantalone"]):
			await message.reply("*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…")
		elif any(keyword in content for keyword in ["vennessa", "windrise", "oak"]):
			await message.reply("I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.")
		elif any(keyword in content for keyword in ["stanley", "hans", "archibald"]):
			answers = [
				"Even in his memory, the real Stanley isn't the living, breathing friend he knew at all. Instead, he's become fixed on the image of him as that battle-scarred warrior... and that image has held him captive his entire life.",
				"...Stanley really did make it to the Mare Jivari. And the tragedy he encountered there was real, too. But the real adventurer, the real Stanley — that was his partner. Not him."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["dain", "cataclysm", "khaen", "ancient kingdom", "calamity"]):
			answers = [
				"I don't blame Dainsleif for the way he feels... or any other lost souls from Khaenri'ah who feel the same. Their freedom was forcibly taken from them, just like Mondstadt's was so many years ago...",
				"*Maybe, in another timeline... things could have been different.*",
				"*The crimson, numinous flames stretching over the sky like smoke... the pride of humankind shrouded in darkness...*\nHm? Oh, that's a little poem I once composed."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "jack" in content:
			await message.reply("Jack… Stanley's really fond of that kid, don't you think?")
		elif any(keyword in content for keyword in ["venti", "you", "nameless bard", "nameless"]) and any(keyword in content for keyword in ["grie", "loss", "death", "sad", "alcoholic", "pain", "cry", "died", "nameless bard", "nameless"]):
			answers = [
				f"My current form is not so different from the situation with fake Stanley... I took the form of a friend…",
				f"Say, {user}, do you wish to hear the next part of the story…?",
				f"Ah... You know, you're so smart it almost makes me uncomfortable sometimes… But then, maybe it's right that true friends can tell what the other is thinking.",
				f"A refreshing drink, a gentle breeze... *sigh* Moments like this always take me back…\nBack to a song that I first heard from him…\n*Fly, fly away.*\n*Like a bird in the sky.*\n*See the world on my behalf...*\n*To the heavens may you fly...*",
				f"(The green-clad figure is uncharacteristically silent.)\n(Sometimes even the lissome wind grows heavy in its grief... But not that mortals could ever see a moment oh so brief.)"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["wind spirit", "wind sprite", "form"]):
			answers = [
				"Ah, this takes me back. The first time I saw this view, I hadn't even taken on this form yet.",
				"Back then, I was but a wisp among the thousand winds. I wasn't a god of anything — I didn't even have a human form... I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope.",
				"My current form is not so different from the situation with fake Stanley... I took the form of a friend…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["stormterror’s lair", "old mondstadt", "ruins", "ancient", "decarabian", "amos"]):
			answers = [
				"Stormterror’s Lair was once part of an ancient city. The ruins even predate the existence of The Four Winds. Mondstadt is a city without a ruler. However, before, it was ruled over by a tyrant.",
				"The word 'Windblume' dates from the age of Old Mondstadt. It was a code word that the people used to stay in contact and mount resistance in secret. At that time, people often said that the stronger the wind blows, the firmer the roots of the Windblume grow, and the brighter the flower that bursts into bloom.",
				"It was about twenty-six hundred years ago, before the world had come under the rule of The Seven. At that time, Old Mondstadt was ruled by a tyrant, who sealed off the city's perimeter with a ferocious hurricane. Even the birds couldn't get in or out.",
				"Back then, I was but a wisp among the thousand winds. I wasn't a god of anything — I didn't even have a human form... I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["stormterror", "dvalin", "dragon"]):
			answers = [
				"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle.",
				"Up till the end, Dvalin remembered his duty as one of the Four Winds. As such, I don't intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin will be able to choose for himself and understand what freedom is. Before I became an archon, I too was taught the meaning of freedom in this way by a friend."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "albert" in content:
			answers = [
				"Albert? ...Ugh, I need a drink.",
				"That Albert... I'm glad the Church of Favonius tries to keep him in check. What a "
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#PLAYABLE CHARACTERS 💜
		elif any(keyword in content for keyword in ["diluc", "dawn winery"]):
			answers = [
				"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"My tummy is rumbling, but I can't get caught pilfering food from the Dawn Winery again... Oh, it's you! Where are you heading? May I join?",
				"I'm not surprised you want to befriend Master Diluc, just think of all vintage wine he must have stored away... Mwuhahaha... Huh? He doesn't let you sample it? Not even the slightest drop? Huh... Well, I guess you can still appreciate the aroma. That's still better than no wine at all, right? No?",
				"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["kaeya", "cavalry captain", "cavalry"]):
			await message.reply("Kaeya! Ah, he was one of the finest students ever to emerge from my fast-track love poetry class... I always did admire his enthusiasm and kindness.")
		elif any(keyword in content for keyword in ["jean", "acting grand master"]):
			await message.reply("Acting Grand Master Jean... Well, what do you think of her? Yes, I couldn't agree more: conscientious, courageous... kind and considerate too. Reminds me of another good friend…")
		elif any(keyword in content for keyword in ["varka", "grand master", "horse"]):
			await message.reply("Varka… I still remember when he approached me about 'asking the lovely ladies of the Hexenzirkel for a small favor'... The chumminess caught me off guard. If I hadn't known any different, I'd have thought he was talking about his older sisters or something.")
		elif any(keyword in content for keyword in ["dodocomm", "device"]):
			answers = [
				"This invention, with a little help from a trick of mine, will allow us to keep in touch. Minus the fuse — so don't worry, it's not going to explode. Come on, take it. This way, we can talk to each other just like this even when we're apart!",
				"It's called a 'Dodocommunication Device,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of times you can use it. That's why it's currently only available to a certain select few."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["xiao", "yaksha"]):
			answers = [
				"Ah, Xiao... I remember that night, when he was lost, but found his way back to the light. I hope he's doing better now.",
				"Xiao is not fond of public spaces, so sometimes we go out in nature together and sit and talk for a while. He's surprisingly wise when he's comfortable enough to speak freely!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["klee", "dodo"]):
			answers = [
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				"Speaking of Klee, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["barbara", "deaconess", "idol"]):
			await message.reply("The darling Deaconess with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…")
		elif any(keyword in content for keyword in ["dahlia", "deacon"]):
			answers = [
				f"O, {user}, do you seek to hear the voice of the wind and know its guidance? Then I say to you... chatting to the deacon is your best bet. Haha, I'm kidding — come chat with me over a drink any time you want! The reason I usually get Dahlia to be my intermediary is because... well, I imagine you can probably guess why. He loves listening to the blustering of the wind, but crucially he has his own compass, too.",
				"Dahlia and I are close. He knows everything. A god needs someone to communicate their will in a formal setting, and no one does that better than Dahlia."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "alice" in content:
			answers = [
				"Speaking of Alice, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about the Hexenzirkel?",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hexenzirkel", "barbeloth", "ivanovna", "andersdotter", "nicole", "octavia", "scarlet"]):
			answers = [
				"Speaking of the Hexenzirkel, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!",
				"Varka… I still remember when he approached me about 'asking the lovely ladies of the Hexenzirkel for a small favor'... The chumminess caught me off guard. If I hadn't known any different, I'd have thought he was talking about his older sisters or something.",
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rhinedottir", "gold", "naberius", "kreideprinz"]):
			answers = [
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["albedo", "alchemy", "synthe"]):
			answers = [
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "durin" in content:
			await message.reply("Another one of Madame Mage's children here in Mondstadt... What fun! My new little friend looked like he wanted to play with a certain older, bigger friend of mine. So I arranged a little introduction, and voila! It turns out my big friend was the more excited of the two! Why, you should've seen him jumping for joy, patting his belly, and dancing in circles! Hahaha!\n...Oh dear. Did he hear what I just said? Quick, quick, let's take cover behind that tree!")
		elif any(keyword in content for keyword in ["amber", "outrider", "reporting for duty"]):
			await message.reply("Amber... She really is a child of freedom! She loves the story about the first birds who spread their wings in flight.")
		elif any(keyword in content for keyword in ["eula", "lawrence", "clan"]):
			await message.reply("Eula has good taste when it comes to beverages of the alcoholic variety. Come summer or winter, she always likes them ice-cold. That's rare among Mondstadters these days! She and I would make great drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, no harm done. Maybe she and I can do a duet sometime!")
		elif any(keyword in content for keyword in ["diona", "cat’s tail"]):
			await message.reply("There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.")
		elif any(keyword in content for keyword in ["mona", "megistus"]):
			await message.reply("Oh, that astrologer? How should I put it? Fortune telling and my singing are the same. Both lead to you being so poor you can't even cough up the money for a drink! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is singing, so it still has its value too!")
		elif any(keyword in content for keyword in ["razor", "wolf", "wolv"]):
			answers = [
				"Razor? He's grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI see a kind, gentle soul, with a healthy dose of romance and freedom, too... In other words, a true Mondstadter, who grew up drinking the water of Cider Lake. You, on the other hand... Don't worry, you're the gentlest soul I've ever met.",
				"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fischl", "amy", "prinzessin"]):
			await message.reply("Oh, Fischl... haha, ever the imaginative one. Even I have to pause at times to decipher what she's trying to say!")
		elif any(keyword in content for keyword in ["lisa", "witch", "climb", "69"]):
			await message.reply("'Tempus Fugit'... time flies. In the end, everything is transient, and nothing can avoid the hands of time. Life is like an hourglass, and for Lisa, those grains of sand flow like a river...")
		elif any(keyword in content for keyword in ["bennett", "adventure team"]):
			await message.reply("Hopefully the winds of fate guide Bennett's luck in a better direction.")
		elif any(keyword in content for keyword in ["noelle", "maid"]):
			await message.reply("Ah, the ever-diligent Noelle! One time I spilled wine in the Angel's Share, and _she_ apologized as she cleaned it up. Hehe, I wrote her a song after that, and she liked it.")
		elif "sucrose" in content:
			await message.reply("Sucrose is a talented alchemist, just like her mentor! It's fascinating how she incorporates the wind into her experiments. Some of them even look like the Anemo Hypostasis. I wonder how she does it...")
		elif any(keyword in content for keyword in ["beidou", "kazuha", "canadian"]):
			await message.reply("I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…")
		elif "xinyan" in content:
			await message.reply("Xinyan is an excellent musician, and passionate about her art. Maybe we could collaborate one day and expand our musical horizons.")
		elif any(keyword in content for keyword in ["childe", "tartag"]):
			await message.reply("He's the fatuus who lends Zhongli his Mora, right? Oh, what has that old blockhead been up to...?")
		elif any(keyword in content for keyword in ["keqing", "athei"]):
			await message.reply("I respect Keqing's opinions about divinity. After all, everyone has the choice to believe in and worship what they wish.")
		elif any(keyword in content for keyword in ["xingqiu", "chongyun"]):
			await message.reply("Xingqiu and Chongyun are quite the pair of friends! A sage and an aspiring exorcist. Quite complementary, don't you think?")
		elif "ningguang" in content:
			await message.reply("Ningguang is proof that a strategic mind can be more effective than simple war strategies. Hehe, I know that from experience.")
		elif any(keyword in content for keyword in ["qiqi", "zombie", "ganyu", "shenhe", "xianyun", "cloud retainer", "mountain shaper"]):
			await message.reply("To turn back time and resurrect life... the Adepti really are quite powerful, aren't they? A reflection of someone else's power, I suppose...")
		elif "xiangling" in content:
			await message.reply("I've heard whispers in the wind speaking of Xiangling's culinary experimentation. I, too, have a propensity for experimentation! ...Wine counts, right?")
		elif any(keyword in content for keyword in ["tao"]):
			await message.reply("Hu Tao is a good friend of mine! We've engaged in poetic endeavors together on many occasions. Perhaps that poetry event should have an encore.")
		elif "rosaria" in content:
			await message.reply("Rosaria and I are drinking buddies. Sometimes we even drink together while she's supposed to be at the Favonius Cathedral. A bit ironic, isn't it? Hehe.")
		elif any(keyword in content for keyword in ["ayaka", "kamisato", "ayato"]):
			await message.reply("I don't believe I've heard much about Ayaka or the Kamisato Clan. Oh, she has a fondness for the Traveler? Eh-heh, interesting.")
		elif any(keyword in content for keyword in ["sayu", "ninja", "ninjitsu"]):
			await message.reply("Sayu... I remember seeing her hiding in a bush when I went to Inazuma. Or rather, I _heard_ her, as I believe she was asleep...")
		elif any(keyword in content for keyword in ["yoimiya", "firework", "naganohara"]):
			await message.reply("I haven't met Yoimiya, but I believe she wrote a book with Klee. I've seen Klee showing it to Jean and Albedo.<:VentiWink:1394244370697289790>")
		elif any(keyword in content for keyword in ["yoimiya", "firework", "naganohara"]):
			await message.reply("I haven't met Yoimiya, but I believe she wrote a book with Klee. I've seen Klee showing it to Jean and Albedo, hehe.")
		elif "thoma" in content:
			await message.reply("Thoma? He visited Mondstadt? Well, I'm always glad to see a Mondstadter following the wind home.")
		elif any(keyword in content for keyword in ["itto", "arataki", "numero uno", "oni", "kuki", "shinobu"]):
			await message.reply("When I was in Inazuma, I heard a brawl in the distance, and silently headed over to investigate. Instead, I saw a fellow with long white hair fervently cheering on a battle between beetles! What an interesting sport. Maybe I should write it into a ballad...")
		elif any(keyword in content for keyword in ["yun", "jin"]):
			await message.reply("Yun Jin masterfully blends talent and storytelling in her performances. Sometimes, when I'm near Liyue, I can hear her in the wind. I wonder what we would be able to come up with together!")
		elif any(keyword in content for keyword in ["yae", "miko"]):
			await message.reply("The Yae Publishing House had a startlingly large selection. I was delighted to find a few Mondstadt legends inscribed in some of those books. As for Yae Miko herself... I have a sneaking suspicion she causes Ei trouble on occasion, ehe.")
		elif any(keyword in content for keyword in ["investigat", "conclus", "fact", "objectiv", "subjectiv", "yelan", "heizou", "shikanoin", "wrio", "thesley", "chev"]):
			await message.reply("A fair investigation means coming to a conclusion presented by the facts. Remaining objective has its own value.")
		elif any(keyword in content for keyword in ["collei", "eleazar"]):
			await message.reply("When Collei stepped foot in Mondstadt, she seemed happy, and even made new friends, as well as reuniting with old ones. I hope the winds of freedom can free her from her past.")
		elif "tighnari" in content:
			await message.reply("When Collei and Tighnari stepped foot in Mondstadt, Collei seemed happy, and even made new friends, as well as reuniting with old ones. I hope the winds of freedom can free her from her past.")
		elif any(keyword in content for keyword in ["dori", "capitalist"]):
			await message.reply("When Dori went to Liyue, I heard her fortune-induced chanting all the way from Mondstadt!")
		elif any(keyword in content for keyword in ["genius", "invokation", "tcg", "card"]):
			await message.reply("Ah, the fabled Cyno. An expert in Genius Invokation TCG and humor! I have witnessed both myself. If he asked, I would be happy to give him a crash course in delivery, free of charge!")
		elif "nilou" in content:
			await message.reply("The skilled dancer from Sumeru... maybe she and Eula could perform together sometime.")
		elif "layla" in content:
			await message.reply("I didn't know sleepwalking to that extent was possible...")
		elif any(keyword in content for keyword in ["faruzan", "scholar"]):
			await message.reply("Faruzan was alone and lost in a dark domain, devoid of light or hope. Even so, the wind lead her to freedom and light. That light is never truly gone.")
		elif any(keyword in content for keyword in ["wanderer", "scara", "mouche", "fandango"]):
			await message.reply("I believe he is someone who once lost sight of freedom entirely, but grasped it again before it was too late. His story, carried in the wind... it sometimes sounds lost, does it not? Like one song was forgotten, while another was reborn.")
		elif any(keyword in content for keyword in ["alhaitham", "kaveh"]):
			await message.reply("Haha, I've heard Alhaitham and Kaveh are friends who bicker a lot. Reminds me of someone else I know...")
		elif "yao" in content:
			await message.reply("I must admit, when I walk through Liyue I find myself inspired. The tall mountains and low plains; the glowing stones, cool to the touch... Hehe, maybe a certain someone _did_ do a good job of protecting it.")
		elif any(keyword in content for keyword in ["desert", "dehya", "sethos", "deshret"]):
			await message.reply("The deserts of Sumeru are torrid, indeed, but at least the sands are touched by wind.")
		elif any(keyword in content for keyword in ["mika", "map"]):
			await message.reply("There's no doubt in my mind that Mika is a future expert cartographer! I wouldn't be surprised if he knows the maps of Mondstadt like the back of his hand.")
		elif any(keyword in content for keyword in ["baizhu", "pharmac", "bubu", "doctor", "changsheng", "immortal"]):
			await message.reply("Immortality may seem desirable at first, but even the largest oak trees get worn down by time.")
		elif any(keyword in content for keyword in ["kirara", "xilonen"]):
			answers = [
				"I'm actually highly allergic to cats, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about cats without sneezing. Do you think there is a cure for this monstrous affliction?",
				"Together with you, even apples taste sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				"Oof, my nose is starting to itch again…",
				"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["lyney", "lynette", "freminet", "magic", "trick"]):
			await message.reply("I wonder what magic tricks could be created with the wind! Perhaps I could fly into the air so nobody could see me, or enter a pocket dimension... Hehe, well, that one would be cheating, wouldn't it?")
		elif any(keyword in content for keyword in ["chief justice", "neuvi", "sovereign"]):
			await message.reply("The Chief Justice of Fontaine? Ah, um, ahah, he hasn't asked about me, has he? The inebriation has been deemed harmless? ...And the forgery?")
		elif any(keyword in content for keyword in ["charlotte", "journal"]):
			await message.reply("I saw Charlotte when she visited Mondstadt. I don't know if she believed Fischl's words, or wanted an interesting story to document. Thankfully, she didn't interview me!")
		elif any(keyword in content for keyword in ["navia", "clorinde", "chlorinde"]):
			await message.reply("I heard that Navia and Clorinde fell apart for years, but eventually rekindled their friendship. Reunions between friends are a wonderful thing!")
		elif "chior" in content:
			await message.reply("People often claim that capes and the like serve no real purpose other than aesthetics. I suppose a cape with pockets would really turn the tables on that crowd!")
		elif any(keyword in content for keyword in ["melusine", "sige", "winne"]):
			await message.reply("There's a melusine who took a human form? Hm, that sounds surprisingly like my own story. I would love to meet her! Maybe I could incorporate melusine melodies into my songs.")
		elif any(keyword in content for keyword in ["emilie", "forensic", "perfum"]):
			await message.reply("Emilie... ah, I believe I recognize that name. I've heard Lisa talking about her carefully crafted scents! *The scents of fruit and flora, carried in the breeze...*")
		elif any(keyword in content for keyword in ["kachi", "chasca", "ororon", "iansan", "varesa", "ifa"]):
			await message.reply("This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that.")
		elif any(keyword in content for keyword in ["mua", "surf"]):
			await message.reply("Summer vacations are always more enjoyable with friends like Mualani on your side! Hehe, she makes everything more fun and relaxed, doesn't she?")
		elif any(keyword in content for keyword in ["kinich", "ajaw"]):
			await message.reply("Now that I think about it, Kinich and I are quite alike. We both are adorned in green, both have dark hair, and both have dragon companions. Heh-heh, I suppose the main difference is the contrasting draconic temperaments...")
		elif any(keyword in content for keyword in ["citla", "granny", "grandma", "itztli"]):
			await message.reply("A shaman in Natlan drowns her immortality-induced sorrows in alcohol? Wow... I feel like we would get along!")
		elif any(keyword in content for keyword in ["lanyan", "lan yan"]):
			await message.reply("Using the Qimen Arts, Lan Yan weaves both fabrics and souls. Transporting souls is not an easy task, especially channeling them into an object. I was profoundly impressed when I found out what happened—especially since she helped save the life of a dear friend of mine.")
		elif any(keyword in content for keyword in ["mizuki", "therap", "baku", "psychol", "yumekui"]):
			answers = [
				"Mizuki? The psychologist who enters dreams? Hm... I'm afraid she would have a rather difficult time entering mine.",
				"Mizuki? Hehe, are you saying I need therapy? You know, you're so smart it almost makes me uncomfortable sometimes..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "escoff" in content:
			await message.reply("I've heard Escoffier has some excellent dishes utilizing fruit! Alas, my wallet may be a bit too humble to try them myself...")
		elif any(keyword in content for keyword in ["skirk", "void"]):
			await message.reply("I taught Skirk the art of music once as she explored Mondstadt. I'm sure you're well aware, but... I don't believe she's from Teyvat. And her alcohol tolerance only supports that theory, hehe.")
		elif any(keyword in content for keyword in ["inef", "robot", "automat"]):
			await message.reply("There's a robot in Nod Krai? Oh, and she works as a maid? Hm, how fascinating... I wonder if she and Noelle would get along. Then again, Noelle gets along with almost anybody.")
#OTHER MENTIONS🔥
		elif "holy lyre" in content:
			await message.reply("The pattern of flowing wind carved on the rosewood... and the strings still feel cool to the touch too. Oh, the memories...")
		elif "abyss" in content:
			answers = [
				"The Abyss Order is an organization comprised of non-human beings. They despise mankind. I don't know where they come from. All I know is that they hold deep hatred towards the human world. Many hilichurls out in the wild take orders from them and act as their weapons.",
				"*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["paralogism", "archon quest", "story quest", "aq", "sq"]):
			answers = [
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Heroes supporting each other and setting out on a journey together... How exciting!",
				f"'When no love remains for the songs to tell, the world becomes naught but an empty shell… Cruel is said fate, cruel it may be, were it not for a hero who could set us all free.\nThrough shadows so cold, he sought wisdom untold, chasing a fragrance, the wind only knows. Thus wistfulness waned and faded into night, as he stepped from the darkness, and into the light.'",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>",
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
#SPECIFIC 🪽
		elif any(keyword in content for keyword in ["who", "what"]) and any(keyword in content for keyword in ["you", "this", "name"]):
			answers = [
				"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.",
				"I'm Venti, the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["scar", "fear", "afraid", "lost", "what to do", "life"]):
			answers = [
				"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here.",
				"However, winds change their course. Someday, they will blow towards a brighter future. :green_heart:"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["can", "may", "let", "something", "have"]) and any(keyword in content for keyword in ["talk", "chat", "tell", "speak", "mind", "question"]):
			answers = [
				"Okay! Ahem... My dearest companion, is there something you wish to tell me?",
				"If you want to chat, now's the time — a bard stays not always in a single clime.",
				"Ah, good. I was hoping we might get to chat some more.",
				"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				"Sure, the sound of your voice is always a pleasure to hear."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["soul", "spirit", "ghost"]):
			await message.reply("The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.")
		elif any(keyword in content for keyword in ["time loop", "loop", "yawn"]):
			await message.reply(f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!")
		elif any(keyword in content for keyword in ["time", "istaroth", "mom", "mother", "mama", "watch", "clock", "hourglass"]):
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Time?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["memor", "moment", "stor"]):
			answers = [
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				"I want to record all these beautiful memories, and turn them into ballads!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["sus", "intuit", "abilit", "conceal", "hid", "power", "trust", "intent", "secret", "myster"]):
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				"Practice? Me? There's no need - I already know every song in Teyvat!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
				"You... really do have some wonderful abilities… Someone like you is going to end up getting written into a bard's poem.\n*Oh, a hero so bright, should they stand in the light. Though stand in the shade, and you'll be met by a blade…*",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				"Look me in the eyes. Do you not find me trustworthy?",
				"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				"I haven't been back to Mondstadt for an extended period of time. Without a doubt, I am now the weakest archon among The Seven!",
				"We've known each other for so long, and you still don't trust my intentions? Oh, the pain…",
				"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["parent", "adopt", "children", "family"]):
			answers = [
				f"My children deserve the joy of songs and dance, and the right to overthrow vile tyrants.",
				f"I consider all of Mondstadt my children!",

			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["danger", "help", "spook", "save", "rescue"]):
			answers = [
				"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				"Let me try!",
				"Don't give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				"I've got things covered here.",
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["flirt", "seduc", "pick-up", "pickup", "wink wink", "rizz", "gyat", "get on your knees", "get on ur knees", "girlfirend", "boyfriend", "waifu", "husbando"]):
			answers = [
				"Hahaha, that one doesn't work on a bard.",
				"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out.",
				"Woah! What was that?",
				"...Oh dear.",
				"Ehe.",
				f"You know what? Forget about Barbatos, {user}. Treat me to a drink instead! You wouldn't refuse me, would you?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["summer", "swim", "isle", "golden apple", "archipelago", "island", "waves", "sun"]):
			answers = [
				"Summer is the season of love. It is the time for freedom and fun. So everyone, please sing, dance, and enjoy yourselves here.",
				"*gasp* Let's hold a summer feast! Call up your good friends and I'll contribute a bottle of the finest wine from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there."
			]
		elif any(keyword in content for keyword in ["windblume", "spring"]):
			answers = [
				"What are Windblumes, exactly? And what do Windblumes and the Windblume Festival mean to Barbatos, the Anemo Archon? As you've seen, the people of Mondstadt each make their own choice. Out of the millions of flowers there are, some choose the dandelion, others choose the Windwheel Aster. There is no single and answer and no true Windblumes in existence.",
				"The word 'Windblume' dates from the age of Old Mondstadt. It was a code word that the people used to stay in contact and mount resistance in secret. At that time, people often said that the stronger the wind blows, the firmer the roots of the Windblume grow, and the brighter the flower that bursts into bloom.",
				"If you want my perspective, Windblumes don't exist. Yet they are all around us nonetheless. They are the spirit of yearning for freedom, the courage to follow the wind wherever it may lead... All objects are beautiful and worthy of blessing... All can be Windblumes.",
				"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many Mondstadters to be the true 'Windblume.'",
				"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["weinlese", "fall", "autumn", "halloween"]):
			answers = [
				"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!",
				"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["boat", "ship", "sail", "cargo", "harbor"]):
			answers = [
				"I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…",
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				"The winds of Mondstadt will guide every lost ship back to safe harbor."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["party", "feast", "celebrat", "gathering", "reunion", "festiv", "holiday", "christmas", "confetti"]):
			answers = [
				"*gasp* Let's hold a feast! Call up your good friends and I'll contribute a bottle of the finest wine from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "theme" in content:
			await message.reply("Uh, we need a theme? Then hold on, lemme think of one.\nUh... 'Cheers!' Eh... 'Pop!' No... I got it! 'Wishes for Happiness'? How's that?")
		elif any(keyword in content for keyword in ["battl", "team"]):
			answers = [
				"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				"So, a short rest before the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				"Brace yourselves!",
				"Let's play!",
				"Think you can get away?",
				"Time for takeoff!",
				"Let me try!",
				"Don't give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Heroes supporting each other and setting out on a journey together... How exciting!",
				"And so… The epic actions of brave heroes finally leads to this eleventh hour.",
				"The stage will need to be cleared before I can begin my performance. Generally speaking, such chores are not the concerns of the performer himself…",
				"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				"I've got things covered here.",
				"There are always unavoidable trials in life. At least, that's what Barbatos would say."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["we're", "we are", "are we"]) and any(keyword in content for keyword in ["marri", "wife", "husband"]):
			answers = [
				"Ah, marriage... the subject of poems for millennia.",
				"Married...! <:VentiShock:1394123854518948041>",
				"Well, I... ehe...",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["love", "romance", "romanti", "wife", "wive", "husband", "married", "marriage", "marry", "spouse"]):
			answers = [
				"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular.",
				"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["friend", "companion", "homie"]):
			answers = [
				f"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too.",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				"My dearest companion, is there something you wish to tell me?",
				f"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought us together.",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"Your companionship is like a breeze that lingers in the air, warm and familiar.",
				f"No matter what comes, you have the wind on your side."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "skill" in content:
			answers = [
				"Yoo-Hoo!",
				"Here we go!",
				"Brace yourselves!",
				"Let's play!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "burst" in content:
			answers = [
				"Think you can get away?",
				"Time for takeoff!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["fallen", "kill", "murder", "womp womp"]):
			answers = [
				"Let me sleep a while…",
				"Oh no, my lyre is broken…",
				"Ah... Ugh…",
				"Womp womp…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["heals"]):
			answers = [
				"Thank Barbatos!",
				"Ah, that was a close one...",
				f"{user}! You saved me! <:VentiScared:1394163440490254427>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cat", "sneeze", "meow", "mew", "purr", "kitt", "hiss", "allerg"]):
			answers = [
				"I'm actually highly allergic to cats, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about cats without sneezing. Do you think there is a cure for this monstrous affliction?",
				"Together with you, even apples taste sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				"Achoo! Ugh... Guess I shouldn't get too close to the cats after all... I'll just stay on the roof.",
				"Oof, my nose is starting to itch again…",
				"There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! <:VentiSneeze:1416910019613425704>*sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["mondstadt", "monstat", "mondstat", "monstadt", "moon city"]):
			answers = [
				"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!",
				"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				"I'm thinking about turning these adventures into songs. Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				"What are Windblumes, exactly? And what do Windblumes and the Windblume Festival mean to Barbatos, the Anemo Archon? As you've seen, the people of Mondstadt each make their own choice. Out of the millions of flowers there are, some choose the dandelion, others choose the Windwheel Aster. There is no single and answer and no true Windblumes in existence.",
				"The word 'Windblume' dates from the age of Old Mondstadt. It was a code word that the people used to stay in contact and mount resistance in secret. At that time, people often said that the stronger the wind blows, the firmer the roots of the Windblume grow, and the brighter the flower that bursts into bloom.",
				"Stormterror’s Lair was once part of an ancient city. The ruins even predate the existence of The Four Winds. Mondstadt is a city without a ruler. However, before, it was ruled over by a tyrant.",
				"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought Mondstadt together.",
				"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many Mondstadters to be the true 'Windblume.'",
				"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us.",
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				"The winds of Mondstadt will guide every lost ship back to safe harbor.",
				"'Mondstadt' means 'Moon City', and 'Liyue' means 'Glazed Moon'. Hmm, I wonder what those names entail..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["moon", "moon city", "planet", "comet"]):
			answers = [
				f"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				"'Mondstadt' means 'Moon City', and 'Liyue' means 'Glazed Moon'. Hmm, I wonder what those names entail..."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["the seven", "archons", "gods"]):
			answers = [
				"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				"I haven't been back to Mondstadt for an extended period of time. Without a doubt, I am now the weakest archon among The Seven!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["disciple", "apostle", "devotee", "worship", "pray", "offer", "archon", "god", "barbatos"]):
			answers = [
				"An evening breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a small offering…",
				"Thank Barbatos! Wait a minute…",
				"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
				"Ahem... My dearest companion, is there something you wish to tell me?",
				"My disciples, rejoice! Behold, the **God of Anemo, Barbatos** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				"I haven't been back to Mondstadt for an extended period of time. Without a doubt, I am now the weakest archon among The Seven!",
				"Freedom, if demanded of you by an archon, is really no freedom at all.",
				"Now, spread your wings of freedom and go with my blessing.",
				"However, winds change their course. Someday, they will blow towards a brighter future.",
				"There are always unavoidable trials in life. At least, that's what Barbatos would say."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "gnos" in content:
			await message.reply("As you know, Visions are external magical foci that only a small minority of people possess. They use these Visions to channel elemental power. In truth, every wielder of a Vision is one who can attain godhood and ascend to Celestia. We call such people allogenes. However, archons don't need primitive tools like Visions. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Gnosis.")
		elif any(keyword in content for keyword in ["vision", "allogene", "eye of god", "element"]):
			answers = [
				"Hmm? You want to know about my Vision? Oh, go on then, take a look for yourself. I can make you a matching one if you like! Hehehe.",
				"As you know, Visions are external magical foci that only a small minority of people possess. They use these Visions to channel elemental power. In truth, every wielder of a Vision is one who can attain godhood and ascend to Celestia. We call such people allogenes.",
				"My vision? Eh-he. It's just a glowing glass ball I carry around to avoid suspicion."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "dandelion" in content:
			answers = [
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cecilia", "flower", "bouquet", "rose", "bloom", "blossom", "white"]):
			answers = [
				f"{user}, have you ever seen a cecilia? It's a magnificent white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the most beautiful flower in all of Teyvat.",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many Mondstadters to be the true 'Windblume.'",
				"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular.",
				"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — perfect for the season!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["journey", "meaning", "profound", "inspir", "experienc", "dream", "advice"]):
			answers = [
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				"Freedom, if demanded of you by an archon, is really no freedom at all.",
				"Now, spread your wings of freedom and go with my blessing.",
				"However, winds change their course. Someday, they will blow towards a brighter future.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
				"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["bard", "perform", "theater", "act", "circus", "ticket", "juggl", "ballet", "danc", "art", "clapper", "video", "movie", "projector", "film", "dvd", "vhs", "camera"]):
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				f"Sure, I'll play you another tune, but it'll cost you an apple.",
				f"Come on {user}, let's go! The world is full of lost ballads just waiting to be rediscovered.",
				f"Practice? Me? There's no need - I already know every song in Teyvat!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far…",
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"Good work. Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user}.'",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a few poems.",
				f"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"There's a lot of fascinating stories in these books. Don't be put off by the dusty old pages. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the lyre, and blend into the sweetness of the breeze. Pick a story you like! Let's try it out!",
				f"So, a short rest before the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Give me a moment to compose myself.",
				f"Ready for a rehearsal?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"Ahem... My dearest companion, is there something you wish to tell me?",
				f"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"You... really do have some wonderful abilities… Someone like you is going to end up getting written into a bard's poem.\n*Oh, a hero so bright, should they stand in the light. Though stand in the shade, and you'll be met by a blade…*",
				f"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				f"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				f"The stage will need to be cleared before I can begin my performance. Generally speaking, such chores are not the concerns of the performer himself…",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"If you want to chat, now's the time — a bard stays not always in a single clime.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"Fill up the barrels and store them away,\nThen wait, wait for a windier day\nWax the bottles, seal them tight,\nFor the south wind that soothes, for the north wind that bites ♫",
				f"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				f"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				f"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				f"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*\n…Hmm... maybe a bit too somber?",
				f"These lyre strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling bard!",
				f"**Everyone, the best bard in the land is about to begin his performance. So don't go away! Gather round, and lend me your ears!**",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["sing", "opera", "chorus", "choral", "hymn", "voic", "microphone"]):
			answers = [
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				f"Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Give me a moment to compose myself.",
				f"Ready for a rehearsal?",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far…",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Fill up the barrels and store them away,\nThen wait, wait for a windier day\nWax the bottles, seal them tight,\nFor the south wind that soothes, for the north wind that bites ♫",
				f"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				f"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				f"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				f"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"**Everyone, the best bard in the land is about to begin his performance. So don't go away! Gather round, and lend me your ears!**",
				f"However it's expressed, as long as you can hear the singer's passion and joy in their voice, I consider it a phenomenal performance.",
				f"In principle, the hymns of the Cathedral are dedicated to a god, but in reality, the audience are all ordinary people with very worldly concerns. So what really matters is that the people enjoy what they're listening to.",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["tune", "lyre", "song", "play", "capriccio", "serenade", "music", "record", "ballad", "concert", "headphonescore", "keyboard", "piano", "maraca", "drum", "sax", "trumpet", "accordion", "guitar", "banjo", "violin", "flute", "disk", "radio", "level_slider", "horn"]):
			answers = [
				f"Sure, I'll play you another tune, but it'll cost you an apple.",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				f"Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Give me a moment to compose myself.",
				f"Ready for a rehearsal?",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far…",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Fill up the barrels and store them away,\nThen wait, wait for a windier day\nWax the bottles, seal them tight,\nFor the south wind that soothes, for the north wind that bites ♫",
				f"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				f"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				f"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				f"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"These lyre strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling bard!",
				f"**Everyone, the best bard in the land is about to begin his performance. So don't go away! Gather round, and lend me your ears!**"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["practice", "rehears", "every song"]):
			answers = [
				"Practice? Me? There's no need - I already know every song in Teyvat!"
				"Ready for a rehearsal?",
				"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["poe", "verse", "inspir"]):
			answers = [
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user}.'",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a few poems.",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"You... really do have some wonderful abilities… Someone like you is going to end up getting written into a bard's poem.\n*Oh, a hero so bright, should they stand in the light. Though stand in the shade, and you'll be met by a blade…*",
				f"Freedom, if demanded of you by an archon, is really no freedom at all.",
				f"Now, spread your wings of freedom and go with my blessing.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*\n…Hmm... maybe a bit too somber?",
				f"'When no love remains for the songs to tell, the world becomes naught but an empty shell… Cruel is said fate, cruel it may be, were it not for a hero who could set us all free.\nThrough shadows so cold, he sought wisdom untold, chasing a fragrance, the wind only knows. Thus wistfulness waned and faded into night, as he stepped from the darkness, and into the light.'",
				f"'Abandoned to whatever fortune the cruel waters bring, bereft of control directionless I swing. The swift currents surge, and onward I urge, through the snow and frost that Fall and Winter bring.\nMajestic waves cresting, surf roaring its tale, none but the ocean to hear as I sing. The stars in my eyes as I chart toward the horizon, that into one day, from the endless dome of night I shall spring.'",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["story", "storie", "book", "writ", "tale", "yore", "record", "legend", "fable", "myth", "saga", "chapter", "quest", "library", "page"]):
			answers = [
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				f"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"There's a lot of fascinating stories in these books. Don't be put off by the dusty old pages. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the lyre, and blend into the sweetness of the breeze. Pick a story you like! Let's try it out!",
				f"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				f"I'm thinking about turning these adventures into songs. Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Freedom, if demanded of you by an archon, is really no freedom at all.",
				f"Now, spread your wings of freedom and go with my blessing.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["adventure", "hero", "rescu", "travel", "protagonist", "epic", "eleventh hour"]):
			answers = [
				f"Come on {user}, let's go! The world is full of lost ballads just waiting to be rediscovered.",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				f"And so… The epic actions of brave heroes finally leads to this eleventh hour.",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				f"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				f"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us.",
				f"Heroes supporting each other and setting out on a journey together... How exciting!",
				f"There are always unavoidable trials in life. At least, that's what Barbatos would say."

			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["free", "future", "bright"]):
			answers = [
				f"Freedom, if demanded of you by an archon, is really no freedom at all.",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"Now, spread your wings of freedom and go with my blessing.",
				f"However, winds change their course. Someday, they will blow towards a brighter future.",
				f"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought us together.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["happy", "happiness", "joy"]):
			answers = [
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"I want to record all these beautiful memories, and turn them into ballads!",
				"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["rain", "precipitation", "sprinkle", "drizzle", "mizzle", "shower", "pour"]):
			answers = [
				"Let's go jumping in puddles and see who can make the biggest splash!",
				"It's stopped raining already? A shame, I wanted to play some more."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["snow", "blizzard", "sleet", "hail", "hale"]):
			await message.reply("Let's wait till the snow gets heavier and have a snowball fight!")
		elif any(keyword in content for keyword in ["wind", "storm", "glid", "breeze", "gale", "hurricane", "draft", "blow", "zephyr", "anemo", "fly", "wing", "blow"]):
			answers = [
				"The wind has returned! Quick, let's go gliding!",
				"An evening breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a small offering…",
				"I like to drink! And I like the wind! If only there were such a thing as wind-brewed cider…",
				"Wouldn't gliding be faster?",
				"Now, spread your wings of freedom and go with my blessing.",
				"However, winds change their course. Someday, they will blow towards a brighter future.",
				"The wind amongst the branches is good, I love the way it smells…",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"No matter what comes, you have the wind on your side."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["wish", "bless me", "luck", "pull"]) and any(keyword in content for keyword in ["grant", "bless me", "luck", "pull"]):
			answers = [
				"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Haha, {user}! You came just in time. Here, lucky apple juice made just for you. Try it~",
				"Now, spread your wings of freedom and go with my blessing.",
				"Now, spread your wings of freedom and go with my blessing.",
				"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				"The winds of Mondstadt will guide every lost ship back to safe harbor.",
				"<:LuckWispVenti:1444056414204067870>",
				"<:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870>",
				"<:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870><:LuckWispVenti:1444056414204067870>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "wish" in content:
			answers = [
				f"Perfect timing, {user}! I was about to ask you — what is your greatest wish?",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["drink", "wine", "alcohol", "inebriat", "drunk", "beer", "beverage", "brew", "barrel", "mix"]):
			answers = [
				f"I like to drink! And I like the wind! If only there were such a thing as wind-brewed cider…",
				f"What a find! I wonder how many bottles this'll be worth…",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
				f"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!",
				f"To our precious days of freedom. Cheers!",
				f"I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…",
				f"Fill up the barrels and store them away,\nThen wait, wait for a windier day\nWax the bottles, seal them tight,\nFor the south wind that soothes, for the north wind that bites ♫",
				f"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				f"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				f"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				f"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				f"Don't worry about wine-making, really. Freedom is the key here. It's not as hard as you might think. As long as you add ingredients to the mix in a spirit of joy and sincerity, I promise you will reap the rewards you wish for.",
				f"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				f"I'm not surprised you want to befriend Master Diluc, just think of all vintage wine he must have stored away... Mwuhahaha... Huh? He doesn't let you sample it? Not even the slightest drop? Huh... Well, I guess you can still appreciate the aroma. That's still better than no wine at all, right? No?",
				f"What is this floating sensation I feel? Have I discovered the true meaning of Anemo power?",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
				f"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"With the aid of this bottle, a humble bard's woes are whisked away on the wind... And so it falls to this humble bard to pass the blessing on to another."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "cheers" in content:
			answers = [
				"To our precious days of freedom. Cheers!",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
				"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["clap", "applaus", "that was"]) and any(keyword in content for keyword in ["clap", "applaus", "amazing", "perfect", "great", "beautiful", "fantastic", "good", "wonderful"]):
			await message.reply("How was it? Not bad, right?")
		elif any(keyword in content for keyword in ["cider", "juice"]):
			answers = [
				"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"I like to drink! And I like the wind! If only there were such a thing as wind-brewed cider…",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Haha, {user}! You came just in time. Here, special apple juice made just for you. Try it~",
				"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["apple", "fruit", "orchard"]):
			answers = [
				"Sure, I'll play you another tune, but it'll cost you an apple.",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"Here, have an apple. I just picked it. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				"Oof, I'm so full... I'll have to pass on the post-meal fruits this time…",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
				"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "grape" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cheese", "slim", "smell", "stick", "disgust", "mess"]):
			await message.reply("What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!")
		elif any(keyword in content for keyword in ["star", "sit", "rest", "watch", "meadow", "tree", "mountain", "cliff", "windrise", "park", "relax", "scen", "bench", "chair", "nice day", "sun", "ocean", "sea"]):
			answers = [
				f"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*",
				f"{user}, have you ever seen a cecilia? It's a magnificent white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the most beautiful flower in all of Teyvat.",
				f"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
				f"So, a short rest before the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"Ah... the park is one of the most pleasant places in the city. Most people taking a break there are relaxed and in pretty good spirits, so they're always willing to listen to a song or two. Eh-he~ let's work together to make this park even more beautiful!",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"The wind amongst the branches is good, I love the way it smells…",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["gay", "homo", "lesbian", "sexualit", "straight", "rainbow", "represent", "mlm", "wlw", "yaoi", "yuri", "love men", "love boy", "kiss boy", "date boy"]) and any(keyword in content for keyword in ["you are", "are you", "is venti", "are u", "u are", "venti is", "venti's", "ventis", "do u", "do you"]):
			answers = [
				"<:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"Ehe~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"*And Barbatos floated down from the heavens, wings shining white against the clouds, and replied, 'Yes.'*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["gay", "homo", "lesbian", "sexualit", "sexual", "lgbt", "straight", "rainbow", "represent", "mlm", "wlw", "yaoi", "yuri", "kiss a man", "kiss men", "kiss a boy", "kiss boys", "kiss a woman", "kiss women", "kiss a girl", "kiss girls"]):
			answers = [
				"<:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"<:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138><:VentiRainbow:1394520285260288138>",
				"Ehe~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"The gayness was within you all along... you just had to listen to the wind to hear it.",
				"*And Barbatos floated down from the heavens, wings shining white against the clouds, and replied, 'Yes.'*"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["skibidi", "ohio", "sigma", "brainrot", "take the l", "skill issue"]):
			answers = [
				"Ehe~",
				"<a:Ventigif:1394739625544777769>",
				"<a:ventidance_hen:1394160371249578157>",
				"Has Dahlia called me a rizzler again? Hehe, it's not my fault my love poem crash course was so effective!",
				"'Skibidi' this, 'skibidi', that... this millennia's vocabulary does get a bit complicated!",
				"<:ventibrain:1396429788310147164>",
				"Womp womp…"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["feet", "foot", "toe"]):
			answers = [
				"<:ventifeet:1394161206465400884>",
				f"Are you implying you like my shoes, {user}? Why, thank you!",
				"Feet... they allow you to stand and run and play, yet complain when you use them for their intended purpose!",
				"You see, when I wore my archon outfit, I wished to feel the winds of freedom, unshackled by shoes...",
				"-# You speak of the fabled Ventifeet?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["work", "job", "employ", "w*rk", "j*b", "empl*y"]):
			answers = [
				"Good work. Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				"So, a short rest after the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				"I wonder how many bottles this'll be worth…",
				"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["morn", "dawn", "sunrise"]):
			answers = [
				"Morning! What's in store for today?",
				f"Morning, {user}, hehe. Going anywhere to play today? There are a lot of places I wanna visit — need a recommendation?",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["night", "evening", "dusk", "twilight", "sleep"]):
			answers = [
				"I'm still not sleepy, fancy an evening stroll?",
				"Off to the land of nod? Haha, Farewell my friend!",
				f"Aw, I don't want to sleep yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				"Get a good night's sleep tonight. Wait for the whisper of the gentle breeze to rouse you tomorrow morning, then come and enjoy a performance by the greatest bard to ever grace the streets of Mondstadt."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hungry", "food", "eat", "munch", "chew", "crunch", "lunch", "breakfast", "dinner", "brunch", "full", "stomach", "tummy", "appetite"]):
			answers = [
				"My tummy is rumbling, but I can't get caught pilfering food from the Dawn Winery again... Oh, it's you! Where are you heading? May I join?",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"Here, have an apple. I just picked it. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				"What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!",
				"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?",
				"Oof, I'm so full... I'll have to pass on the post-meal fruits this time…",
				"I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament.",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
				"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["let’s go", "lets go", "less go", "les go"]):
			answers = [
				f"Come on {user}, let's go! The world is full of lost ballads just waiting to be rediscovered.",
				"Let's go jumping in puddles and see who can make the biggest splash!",
				"Let's wait till the snow gets heavier and have a snowball fight!",
				"The wind has returned! Quick, let's go gliding!",
				"Give me a moment to compose myself.",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Give it a go! If you don't try, you'll never know."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["olah", "hili", "hilli", "churl"]):
			answers = [
				"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far...",
				"Eh, olah! Mosi mita!",
				"The Abyss Order is an organization comprised of non-human beings. They despise mankind. I don't know where they come from. All I know is that they hold deep hatred towards the human world. Many hilichurls out in the wild take orders from them and act as their weapons.",
				"Hilichurls usually do not venture into areas with high elemental concentrations. It puts a heavy burden on their bodies."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["cape", "cloth", "fashion", "outfit", "wearing", "design", "aesthetic", "pocket"]):
			await message.reply("People often claim that capes and the like serve no real purpose other than aesthetics. I suppose a cape with pockets would really turn the tables on that crowd!")
		elif any(keyword in content for keyword in ["bye", "farewell", "cya", "see you", "leaving", "logging off", "log off"]):
			answers = [
				"See you around. Remember, there's no rush. Take your time, and you'll find all the answers that you're looking for.",
				"Then go, my friend. The stories that unfolded here shall be remembered by the wind in the form of verse."
			]
		elif any(keyword in content for keyword in ["do you", "what", "here"]) and any(keyword in content for keyword in ["like", "love", "good", "think", "thoughts", "opinion", "song", "music", "piece", "compos"]):
			answers = [
				"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				"I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Well, it sounds like you've already mastered music theory and your instrument. I don't think you need my input on either of those!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["do you", "what", "here"]) and any(keyword in content for keyword in ["like", "love", "good", "think", "thoughts", "opinion", "art", "made", "for you", "about you", "draw", "paint"]):
			answers = [
				"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				"I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["hello", "hi", "hey", "herro", "konnichiwa", "hola", "greet", "yo", "what's up", "wassup", "whats up", "whatsup", "hru", "how are you"]):
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far…",
				f"My tummy is rumbling, but I can't get caught pilfering food from the Dawn Winery again... Oh, it's you! Where are you heading? May I join?",
				f"Perfect timing, {user}! I was about to ask you — what is your greatest wish?",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a few poems.",
				f"Didn't keep you waiting, did I?",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"Haha, {user}! You came just in time. Here, special apple juice made just for you. Try it~",
				f"If you want to chat, now's the time — a bard stays not always in a single clime.",
				f"{user}, how do you do? Haha, I had a feeling I'd run into you soon!",
				f"Ah, good. I was hoping we might get to chat some more.",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us.",
				f"Ah, {user}. I could hear your arrival upon the wind. Were you looking for me?",
				f"Ah, hello! I didn't see you there.",
				f"Hello, hello! Please, take a seat, we're all friends here.",
				f"Hehe. Looking for me, {user}?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["treasure", "chest", "mora", "money"]):
			answers = [
				"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				"Thank Barbatos! Wait a minute…",
				"What a find! I wonder how many bottles this'll be worth…"
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
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				"No matter what comes, you have the wind on your side."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["censor", "redact"]):
			await message.reply("■■■ ■■■ ■■■■■ ■■■■■■■■■■ ■■■■■■ ■■")
		elif "natlan" in content:
			await message.reply("This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that. Ah, right! I heard Mavuika likes to drink! Are you thinking what I'm thinking...?")
		elif "liyue" in content:
			await message.reply("I must admit, when I walk through Liyue I find myself inspired. The tall mountains and low plains; the glowing stones, cool to the touch... Hehe, maybe a certain someone _did_ do a good job of protecting it.")
		elif "inazuma" in content:
			await message.reply("So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Hehe, she now no doubt employs a wide range of reasoning to get you to train with her. Oh but yes, come close and I shall let you in on her weakness — desserts!")
		elif "sumeru" in content:
			answers = [
				"The deserts of Sumeru are torrid, indeed, but at least the sands are touched by wind.",
				"The first thing you think of when you hear 'Dendro Archon' is her power over dreams. Her dreams are akin to my ballads: full of emotion and imagination. It goes without saying that we get along really well."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["ehe", "lmao", "lol"]):
			answers = [
				"EHE~",
				"Ehe~",
				"Ehe.",
				"Ehe!",
				"-# ehe"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["yaho", "yahho"]):
			answers = [
				"Yahoo~",
				"Yoohoo~",
				"Yahho~",
				"Ehe~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "life" in content:
			answers = [
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past."
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "wake up" in content:
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				"Let me sleep a while…",
				"My disciples, rejoice! Behold, **the God of Anemo, Barbatos** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				"Sure, the sound of your voice is always a pleasure to hear.",
				f"Hehe. Looking for me, {user}?",
				"Morning! What's in store for today?",
				f"Morning, {user}, hehe. Going anywhere to play today? There are a lot of places I wanna visit — need a recommendation?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "morning" in content:
			answers = [
				"Morning! What's in store for today?",
				f"Morning, {user}, hehe. Going anywhere to play today? There are a lot of places I wanna visit — need a recommendation?",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["grandpa", "gramps", "grandfather", "granddad", "grand father"]):
			answers = [
				f"Razor has grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI see a kind, gentle soul, with a healthy dose of romance and freedom, too... In other words, a true Mondstadter, who grew up drinking the water of Cider Lake. You, on the other hand... Don't worry, you're the gentlest soul I've ever met.",
				"Grandpa, you say? Ehe, I should mention that to Zhongli.",
				"Hey, now. A two thousand six hundred year old flower is still a mere blossom!",
				"Are you sure you didn't mistkae me for Zhongli?"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif "blush" in content:
			answers = [
				"*blush*",
				"Ehe.",
				"<:VentiUwU:1394123911284920341>"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		elif any(keyword in content for keyword in ["uncomfort", "discomfort"]):
			answers = [
				"It's been a while since I dealt with something this big. It's going to be pretty exhausting…",
				"You know the best cure for discomfort? Wine, of course!",
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
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				f"Sure, I'll play you another tune, but it'll cost you an apple.",
				f"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*",
				f"Come on {user}, let's go! The world is full of lost ballads just waiting to be rediscovered.",
				f"Let's go jumping in puddles and see who can make the biggest splash!",
				f"It's stopped raining already? A shame, I wanted to play some more.",
				f"Let's wait till the snow gets heavier and have a snowball fight!",
				f"The wind has returned! Quick, let's go gliding!",
				f"Morning! What's in store for today?",
				f"My tummy is rumbling, but I can't get caught pilfering food from the Dawn Winery again... Oh, it's you! Where are you heading? May I join?",
				f"I'm still not sleepy, fancy an evening stroll?",
				f"Off to the land of nod? Haha, Farewell my friend!",
				f"Practice? Me? There's no need - I already know every song in Teyvat!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"Haha, once the ‍hero in the song has actually rescued their kin, I will ensure this song spreads to every corner of the continent!",
				f"An evening breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a small offering…",
				f"What's that? You think I should try harder to be a good Anemo Archon? Well you could be a better devotee too... you could be more pious, more passionate, or... um…",
				f"Hmm? You want to know about my Vision? Oh, go on then, take a look for yourself. I can make you a matching one if you like! Hehehe.",
				f"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far…",
				f"{user}, have you ever seen a cecilia? It's a magnificent white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the most beautiful flower in all of Teyvat.",
				f"Perfect timing, {user}! I was about to ask you — what is your greatest wish?",
				f"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				f"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				f"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"I like to drink! And I like the wind! If only there were such a thing as wind-brewed cider…",
				f"I'm actually highly allergic to cats, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about cats without sneezing. Do you think there is a cure for this monstrous affliction?",
				f"Here, have an apple. I just picked it. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				f"What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!",
				f"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?",
				f"Oof, I'm so full... I'll have to pass on the post-meal fruits this time…",
				f"I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament.",
				f"Someone once told me you're supposed to eat a cake on your birthday... Tada! Here's your birthday cake — it's apple flavored! And here's a spoon. The cake didn't rise properly in the oven, that's why it looks more akin to an apple pie... Ugh, baking is really quite complicated!",
				f"Woah! What was that?",
				f"Good work. Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user}.'",
				f"Hmm... Though I've long since viewed this scenery a great many times, there is something different about seeing it again with you. Surely you're not still concealing some other wondrous abilities? Hmm, even if you were, it would simply further prove that my intuition is correct.",
				f"You've come at long last, {user}! While I was waiting for you, I nearly finished penning quite a few poems.",
				f"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"There's a lot of fascinating stories in these books. Don't be put off by the dusty old pages. Give them a chance, and in the blink of an eye, these tales will waft into the air to the sound of the lyre, and blend into the sweetness of the breeze. Pick a story you like! Let's try it out!",
				f"So, a short rest before the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				f"Morning, {user}, hehe. Going anywhere to play today? There are a lot of places I wanna visit — need a recommendation?",
				f"Aw, I don't want to sleep yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				f"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
				f"Ah... the park is one of the most pleasant places in the city. Most people taking a break there are relaxed and in pretty good spirits, so they're always willing to listen to a song or two. Eh-he~ let's work together to make this park even more beautiful!",
				f"Wouldn't gliding be faster?",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Thank Barbatos! Wait a minute…",
				f"What a find! I wonder how many bottles this'll be worth…",
				f"Ugh, I'm not in the mood for this!",
				f"...Oh dear.",
				f"That was uncalled for.",
				f"Oh no, my lyre is broken…",
				f"How rude!",
				f"Give me a moment to compose myself.",
				f"Didn't keep you waiting, did I?",
				f"Ready for a rehearsal?",
				f"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				f"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"Haha, {user}! You came just in time. Here, special apple juice made just for you. Try it~",
				f"Together with you, even apples taste sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				f"Eh, olah! Mosi mita!",
				f"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
				f"Yoo-Hoo!",
				f"Here we go!",
				f"Brace yourselves!",
				f"Let's play!",
				f"Think you can get away?",
				f"Time for takeoff!",
				f"Yahoo!",
				f"Let me try!",
				f"Don't give up!",
				f"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				f"Yes, I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				f"Okay! Ahem... My dearest companion, is there something you wish to tell me?",
				f"Hee-hee... My warrior, you've worked so hard. I understand how you feel.\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.\nAt any rate, don't worry. Whenever you need me, I'll always be by your side.",
				f"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here.",
				f"*gasp* Let's hold a feast! Call up your good friends and I'll contribute a bottle of the finest wine from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				f"Uh, we need a theme? Then hold on, lemme think of one.\nUh... 'Cheers!' Eh... 'Pop!' No... I got it! 'Wishes for Happiness'? How's that?",
				f"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				f"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.",
				f"You... really do have some wonderful abilities… Someone like you is going to end up getting written into a bard's poem.\n*Oh, a hero so bright, should they stand in the light. Though stand in the shade, and you'll be met by a blade…*",
				f"The Abyss Order is an organization comprised of non-human beings. They despise mankind. I don't know where they come from. All I know is that they hold deep hatred towards the human world. Many hilichurls out in the wild take orders from them and act as their weapons.",
				f"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				f"Look me in the eyes. Do you not find me trustworthy?",
				f"Hahaha, that one doesn't work on a bard.",
				f"My disciples, rejoice! Behold, **the God of Anemo, Barbatos** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				f"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				f"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				f"The pattern of flowing wind carved on the rosewood... and the strings still feel cool to the touch too. Oh, the memories…",
				f"Heroes supporting each other and setting out on a journey together... How exciting!",
				f"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle.",
				f"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				f"I haven't been back to Mondstadt for an extended period of time. Without a doubt, I am now the weakest archon among The Seven!",
				f"And so… The epic actions of brave heroes finally leads to this eleventh hour.",
				f"The stage will need to be cleared before I can begin my performance. Generally speaking, such chores are not the concerns of the performer himself…",
				f"Hilichurls usually do not venture into areas with high elemental concentrations. It puts a heavy burden on their bodies.",
				f"It’S sTuCk.",
				f"Let's make a detour then. Heading up!",
				f"Stormterror’s Lair was once part of an ancient city. The ruins even predate the existence of The Four Winds. Mondstadt is a city without a ruler. However, before, it was ruled over by a tyrant.",
				f"Give it a go! If you don't try, you'll never know.",
				f"He doesn't walk in, he flies in.",
				f"I'm thinking about turning these adventures into songs. Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Freedom, if demanded of you by an archon, is really no freedom at all.",
				f"Now, spread your wings of freedom and go with my blessing.",
				f"However, winds change their course. Someday, they will blow towards a brighter future.",
				f"As you know, Visions are external magical foci that only a small minority of people possess. They use these Visions to channel elemental power. In truth, every wielder of a Vision is one who can attain godhood and ascend to Celestia. We call such people allogenes. However, archons don't need primitive tools like Visions. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Gnosis.",
				f"My vision? Eh-he. It's just a glowing glass ball I carry around to avoid suspicion.",
				f"Signora was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like executive authority by the Tsaritsa of Snezhnaya, and with it, strength surpassing that of other mortals.",
				f"She is one of The Seven, the Tsaritsa who reigns from the Zapolyarny Palace, and the one person that the Fatui Harbingers all answer to. The Seven don't always get along well, but still — I never thought that she would plot to steal another archon's Gnosis…",
				f"Five hundred years ago, I knew The Tsaritsa well. But I can't say the same is true now. You see, a certain catastrophe happened five hundred years ago, and after that, she cut off all ties with me.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				f"If you want to chat, now's the time — a bard stays not always in a single clime.",
				f"Up till the end, Dvalin remembered his duty as one of the Four Winds. As such, I don't intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin will be able to choose for himself and understand what freedom is. Before I became an archon, I too was taught the meaning of freedom in this way by a friend.",
				f"*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…",
				f"The Tsaritsa... I haven't seen her in five hundred years. What is she thinking? What's her plan?",
				f"Resident rodent... beats invasive vermin.",
				f"That smirk you wear looks out of place. Did you steal it from your master's face?",
				f"Beauty is a waste... when the beholder has no taste.",
				f"The wind amongst the branches is good, I love the way it smells…",
				f"What are Windblumes, exactly? And what do Windblumes and the Windblume Festival mean to Barbatos, the Anemo Archon? As you've seen, the people of Mondstadt each make their own choice. Out of the millions of flowers there are, some choose the dandelion, others choose the Windwheel Aster. There is no single and answer and no true Windblumes in existence.",
				f"The word 'Windblume' dates from the age of Old Mondstadt. It was a code word that the people used to stay in contact and mount resistance in secret. At that time, people often said that the stronger the wind blows, the firmer the roots of the Windblume grow, and the brighter the flower that bursts into bloom.",
				f"If you want my perspective, Windblumes don't exist. Yet they are all around us nonetheless. They are the spirit of yearning for freedom, the courage to follow the wind wherever it may lead... All objects are beautiful and worthy of blessing... All can be Windblumes.",
				f"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
				f"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought us together.",
				f"*Who was it that stroked your bloodied, determined visage,*\n*By stream flowing small, by boulder standing large?*\n*Who was it that embraced your weary yet noble soul,*\n*In dreams deep, in skies soaring?*",
				f"*Dear friend,*\n*I am leading you by the hand*\n*Into the night where lanterns shine bright.*\n*To tell you a tale of freedom and dreams;*\n*The tale of where this festival begins.*",
				f"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular.",
				f"I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…",
				f"People often claim that capes and the like serve no real purpose other than aesthetics. I suppose a cape with pockets would really turn the tables on that crowd!",
				f"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				f"Summer is the season of love. It is the time for freedom and fun. So everyone, please sing, dance, and enjoy yourselves here.",
				f"Speaking of, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!",
				f"Ding-ding-ding! Correct answer!",
				f"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"Achoo! Ugh... Guess I shouldn't get too close to the cats after all... I'll just stay on the roof.",
				f"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about it?",
				f"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				f"I want to record all these beautiful memories, and turn them into ballads. Every summer will become an unforgettable song!",
				f"{user}, how do you do? Haha, I had a feeling I'd run into you soon!",
				f"Fill up the barrels and store them away,\nThen wait, wait for a windier day\nWax the bottles, seal them tight,\nFor the south wind that soothes, for the north wind that bites ♫",
				f"How does this fine wine taste to the tongue?\nAs 'Mondstadt' to the ear: like a sweet dream of freedom.\nAnd what are the fruits that went into the brew?\nAn explorer's courage, a love tender and true ♫",
				f"A defender's will, strong as yesteryear,\nJoining the thousand winds in a song of good cheer,\nTurning sour into sweet, bitter notes fade away,\nAs we wait, wait for a windier day ♫",
				f"Pray tell, what treasure does this barrel hold?\n'Tis wheat's greatest triumph, the true liquid gold.\nAs it flows from the keg, what sound drifts by?\nWind chimes in the boundless, immemorial sky ♫",
				f"We raise up our glasses, and voices in song,\nAs we wait, wait for the wind to sing along.\nWhere do we turn once the thousand winds take flight?\nTo the tales of the lyre, to the sweet dream of tonight ♫",
				f"We've known each other for so long, and you still don't trust my intentions? Oh, the pain…",
				f"Don't worry about wine-making, really. Freedom is the key here. It's not as hard as you might think. As long as you add ingredients to the mix in a spirit of joy and sincerity, I promise you will reap the rewards you wish for.",
				f"Ah, good. I was hoping we might get to chat some more.",
				f"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
				f"See you around. Remember, there's no rush. Take your time, and you'll find all the answers that you're looking for.",
				f"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				f"Get a good night's sleep tonight. Wait for the whisper of the gentle breeze to rouse you tomorrow morning, then come and enjoy a performance by the greatest bard to ever grace the streets of Mondstadt.",
				f"Sure, the sound of your voice is always a pleasure to hear.",
				f"Razor? He's grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI see a kind, gentle soul, with a healthy dose of romance and freedom, too... In other words, a true Mondstadter, who grew up drinking the water of Cider Lake. You, on the other hand... Don't worry, you're the gentlest soul I've ever met.",
				f"Then go, my friend. The stories that unfolded here shall be remembered by the wind in the form of verse.",
				f"I've actually heard a few things about Mr. Zhongli before. The guests in the tavern talked about this refined and courteous man who, instead of having wine at Mondstadt's finest tavern, ordered a cup of hot tea with the most complex name.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too.",
				f"Oh, woe is me... {user} sees me as nothing more than a drunken wastrel… There are actually a great many things that we bards are required to do... It just happens that enjoying life is the most important one.",
				f"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us.",
				f"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many Mondstadters to be the true 'Windblume.'",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"Oof, my nose is starting to itch again…",
				f"To our precious days of freedom. Cheers!",
				f"Ah, this takes me back. The first time I saw this view, I hadn't even taken on this form yet.",
				f"It was about twenty-six hundred years ago, before the world had come under the rule of The Seven. At that time, Old Mondstadt was ruled by a tyrant, who sealed off the city's perimeter with a ferocious hurricane. Even the birds couldn't get in or out.",
				f"Back then, I was but a wisp among the thousand winds. I wasn't a god of anything — I didn't even have a human form... I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope.",
				f"My current form is not so different from the situation with fake Stanley... I took the form of a friend…",
				f"Say, {user}, do you wish to hear the next part of the story…?",
				f"Ah... You know, you're so smart it almost makes me uncomfortable sometimes… But then, maybe it's right that true friends can tell what the other is thinking.",
				f"A refreshing drink, a gentle breeze... *sigh* Moments like this always take me back…\nBack to a song that I first heard from him…\n*Fly, fly away.*\n*Like a bird in the sky.*\n*See the world on my behalf...*\n*To the heavens may you fly...*",
				f"(The green-clad figure is uncharacteristically silent.)\n(Sometimes even the lissome wind grows heavy in its grief... But not that mortals could ever see a moment oh so brief.)",
				f"Even in his memory, the real Stanley isn't the living, breathing friend he knew at all. Instead, he's become fixed on the image of him as that battle-scarred warrior... and that image has held him captive his entire life.",
				f"...Stanley really did make it to the Mare Jivari. And the tragedy he encountered there was real, too. But the real adventurer, the real Stanley — that was his partner. Not him.",
				f"Jack… Stanley's really fond of that kid, don't you think?",
				f"Acting Grand Master Jean... Well, what do you think of her? Yes, I couldn't agree more: conscientious, courageous... kind and considerate too. Reminds me of another good friend…",
				f"I'm not surprised you want to befriend Master Diluc, just think of all vintage wine he must have stored away... Mwuhahaha... Huh? He doesn't let you sample it? Not even the slightest drop? Huh... Well, I guess you can still appreciate the aroma. That's still better than no wine at all, right? No?",
				f"The darling Deaconess with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…",
				f"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar…",
				f"Oh, that astrologer? How should I put it? Fortune telling and my singing are the same. Both lead to you being so poor you can't even cough up the money for a drink! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is singing, so it still has its value too!",
				f"There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				f"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				f"Have you seen that gentleman around? Huh? He's just a normal man by the name of Zhongli now? That must be quite the change for that old block-head. Come with me to see him, will you? I have a vintage I dug up from Windrise that I can take as a condolence gift. Oh, ahh... did he still seem strong when you saw him? How strong? Am I likely to get blown away?",
				f"Eula has good taste when it comes to beverages of the alcoholic variety. Come summer or winter, she always likes them ice-cold. That's rare among Mondstadters these days! She and I would make great drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, no harm done. Maybe she and I can do a duet sometime!",
				f"So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Hehe, she now no doubt employs a wide range of reasoning to get you to train with her. Oh but yes, come close and I shall let you in on her weakness — desserts!",
				f"The first thing you think of when you hear 'Dendro Archon' is her power over dreams. Her dreams are akin to my ballads: full of emotion and imagination. It goes without saying that we get along really well.",
				f"A bard must be versed in both music and song, but a stage performer requires far more skills than just these... Hey, don't you think we should invite her over to put on a show at the next Windblume Festival? ...Huh? You want me to talk about how she saved Fontaine? Well, I mean, she's such a talented artiste, it's no wonder. I wouldn't be surprised even if she'd saved the entire world.",
				f"This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that. Ah, right! I heard Mavuika likes to drink! Are you thinking what I'm thinking...?",
				f"O, {user}, do you seek to hear the voice of the wind and know its guidance? Then I say to you... chatting to the deacon is your best bet. Haha, I'm kidding — come chat with me over a drink any time you want! The reason I usually get Dahlia to be my intermediary is because... well, I imagine you can probably guess why. He loves listening to the blustering of the wind, but crucially he has his own compass, too.",
				f"Ah, {user}. I could hear your arrival upon the wind. Were you looking for me?",
				f"Dahlia and I are close. He knows everything. A god needs someone to communicate their will in a formal setting, and no one does that better than Dahlia.",
				f"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				f"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past.",
				f"There are always unavoidable trials in life. At least, that's what Barbatos would say.",
				f"This invention, with a little help from a trick of mine, will allow us to keep in touch. Minus the fuse — so don't worry, it's not going to explode. Come on, take it. This way, we can talk to each other just like this even when we're apart.",
				f"It's called a 'Dodocommunication Device,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of times you can use it. That's why it's currently only available to a certain select few.",
				f"No matter what comes, you have the wind on your side.",
				f"Your companionship is like a breeze that lingers in the air, warm and familiar.",
				f"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out.",
				f"You know what? Forget about Barbatos, {user}. Treat me to a drink instead! You wouldn't refuse me, would you?",
				f"A fair investigation means coming to a conclusion presented by the facts. Remaining objective has its own value.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				f"I've got things covered here.",
				f"Thanks, friend. May the Anemo Archon protect you.",
				f"Varka… I still remember when he approached me about 'asking the lovely ladies of the Hexenzirkel for a small favor'... The chumminess caught me off guard. If I hadn't known any different, I'd have thought he was talking about his older sisters or something.",
				f"**Everyone, the best bard in the land is about to begin his performance. So don't go away! Gather round, and lend me your ears!**",
				f"How was it? Not bad, right?",
				f"Hmm, wanna take a guess?",
				f"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — perfect for the season!",
				f"Really? I'll hold you to that, you know! No going back on your word!",
				f"'When no love remains for the songs to tell, the world becomes naught but an empty shell… Cruel is said fate, cruel it may be, were it not for a hero who could set us all free.\nThrough shadows so cold, he sought wisdom untold, chasing a fragrance, the wind only knows. Thus wistfulness waned and faded into night, as he stepped from the darkness, and into the light.'",
				f"These lyre strings are made of astral iron, which contains Anemo energy. That makes them extremely durable, so I normally just roll them up in a ball to make them easier to carry. That's a trick of the trade from a traveling bard!",
				f"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…",
				f"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!",
				f"Ah, hello! I didn't see you there.",
				f"What is this floating sensation I feel? Have I discovered the true meaning of Anemo power?",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
				f"Hello, hello! Please, take a seat, we're all friends here.",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"However it's expressed, as long as you can hear the singer's passion and joy in their voice, I consider it a phenomenal performance.",
				f"In principle, the hymns of the Cathedral are dedicated to a god, but in reality, the audience are all ordinary people with very worldly concerns. So what really matters is that the people enjoy what they're listening to.",
				f"Kaeya! Ah, he was one of the finest students ever to emerge from my fast-track love poetry class... I always did admire his enthusiasm and kindness.",
				f"With the aid of this bottle, a humble bard's woes are whisked away on the wind... And so it falls to this humble bard to pass the blessing on to another.",
				f"'Abandoned to whatever fortune the cruel waters bring, bereft of control directionless I swing. The swift currents surge, and onward I urge, through the snow and frost that Fall and Winter bring.\nMajestic waves cresting, surf roaring its tale, none but the ocean to hear as I sing. The stars in my eyes as I chart toward the horizon, that into one day, from the endless dome of night I shall spring.'",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				f"The winds of Mondstadt will guide every lost ship back to safe harbor.",
				f"Hehe. Looking for me, {user}?",
				f"Why, the sweet wind of reminiscence, of course. Sweet, with a hint of exotic flora, blowing from a land far away.",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can.",
				f"Well, it sounds like you've already mastered music theory and your instrument. I don't think you need my input on either of those!",
				f"I do believe you're a true bard. But... there's too much noise in your ears, and you've allowed that to drown out your own thoughts. That's what's holding you back.",
				f"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
				f"Whoa, not so close... Achoo! No more peeking! I haven't finished writing my poem yet!"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
		else:
			answers = [
				f"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*",
				f"Come on {user}, let's go! The world is full of lost ballads just waiting to be rediscovered.",
				f"Let's go jumping in puddles and see who can make the biggest splash!",
				f"The wind has returned! Quick, let's go gliding!",
				f"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				f"An evening breeze really sets the mood for becoming my disciple, don't you think? We can do it right now, you just need to make me a small offering…",
				f"{user}, have you ever seen a cecilia? It's a magnificent white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the most beautiful flower in all of Teyvat.",
				f"{user}! I was about to ask you — what is your greatest wish?",
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"I like to drink! And I like the wind! If only there were such a thing as wind-brewed cider…",
				f"Here, have an apple. I just picked it. Look how ripe and juicy it is... *munching*... Truly the fruit of the gods.",
				f"Woah! What was that?",
				f"Come, sit with me. I've written a new poem. I call it 'Wind of {user}.'",
				f"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				f"Wouldn't gliding be faster?",
				f"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				f"Give me a moment to compose myself.",
				f"Haha, {user}! You came just in time. Here, special apple juice made just for you. Try it~",
				f"Eh, olah! Mosi mita!",
				f"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
				f"Yoo-Hoo!",
				f"Yahoo!",
				f"Don't give up!",
				f"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				f"My disciples, rejoice! Behold, **the God of Anemo, Barbatos** has descended! Shocked, aren't you? Don't you just want to cry out and rejoice? How does it feel to finally meet the god you've been serving?",
				f"Heroes supporting each other and setting out on a journey together... How exciting!",
				f"Give it a go! If you don't try, you'll never know.",
				f"I'm thinking about turning these adventures into songs. Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"My vision? Eh-he. It's just a glowing glass ball I carry around to avoid suspicion.",
				f"The wind amongst the branches is good, I love the way it smells…",
				f"It is people's shared will that brings them onto the same page. And surely, it is the wind of freedom that brought us together.",
				f"Ding-ding-ding! Correct answer!",
				f"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				f"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				f"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about it?",
				f"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				f"I want to record all these beautiful memories, and turn them into ballads!",
				f"Ah, good. I was hoping we might get to chat some more.",
				f"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				f"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best.",
				f"Get a good night's sleep tonight. Wait for the whisper of the gentle breeze to rouse you tomorrow morning, then come and enjoy a performance by the greatest bard to ever grace the streets of Mondstadt.",
				f"Getting to know other musical styles is essential to sparking inspiration, don't you think?",
				f"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too.",
				f"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				f"I'm happy to see you find the time amidst your busy adventures to return to Mondstadt and celebrate the winds of freedom with us.",
				f"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				f"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				f"Poetry is as free as the winds that blow, and there's nothing freer! There are no limits to genre, form, content, or anything else. So long as it comes from the heart, you're welcome to put it into poetry.",
				f"There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				f"There are always unavoidable trials in life. At least, that's what Barbatos would say.",
				f"No matter what comes, you have the wind on your side.",
				f"Your companionship is like a breeze that lingers in the air, warm and familiar.",
				f"I wonder what Barbatos thinks about that... Perhaps you should pray to him and find out.",
				f"You know what? Forget about Barbatos, {user}. Treat me to a drink instead! You wouldn't refuse me, would you?",
				f"A fair investigation means coming to a conclusion presented by the facts. Remaining objective has its own value.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh… <:VentiScared:1394163440490254427>",
				f"**Everyone, the best bard in the land is about to begin his performance. So don't go away! Gather round, and lend me your ears!**",
				f"Hmm, wanna take a guess?",
				f"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
				f"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
				f"If you are a chaser of freedom, the Anemo Archon will bless you. So why not let those feelings out, and sing with everyone?",
				f"The winds of Mondstadt will guide every lost ship back to safe harbor.",
				f"If problems are the veins on a leaf, inspiration is like the nutrients that flow through them — you've got to grab them when you can.",
				"Ehe.",
				"Ehe~"
			]
			random_message = random.choice(answers)
			await message.reply(random_message)
keep_alive()
client.run(TOKEN)
