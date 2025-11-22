class Script(object):
    # 1. START_TXT: Welcome Message (မြန်မာလို)
    START_TXT = """မင်္ဂလာပါ {} 👋

**Cine Collect Bot** ကနေ ကြိုဆိုပါတယ်။🫶
ကြိုက်နှစ်သက်ရာ **Movie/Series** နာမည်ကို ရိုက်ထည့်ပြီး ရှာဖွေနိုင်ပါတယ်။

**💡 ကူညီမှုလိုပါက အောက်ပါ Help ကို နှိပ်ပါ**"""

    # 2. HELP_TXT: Help Message (မြန်မာလို)
    HELP_TXT = """
    🙋🏻‍♂️ **အကူအညီ လိုအပ်ပါက**

○  **ဆက်သွယ်ရန် :** @williamvan23 / @williamvan1
    
○  **အခြား Commands များ**
    /start - Bot ကို စစ်ဆေးခြင်း
    /status - Bot အခြေအနေ စစ်ဆေးခြင်း
    /info  - User အချက်အလက်
    /id    - ID စစ်ဆေးခြင်း
"""
    
    # 3. ABOUT_TXT: About Message (မြန်မာလို)
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
\n**Cine Collect ၏ ကိုယ်ပိုင် Bot တစ်ခု ဖြစ်ပါသည်။**

✯ Main Channel : <a href='https://t.me/cinecollect'>Cine Collect Channel</a>"""
    
    # 4. LOG_TEXT (Log အတွက် လိုအပ်သည်)
    LOG_TEXT = """#NewUser
Name : {}
ID : {}
"""
    # မလိုအပ်သော SOURCE_TXT, BOT_STATS_TXT, BOT_COMMANDS, MANUELFILTER_TXT, BUTTON_TXT များကို ဖယ်ရှားလိုက်ပါပြီ။
# ... (ခင်ဗျားရဲ့ Script.py ထဲက START_TXT, HELP_TXT, ABOUT_TXT ကုတ်များ) ...

# 4. LOG_TEXT (Log အတွက် လိုအပ်သည်)
LOG_TEXT = """#NewUser
Name : {}
ID : {}
"""

# ----------------------------------------------------
# 📌 ဖြေရှင်းရန် - ဒီစာကြောင်းကို အောက်ဆုံးမှာ ထည့်ပါ။
# ----------------------------------------------------
script = Script() # <<< ဒီစာကြောင်းက မပါလို့ Error တက်နေတာပါ
