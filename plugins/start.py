from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support", url="https://telegram.me/share/url?url=**Syn%20-%20YouTube%20Uploader%20**%20%0A%0AA%20Bot%20Which%20Can%20Download%20Videos%20from%20YouTube%20-%20@SynYoutubebot")],
        [InlineKeyboardButton(
            "Report Bugs", url="https://t.me/synuser")]
    ])
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>YouTube Uploader Bot.</b>\n\nfor more details /help\nDeveloper: @Synuser"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
