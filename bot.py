import os
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📱 Send Mobile Number Without +91")

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    await update.message.reply_text("🔎 Searching...")

    api = f"https://all.proportalxc.workers.dev/number?number={number}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api, timeout=8) as resp:
                text = await resp.text()

        await update.message.reply_text("✅ API Response Received")
        await update.message.reply_text(text[:1000])

    except Exception as e:
        await update.message.reply_text("❌ API Not Working")
        print(e)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup))

print("🤖 Bot Started")

app.run_polling()
