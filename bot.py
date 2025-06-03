from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Приветствие при /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = (
        "👋 Привет! Тебя приветствует команда *Keleshek.kz*! Мы рады видеть тебя здесь 🙌\n\n"
        "Мы создали этого бота, чтобы быть с тобой на одной волне — говорить просто, по делу и помогать тебе сделать важный шаг в будущее.\n\n"
        "🎓 Впереди — выбор профессии, вуза, направления. Это может быть волнительно, и мы здесь, чтобы сопровождать тебя на этом пути.\n\n"
        "Задавай вопросы, проходи тест, читай советы, а главное — не бойся мечтать и выбирать себя 💡\n\n"
        "👇 Выбери, что тебя интересует:"
    )
    await update.message.reply_text(welcome, reply_markup=main_menu(), parse_mode="Markdown")

# Главное меню — для /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Главное меню — выбери интересующий раздел:", reply_markup=main_menu())

# Инструкция /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🛠 *Как пользоваться ботом Keleshek.kz*\n\n"
        "Этот бот создан, чтобы помочь тебе выбрать профессию и спланировать своё будущее.\n\n"
        "Ты можешь:\n"
        "✅ Пройти профориентационный тест\n"
        "✅ Найти подходящий вуз / колледж\n"
        "✅ Изучить востребованные профессии\n"
        "✅ Получить советы и поддержку\n\n"
        "💬 Используй команды:\n"
        "/start — запустить бота\n"
        "/menu — открыть главное меню\n"
        "/help — показать эту инструкцию\n\n"
        "🌐 Перейди на сайт для полного функционала:\n"
        "https://keleshek.site.kz"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# Ответ на кнопку "💡 Как пользоваться сайтом"
async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📘 *Как пользоваться платформой Keleshek.kz*\n\n"
        "🙋‍♀️ _Какие профессии мне подойдут?_\n"
        "На нашем сайте ты можешь пройти полноценный профориентационный тест, основанный на международной методике.\n"
        "Результаты покажут твои сильные стороны и подскажут, в каких сферах ты сможешь реализовать себя наилучшим образом.\n\n"
        "🎯 _В чём уникальность вашей платформы?_\n"
        "Мы объединили аналитику рынка труда, образовательные возможности и рекомендации ИИ в одном месте.\n"
        "Ты не просто получаешь тест — ты получаешь **осмысленный путь к профессии, вузу и навыкам будущего.**\n\n"
        "🏛 _Как понять, в какой университет или колледж мне поступать?_\n"
        "После выбора профессии ты увидишь, какие вузы и колледжи готовят по нужному направлению.\n"
        "Фильтруй по городу, минимальным баллам, наличию грантов и даже по востребованности на рынке.\n\n"
        "📊 _Какие профессии актуальны в Казахстане?_\n"
        "Мы собираем данные о вакансиях и зарплатах, чтобы показать, какие направления востребованы именно сейчас и в будущем.\n\n"
        "🌐 Всё это доступно на [Keleshek.kz](https://keleshek.site.kz)"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


