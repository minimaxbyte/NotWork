from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """𝓓𝓸 𝓘 𝓝𝓮𝓮𝓭 𝓣𝓸 𝓢𝓪𝔂 𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰?
<a href="t.me/OngoingAnimess">𝓙𝓸𝓲𝓷 𝓞𝓾𝓻 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓖𝓻𝓸𝓾𝓹</a>
    """
    HELP_TEXT = """𝓓𝓸 𝓘 𝓝𝓮𝓮𝓭 𝓣𝓸 𝓢𝓪𝔂 𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰?
<a href="t.me/OngoingAnimess">𝓙𝓸𝓲𝓷 𝓞𝓾𝓻 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓖𝓻𝓸𝓾𝓹</a>
    """
    ABOUT_TEXT = """𝓓𝓸 𝓘 𝓝𝓮𝓮𝓭 𝓣𝓸 𝓢𝓪𝔂 𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰?
<a href="t.me/OngoingAnimess">𝓙𝓸𝓲𝓷 𝓞𝓾𝓻 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓖𝓻𝓸𝓾𝓹</a>
    """
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ongoing', callback_data='about'),
        InlineKeyboardButton('Animess', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ongoing', callback_data='about'),
        InlineKeyboardButton('Animess', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ongoing', callback_data='help'),
        InlineKeyboardButton('Animess', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "Checking Entered URL"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My Temp Server</code>"    
    UPLOAD_START = "<code>Uploading Into Telegram</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "@𝓞𝓷𝓰𝓸𝓲𝓷𝓰𝓐𝓷𝓲𝓶𝓮𝓼𝓼"
    SLOW_URL_DECED = "Slow URL Detected Press Cancel"
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using Me</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
