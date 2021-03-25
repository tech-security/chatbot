import random, boto3

from opsdroid.matchers import match_regex
from opsdroid.skill import Skill

## Config
session = boto3.Session(profile_name='sc-dafiti1')
#session = boto3.Session()
iam = session.client("iam")
resource = session.resource("iam")

class AwsSkills(Skill):
    @match_regex(r"which aws account is it\?|which aws account\?|which account is it\?|which account is that\?", case_sensitive=False)
    async def accID(self, message):
        await message.respond(f"Please wait.. let me check!")
        ac_id = session.client('sts').get_caller_identity().get('Account')
        alias = session.client('iam').list_account_aliases()['AccountAliases'][0]
        await message.respond(f"It's {alias}: `{ac_id}`.")

    @match_regex(r'list all keys|tell me all the keys for all users|tell me keys of all the users', case_sensitive=False)
    async def listKeys(self, message):
        keyss = []
        await message.respond('Sure thing! on it.. please wait..')
        for user in resource.users.all():
            list_keys = iam.list_access_keys(UserName=user.user_name)
            for key in list_keys["AccessKeyMetadata"]:
                keyss.append(key["UserName"] + ': ' + key["AccessKeyId"])
        kz = '```' + '\n'.join(keyss) + '```'
        await message.respond('Here you go:\n'+kz)

'''
list_keys = iam.list_access_keys(UserName="tajinder")
for key in list_keys["AccessKeyMetadata"]:
    print (key["UserName"] + ': ' + key["AccessKeyId"])
'''
