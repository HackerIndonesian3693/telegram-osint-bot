import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📱 Enter Mobile Number Without +91")

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    if not number.isdigit():
        await update.message.reply_text("❌ Send valid number")
        return

    await update.message.reply_text("🔎 Searching...")

    try:
        api = f"https://all.proportalxc.workers.dev/number?number=9876543210"
        r = requests.get(api, timeout=10)
        data = r.json()
    except Exception as e:
        await update.message.reply_text("⚠️ API Error")
        print(e)
        return

    records = data.get("result", [])

    if not records:
        await update.message.reply_text("❌ No Data Found")
        return

    r = records[0]

    msg = f"""
📱 Mobile : {r.get('mobile','N/A')}
👤 Name : {r.get('name','N/A')}
👨 Father : {r.get('father name','N/A')}
🏠 Address : {r.get('address','N/A')}
📡 SIM : {r.get('circles/sim','N/A')}
📧 Mail : {r.get('mail','N/A')}
"""

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup))

print("🤖 Bot Started")

app.run_polling(drop_pending_updates=True)
