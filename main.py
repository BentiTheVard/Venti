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
    if message.author == client.user:
            return
    elif any(keyword in message.content.lower() for keyword in ["v!", "<@1402784150301184020>", "hey venti", "hi venti", "hello venti", "@venti", "!venti"]):
	    if "v!sleep" in message.content.lower() and message.mentions:
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
	    elif "v!give" in message.content.lower():
		    if "apple" in message.content.lower():
			    answers = [
				    "Oh, is this apple for me? Haha, that won't do, come share this apple with me.\nSplit it open like this...and you will feel the breeze from the apple core.\nIn some fairy tales, it is written that there is a whole tiny world hidden inside an apple core, and this breeze is a gift from the tiny world.\nHere, this half is for you. Once you're done eating, let's take a stroll in the tiny little world.\nBut remember to keep it a secret and don't tell anyone else. That's because... you're the only one I want to bring there.",
				    "Apples are truly wonderful. You can eat them, make cider with them... Why, there's no problem that can't be solved by throwing apples at it! Mm-mmm~",
				    "Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
			    ]
			    random_message = random.choice(answers)
			    await message.channel.send(random_message)
		     elif "grape" in message.content.lower():
				    answers = [
					    "Whoa! This orchard smells wonderful! The apples must be super big and juicy! And these bunches of grapes weighing down the dense vines... *sigh* They'll become delicious wine one day… Why don't we... sample some of these future wines? Hehe, it can't hurt to enjoy them a little. Come on, open wide~",
					    "Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?"
				    ]
				    random_message = random.choice(answers)
				    await message.channel.send(random_message)
		     elif "wine" in message.content.lower():
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
		     elif any(keyword in message.content.lower() for keyword in ["beverage", "sake", "beer", "champagne", "wine", "tumbler", "cocktail", "tropical", "drink", "alcohol"]):
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
		     elif any(keyword in message.content.lower() for keyword in ["cheese", "pancake"]):
				    answers = [
					    "What's that tasty morsel you've got there... Eew! A melted cheese pancake! A smelly, sticky, slimy disgusting mess!",
					    "I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament."
				    ]
				    random_message = random.choice(answers)
				    await message.channel.send(random_message)	
		     elif any(keyword in message.content.lower() for keyword in ["pear", "tangerine", "lemon", "lime", "banana", "melon", "berry", "cherr", "peach", "mango", "coconut", "kiwi", "cookie", "cake", "pie", "birthday", "nut", "cup", "glass"]):
				    await message.channel.send("Ahh, quite delightful! So... could I get the same thing again tomorrow? ...And maybe the day after that?")
		     elif any(keyword in message.content.lower() for keyword in ["plant", "tomato", "avocado", "pea", "broccoli", "leaf", "cucumber", "pepper", "corn", "carrot", "olive", "potato", "ginger", "croissant", "bagel", "bread", "pretzel", "meat", "poultry", "hot dog", "burger", "fries", "sandwich", "falafel", "salad", "food", "stew", "bento", "rice", "oden", "dango", "ice", "lollipop", "candy", "chocolate", "popcorn", "doughnut", "donut", "bean", "tea", "coffee", "mate", "salt", "takeout”]):
				    await message.channel.send("Oof, I'm so full... I'll have to pass on the post-meal fruits this time…")
		     elif any(keyword in message.content.lower() for keyword in ["garlic", "onion", "egg", "cooking", "butter", "waffle", "bacon", "bone", "pizza", "taco", "burrito", "tamale", "fondue", "canned", "jar", "spaghetti", "ramen", "curry", "sushi", "dumpling", "oyster", "shrimp", "custard", "pudding", "honey", "milk", "liquid”]):
				    await message.channel.send("I can't believe it, but I don't think I can stomach this... Oh boy... What a predicament.")
        ]):
keep_alive()
client.run(TOKEN)
