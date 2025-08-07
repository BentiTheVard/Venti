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
	elif any(keyword in content for keyword in ["v!", "<@1402784150301184020>", "hey venti", "hi venti", "hello venti", "@venti", "!venti"]):
		if "v!sleep" in content and message.mentions:
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
#💎GIVE COMMAND (Food)
		elif "v!give" in content:
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
					"I'm Venti the Bard. Three-time winner of the "Most Popular Bard of Mondstadt," to be precise.<:VentiWink:1394244370697289790> What’s your name?",
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
					"I'm Venti the Bard. Three-time winner of the "Most Popular Bard of Mondstadt," to be precise.<:VentiWink:1394244370697289790> What’s your name?",
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
		elif any(keyword in content for keyword in ["Sad", "Cry", "Sick", "Hard", "Hurt", "Tear", "Pain", "Depress", "Tir", "Energy", "Suic", "Upset", "Help me", "Sniffle", "Weep", "Bad day"]):
			answers = [
				"Hee-hee... My warrior, you've worked so hard. I understand how you feel.\n...When you just can't find any more energy, and the world falls into a haze — even apples lose their sweet flavor.\nIf you can get some quality shut-eye at this time, you'll feel a lot better when you wake up. Here, I'll lend you my shoulder.\nAt any rate, don't worry. Whenever you need me, I'll always be by your side.",
				"Hmm… Many people may feel lost at times. After all, it's impossible for everything to happen according to your own wishes. At a time like this, ask yourself what the most important thing is!\nEven if life's all in a jumble, you can sort it out as long as there's a whisper of the wind.\n...Don't be afraid, I'm here."
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["You are", "Your", "Ur", "You’re", "Youre", "Venti is", "Barbatos is", "Venti’s", "Barbatos’s"]) and any(keyword in content for keyword in ["Lazy", "Bad", "Annoying", "Worst", "Useless", "Terrible", "Ugly", "Stupid", "Awful", "Drunkard", "Wastrel", "Drunken"]):
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
		elif any(keyword in content for keyword in ["I hate", "I dislike"]) and "u" in content: 
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
		elif any(keyword in content for keyword in ["Rodent", "Scurry", "Rat", "Pest", "Vermin"]):
			await message.channel.send("Resident rodent... beats invasive vermin.")
		elif any(keyword in content for keyword in ["Attack", "Fight", "Shoot", "Skill", "Burst", "Punch", "Slap", "Hit", "Kick", "Smack", "Bite", "Chew", "Steal", "Take", "Grab", "Slash"]):
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
		elif any(keyword in content for keyword in ["I love", "ily"]) and any(keyword in content for keyword in ["you", "venti", "barbatos", "u", "ily"]):
			answers = [
				f"My greatest wish? It has always been to roam free and experience the whole world. Now I would add that wherever I go, it simply must be with you! Each day with you is an adventure, and where adventurers go, storytellers must follow!",
				f"My dear, courageous {user}, if you will allow this humble bard to join you on your journey, it would be my honor to compose an epic poem to remember your deeds. I'm willing to bet a whole glass of Apple Cider that your story will be one for the ages!",
				f"Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				f"Yahoo~ Look up, I'm here!\nIt's been a long time, my warrior, ready to tell me your new story?\nHaha, you want to know if it's for my verses? Oh, don't make that face. I just want to hear about your adventures, isn't that reason enough?\nI want to know more about what you saw on your travels or the lives of others. The most important thing for me is to hear you talk about your own experiences and what you think about them.\nCome on, come sit next to me. This bottle of aged cider will be enough for us to chat from first dawn of the morning light until the stars cover the sky.",
				f"The morning sun is pretty pleasant, isn't it? Ehe, you can barely keep your eyes open.\nHere, come sit with me and enjoy the scent of Cecilias! They'll perk you up.\nAh, I lost track of time just chatting with you... Wait just a moment, I'm almost done!\nYou haven't eaten apple pie in a long time, have you? Then I'll make us breakfast today~",
				f"The breeze combing through your hair today feels a little different, don't you think?\nIt smells faintly of flowers and also carries a refreshing scent of spring water…\nIf you are sensitive to smells, I wouldn't be surprised if you can pick a hint of sweetness in today's wind. That's because I just ate an apple, haha!\nCome on now, let's go for a walk outside!\nWe can pick berries for a picnic and rest at a roadside tavern. With me, the best bard there is by your side, the journey will be great wherever we go.\nOops, I almost forgot. Here, this Cecilia bouquet is for you. Heh, we both smell like flowers now.",
				f"When you receive this letter, hold it in your hands and stand by the window.",
				f"Do you feel it? That gentle breeze nudging at your back? Hehe, why not follow the little leaf it carries — just big enough to rest in your palm — and let it guide you here, to me?",
				f"But don't get distracted by the scent of hash browns along the way, you hear? If you stuff yourself silly, the feast I've prepared might end up feeling a little... neglected.\nKeep walking, just a little further — go on and leave Mondstadt's lively bustle behind for now. Can you hear it? That melody is growing clearer by the moment.\nThe sunshine is beautiful today, and the picnic mat is as cool and airy as the breeze dancing across the lake. You'll spot it from far away, but of course, take your time~\nI'll be right here, waiting for you and strumming a tune.",
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
		elif any(keyword in content for keyword in ["Kiss/Smooch/Mwah"]):
			answers = [
				"A kiss? How kind of you!",
				"Oh, to hold such bardly charm… woe is me!",
				"Oh! Does this mean you want to buy me a drink?",
				"Oh dear…!",
				*gasp* Such PDA! <:VentiShock:1394123854518948041>",
				"You have to find the thing that makes you happy. Haha, mostly because your happiness is very important to me.",
				"If you have a moment now, would you care to hear a new love poem I wrote this year? Ahem! Allow me to recite it for you.\n*This world has never seen such vibrant color*\n*it bestows upon everyone a brilliant hue*\n*A shade more ethereal than white*\n*yet more radiant still than gold*\n*it eases into your eyes*\n*and restores to light a solitary soul.*",
				"Woah! What was that?",
				"Hahaha, that one doesn't work on a bard.",
				"<:VentiUwU:1394123911284920341>"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["Do you/What/Here"]) and any(keyword in content for keyword in ["Like/Love/Good/Think/Thoughts/Opinion/Song/Music/Piece/Compos"]):
			answers = [
				"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				"I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!",
				"Well, it sounds like you've already mastered music theory and your instrument. I don't think you need my input on either of those!"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
		elif any(keyword in content for keyword in ["Do you/What/Here"]) and any(keyword in content for keyword in ["Like/Love/Good/Think/Thoughts/Opinion/Art/Made/For you/About you/Draw/Paint"]):
			answers = [
				"It's great, of course. I know that every detail is the result of your hard work. I hold immense gratitude for all you've done.",
				"I love it! Oh, I'm flattered that you asked for my thoughts. But you should be more confident in your own tastes! Here, you're the real-deal protagonist! Try things with confidence and turn your ideas into reality. And if you ever run into trouble, I'll lend a helping hand!"
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
		elif any(keyword in content for keyword in ["Ding/Answer/Correct"]):
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
				'**I hereby declare that every son and daughter of the City of the Wind must be compelled to taste this finest of wines... Here's to femboys!**"
			]
			random_message = random.choice(answers)
			await message.channel.send(random_message)
#CHARACTERS ❤️
keep_alive()
client.run(TOKEN)
