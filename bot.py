import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.getenv("7684622074:AAEn2D3e9y7nSr47srQN80aGtVS1aE-pj7A")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Send Mobile Number\n\nExample:\n9876543210"
    )

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    api = f"https://all.proportalxc.workers.dev/number?number={number}"

    try:
        r = requests.get(api, timeout=10)
        data = r.json()
    except:
        await update.message.reply_text("⚠️ API Error")
        return

    records = data.get("result", [])

    if not records:
        await update.message.reply_text("❌ Number Details Not Found")
        return

    output = ""

    for r in records[:3]:
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

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup))

print("🤖 Bot Started")

app.run_polling()
