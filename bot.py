import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8517903145:AAEvnyh95sAqPkjYUMtLSupD8t-R8e4ny6Y"

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    number = update.message.text

    api = f"https://all.proportalxc.workers.dev/number?number={number}"

    r = requests.get(api)
    data = r.json()

    await update.message.reply_text(str(data))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, lookup))

app.run_polling()
