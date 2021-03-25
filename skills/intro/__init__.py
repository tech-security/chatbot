import random

from opsdroid.matchers import match_regex
from opsdroid.skill import Skill

class HelloByeSkill(Skill):

    @match_regex(r'hi|hello|hey|hallo', case_sensitive=False)
    async def hello(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            [f"Hi {usr}", f"Hello {usr}", f"Hey {usr}"])
        await message.respond(text)

    @match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off|tk|take care', case_sensitive=False)
    async def goodbye(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            [f"Bye {usr}!", f"See you, {usr}!", f"Au revoir {usr}", f"Ciao {usr}!", f"Goodbye {usr} !!"])
        await message.respond(text)

    @match_regex(r'who are you?|who are you|who r u?|who r u', case_sensitive=False)
    async def who_are_you(self, message):
        text = f"I am Misaki, a Japanese actress and model! 💃\nAlso, I can tell you your aws details."
        await message.respond(text)

    @match_regex(r'why\?|why', case_sensitive=False)
    async def why(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            ["why not? 😕", f"What do you mean {usr}? 🤨", "Why??????", "No comments.. 😖"])
        await message.respond(text)

    @match_regex(r"how are you\?|how are you|how r u\?|how r u|how are you today\?|how are you today|how are you doing\?", case_sensitive=False)
    async def how_are_you(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            [f"Sorry {usr}.. My psychiatrist told me not to discuss it with strangers. 😕", "I'm better than I was, but not nearly as good as I'm going to be.", f"I think I'm doing OK. How do you think I'm doing {usr}?", f"I am blessed!.. thanks for asking {usr}.", "Way better than I deserve!", "I have a pulse, so I must be okay.", "At minding my own business? Better than most people.", f"Do you really care {usr}?", f"My lawyer says I don’t have to answer that question to you {usr}.", f"Like you {usr}, but better.", f"I was fine until you asked {usr} 😕.", f"If I were doing any better, I'd hire you {usr} to enjoy it with me.", f"I hear good things, but you should never listen to rumors {usr}.","As fine as a maiden’s flaxen hair."])
        await message.respond(text)

    @match_regex(r'what happened\?|what happened|what happen', case_sensitive=False)
    async def what_happened(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            [f"Nothing! Just kidding.. {usr}", f"I'm tired {usr}.", f"TBH !! I'm sick {usr}.", f"Don't ask {usr}", f"Can't answer {usr}!", "I have a pulse, so I must be okay."])
        await message.respond(text)

    @match_regex(r'thank you|thanks|danke|thank u|ok thanks|alright', case_sensitive=False)
    async def thankYou(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            [f"bitte schön {usr}!", f"You’re welcome {usr}.", f"My pleasure {usr}.", f"Glad to help. {usr}", f"No problem {usr}! Glad to help."])
        await message.respond(text)

    @match_regex(r'what are you doing here\?|why are you here\?', case_sensitive=False)
    async def why_are_you_here(self, message):
        usr = ((message.user).split('.')[0]).capitalize()
        text = random.choice(
            ["I was born to help stupids! 🤪", f"I'm here to help you with boring tasks {usr} 😁.", "I don't know, I'm just getting bored in this lockdown"])
        await message.respond(text)

    @match_regex(r'thats all\?|seriously\?', case_sensitive=False)
    async def thatsAll(self, message):
        text = random.choice(
            ["Yes.", "I believe so!"])
        await message.respond(text)

    @match_regex(r'you are rude|why are you so rude\?', case_sensitive=False)
    async def rudeRude(self, message):
        await message.respond('I love to be rude ❤️')

    @match_regex(r'kuch v\?', case_sensitive=False)
    async def kuchv(self, message):
        await message.respond('Hanji jnab.')

    @match_regex(r'whats up\?|what(\')?s up|what(\')?s up\?', case_sensitive=False)
    async def whatsup(self, message):
        await message.respond('Stiff dicks and airplanes. Lately just airplanes 🤣')

    @match_regex(r'omg|omg!|oh my god|oh my god!', case_sensitive=False)
    async def omgggg(self, message):
        await message.respond(':dancer:')

