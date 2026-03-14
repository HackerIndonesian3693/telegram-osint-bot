import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8517903145:AAEvnyh95sAqPkjYUMtLSupD8t-R8e4ny6Y"

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text

    api = f"https://all.proportalxc.workers.dev/number?number={number}"

    try:
        r = requests.get(api)
        data = r.json()
    except:
        await update.message.reply_text("⚠️ API Error")
        return

    records = data.get("result", [])

    if not records:
        await update.message.reply_text("❌ Number Details Not Found")
        return

    output = ""

    for r in records[:5]:   # limit 5 results
        output += (
            f"📱 Mobile : {r.get('mobile','N/A')}\n"
            f"👤 Name : {r.get('name','N/A')}\n"
            f"👨 Father : {r.get('father name','N/A')}\n"
            f"🏠 Address : {r.get('address','N/A')}\n"
            f"📡 SIM : {r.get('circles/sim','N/A')}\n"
            f"📧 Mail : {r.get('mail','N/A')}\n"
            f"━━━━━━━━━━━━━━━━━━\n"
        )

    output += "\n👨‍💻 API Developer : Cybershiva"

    await update.message.reply_text(output)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup))

print("Bot Started...")

app.run_polling()
