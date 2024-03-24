# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from Ryn.dB._core import LIST
from telethon.errors.rpcerrorlist import BotInlineDisabledError
from telethon.tl.custom import Button

from . import HNDLR, asst, ryn_cmd, get_string

_main_help_menu = [
    [
        Button.inline(get_string("help_4"), data="uh_Official_"),
    ],
]


@ayra_cmd(pattern="^[Hh][Ee][Ll][Pp]( (.*)|$)")
async def _help(ryn):
    plug = ryn.pattern_match.group(1).strip()
    chat = await ryn.get_chat()
    if plug:
        try:
            x = get_string("help_11").format(plug)
            for d in LIST[plug]:
                x += HNDLR + d
                x += "\n"
                x += "\n© @CariSahabatOnline_Id"
                await ryn.eor(x)
        except BaseException as e:
            await ryn.eor(f"{e}")
    else:
        try:
            results = await ryn.client.inline_query(asst.me.username, "help")
        except BotInlineDisabledError:
            return await ryn.eor(get_string("help_3"))
        await results[0].click(chat.id, reply_to=ryn.reply_to_msg_id)
        await ryn.delete()
