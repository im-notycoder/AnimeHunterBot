import random
from pyrogram import Client, filters, enums
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "God... every child's... passion...",
    "I don't know how to write sir... I don't know how to read...",
    "Don't be silent today...after today's fort...",
    "Thinking that it is ash, it will burn if you don't build it."
    "Understand that there is only one life, there is no heaven and no hell, 'one life', where and how he wants it."
    "What a bombastic explosion! Such a terrific reveal!!",
    "Go Away Stupid in the House of My Wife and Daughter You Will Not See My Minute of Today... Don't Get Down...",
    "I Can Do That Do Can I That",
    "Just because there is cream in a cream biscuit, there is no tiger in a tiger biscuit. Pani milk, man...",
    "It's like when Pata got scared and went to the panthalam, it's like Pantom said to go to the panthalam."
    "My Lord.... You will not allow me to be good.",
    "Car engine out completely...",
    "It's not over now!"
    "Has your father made porotta and chicken for midnight...",
    "Oh, when you fall in love, it's love. When we fall in love, it's wire...."
    "God save me alone...",
    "Waste the toddy and wet rain drunk for her sake...",
    "Where have you been all this time...!",
    "You don't know much English, do you?"
    "All the Dreams Like Twinkle Stars...",
    "My Pranthan Thappa make him a way",
    "Will you give me the dowry amount, Ali?"
    "You're so tired"
    "I was waiting with tears in my eyes."
    "Let's go and say, wood. Ya .\
    Shut your mouth bloody gramavasis.",
    "Go shit.\
    patto die with you.",
    "Because of you, the locals and those who left Gunollya, why are Gunollya ashamed and living like this, Lord Chengtali Vazha."
)

@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
