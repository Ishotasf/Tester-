# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
▢ **Bantuan Untuk Animasi 3**

• **Perintah:** `Love` | `dino`
• **Keterangan:** Coba sendiri.

• **Perintah:** `Yatim` | `Kamu`
• **Keterangan:** Coba sendiri.

• **Perintah:** `bundir`
• **Keterangan:** Coba sendiri.

• **Perintah:** `Ryn` | `awk`
• **Keterangan:** Coba sendiri.

• **Perintah:** `bulan`
• **Keterangan:** Coba sendiri.

• **Perintah:** `waktu` | `santet`
• **Keterangan:** Coba sendiri.

• **Perintah:** `ajg`
• **Keterangan:** Coba sendiri.
"""

import asyncio
from time import sleep

from . import *


@ayra_cmd(pattern="^[Bb][u][l][a][n]$")
async def _(event):
    event = await eor(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ayra_cmd(pattern="^[Ll][o][v][e]$")
async def _(event):
    e = await eor(event, "I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")


@ayra_cmd(pattern=r"^[Dd][i][n][o]$")
async def _(event):
    typew = await eor(event, "**DIN DINNN.....**")
    # sleep(1)
    await typew.edit("**DINOOOOSAURUSSSSS!!**")
    # sleep(1)
    await typew.edit("**🏃                        🦖**")
    await typew.edit("**🏃                       🦖**")
    await typew.edit("**🏃                      🦖**")
    await typew.edit("**🏃                     🦖**")
    await typew.edit("**🏃   **LARII**          🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃WOARGH!   🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                    🦖**")
    await typew.edit("**🏃                     🦖**")
    await typew.edit("**🏃  Huh-Huh           🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃          🦖**")
    await typew.edit("**🏃         🦖**")
    await typew.edit("**DIA SEMAKIN MENDEKAT!!!**")
    sleep(1)
    await typew.edit("**🏃       🦖**")
    await typew.edit("**🏃      🦖**")
    await typew.edit("**🏃     🦖**")
    await typew.edit("**🏃    🦖**")
    await typew.edit("**Dahlah Kontol Pasrah Gua**")
    sleep(1)
    await typew.edit("**🧎🦖**")
    sleep(2)
    await typew.edit("**-TAMAT-**")


@ayra_cmd(pattern="^[yY][a][t][i][m]$")
async def _(event):
    e = await eor(event, "**EH SI ANAK YATIM**")
    await e.edit("**BIAR APA SI LU BEGITU ANJG?**")
    await e.edit("**NORAK LU GOBLOK**")
    await e.edit("**BARU MAIN TELE YA?**")
    await e.edit("**PANTES AJA SI JADI ANAK YATIM**")
    await e.edit("**KASIAN YAA GA DI URUSIN SAMA KELUARGA NYA**")
    await e.edit("**DASAR IDIOT LU YATIM**")
    await e.edit("**ANAK KONTOL HAHAHAHA**")
    await e.edit("**APA? GA SUKA?**")
    await e.edit("**MAU MARAH? MARAH AJA**")
    await e.edit("**EMANG LU PIKIR**")
    await e.edit("**GUA PEDULI SAMA LU?""")
    await e.edit("**HAHAHAHAHA**")
    await e.edit("**DASAR ANAK YATIM KONTOL**")


@ayra_cmd(pattern=r"^[Rr][y][n]$")
async def _(event):
    typew = await eor(event, "**Hello, I'm Yoshieki**")
    sleep(2)
    await typew.edit("**Siapa Si Yg Ga Kenal Gua?*")
    sleep(2)
    await typew.edit("**Lu Cuma Jadi Kacung Gua Doang.**")
    sleep(2)
    await typew.edit("**Gua Petinggi Nih Awokawok**")
    sleep(2)
    await typew.edit("**Apa? Mau Marah? Marah Aja Wlee**")
    sleep(2)
    await typew.edit("**Ga Deng Bg Bercanda Aku Tu Wleowleo**")
    sleep(2)
    await typew.edit("**Kalo Mau Yg Serius Di Pc Aja Ya Mwehehe**")


# Create by myself @localheart


@ayra_cmd(pattern=r"^[Mm][f]$")
async def _(event):
    await eor(event, "`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@ayra_cmd(pattern=r"^[Cc][i][n][t][a]$")
async def _(event):
    animation_chars = [
        "**Connecting Ke Server Cinta**",
        "**Mencari Target Cinta**",
        "**Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
        "**Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ **",
        "**Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ **",
        "**Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You 💞**",
    ]
    animation_interval = 2
    animation_ttl = range(11)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@ayra_cmd(pattern=r"^[Kk][a][m][u]$")
async def _(event):
    typew = await eor(event, "**Hai kamu, I LOVE YOU 💞**")
    sleep(1)
    await typew.edit("**I LOVE YOU SO MUCH!**")
    sleep(1)
    await typew.edit("**I NEED YOU!**")
    sleep(1)
    await typew.edit("**I WANT TO BE YOUR BOYFRIEND!**")
    sleep(1)
    await typew.edit("**I LOVEE YOUUUU💕💗**")
    sleep(1)
    await typew.edit("**I LOVEE YOUUUU💗💞**")
    sleep(1)
    await typew.edit("**I LOVEE YOUUUU💝💗**")
    sleep(1)
    await typew.edit("**I LOVEE YOUUUU💟💖**")
    sleep(1)
    await typew.edit("**I LOVEE YOUUUU💘💓**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong**")


# Create by myself @localheart


@ayra_cmd(pattern="^[bB][u][n][d][i][r]$")
async def _(event):
    await eor(
        event,
        "**Dadah Semuanya...**          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@ayra_cmd(pattern="^[Aa][w][k]$")
async def _(event):
    await eor(
        event,
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n**Awkwokwokwok...**",
    )


@ayra_cmd(pattern="^[Uu][l][a][r]$")
async def _(event):
    await eor(
        event,
        "░░░░▓\n"
        "░░░▓▓\n"
        "░░█▓▓█\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓███\n"
        "░░░░██▓▓████\n"
        "░░░░░██▓▓█████\n"
        "░░░░░░██▓▓██████\n"
        "░░░░░░███▓▓███████\n"
        "░░░░░████▓▓████████\n"
        "░░░░█████▓▓█████████\n"
        "░░░█████░░░█████●███\n"
        "░░████░░░░░░░███████\n"
        "░░███░░░░░░░░░██████\n"
        "░░██░░░░░░░░░░░████\n"
        "░░░░░░░░░░░░░░░░███\n"
        "░░░░░░░░░░░░░░░░░░░\n",
    )


@ayra_cmd(pattern="^[yY]$")
async def _(event):
    await eor(
        event,
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


@ayra_cmd(pattern="^[Bb][a][b][i]$")
async def _(event):
    await eor(
        event,
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@ayra_cmd(pattern="^[Aa][j][g]$")
async def _(event):
    await eor(
        event,
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


@ayra_cmd(pattern="^[Ss][a][n][t][e][t]$")
async def _(event):
    typew = await eor(event, "**Mengaktifkan Perintah Santet Online....**")
    sleep(2)
    await typew.edit("**Mencari Nama Orang Ini...**")
    sleep(1)
    await typew.edit("**Santet Online Segera Dilakukan**")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    sleep(1)
    await typew.edit("**Target Berhasil Tersantet Online**")
