import json
from calendar import month_name

import aiohttp
from Abg.helpers.human_read import get_readable_time
from Abg.helpers.ratelimit import ratelimiter
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AsuX import Abishnoi

anime_query = """
query ($id: Int, $idMal: Int, $search: String) {
  Media(id: $id, idMal: $idMal, type: ANIME, search: $search) {
    id
    idMal
    title {
      romaji
      english
      native
    }
    type
    format
    status(version: 2)
    description(asHtml: true)
    startDate {
      year
      month
      day
    }
    endDate {
      year
      month
      day
    }
    season
    seasonYear
    episodes
    duration
    chapters
    volumes
    countryOfOrigin
    source
    hashtag
    trailer {
      id
      site
      thumbnail
    }
    updatedAt
    coverImage {
      large
    }
    bannerImage
    genres
    synonyms
    averageScore
    meanScore
    popularity
    trending
    favourites
    tags {
      name
      description
      rank
    }
    relations {
      edges {
        node {
          id
          title {
            romaji
            english
            native
          }
          format
          status
          source
          averageScore
          siteUrl
        }
        relationType
      }
    }
    characters {
      edges {
        role
        node {
          name {
            full
            native
          }
          siteUrl
        }
      }
    }
    studios {
      nodes {
         name
         siteUrl
      }
    }
    isAdult
    nextAiringEpisode {
      airingAt
      timeUntilAiring
      episode
    }
    airingSchedule {
      edges {
        node {
          airingAt
          timeUntilAiring
          episode
        }
      }
    }
    externalLinks {
      url
      site
    }
    rankings {
      rank
      year
      context
    }
    reviews {
      nodes {
        summary
        rating
        score
        siteUrl
        user {
          name
        }
      }
    }
    siteUrl
  }
}
"""


async def get_anime(title):
    async with aiohttp.ClientSession() as sesi:
        r = await sesi.post(
            "https://graphql.anilist.co",
            json={"query": anime_query, "variables": title},
        )
        return await r.read()


def shorten(description, info="anilist.co"):
    ms_g = ""
    if len(description) > 700:
        description = f"{description[:500]}...."
        ms_g += f'\n<strong>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:</strong> <em>{description}</em><a href="{info}">More info</a>'
    else:
        ms_g += f"\n<strong>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:</strong> <em>{description}</em>"
    return (
        ms_g.replace("<br>", "")
        .replace("</br>", "")
        .replace("<i>", "")
        .replace("</i>", "")
    )


@Abishnoi.on_cmd("anime")
@ratelimiter
async def anime_search(_, mesg):
    search = mesg.text.split(" ", 1)
    reply = await mesg.reply("⏳ <i>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ...</i>", quote=True)
    if len(search) == 1:
        return await reply.edit("⚠️ <b>ɢɪᴠᴇ ᴀɴɪᴍᴇ ɴᴀᴍᴇ ᴘʟᴇᴀsᴇ.</b>")
    else:
        search = search[1]
    variables = {"search": search}
    if not (res := json.loads(await get_anime(variables))["data"].get("Media", None)):
        return await reply.edit("💢 ɴᴏ ʀᴇsᴏᴜʀᴄᴇ ᴀɴɪᴍᴇ ғᴏᴜɴᴅ! [404]")
    # LOGGER.info(json.dumps(res, indent=3)) # For Debug JSON
    durasi = (
        get_readable_time(int(res.get("duration") * 60))
        if res.get("duration") is not None
        else "0"
    )
    msg = f"<b>{res['title']['romaji']}</b> (<code>{res['title']['native']}</code>)\n<b>Type</b>: {res['format']}\n<b>Status</b>: {res['status']}\n<b>Episodes</b>: {res.get('episodes', 'N/A')}\n<b>Duration </b>: {durasi} Per Eps.\n<b>Score</b>: {res['averageScore']}%\n<b>Category</b>: <code>"
    for x in res["genres"]:
        msg += f"{x}, "
    msg = msg[:-2] + "</code>\n"
    try:
        sd = res["startDate"]
        startdate = str(f"{month_name[sd['month']]} {sd['day']}, {sd['year']}")
    except:
        startdate = "-"
    msg += f"<b>sᴛᴀʀᴛ ᴅᴀᴛᴇ</b>: <code>{startdate}</code>\n"
    try:
        ed = res["endDate"]
        enddate = str(f"{month_name[ed['month']]} {ed['day']}, {ed['year']}")
    except:
        enddate = "-"
    msg += f"<b>ᴇɴᴅ ᴅᴀᴛᴇ</b>: <code>{enddate}</code>\n"
    msg += "<b>sᴛᴜᴅɪᴏs</b>: <code>"
    for x in res["studios"]["nodes"]:
        msg += f"{x['name']}, "
    msg = msg[:-2] + "</code>\n"
    info = res.get("siteUrl")
    trailer = res.get("trailer", None)
    if trailer:
        trailer_id = trailer.get("id", None)
        site = trailer.get("site", None)
        if site == "youtube":
            trailer = f"https://youtu.be/{trailer_id}"
    description = (
        res.get("description")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("<br>", "")
        if res.get("description") is not None
        else "N/A"
    )
    msg += shorten(description, info)
    image = info.replace("anilist.co/anime/", "img.anili.st/media/")
    btn = (
        [
            [
                InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏ", url=info),
                InlineKeyboardButton("ᴛʀᴀɪʟᴇʀ 🎬", url=trailer),
            ]
        ]
        if trailer
        else [[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏ", url=info)]]
    )

    if image:
        try:
            await mesg.reply_photo(
                image, caption=msg, reply_markup=InlineKeyboardMarkup(btn)
            )
        except:
            msg += f" [〽️]({image})"
            await reply.edit(msg)
    else:
        await reply.edit(msg)
    await reply.delete()