# Главное меню в виде клавиатуры
def main_menu():
    keyboard = [
        ["💡 Как пользоваться сайтом", "ℹ️ Советы"],
        ["📬 Обратная связь", "🆘Поддержка"],
        ["🤝 Истории успеха", "📅 Календарь событий"],
        ["🛠 Навыки будущего", "👩‍💻 Стажировки"],
        ["👨‍🏫 Консультант"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Ответ на кнопку "Советы"

async def tip_profession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 *Как выбрать профессию:*\n\n"
        "✅ Не думай сразу про «кем работать», начни с вопроса: *что я люблю делать?*\n"
        "— Любишь анализировать? → Инженер, аналитик, программист\n"
        "— Нравится помогать другим? → Психолог, врач, учитель\n"
        "— Обожаешь креатив? → Дизайнер, маркетолог, копирайтер\n\n"
        "✅ Пройди наш профориентационный тест — он покажет твои сильные стороны\n"
        "✅ Ознакомься с реальными историями выпускников на сайте\n"
        "✅ Сравни профессии по востребованности и зарплате\n\n"
        "👉 Всё это есть на сайте: [keleshek.site.kz](https://keleshek.site.kz)",
        parse_mode="Markdown"
    )

async def tip_learning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎧 *Как эффективно учиться: выбери подход под свой стиль мышления*\n\n"
        "🔹 _Если ты визуал:_\n"
        "📊 Используй интеллект-карты, схемы, цветные заметки\n"
        "🧠 Метод: \"Mind Mapping\" — структурируй материал визуально\n"
        "📘 Веди понятный конспект с рамками, выделениями и блоками\n\n"
        "🔹 _Если ты аудиал:_\n"
        "🎧 Слушай объяснения, читай вслух, пересказывай другу\n"
        "🧠 Метод: \"Self-Explanation\" — пересказывай своими словами\n"
        "📢 Повторяй ключевые определения голосом — это усиливает запоминание\n\n"
        "🔹 _Если ты кинестетик:_\n"
        "✍️ Пиши от руки, решай задачи, делай карточки\n"
        "🧠 Метод: \"Active Recall\" — закрываешь материал и вспоминаешь с нуля\n"
        "📝 Делай реальные упражнения, а не просто читай теорию\n\n"
        "⏱ И универсальный метод:\n"
        "🕒 *Pomodoro* — 25 минут учёбы + 5 минут перерыв. После 4 циклов — длинный отдых.\n\n"
        "💡 Совет: совмещай методы, пробуй новое и отслеживай, что сработало лично для тебя!"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def tip_university(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 *Как выбрать подходящий вуз или колледж:*\n\n"
        "🎯 Определи, какая профессия тебе интересна (поможет тест на сайте)\n"
        "📍 Зайди в раздел вузов и используй фильтры:\n"
        "• Город\n"
        "• Проходной балл\n"
        "• Наличие грантов\n"
        "• Уровень востребованности профессии\n\n"
        "🎓 После фильтрации ты увидишь список вузов, которые подходят именно тебе!\n"
        "👉 Перейди к разделу: [keleshek.site.kz/universities](https://keleshek.site.kz/universities)",
        parse_mode="Markdown"
    )

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔙 Возвращаюсь в главное меню", reply_markup=main_menu())

async def tips_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📌 Как выбрать профессию"],
        ["🎧 Как эффективно учиться"],
        ["💼 Как выбрать вуз"],
        ["🔙 Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🧠 Выбери, что тебя интересует:", reply_markup=reply_markup)


# Ответ на кнопку "Обратная связь"
async def feedback_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✍️ Оставить отзыв"],
        ["🐞 Сообщить об ошибке"],
        ["📩 Связаться с поддержкой"],
        ["🔙 Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("📬 Выберите тип обратной связи:", reply_markup=reply_markup)

# Задаём ID куда слать сообщения
MY_TELEGRAM_ID = 123456789  # <-- замени на свой

async def leave_review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["feedback_type"] = "[ОТЗЫВ]"
    await update.message.reply_text("✍️ Напиши свой отзыв — мы передадим его команде!")

async def report_bug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["feedback_type"] = "[ОШИБКА]"
    await update.message.reply_text("🐞 Опиши, что именно не работает или вызывает проблему")

async def support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["feedback_type"] = "[ПОДДЕРЖКА]"
    await update.message.reply_text("📩 Напиши, в чём нужна помощь — мы ответим как можно скорее!")

# Вставь сюда свой ID — получи его у @userinfobot
MY_TELEGRAM_ID = 470468713  # ← замени на свой!

async def collect_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "feedback_type" in context.user_data:
        feedback_type = context.user_data["feedback_type"]
        user_text = update.message.text
        user_name = update.effective_user.full_name

        message = f"{feedback_type} от {user_name}:\n\n{user_text}"

        # 👇 ЭТО отправляет тебе (автору бота), не пользователю
        await context.bot.send_message(chat_id=470468713, text=message)

        # 👇 А это благодарность пользователю
        await update.message.reply_text("✅ Спасибо! Ваше сообщение отправлено.")

        context.user_data.clear()


# Ответ на кнопку "помощь"
async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["😟 Я тревожусь о будущем", "🤯 Я не справляюсь / перегруз"],
        ["🙍‍♂️ У меня не получается", "🤔 Я не уверен(а) в себе"],
        ["🔙 Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🧠 С чем ты сейчас сталкиваешься?", reply_markup=reply_markup)



async def support_future(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "😟 *Ты тревожишься о будущем?* Это нормально.\n\n"
        "🔹 У всех бывают моменты, когда кажется, что ты не знаешь, куда идти.\n"
        "🔹 Но тревога не означает, что ты не справишься — наоборот, она показывает, что тебе важно.\n\n"
        "💡 Раздели путь на маленькие шаги:\n"
        "1. Попробуй наш тест — он сузит круг профессий\n"
        "2. Изучи вузы, не выбирая сразу один\n"
        "3. Позволь себе быть в процессе, а не сразу знать ответ\n\n"
        "🫂 Ты не один. И всё, что ты чувствуешь — окей."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def support_overload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤯 *Перегруз и ощущение «я не справляюсь»* — сигнал, что пора передохнуть.\n\n"
        "🛑 Остановись на пару минут. Сделай дыхание: вдох — 4 сек, выдох — 6 сек.\n"
        "📌 Составь план на завтра. Не на 10 дел. На 2–3 главных.\n"
        "📅 Расставь приоритеты: не всё срочно и не всё важно.\n\n"
        "🍵 Пауза = не слабость, а стратегия. Ты восстановишь силы быстрее, чем кажется."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def support_failure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🙍‍♂️ *У тебя не получается? Это не конец пути.*\n\n"
        "🧠 Ошибки = часть обучения. У каждого, кто добился чего-то, были срывы и провалы.\n"
        "💬 Задай себе вопрос: _что именно не получается?_ — и разложи это на мелкие части.\n"
        "🛠 Иногда достаточно просто уточнить, где именно затык — и ты найдёшь выход.\n\n"
        "📈 Не прогресс каждый день, а устойчивость важна. И ты с ней справишься."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def support_confidence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤔 *Ты не уверен(а) в себе?*\n\n"
        "Это чувство знакомо многим — особенно перед экзаменами, выбором вуза или профессии.\n"
        "💡 Помни: неуверенность = не отсутствие способностей. Это отсутствие ясности и опыта.\n"
        "📍 Действуй маленькими шагами. Ты будешь чувствовать уверенность ПОСЛЕ действия, а не до него.\n\n"
        "💬 Хочешь — напиши нашему консультанту. Ты не обязан(а) делать это в одиночку."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


# Инициализация
app = ApplicationBuilder().token("7962303221:AAGp35Hvg3tgB0yU0IyJhkCnEKfbndraIJA").build()

# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("help", help_command))

# Обработчики сообщений
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("💡 Как пользоваться сайтом"), guide))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("ℹ️ Советы"), tips_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("📌 Как выбрать профессию"), tip_profession))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🎧 Как эффективно учиться"), tip_learning))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("💼 Как выбрать вуз"), tip_university))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🔙 Назад"), back_to_main))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("📬 Обратная связь"), feedback_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("✍️ Оставить отзыв"), leave_review))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🐞 Сообщить об ошибке"), report_bug))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("📩 Связаться с поддержкой"), support_message))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, collect_feedback))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🆘Поддержка"), support_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("😟 Я тревожусь о будущем"), support_future))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🤯 Я не справляюсь / перегруз"), support_overload))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🙍‍♂️ У меня не получается"), support_failure))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🤔 Я не уверен(а) в себе"), support_confidence))


# Запуск
app.run_polling()
