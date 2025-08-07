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
	if message.author == client.user:
		return
	elif any(keyword in content for keyword in ["v!", "<@1402784150301184020>", "hey venti", "hi venti", "hello venti", "@venti", "!venti", "venti,", "!v"]):
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
			await message.channel.send(random_message)
		elif "!help" in content:
			await message.channel.send("v!sleep [user] (tells the mentioned user to sleep\nv!give [object] (gives Venti a gift)\nv!random (says a random voice line)")
#💎GIVE COMMAND (Food)
		elif "!give" in content:
			if "apple" in content:
				answers = [
					"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
					"Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif "grape" in content:
				answers = [
					"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif "wine" in content:
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
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["beverage", "sake", "beer", "champagne", "tumbler", "cocktail", "tropical", "drink", "alcohol"]):
				answers = [
					"Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?",
					"A drink? I'll hold you to that, you know! No going back on your word!",
					"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable.",
					"With the aid of this drink, a humble bard's woes are whisked away on the wind... And so it falls to this humble bard to pass the blessing on to another.",
					"To our precious days of freedom. Cheers!",
					"What is this floating sensation I feel? Have I discovered the true meaning of Anemo power?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["cheese", "pancake"]):
				answers = [
					"What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!",
					"I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["pear", "tangerine", "lemon", "lime", "banana", "melon", "berry", "cherr", "peach", "mango", "coconut", "kiwi", "cookie", "cake", "pie", "birthday", "nut", "cup", "glass"]):
				await message.channel.send("Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?")
			elif any(keyword in content for keyword in ["plant", "tomato", "avocado", "pea", "broccoli", "leaf", "cucumber", "pepper", "corn", "carrot", "olive", "potato", "ginger", "croissant", "bagel", "bread", "pretzel", "meat", "poultry", "hot dog", "burger", "fries", "sandwich", "falafel", "salad", "food", "stew", "bento", "rice", "oden", "dango", "ice", "lollipop", "candy", "chocolate", "popcorn", "doughnut", "donut", "bean", "tea", "coffee", "mate", "salt", "takeout"]):
				await message.channel.send("Oof, I'm so full... I'll have to pass on the post-meal fruits this time…")
			elif any(keyword in content for keyword in ["garlic", "onion", "egg", "cooking", "butter", "waffle", "bacon", "bone", "pizza", "taco", "burrito", "tamale", "fondue", "canned", "jar", "spaghetti", "ramen", "curry", "sushi", "dumpling", "oyster", "shrimp", "custard", "pudding", "honey", "milk", "liquid"]):
				await message.channel.send("I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament.")
#💎GIVE COMMAND (Animals)
			elif "dragon" in content:
				answers = [
					"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
					"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle.",
					"Up till the end, Dvalin remembered his duty as one of the Four Winds. As such, I don't intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin will be able to choose for himself and understand what freedom is. Before I became an archon, I too was taught the meaning of freedom in this way by a friend."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif "feather" in content:
				answers = [
					"Surely, he too would have wanted to live in such a place…",
					"*Fly, fly away.*\n*Like a bird in the sky.*\n*See the world on my behalf...*\n*To the heavens may you fly...*"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["rex", "saur", "mammoth", "elephant", "dodo"]):
				answers = [
					"Well, hello there. You made it all the way from Natlan to Mondstadt?",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon. And you are…?",
					"What brings you to Mondstadt, my friend? Hunger? A wish for freedom? Well, I’ll tell you a little secret… behind the Dawn Winery, you may or may not find food scraps from time to time. Hehe, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a rare and beautiful creature!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["horse", "zebra", "donkey"]):
				answers = [
					"I haven’t seen horses since Varka–... well, you know!",
					"Why, thank you! The Cavalry for Captain Kaeya."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif "wolf" in content:
				answers = [
					"The North Wind in the silent forest slumbers,\nAnd around it pace the wolves in their numbers.",
					"You know, I have a friend named Razor you may get along with. No, he won’t hurt you, don’t worry.",
					"I have a friend named Razor who–... oh, he’s already in your Lupical? Glad to hear it!",
					"How is Andrius? It’s been a long time since we last crossed paths."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["bear", "tiger", "moose", "crocodile", "leopard", "gorilla", "hippo", "rhino", "bison", "buffalo", "ox"]):
				answers = [
					"Oh–! What a… large animal…",
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif "lion" in content:
				answers = [
					"In summer the lion walks the plains,\nNo words one finds to praise it but these:\nDo you sweat out your water to make way for wine?\nComes the heat of the summer from your mane of sunshine?",
					f"**Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["dog", "puppy", "mouse", "hamster", "rabbit", "panda", "koala", "cow", "pig", "frog", "monkey", "no_evil", "bat", "boar", "bee", "worm", "bug", "snail", "beetle", "ant", "cricket", "spider", "turtle", "lizard", "seal", "orangutan", "camel", "giraffe", "kangaroo", "ram", "sheep", "llama", "goat", "deer", "poodle", "raccoon", "skunk", "badger", "beaver", "otter", "sloth", "rat", "chipmunk", "hedgehog", "butterfly", "fox", "unicorn", "phoenix"]):
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
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["fly", "cockroach", "mosquito", "scorpion", "snake"]):
				answers = [
					"Time for takeoff!",
					"Think you can get away?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["bird", "goose", "eagle", "owl", "peacock", "parrot", "swan", "flamingo", "dove", "penguin", "chick", "duck", "rooster", "turkey"]):
				answers = [
					"What you lacked was not wind, but courage\nIt is courage that has allowed you to become the first flying birds of this world.",
					f"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.<:VentiWink:1394244370697289790> What’s your name?",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon. And you are…?",
					"What brings you to Mondstadt, my feathery friend? Hunger? A wish for freedom? Or were you born here? Well, I’ll tell you a little secret… behind the Dawn Winery, you may or may not find food scraps from time to time. Hehe, just don’t get caught.",
					"Hm, you look surprised that I can communicate with you. Well, don’t be afraid; that’s just the wind’s unique ability!",
					"What a beautiful bird!\n…Hm? Oh, you’re welcome!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["cat", "kitten"]):
				answers = [
					"Oof, my nose is starting to itch again…",
					"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…",
					"Aha, it must be my second avid reader! Let's go ask it about its thoughts on my... my... achoo!",
					"Whoa, not so close... Achoo! No more peeking! I haven't finished writing my poem yet!",
					"Ah, hello! I didn't see you there. I’m Barbatos, the Anemo Archon, and– ACHOO!<:VentiSneeze:1394239013254201444>"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["octopus", "squid", "fish", "shrimp", "lobster", "crab", "dolphin", "whale", "shark"]):
				await message.channel.send("Oh no, they’re going to drown! I’ll blow them all the way to Fontaine.")
#💎GIVE COMMAND (Misc)
			elif any(keyword in content for keyword in ["love", "heart", "cupid", "ring", "couple"]):
				answers = [
					"*blush* This is for me? <:VentiShock:1394123854518948041>",
					"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
					"I want to record all these beautiful memories, and turn them into ballads!",
					"When you receive this letter, hold it in your hands and stand by the window. Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
					f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["bouquet", "tulip", "rose", "hyacinth", "lotus", "hibiscus", "blossom", "flower"]):
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
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["phone", "calling", "computer", "keyboard", "desktop", "pager", "fax", "tv", "television", "x_ray", "robot"]):
				await message.channel.send("What an interesting device! Is it from Fontaine? <:VentiIdea:1394242659870179428>")
			elif any(keyword in content for keyword in ["crystal_ball", "amulet", "hamsa", "frame", "mirror", "lantern", "chime", "red_envelope", "scroll", "book", "ghost", "alien"]):
				answers = [
					"How fascinating!",
					"What is this? Hm…",
					"I’m going to have to look at this more closely…"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["ice", "sled", "ski", "snowboard"]):
				await message.channel.send("Let's wait till the snow gets heavier and have a snowball fight!")
			elif any(keyword in content for keyword in ["kite", "parachute"]):
				await message.channel.send("The wind has returned! Quick, let's go gliding!")
			elif any(keyword in content for keyword in ["fishing", "diving"]):
				await message.channel.send("Let's go jumping in puddles and see who can make the biggest splash!")
			elif "umbrella" in content:
				answers = [
					"Let's go jumping in puddles and see who can make the biggest splash!",
					"It's stopped raining already? A shame, I wanted to play some more."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["balloon", "wand", "soccer", "basketball", "football", "baseball", "softball", "tennis", "volleyball", "rugby", "flying_disc", "8ball", "yo_yo", "ping_pong", "badminton", "hockey", "lacrosse", "cricket_game", "boomerang", "goal", "golf", "playground", "bow_and_arrow", "archery", "boxing", "martial", "curling", "skate", "teddy", "dolls", "trackball", "joystick"]):
				answers = [
					"Let’s play some more!",
					"Let’s play with this together!",
					"Hehe, this will be fun to play with."
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["shower", "bath", "soap", "toothbrush", "sponge"]):
				answers = [
					"Hehe, are you implying I need a shower?",
					"Hey! As a wind spirit, I lack the tribulations of bodily odor. …I hope.",
					"Heh, message received.",
					"A hygiene product… Ah, I guess one can always use more of those, right?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["printer", "compression", "clamp", "control", "compass", "satellite", "battery", "electric", "bulb", "flashlight", "candle", "lamp", "fire_extinguisher", "oil_drum", "scale", "ladder", "tool", "screwdriver", "wrench", "hammer", "pick", "saw", "nut", "bolt", "gear", "trap", "brick", "chain", "link", "magnet", "barber", "telescope", "microscope", "stethoscope", "thermometer", "broom", "basket", "potable", "bucket", "squeeze", "lotion", "bell", "key", "door", "chair", "couch", "window", "shopping", "flag", "ribbon", "fan", "envelope", "mail", "package", "label", "placard", "post", "page", "bookmark", "receipt", "notepad", "calender", "date", "card", "ballot", "file", "clip", "paper", "ledger", "pin", "clip", "ruler", "abacus", "pen", "nib", "paint", "crayon", "pencil", "mag", "lock", "lipstick", "knot", "yarn", "thread", "needle", "coat", "vest", "cloth", "shirt", "jeans", "shorts", "necktie", "dress", "kimono", "sari", "sandal", "shoe", "heel", "boot", "sock", "glove", "scarf", "hat", "cap", "board", "helmet", "bag", "purse", "pouch", "case", "backpack", "satchel", "luggage", "glasses", "goggles", "beads", "razor", "pick", "wastebasket", "bandage", "shield", "albemic", "gift"]):
				answers = [
					"Thanks, friend. May the Anemo Archon protect you.",
					"How kind of you!",
					"Hm, where shall I put this…?",
					"For me? Thank you!",
					f"Oh, this is for me? Thank you, {user}!",
					"Ah, this could come in handy!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["bed", "sleeping"]):
				answers = [
					"Thank you! Just in time for me to sleep. *yawn* <:VentiSleep:1394238176410730669>",
					f"Aw, I don't want to sleep yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
					f"Goodnight, {user}. Zzzz… <:VentiSleep:1394238176410730669>",
					"It’s… so comfy! Let me sleep a while… <:VentiSleep:1394238176410730669>"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["identification_card", "gun", "pistol", "axe", "knife", "dagger", "knife", "axe", "dagger", "sword", "smoking", "cigar", "pill", "syringe", "tube", "scissor"]):
				answers = [
					"Sorry, I’ll have to pass on that.<:VentiRefuse:1394238074707251271>",
					"I’m afraid I have to turn this one down.",
					"Thank you, but this is not useful for me at the moment…",
					"Ah… isn’t this a bit too dangerous?"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["money", "dollar", "yen", "euro", "pound", "mora", "coin", "credit", "gem", "crown"]):
				answers = [
					"Thank Barbatos! Wait a minute…",
					"What a find! I wonder how many bottles this'll be worth…",
					"*clears throat* Have you heard The Ballad of the Treasure Chest?",
					"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["coffin", "headstone", "urn", "amphora", "hole", "dna", "plunger", "roll_of_paper", "toilet", "tooth", "tongue", "ear", "nose", "foot", "eye", "anatomical", "lungs", "clown", "goblin", "briefs", "bikini", "swimsuit", "lip", "poo", "shit", "ogre"]):
				answers = [
					"Hehe, very funny. <:VentiScared:1394163440490254427>",
					"Aww, for me? How… *generous*. <:VentiRefuse:1394238074707251271>",
					"Just what I always wanted!",
					f"Haha, now you’re playing with me, {user}. <:VentiEhe:1394237963923226737>"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
			elif any(keyword in content for keyword in ["bomb", "firecracker", "blood", "microbe", "petri_dish", "brain"]):
				answers = [
					"<a:ventismh:1394722750223880202>",
					"Time for takeoff!",
					"That was uncalled for. <:VentiShock:1394123854518948041>",
					"...Oh dear.",
					"How rude!"
				]
				random_message = random.choice(answers)
				await message.channel.send(random_message)
#PRIORITY ⭐
		elif any(keyword in content for keyword in ["sad", "cry", "sick", "hard", "hurt", "tear", "pain", "depress", "tir", "energy", "suic", "upset", "help me", "sniffle", "weep", "bad day"]):
			answers = [
				"Hee-hee... My warrior, you've worked so hard. I understand how you feel.\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.\nAt any rate, don't worry. Whenever you need me, I'll always be by your side.",
				"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["you are", "your", "ur", "you’re", "youre", "venti is", "barbatos is", "venti’s", "barbatos’s", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos"]) and any(keyword in content for keyword in ["lazy", "bad", "annoying", "worst", "useless", "terrible", "ugly", "stupid", "awful", "drunkard", "wastrel", "drunken", "worst", "i dislike you", "i hate you", "i dislike u", "i hate u", "i dislike venti", "i hate venti", "i dislike barbatos", "i hate barbatos"]):
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["i hate", "i dislike"]) and "u" in content:
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["rodent", "scurry", "rat", "pest", "vermin"]):
			await message.channel.send("Resident rodent... beats invasive vermin.")
		elif any(keyword in content for keyword in ["attack", "fight", "shoot", "skill", "burst", "punch", "slap", "hit", "kick", "smack", "bite", "chew", "steal", "take", "grab", "slash"]):
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
			await message.channel.send(random_message)
		elif "better" in content and "archon" in content:
			await message.channel.send("What's that? You think I should try harder to be a good Anemo Archon? Well you could be a better devotee too... you could be more pious, more passionate, or... um…")
		elif any(keyword in content for keyword in ["i love", "ily", "you make", "dearest", "beloved", "my love", "mean", "deserve", "adore"]) and any(keyword in content for keyword in ["you", "venti", "barbatos", "u", "ily", "me happy", "dearest", "beloved", "my love", "to me", "deserve"]):
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["kiss", "smooch", "mwah"]):
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
		elif any(keyword in content for keyword in ["venti", "barbatos", "you", "u are", "ur", "you have", "u have"]) and any(keyword in content for keyword in ["cute", "adorable", "sweet", "beautiful", "pretty", "amazing", "precious", "favorite", "charming", "lovely", "endearing", "lovable", "delightful", "heartwarming", "wholesome", "gentle", "kind", "caring", "soft", "comforting", "comfort character", "sunshine", "angel", "handsome", "gorgeous", "stunning", "dreamy", "ethereal", "radiant", "divine", "elegant", "enchanting", "sparkly", "talented", "poetic", "genius", "lyrical", "inspiring", "whimsical", "brilliant", "clever", "grace", "soothing", "magical", "iconic", "legendary", "goat", "my heart", "my eye", "baby", "best", "top tier", "fave", "my muse", "perfect", "king", "slay", "i like", "i want"]):
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
				f"I could say the same about you, {user}!"
				"Hehe, you flatter me..."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif "it" in content and "stuck" in content:
			await message.channel.send("It’S sTuCk.")
		elif "detour" in content:
			await message.channel.send("Let’s make a detour then. Heading up!")
		elif "walk in" in content and "flies in" in content:
			await message.channel.send("He doesn’t *walk* in, he *flies* in.")
		elif any(keyword in content for keyword in ["Ding", "Answer", "Correct"]):
			await message.channel.send("Ding-ding-ding! Correct answer!")
		elif "fembo" in content:
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
			await message.channel.send(random_message)
#CHARACTERS ❤️
		elif "paimon" in content:
			answers = [
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				"Without a friend constantly by your side, a long journey would become dreadfully lonesome. But once you have someone there to brighten up the atmosphere, everything along the way will become lively and vibrant too."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["mavuika", "xbalanque", "harborym", "god", "archon"]) and any(keyword in content for keyword in ["fire", "pyro", "natlan", "war", "mavuika", "xbalanque", "harborym"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				"This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that. Ah, right! I heard Mavuika likes to drink! Are you thinking what I'm thinking...?"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["god", "archon", "zhongli", "morax", "rex lapis"]) and any(keyword in content for keyword in ["geo", "earth", "stone", "rock", "liyue", "contract", "zhongli", "morax", "rex lapis"]):
			answers = [
				"The Pyro Archon is a wayward, warmongering wretch, and the Geo Archon is a brutish blundering buffoon! How do I know? Because, this is written in the epic poems of days gone by!",
				"Have you seen that gentleman around? Huh? He's just a normal man by the name of Zhongli now? That must be quite the change for that old block-head. Come with me to see him, will you? I have a vintage I dug up from Windrise that I can take as a condolence gift. Oh, ahh... did he still seem strong when you saw him? How strong? Am I likely to get blown away?",
				"I've actually heard a few things about Mr. Zhongli before. The guests in the tavern talked about this refined and courteous man who, instead of having wine at Mondstadt's finest tavern, ordered a cup of hot tea with the most complex name."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["raiden", "shogun", "ei", "baal", "god", "archon"]) and any(keyword in content for keyword in ["raiden", "shogun", "ei", "baal", "electro", "thunder", "lightning", "eternity", "inazuma"]):
			await message.channel.send("So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Hehe, she now no doubt employs a wide range of reasoning to get you to train with her. Oh but yes, come close and I shall let you in on her weakness — desserts!")
		elif any(keyword in content for keyword in ["god", "archon", "nahida", "kusanali", "buer", "lesser lord"]) and any(keyword in content for keyword in ["nahida", "kusanali", "buer", "lesser lord", "dendro", "grass", "plant", "nature", "wisdom", "sumeru"]):
			await message.channel.send("The first thing you think of when you hear 'Dendro Archon' is her power over dreams. Her dreams are akin to my ballads: full of emotion and imagination. It goes without saying that we get along really well.")
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["furina", "focalors", "regina", "ousia", "pneuma", "god", "archon"]) and any(keyword in content for keyword in ["furina", "focalors", "regina", "ousia", "pneuma", "hydro", "water", "ocean", "sea", "justice", "fontaine"]):
			await message.channel.send("A bard must be versed in both music and song, but a stage performer requires far more skills than just these... Hey, don't you think we should invite her over to put on a show at the next Windblume Festival? ...Huh? You want me to talk about how she saved Fontaine? Well, I mean, she's such a talented artiste, it's no wonder. I wouldn't be surprised even if she'd saved the entire world.")
		elif any(keyword in content for keyword in ["fontaine", "france", "french"]):
			await message.channel.send("Ohoho travelère, wouldn’t gliding be fastère? <:VentiFrench:1394234467832561717> Hehehehe…\nBONJOUR YOU F*CKING A-")
		elif any(keyword in content for keyword in ["tsaritsa", "god", "archon"]) and any(keyword in content for keyword in ["cryo", "ice", "snow", "snezhnaya", "tsaritsa"]):
			answers = [
				"She is one of The Seven, the Tsaritsa who reigns from the Zapolyarny Palace, and the one person that the Fatui Harbingers all answer to. The Seven don't always get along well, but still — I never thought that she would plot to steal another archon's Gnosis…",
				"Five hundred years ago, I knew The Tsaritsa well. But I can't say the same is true now. You see, a certain catastrophe happened five hundred years ago, and after that, she cut off all ties with me.",
				"The Tsaritsa... I haven't seen her in five hundred years. What is she thinking? What's her plan?"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["signora", "rosalyne"]):
			await message.channel.send("Signora was No. 8 of the harbingers. She and the rest of the harbingers have been given god-like executive authority by the Tsaritsa of Snezhnaya, and with it, strength surpassing that of other mortals.")
		elif "celestia" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Celestia?"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["primordial", "phanes", "heavenly principles", "hp", "dad", "father", "papa"]):
			answers = [
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Phane–ahem, the Heavenly Principles?",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about the Heavenly Principles?",
				"A secret is like a well-aged brew. The aroma from the bottle is sweetest when revealed in the company of friends.",
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "fatui" in content:
			await message.channel.send("*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…")
		elif any(keyword in content for keyword in ["vennessa", "windrise", "oak"]):
			await message.channel.send("I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.")
		elif any(keyword in content for keyword in ["stanley", "hans", "archibald"]):
			answers = [
				"Even in his memory, the real Stanley isn't the living, breathing friend he knew at all. Instead, he's become fixed on the image of him as that battle-scarred warrior... and that image has held him captive his entire life.",
				"...Stanley really did make it to the Mare Jivari. And the tragedy he encountered there was real, too. But the real adventurer, the real Stanley — that was his partner. Not him."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "jack" in content:
			await message.channel.send("Jack… Stanley's really fond of that kid, don't you think?")
		elif any(keyword in content for keyword in ["venti", "you", "nameless bard", "nameless"]) and any(keyword in content for keyword in ["grie", "loss", "death", "sad", "alcoholic", "pain", "cry", "died", "nameless bard", "nameless"]):
			answers = [
				f"My current form is not so different from the situation with fake Stanley... I took the form of a friend…",
				f"Say, {user}, do you wish to hear the next part of the story…?",
				f"Ah... You know, you're so smart it almost makes me uncomfortable sometimes… But then, maybe it's right that true friends can tell what the other is thinking.",
				f"A refreshing drink, a gentle breeze... *sigh* Moments like this always take me back…\nBack to a song that I first heard from him…\n*Fly, fly away.*\n*Like a bird in the sky.*\n*See the world on my behalf...*\n*To the heavens may you fly...*",
				f"(The green-clad figure is uncharacteristically silent.)\n(Sometimes even the lissome wind grows heavy in its grief... But not that mortals could ever see a moment oh so brief.)"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["wind spirit", "wind sprite", "form"]):
			answers = [
				"Ah, this takes me back. The first time I saw this view, I hadn't even taken on this form yet.",
				"Back then, I was but a wisp among the thousand winds. I wasn't a god of anything — I didn't even have a human form... I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope.",
				"My current form is not so different from the situation with fake Stanley... I took the form of a friend…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["stormterror’s lair", "old mondstadt", "ruins", "ancient", "decarabian"]):
			answers = [
				"Stormterror’s Lair was once part of an ancient city. The ruins even predate the existence of The Four Winds. Mondstadt is a city without a ruler. However, before, it was ruled over by a tyrant.",
				"The word 'Windblume' dates from the age of Old Mondstadt. It was a code word that the people used to stay in contact and mount resistance in secret. At that time, people often said that the stronger the wind blows, the firmer the roots of the Windblume grow, and the brighter the flower that bursts into bloom.",
				"It was about twenty-six hundred years ago, before the world had come under the rule of The Seven. At that time, Old Mondstadt was ruled by a tyrant, who sealed off the city's perimeter with a ferocious hurricane. Even the birds couldn't get in or out.",
				"Back then, I was but a wisp among the thousand winds. I wasn't a god of anything — I didn't even have a human form... I was just a tiny elemental being who lived in the wind, a gentle breeze bringing subtle changes for the better, or tiny seeds of hope."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["stormterror", "dvalin"]):
			answers = [
				"The story I want to tell starts at... the sky dragon heeding his grave calls…\nBrutal battle with the wicked dragon... ingested venomous blood and fell into a slumber... only to awake to be expelled in abhor…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle.",
				"Up till the end, Dvalin remembered his duty as one of the Four Winds. As such, I don't intend to forcibly strip him of that duty and force my ideals of freedom onto him. I just hope that Dvalin will be able to choose for himself and understand what freedom is. Before I became an archon, I too was taught the meaning of freedom in this way by a friend."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
#PLAYABLE CHARACTERS 💜
		elif any(keyword in content for keyword in ["diluc", "dawn winery"]):
			answers = [
				"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"My tummy is rumbling, but I can't get caught pilfering food from the Dawn Winery again... Oh, it's you! Where are you heading? May I join?",
				"I'm not surprised you want to befriend Master Diluc, just think of all vintage wine he must have stored away... Mwuhahaha... Huh? He doesn't let you sample it? Not even the slightest drop? Huh... Well, I guess you can still appreciate the aroma. That's still better than no wine at all, right? No?",
				"The Dawn Winery's wine is every bit as delectable as they say! I would never be able to afford this normally, so in the spirit of enjoying the moment while it lasts... Another glass for the bard, please!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["kaeya", "cavalry captain", "cavalry"]):
			await message.channel.send("Kaeya! Ah, he was one of the finest students ever to emerge from my fast-track love poetry class... I always did admire his enthusiasm and kindness.")
		elif any(keyword in content for keyword in ["jean", "acting grand master"]):
			await message.channel.send("Acting Grand Master Jean... Well, what do you think of her? Yes, I couldn't agree more: conscientious, courageous... kind and considerate too. Reminds me of another good friend…")
		elif any(keyword in content for keyword in ["dodocomm", "device"]):
			answers = [
				"This invention, with a little help from a trick of mine, will allow us to keep in touch. Minus the fuse — so don't worry, it's not going to explode. Come on, take it. This way, we can talk to each other just like this even when we're apart!",
				"It's called a 'Dodocommunication Device,' and it allows people to stay in touch over vast distances. However, you can't just use it anytime you want, and there's also a limit on the number of times you can use it. That's why it's currently only available to a certain select few."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["klee", "dodo"]):
			answers = [
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				"Speaking of Klee, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["barbara", "deaconess", "idol"]):
			await message.channel.send("The darling Deaconess with the sweet singing voice — do you know her? You do? Idol, huh? Meet and greets? Concerts? Wow... That's the power of music for you…")
		elif any(keyword in content for keyword in ["dahlia", "deacon"]):
			answers = [
				"O, Traveler, do you seek to hear the voice of the wind and know its guidance? Then I say to you... chatting to the deacon is your best bet. Haha, I'm kidding — come chat with me over a drink any time you want! The reason I usually get Dahlia to be my intermediary is because... well, I imagine you can probably guess why. He loves listening to the blustering of the wind, but crucially he has his own compass, too.",
				"Dahlia and I are close. He knows everything. A god needs someone to communicate their will in a formal setting, and no one does that better than Dahlia."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["varka", "grand master"]):
			await message.channel.send("Varka… I still remember when he approached me about 'asking the lovely ladies of the Hexenzirkel for a small favor'... The chumminess caught me off guard. If I hadn't known any different, I'd have thought he was talking about his older sisters or something.")
		elif "alice" in content:
			answers = [
				"Speaking of Alice, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about the Hexenzirkel?",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["hexenzirkel", "barbeloth", "ivanovna", "andersdotter", "nicole", "octavia", "scarlet"]):
			answers = [
				"Speaking of the Hexenzirkel, guess which two people I ran into on my way to the tavern today? A mother and daughter, both with long elf ears and the most amazingly adorable personalities!",
				"Varka… I still remember when he approached me about 'asking the lovely ladies of the Hexenzirkel for a small favor'... The chumminess caught me off guard. If I hadn't known any different, I'd have thought he was talking about his older sisters or something.",
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["eula", "lawrence", "clan"]):
			await message.channel.send("Eula has good taste when it comes to beverages of the alcoholic variety. Come summer or winter, she always likes them ice-cold. That's rare among Mondstadters these days! She and I would make great drinking buddies. Huh? My songs about the Lawrence Clan... She's heard them already? Eh, no harm done. Maybe she and I can do a duet sometime!")
		elif any(keyword in content for keyword in ["diona", "cat’s tail"]):
			await message.channel.send("There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! *sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.")
		elif any(keyword in content for keyword in ["mona", "megistus"]):
			await message.channel.send("Oh, that astrologer? How should I put it? Fortune telling and my singing are the same. Both lead to you being so poor you can't even cough up the money for a drink! ...You think that astrology is a cultural tradition, so at least still has some value? Hmph, so rude. In that case, so too is singing, so it still has its value too!")
		elif any(keyword in content for keyword in ["razor", "wolf", "wolv"]):
			answers = [
				"Razor? He's grown up so much recently... It's such a joy to see. Huh... Suddenly I sound just like an old grandpa.\nI see a kind, gentle soul, with a healthy dose of romance and freedom, too... In other words, a true Mondstadter, who grew up drinking the water of Cider Lake. You, on the other hand... Don't worry, you're the gentlest soul I've ever met.",
				"Ah yes, the white-haired fellow from Wolvendom? Raised by wolves? Really? ... No wonder his scent is so familiar…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "beidou" in content:
			await message.channel.send("I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…")
		elif any(keyword in content for keyword in ["rhinedottir", "gold", "naberius", "kreideprinz"]):
			answers = [
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["albedo", "alchemy", "life", "synthe", "durin"]):
			answers = [
				"How do you explain white chalk in black soil, or the earth's dense crust amidst the emptiness of space? Same reason the purest soil gave birth to human life... It's an ancient power with unmistakable properties. Trying to harness it is dangerous indeed, I can't imagine what would happen if someone lost control of it in the city... Ah, never mind! What goes on within Mondstadt's walls is up to Mondstadt's people to deal with!",
				"I knew something would happen from the moment Rhinedottir and Alice brought Albedo to Mondstadt. When those two are in town, no one can afford to slack off.",
				"The Kreideprinz, a perfect specimen of synthetic life... We should be grateful Albedo's true identity remains hidden. If it gets out that he's one of Rhinedottir's creations... there'd be no separating him from her past."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
#OTHER MENTIONS🔥
		elif "holy lyre" in content:
			await message.channel.send("The pattern of flowing wind carved on the rosewood... and the strings still feel cool to the touch too. Oh, the memories...")
		elif "abyss" in content:
			answers = [
				"The Abyss Order is an organization comprised of non-human beings. They despise mankind. I don't know where they come from. All I know is that they hold deep hatred towards the human world. Many hilichurls out in the wild take orders from them and act as their weapons.",
				"*sigh*... If only the seven nations had banded together against the Abyss Order in the first place. The Fatui possess the strongest military among the seven nations. Yet they've used it to steal the Holy Lyre, covet the power of gods, and use Dvalin as a bargaining chip against the Knights…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["paralogism", "archon quest", "story quest", "aq", "sq"]):
			answers = [
				f"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!",
				f"I'm thinking about turning these adventures into songs after we're done… Hopefully, this song will be sung for years to come by the people of Mondstadt, just like The Legend of Vennessa.",
				f"Heroes supporting each other and setting out on a journey together... How exciting!",
				f"'When no love remains for the songs to tell, the world becomes naught but an empty shell… Cruel is said fate, cruel it may be, were it not for a hero who could set us all free.\nThrough shadows so cold, he sought wisdom untold, chasing a fragrance, the wind only knows. Thus wistfulness waned and faded into night, as he stepped from the darkness, and into the light.'",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>",
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
#SPECIFIC 🪽
		elif any(keyword in content for keyword in ["who", "what"]) and any(keyword in content for keyword in ["you", "this", "name"]):
			answers = [
				"I'm Venti the Bard. Three-time winner of the 'Most Popular Bard of Mondstadt,' to be precise.",
				"I'm Venti, the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["scar", "fear", "afraid", "lost", "what to do", "life"]):
			answers = [
				"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here.",
				"However, winds change their course. Someday, they will blow towards a brighter future. :green_heart:"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["can", "may", "let", "something", "have"]) and any(keyword in content for keyword in ["talk", "chat", "tell", "speak", "mind", "question"]):
			answers = [
				"Okay! Ahem... My dearest companion, is there something you wish to tell me?",
				"If you want to chat, now's the time — a bard stays not always in a single clime.",
				"Ah, good. I was hoping we might get to chat some more.",
				"It's been too long! I'll bet you have some thrilling new tales from your journey to fill me in on? I can see it in your eyes.",
				"Sure, the sound of your voice is always a pleasure to hear."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["soul", "spirit", "ghost"]):
			await message.channel.send("The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.")
		elif any(keyword in content for keyword in ["time loop", "loop", "yawn"]):
			await message.channel.send("*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!")
		elif any(keyword in content for keyword in ["time", "istaroth", "mom", "mother", "mama", "watch", "clock", "hourglass"]):
			answers = [
				f"*Yawn* That was a refreshing sleep. Ah, {user}, we meet again! What? You don't remember me? Ahaha, well, allow me to join you on your quest once again. I must see to it that the bards of the world tell {user}'s tales!",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future.",
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				"Alas, I am but a humble bard who sings for his Mora in the tavern. Why would I know anything about Time?"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["memor", "moment", "stor"]):
			answers = [
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				f"{user}, as you set off on your journey once again, you must remember that the journey itself has meaning. The birds of Teyvat, the songs and the cities, the Tsaritsa, her Fatui and the monsters... they are all part of your journey. The destination is not everything. So before you reach the end, keep your eyes open. Use the chance to take in the world around you…",
				"I want to record all these beautiful memories, and turn them into ballads!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["danger", "help", "spook"]):
			answers = [
				"'When danger rose they overcame their foes, onward forging to the journey's end'...",
				"Let me try!",
				"Don't give up!",
				"You're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Adventuring is what you do best. It's only natural to encounter a few surprises when you head somewhere new, but just remember, not all unexpected encounters are dangerous.",
				"I've got things covered here.",
				f"Shoot, someone's coming… **Help me! Please! Someone help me!**\n…Oh, y'know. Just a wandering bard calling for help! Thank goodness {user} found me! Got me out of a tough spot, heh…<:VentiScared:1394163440490254427>"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["flirt", "seduc", "pick-up", "pickup", "wink wink"]):
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["boat", "ship", "sail", "cargo", "harbor"]):
			answers = [
				"I once happened upon a cargo ship bound for Inazuma transporting Dandelion Wine, so, naturally, I decided to set sail with them. Once aboard, I found the captain to be a kindred spirit, and I was treated to an abundance of fine liquor along the way. Uh, I must have fallen asleep in the cargo crate while carefully comparing the tastes of Dandelion Wine and Inazuman sake…",
				"Legends tell of an emerald isle in the middle of the ocean. There, the Dodo-King and his people live a blissful existence. When a Dodoco is born, it dives into the water. Some learn to swim, others are carried away by the waves all the way to Mondstadt, where they befriend the children there.",
				"The winds of Mondstadt will guide every lost ship back to safe harbor."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["party", "feast", "celebrat", "gathering", "reunion", "festiv", "holiday", "christmas", "confetti"]):
			answers = [
				"*gasp* Let's hold a feast! Call up your good friends and I'll contribute a bottle of the finest wine from my collection! As for the location… Let's just have it here! We can find a clear space and decorate it with benches, a porch, and beautiful fresh flowers!\nOh, yeah! Can I trouble you to prepare one of your specialty dishes? Anything's fine — I like to eat any dish you make!\nAlright, then let us officially start the preparations!  What a joyous day... It calls for a drink to celebrate.",
				"I am fond of each and every one of Mondstadt's festivals, but if I'm honest, Weinlesefest has an extra-special place in my heart. You know, the Anemo Archon goes into a slumber after the west wind dies down, leaving the north wind to blow during the winter. Which means, this festival is the big feast before the winter slumber!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "theme" in content:
			await message.channel.send("Uh, we need a theme? Then hold on, lemme think of one.\nUh... 'Cheers!' Eh... 'Pop!' No... I got it! 'Wishes for Happiness'? How's that?")
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["love", "romance", "romanti", "wife", "wive", "husband", "married", "marriage", "marry", "spouse"]):
			answers = [
				"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular.",
				"What are Windblumes? Something that the Anemo Archon Barbatos will not define. Flowers of blessings, flowers of respect, flowers of love. Every individual has their own Windblumes and every individual has the right to define them.",
				"The same wind graces the seaside as that which wafts over pastures green. Wherever you see clouds, it was the wind that carried them there. Don't worry, my friend, the wind will always be with you.",
				"if you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["friend", "companion"]):
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
			await message.channel.send(random_message)
		elif "skill" in content:
			answers = [
				"Yoo-Hoo!",
				"Here we go!",
				"Brace yourselves!",
				"Let's play!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "burst" in content:
			answers = [
				"Think you can get away?",
				"Time for takeoff!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["fallen", "kill", "murder"]):
			answers = [
				"Let me sleep a while…",
				"Oh no, my lyre is broken…",
				"Ah... Ugh…",
				"Womp womp…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["cat", "sneeze", "meow", "mew", "purr", "kitt", "hiss", "allerg"]):
			answers = [
				"I'm actually highly allergic to cats, I start sneezing as soon as they enter the vicinity, and... Aaah... Aa-choo! Ugh, apparently I can't even THINK about cats without sneezing. Do you think there is a cure for this monstrous affliction?",
				"Together with you, even apples taste sweeter.\nBut something isn't quite right, it feels like... I'm gonna s—sneeze.",
				"Achoo! Ugh... Guess I shouldn't get too close to the cats after all... I'll just stay on the roof.",
				"Oof, my nose is starting to itch again…",
				"There's a special drink known far and wide at Cat's Tail. But it ah... ahh... ACHOO! <:VentiSneeze:1394239013254201444>*sniffs* How about you go and fetch one for me? I'll be truly thankful, I promise.",
				"ACHOO! *cough* Haha... Apologies. At this distance, my cat allergy seems to be rearing its head…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "mondstadt" in content:
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
				"The winds of Mondstadt will guide every lost ship back to safe harbor."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["the seven", "archons", "gods"]):
			answers = [
				"'The Seven' as people now know them, were once known as 'The Seven Archons.' Each archon presides over their own part of Teyvat. That is the role the archons play. Only in performing this duty can we attain power, but I don't like the idea of 'ruling' Mondstadt — and I don't feel Mondstadt would really like it either.",
				"I haven't been back to Mondstadt for an extended period of time. Without a doubt, I am now the weakest archon among The Seven!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif "gnos" in content:
			await message.channel.send("As you know, Visions are external magical foci that only a small minority of people possess. They use these Visions to channel elemental power. In truth, every wielder of a Vision is one who can attain godhood and ascend to Celestia. We call such people allogenes. However, archons don't need primitive tools like Visions. Instead, each archon has an internal magical focus that resonates directly with Celestia itself... known as a Gnosis.")
		elif any(keyword in content for keyword in ["vision", "allogene", "eye of god", "element"]):
			answers = [
				"Hmm? You want to know about my Vision? Oh, go on then, take a look for yourself. I can make you a matching one if you like! Hehehe.",
				"As you know, Visions are external magical foci that only a small minority of people possess. They use these Visions to channel elemental power. In truth, every wielder of a Vision is one who can attain godhood and ascend to Celestia. We call such people allogenes.",
				"My vision? Eh-he. It's just a glowing glass ball I carry around to avoid suspicion."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif "dandelion" in content:
			answers = [
				"The people of Mondstadt believe that the wind can bring back the soul, and also preserve memories. Dandelion Seeds are like living gemstones, formed from the first wisps of wind in the year. People add them to the mix at the last second as a way of capturing the wind in the very moment that the barrel is sealed. The memory of that moment is then stored in the wine, for all time.",
				"Master Diluc, the boss of... ah, the owner of the Angel’s Share. He's very famous. By the way, his dandelion wine is one of my favorites. Though most of the time I can only afford a bottle or two…",
				"Dvalin and I used to listen to the songs of the wind and sing Ode to the Dandelion together… That's why I remember him as someone gentle."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["cecilia", "flower", "bouquet", "rose", "bloom", "blossom", "white"]):
			answers = [
				f"{user}, have you ever seen a cecilia? It's a magnificent white wildflower that only grows on the most remote mountains and clifftops. To me, at least, it is the most beautiful flower in all of Teyvat.",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				"A flower that blooms on the highest peaks and known for its exquisite beauty, the Cecilia is held by many Mondstadters to be the true 'Windblume.'",
				"Be it for the gods or that special someone, flowers should be offered in utmost sincerity. It's the most important ceremony of the Windblume Festival. Flowers of love and blessing, sent on such a special occasion... No effort should be wasted to make it spectacular.",
				"'The true feelings of the prodigal son.' A sentiment as sweet and warm as a gentle spring breeze — perfect for the season!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["journey", "meaning", "profound", "inspir", "experienc"]):
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["practice", "rehears", "every song"]):
			answers = [
				"Practice? Me? There's no need - I already know every song in Teyvat!"
				"Ready for a rehearsal?",
				"I'll sing along to a suite I haven't played in a long time. Any songs you wanna hear? I can practice a bit beforehand. Of course, this won't take up much time.",
				"I'm the best bard in the world. There's not a single song I do not know, no matter if it's from the past, present, or future."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["happy", "happiness", "joy"]):
			answers = [
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"I want to record all these beautiful memories, and turn them into ballads!",
				"The point of traveling is to record any feelings stirred along the way. As long as you had an unforgettable experience, this journey has served its purpose.",
				"Staying true to their journey and discovering joy and freedom for themselves is what Mondstadters do best."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["rain", "precipitation", "sprinkle", "drizzle", "mizzle", "shower", "pour"]):
			answers = [
				"Let's go jumping in puddles and see who can make the biggest splash!",
				"It's stopped raining already? A shame, I wanted to play some more."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["snow", "blizzard", "sleet", "hail", "hale"]):
			await message.channel.send("Let's wait till the snow gets heavier and have a snowball fight!")
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
			await message.channel.send(random_message)
		elif "wish" in content:
			answers = [
				f"Perfect timing, {user}! I was about to ask you — what is your greatest wish?",
				"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				"Right now I wish I was sitting at the top of a tree, looking out over a meadow, cider in hand... *sigh*"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif "cheers" in content:
			answers = [
				"To our precious days of freedom. Cheers!",
				"**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to good wine!**",
				"Here's to the time spent drinking with friends, which is more unforgettable than the drinks are delectable."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["clap", "applaus", "that was"]) and any(keyword in content for keyword in ["clap", "applaus", "amazing", "perfect", "great", "beautiful", "fantastic", "good", "wonderful"]):
			await message.channel.send("How was it? Not bad, right?")
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif "grape" in content:
			answers = [
				"Celestia... I'm not sure even I could fly that far. In any case, the water there tastes foul and the fruit is bland. You know what that means? No cider! Haha, in that case, I wouldn't go there even if I was invited.",
				"Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["cheese", "slim", "smell", "stick", "disgust", "mess"]):
			await message.channel.send("What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!")
		elif any(keyword in content for keyword in ["sit", "rest", "watch", "meadow", "tree", "mountain", "cliff", "windrise", "park", "relax", "scen", "bench", "chair", "nice day", "sun", "ocean", "sea"]):
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["work", "job", "employ", "w*rk", "j*b", "empl*y"]):
			answers = [
				"Good work. Shall we repose for a moment, with a tune? Shall it be a capriccio, or a serenade?",
				"So, a short rest after the big battle, huh? In that case, I think some light-hearted music is in order. Something easygoing enough to help everyone relax, but not to the point where it becomes too snoozeworthy. Take a seat wherever you like! Once you're comfortable, Der Frühling and I shall begin our serenade.",
				"I wonder how many bottles this'll be worth…",
				"Caught you~!\nThe farther your journey takes you, the less time we have to spend together in Mondstadt.\nBut... I knew I'd run into you today.\nQuick, just sit down, right here! It's a rare chance, so allow me to croon you a dulcet tune, accompanied by the melody of the water's revelry.",
				"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["morn", "dawn", "sunrise"]):
			answers = [
				"Morning! What's in store for today?",
				f"Morning, {user}, hehe. Going anywhere to play today? There are a lot of places I wanna visit — need a recommendation?",
				"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				"Hmm~ Whew, the weather today's just perfect for relaxing atop a tree.\nCompared to the terribly exciting life I've been leading lately, this kind of leisurely routine just suits me better.\nThanks to you, Mondstadt was able to pull through its time of crisis and return to a time of peace. That means I get to return to being an easy-going bard again!\nMayhaps I shall grace you with a song written in your honor, as an expression of my thanks? Hear ye, hear ye, my gratitude already rustles like a melody through the leaves!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["night", "evening", "dusk", "twilight", "sleep"]):
			answers = [
				"I'm still not sleepy, fancy an evening stroll?",
				"Off to the land of nod? Haha, Farewell my friend!",
				f"Aw, I don't want to sleep yet, {user}. Wanna keep me company a bit longer? Or... I'll keep you company?",
				"Get a good night's sleep tonight. Wait for the whisper of the gentle breeze to rouse you tomorrow morning, then come and enjoy a performance by the greatest bard to ever grace the streets of Mondstadt."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["olah", "hili", "hilli", "churl"]):
			answers = [
				"Olah! Haha, that's how the Hilichurls say 'hello'. Why, I learned it to aid with my songwriting, of course! Vast knowledge makes for a richer composition... That said, I haven't actually written any songs in Hilichurlian so far...",
				"Eh, olah! Mosi mita!",
				"The Abyss Order is an organization comprised of non-human beings. They despise mankind. I don't know where they come from. All I know is that they hold deep hatred towards the human world. Many hilichurls out in the wild take orders from them and act as their weapons.",
				"Hilichurls usually do not venture into areas with high elemental concentrations. It puts a heavy burden on their bodies."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["cape", "cloth", "fashion", "outfit", "wearing", "design", "aesthetic", "pocket"]):
			await message.channel.send("People often claim that capes and the like serve no real purpose other than aesthetics. I suppose a cape with pockets would really turn the tables on that crowd!")
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["do you", "what", "here"]) and any(keyword in content for keyword in ["like", "love", "good", "think", "thoughts", "opinion", "art", "made", "for you", "about you", "draw", "paint"]):
			answers = [
				"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				"I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["hello", "hi", "hey", "herro", "konnichiwa", "hola", "greet"]):
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
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["treasure", "chest", "mora", "money"]):
			answers = [
				"I have decided to write a song about you! What are you giving me that look for? Can't afford it? Don't be preposterous, the price for you, my friend, is precisely zero Mora! Although... one thing you could do is tell me a few more of your stories!",
				"There's never a dull moment traveling with you! The only minor inconvenience is that pesky little pixie thing that follows you everywhere... she never stops eating, I can't begin to imagine how much you spend on food!",
				"*clears throat* Have you heard The Ballad of the Treasure Chest?",
				"Thank Barbatos! Wait a minute…",
				"What a find! I wonder how many bottles this'll be worth…"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["investigat", "conclus", "fact", "objectiv", "subjectiv"]):
			await message.channel.send("A fair investigation means coming to a conclusion presented by the facts. Remaining objective has its own value.")
		elif "natlan" in content:
			await message.channel.send("This world sure is cruel, forcing generation upon generation of human heroes to become cannon fodder in the fight against the darkness. But, under Mavuika's leadership, they achieved a truly god-like feat... Hehe, starting with 'her,' I suppose the Natlanese have always been like that. Ah, right! I heard Mavuika likes to drink! Are you thinking what I'm thinking...?")
		elif "liyue" in content:
			await message.channel.send("Have you seen that gentleman around? Huh? He's just a normal man by the name of Zhongli now? That must be quite the change for that old block-head. Come with me to see him, will you? I have a vintage I dug up from Windrise that I can take as a condolence gift. Oh, ahh... did he still seem strong when you saw him? How strong? Am I likely to get blown away?")
		elif "inazuma" in content:
			await message.channel.send("So, I hear you defeated the mighty Raiden Shogun? Ah, I recall the days when she was a kagemusha, seeking to perfect her martial prowess. Hehe, she now no doubt employs a wide range of reasoning to get you to train with her. Oh but yes, come close and I shall let you in on her weakness — desserts!")
		elif "sumeru" in content:
			await message.channel.send("The first thing you think of when you hear 'Dendro Archon' is her power over dreams. Her dreams are akin to my ballads: full of emotion and imagination. It goes without saying that we get along really well.")
		else:
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
				f"O, Traveler, do you seek to hear the voice of the wind and know its guidance? Then I say to you... chatting to the deacon is your best bet. Haha, I'm kidding — come chat with me over a drink any time you want! The reason I usually get Dahlia to be my intermediary is because... well, I imagine you can probably guess why. He loves listening to the blustering of the wind, but crucially he has his own compass, too.",
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
			await message.channel.send(random_message)
keep_alive()
client.run(TOKEN)
