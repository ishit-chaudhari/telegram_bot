from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7268648289:AAHCKTuu0BFPeb6QWMPauSZmz50LjTactOA'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! I am your FAQ Bot. Ask me anything.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'price' in text:
        await update.message.reply_text('Our services start at ₹1,000 per bot.')
    elif 'contact' in text:
        await update.message.reply_text('You can reach us at example@email.com.')
    elif 'ishit' in text:
        await update.message.reply_text("Mr.Ishit chaudhari is the owner of this bot.")
    else:
        await update.message.reply_text('Sorry, I do not understand. Please ask something else!')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
