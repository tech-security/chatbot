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
