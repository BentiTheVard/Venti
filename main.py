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
    if message.channel.name == "🪽barbatos-statue":
        if message.author == client.user:
            return

        #OFFER DANDELIONS COMMAND
        elif any(keyword in message.content.lower() for keyword in [
                "!wish", "!offer", ":dandelion:", ":flower_dandelion:", "💐",
                "!dandelion", ":ventiflower", ":cecilia"
        ]):
            user = message.author.display_name

            offerings = [
                f"**Seeds of stories, brought by the wind and cultivated by time, will in due time become legends...**\n\n(*{user} offers turquoise dandelion seeds to the statue, and they float away in the wind.*)",
                f"**Seeds of stories, brought by the wind and cultivated by time, will in due time become legends...**\n\n(*{user} offers glowing dandelion seeds to the statue, and they float away into the sky.*)",
                f"**Seeds of stories, brought by the wind and cultivated by time, will in due time become legends...**\n\n(*The dandelion seeds from {user} disperse across the Anemo Archon statue's hands, and flutter away in the breeze.*)",
                f"**Seeds of stories, brought by the wind and cultivated by time, will in due time become legends...**\n\n(*{user}'s Dandelion Seeds miss the hands of the statue, but drift away in the North Wind even so.*)"
            ]

            random_message = random.choice(offerings)
            await message.channel.send(random_message)

        #PRAY COMMAND
        elif any(keyword in message.content.lower() for keyword in [
                "!pray", ":dahliapray:", ":barbarapray_ikazu401:", "!ask",
                ":ventipray:"
        ]):
            user = message.author.display_name

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
                "Your prayers have been heard."
            ]

            random_message = random.choice(answers)
            await message.channel.send(f"{user}...\n\n*{random_message}*")

    #KISS COMMAND
        elif any(keyword in message.content.lower() for keyword in ["!kiss"]):
            user = message.author.display_name

            messages = [
                f"(The statue does not react to being kissed.)",
                f"(The statue does not react to being kissed, but a dandelion floats down and lands on {user}'s head.)",
                f"<:VentiShock:1394123854518948041>",
                f"(The statue does not kiss {user} back.)",
                "(Isn't 2600 years too old for you...?)",
                f"(A child notices {user} kissing their god's statue and runs away.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #HUG COMMAND
        elif any(keyword in message.content.lower() for keyword in ["!hug"]):
            user = message.author.display_name

            messages = [
                f"(The statue is slightly cool to the touch.)",
                f"(A gentle breeze surrounds {user}.)",
                f"({user} feels a sense of serenity.)",
                f"(The statue does not react to being hugged.)",
                f":red_heart:", f":green_heart:",
                f"<:VentiLyre:1394240762060734546>", f":light_blue_heart:"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #PAT COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!pat", "!pet"]):
            user = message.author.display_name

            messages = [
                f"(The statue is slightly cool to the touch.)",
                f"(A gentle breeze surrounds {user}.)", ":heart:",
                f"({user} feels a sense of serenity.)",
                f"(The statue does not react to being patted.)",
                f"(A cat approaches {user} and wants to be petted instead.<:b_pat:1395796337701945485>)",
                f"(A dog approaches {user} and wants to be petted instead.)",
                f"(A group of children notice {user} petting the Barbatos statue and begin petting him as well.)",
                f"<:VentiLyre:1394240762060734546>", f":red_heart:",
                f":green_heart:", f":light_blue_heart:"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #STEAL COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!steal", "!grab", "!take"]):
            user = message.author.display_name

            messages = [
                f"({user} tries to move the statue, but it is far too heavy.)",
                f"({user} fails to steal the statue.)",
                f"({user} feels a breeze deliberately tickling their nose.)",
                f"({user} fails.)",
                f"({user} tries to steal the statue, but it is far too heavy.)",
                f"(A breeze begins to blow {user} away from the statue.)",
                f"(A leaf floats from afar and leads {user} to the direction of <#1394172531207831572>.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #VANDALIZE COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!vandalize", "vandalise"]):
            user = message.author.display_name

            messages = [
                f"<:VentiRainbow:1394520285260288138>",
                "(The colors fade off of the statue.)",
                "(Would Barbatos be laughing or crying?)",
                "(The Barbatos statue has been vandalized.)",
                f"(The Favonius Church is now annoyed with {user}.)",
                f"({user}: -10 Reputation!)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #SEDUCE COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!seduce", "!seduc"]):
            user = message.author.display_name

            messages = ["...", "(???)"]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #FLIRT COMMAND
        elif any(keyword in message.content.lower() for keyword in ["!flirt"]):
            user = message.author.display_name

            messages = [
                "...", "(???)", "(That one doesn't work on an archon.)",
                "(That one doesn't work on a statue.)", "(🫵simp)",
                f"({user} is down bad.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #SQUISH CHEEKS COMMAND
        elif any(
                keyword in message.content.lower() for keyword in
            ["!squishcheeks", "!squishcheek", "!squish", "!smush", "!cheeks"]):
            user = message.author.display_name

            messages = [
                f"({user} fails to squish the statue's cheeks.)",
                f"({user} is unable to squish the Barbatos statue's cheeks.)",
                "(The freedom to squish stone is not one even Barbatos can grant.)",
                "<:VentiSneeze:1394239013254201444>",
                "<:VentiUwU:1394123911284920341>"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #CLEAN COMMAND
        elif any(
                keyword in message.content.lower() for keyword in
            ["!clean", "!polish", "!smooth", "!smoothen", "!brush", "!wash"]):
            user = message.author.display_name

            messages = [
                "(The Barbatos statue looks even shinier.)",
                "(Anemo energy radiates from the statue.)",
                "<:ventichopstick_hen:1394193049223168071>",
                "<:VentiLyre:1394240762060734546>",
                "(The statue's braids are even more beautiful.)",
                "<:VentiCool:1394244153239404545>",
                "(The vandalization appears to be fixed.)",
                f"(The Church of Favonius is pleased with {user} for cleaning the Barbatos statue.)",
                f"({user}: +10 Reputation!)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #CAT COMMAND
        elif any(keyword in message.content.lower() for keyword in
                 ["!cat", "!meow", "!purr", "!nya", "!mew", "!kitt", "!hiss"]):
            user = message.author.display_name

            messages = [
                "<:VentiSneeze:1394239013254201444>",
                "<:VentiSneeze:1394239013254201444>"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #STEAK COMMAND
        elif any(keyword in message.content.lower() for keyword in ["!steak"]):
            user = message.author.display_name

            messages = [":cut_of_meat:", ":cut_of_meat:"]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #BARBATOES COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!barbatoes", "!ventifeet"]):
            user = message.author.display_name

            messages = [
                "(The Barbatoes glow dimly.)",
                "(The Barbatoes emit Anemo energy.)", "(The Barbatoes exist.)",
                "(Barbatoes)", "(The statue does, indeed, have Barbatoes.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #EAT COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!eat", "!bite", "!chew", "!munch", "!nom"]):
            user = message.author.display_name

            messages = [
                "(Barbatos is not emergency food!)",
                f"({user}'s tooth cracks.)",
                f"({user} tries to chew on the statue and fails horribly.)",
                "(Barbatos is not Barbatoast.)",
                f"({user} is not Rhinedottir.)", "(Barbatos is not Naberius.)",
                "(The Favonius Church is concerned.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #HIT COMMAND
        elif any(keyword in message.content.lower() for keyword in [
                "!hit", "!punch", "!slap", "!fight", "!smack", "!attack",
                "!yeet", "!bodyslam", "!violence", "!duel"
        ]):
            user = message.author.display_name

            messages = [
                "(??)", "(The wind feels colder now.)",
                "(There's a sharp chill in the air.)",
                "(Plucking its strings, he scattered the ice and snow and **split the mountains** with a divine wind.)",
                f"(The Favonius Church is angry at {user}.)",
                "(Barbatos notices.)", "(Against  the God of Wind?)",
                "(Pacifism is a trait best worn.)",
                "<:VentiRefuse:1394238074707251271>", "(-10 aura.)",
                f"({user} attacks the statue.)", "(???)",
                "(Is violence truly necessary?)",
                f"(Surely {user} knows of Barbatos' pacifistic nature.)",
                f"({user} feels cold.)", f"(A strong wind surrounds {user}.)"
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)

    #COMPLIMENT COMMAND
        elif any(keyword in message.content.lower() for keyword in [
                "i love", "ily", "love you", "love u", "thank you", "thanks",
                "beautiful", "pretty", "cute", "adorable", "the best", "sweet",
                "precious", "favorite", "fave", "favourite"
        ]) and any(keyword in message.content.lower()
                   for keyword in ["venti", "barbatos"]):
            user = message.author.display_name

            if len(message.content) > 50:
                messages = [
                    f":red_heart:", f":green_heart:",
                    f"(**{user}: Beloved of the Anemo Archon :tulip:**)",
                    "*However far you drift, the wind will guide you home...*",
                    f"(A dandelion floats down and lands on {user}'s head.)",
                    f"(A gentle breeze surrounds {user}, bringing the hopeful scent of spring.)"
                ]
            else:
                messages = [
                    f":red_heart:", f":green_heart:",
                    f"<:VentiLyre:1394240762060734546>", f":light_blue_heart:",
                    f"(A gentle breeze surrounds {user}.)",
                    f"(**{user}: Beloved of the Anemo Archon :tulip:**)"
                ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)
            if len(message.content) > 50:
                randImg = random.randint(1, 10)
                image_name = f"venti{randImg}.gif"
                file = discord.File(image_name)
                await message.channel.send(file=file)

    #VENTI BARBATOS COMMAND
        elif any(keyword in message.content.lower() for keyword in [
                "!vent", "!barbat", "!vanti", "@venti", "@barbatos",
                "hey venti", "hey barbatos", "dear venti", "hi venti",
                "venti?", "barbatos?"
        ]):
            randImg = random.randint(1, 10)
            image_name = f"venti{randImg}.gif"
            file = discord.File(image_name)
            await message.channel.send(file=file)

    #SIT COMMAND
        elif any(keyword in message.content.lower()
                 for keyword in ["!sit", ":ventiwatch:"]):
            user = message.author.display_name

            messages = [
                "***The wind feels gentler now.***",
                "***Atop the Anemo Archon statue, the sounds carried by the wind seem to reverberate.***",
                '***The lights in the City of Freedom glow down below.***\n\n("Surely, he too would have wanted to live in such a place.")'
            ]
            random_message = random.choice(messages)
            await message.channel.send(random_message)
            user = message.author.display_name
            role = discord.utils.get(message.guild.roles,
                                     name="🌷Beloved of the Anemo Archon")
            if role is None:
                await message.channel.send(f"(Role not found.)")
            if role in message.author.roles:
                await message.channel.send(
                    f"(**{user}: Beloved of the Anemo Archon :tulip:**)")
                randImg = random.randint(1, 10)
                image_name = f"venti{randImg}.gif"
                file = discord.File(image_name)
                await message.channel.send(file=file)
            else:
                await message.author.add_roles(role)
                await message.channel.send(
                    f":dizzy:(**{user} gained role: Beloved of the Anemo Archon :tulip:**)"
                )
                randImg = random.randint(1, 10)
                image_name = f"venti{randImg}.gif"
                file = discord.File(image_name)
                await message.channel.send(file=file)


keep_alive()
client.run(TOKEN)
