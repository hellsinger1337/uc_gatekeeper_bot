from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ParseMode

TOKEN = '6814634093:AAFMzTByz-Cjr12kRyAWMiJzcvp_L9sMt-0'

def welcome_new_member(update, context):
    for new_member in update.message.new_chat_members:
        # Constructing a clickable username link
        username_link = f"[{new_member.first_name}](tg://user?id={new_member.id})"
        message = (
            f"{username_link}, приветствуем тебя в профсоюзе 'Унесённых чаем'! "
            "Мы рады, что ты присоединился к нашему сообществу. Пожалуйста, расскажи немного о себе:\n\n"
            "🔹 Какой чай ты предпочитаешь?\n"
            "🔹 Как давно увлекаешься чаем и с чего все началось?\n"
            "🔹 Как ты нас нашёл?\n\n"
            "Пожалуйста, ознакомься с правилами и традициями нашего чата:\n"
            "📜 [ЛОР УЧ](https://telegra.ph/LOR-Unesennye-CHaem-05-17-2)\n\n"
            "Мы уверены, что со временем ты освоишься и постигнешь все премудрости нашего чая. "
            "Не стесняйся задавать любые вопросы и делиться своим опытом. Пей хороший чай вместе с нами!\n\n"
            "⚠️ Важно: Если в течение 3 дней ты не проявишь активность и не расскажешь о себе, "
            "мы, возможно, подумаем, что ты бот, и исключим тебя из чата."
        )
        context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

def send_lore_link(update, context):
    lore_link = "https://telegra.ph/LOR-Unesennye-CHaem-05-17-2"
    update.message.reply_text(lore_link)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handle new chat members
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_new_member))

    # Handle /lore and /лор commands with any case
    lore_handler_eng = CommandHandler('lore', send_lore_link)
    dispatcher.add_handler(lore_handler_eng)


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()