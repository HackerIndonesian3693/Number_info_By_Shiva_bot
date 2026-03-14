import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("8780934896:AAHrlDn778kbn5OLSwNMZ2qezf_rFVhPUHI")

async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    api = f"https://all.proportalxc.workers.dev/number?number={number}"

    r = requests.get(api)
    data = r.json()

    if data.get("result", {}).get("success"):
        records = data["result"]["result"]
        output = ""

        for record in records:
            output += (
                f"📱 Mobile : {record.get('mobile', 'N/A')}\n"
                f"👤 Name : {record.get('name', 'N/A')}\n"
                f"👨 Father : {record.get('father name', 'N/A')}\n"
                f"🏠 Address : {record.get('address', 'N/A')}\n"
                f"📡 SIM : {record.get('circle/sim', record.get('circle/im', 'N/A'))}\n"
                f"🆔 ID : {record.get('id number', 'N/A')}\n"
                f"📧 Mail : {record.get('mail', 'N/A')}\n"
                f"━━━━━━━━━━━━━━━━━━\n"
            )

        output += "\n👨‍💻 API Developer : Cybershiva"
    else:
        output = "❌ Invalid Number"

    await update.message.reply_text(output)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, lookup))
app.run_polling()
