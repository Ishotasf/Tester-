# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """ **Terima Kasih Telah Deploy Ryn-Userbot!**

Beberapa Bantuan Untuk Kamu Pelajari.""",
    2: """🎉** Tentang Ryn-Userbot**

 Ryn-Userbot adalah repo userbot yang dibuat untuk kekasih saya, userbot ini memiliki beberapa fitur kamu bisa melihat nya dihalaman 4.

▢ Dibuat oleh **@Usern4meDoestExist404**""",
    3: """

-> Kamu bisa memutar musik melalui userbot ini.
-> Kamu bisa menggunakan chatgpt atau openai.
-> Kamu bisa merubah teks menjadi beberapa gaya font.
-> Kamu convert foto kamu menjadi anime.
-> Kamu bisa membalas seseorang dari Naya-Userbot Logs ketika kamu di tag oleh seseorang digrup lain.
-> Kamu bisa menggunakan fitur joinvc untuk menaikkan bot ke dalam obrolan suara
-> Userbot ini memliki fitur pmpermit inline
-> Kamu bisa menyimpan catatan apapun dengan media gambar serta button.
-> Kamu dapat berinteraksi dengan seseorang melali fitur chatbot

**• To Know About Updates**
  - Join @TeamAllBots.""",
    4: f"""**▢ Bantuan yang mungkin kamu ingin lihat •**

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """▢ **Selamat Bersenang senang**""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("Kembali", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("◁", f"initbk_{str(CURRENT - 1)}"),
            Button.inline("▷", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("◁", f"initbk_{str(CURRENT - 1)}"),
            Button.inline("▷", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
