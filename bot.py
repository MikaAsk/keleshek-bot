from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram.ext import filters

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
        ["📬 Обратная связь", "🆘 Поддержка"],
        ["🤝 Истории успеха", "📅 Календарь событий"],
        ["🛠 Навыки будущего"]
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
app = ApplicationBuilder().token("7601831924:AAHscYHSLwsPcgVDfneW7E0picV0IuuJQkc").build()

# Обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("help", help_command))

# Ответ на кнопку "успех"
async def success_stories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "\U0001F4DA *Истории успеха выпускников из Казахстана*\n\n"
        "\U0001F393 *Айсултан Алтынбек*\n"
        "Выпускник лицея \"Бiлiм-Инновация\". Получил приглашения от 86 университетов мира с грантами на сумму $4.6 млн.\n"
        "[Читать статью](https://tengrinews.kz/curious/otkazalsya-ent-top-vuzyi-mira-predlojili-millionyi-istoriya-570257/)\n\n"

        "\U0001F393 *Алибек Достияров и Ерсултан Сапар*\n"
        "Выпускники РФМШ. Работали в Apple и McKinsey, основали стартап Perceptis, привлекший $3.6 млн инвестиций.\n"
        "[Читать статью](https://digitalbusiness.kz/2025-04-18/kazahstantsi-ushli-iz-bolshih-korporatsiy-radi-startapa-i-privlekli-3-6-mln-investitsiy-v-ssha-istoriya-perceptis/)\n\n"

        "\U0001F393 *Мурат Бактыбаев*\n"
        "Выпускник НИШ Алматы. Поступил в Стэнфорд, стажировался в топ-компаниях в Кремниевой долине.\n"
        "[Читать статью](https://vidal.kz/novosti/ot-mechty-k-realnosti-istorii-uspekha-kazakhstancev-s-mezhdunarodnym-obrazovaniem.html)\n\n"

        "\U0001F393 *Азат Серикулы*\n"
        "Выпускник НИШ Тараз. Прошел стажировку в Caltech, участвовал в инженерных олимпиадах.\n"
        "[Читать статью](https://vidal.kz/novosti/ot-mechty-k-realnosti-istorii-uspekha-kazakhstancev-s-mezhdunarodnym-obrazovaniem.html)\n\n"

        "\U0001F3A7 *Подкасты:*\n"
        "• [nFactorial Podcast](https://nfactorialpodcast.podbean.com/) — выпускники в Google, Meta и др.\n"
        "• [MOST подкаст #23](https://www.youtube.com/watch?v=lfod9Ud0v9c)\n"
        "• [Замандас](https://creators.spotify.com/pod/profile/zamandas-podcast/episodes/3amandas-e1lavn8) — разговоры с молодыми специалистами\n"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# Ответ на кнопку "даты"
async def events_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📅 *Календарь событий – не пропусти важное!*\n\n"
        "🎓 *Ярмарки вузов и колледжей*\n"
        "Познакомься с университетами Казахстана, узнай об условиях поступления, грантах и специальностях.\n"
        "👉 [EDLIGHT Education Fair](https://edlight.kz/)\n"
        "👉 [Ярмарка в Nazarbayev University](https://nu.edu.kz/admissions/open-house-day)\n\n"
        "💼 *Карьерные мероприятия и стажировки*\n"
        "Участвуй в карьерных фестивалях и найди стажировку мечты!\n"
        "👉 [Zhas Camp от Enactus](https://enactus.kz/news/zhas-camp)\n"
        "👉 [Job Fair от Astana Hub](https://astanahub.com/job)\n\n"
        "🌐 *Образовательные и ИТ-конференции*\n"
        "Следи за технологиями и трендами будущего!\n"
        "👉 [Digital Bridge](https://digitalbridge.kz/)\n"
        "👉 [Education Transformation Forum](https://kazakhstaneducationforum.com/)\n\n"
        "📌 Мы обновляем список событий регулярно. Следи за новостями на [keleshek.site.kz](https://keleshek.site.kz)"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# Навыки будущего
async def future_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🛠 *Навыки будущего: чему стоит учиться уже сейчас*\n\n"
        "🌍 Мир быстро меняется, и чтобы быть востребованным специалистом, важно развивать навыки, которые будут актуальны через 3–5–10 лет.\n\n"
        "📌 Вот ключевые направления и ресурсы:\n\n"
        "🔹 *Аналитика данных и Python*\n"
        "— Курс: [Stepik — Основы Python](https://stepik.org/course/67)\n"
        "— Курс: [Coursera — Data Science от МФТИ](https://www.coursera.org/specializations/data-science)\n\n"
        "🔹 *Искусственный интеллект и машинное обучение*\n"
        "— Курс: [Google — Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)\n"
        "— Курс: [Coursera — AI For Everyone](https://www.coursera.org/learn/ai-for-everyone)\n\n"
        "🔹 *Креативное мышление и дизайн*\n"
        "— Курс: [Coursera — Creative Problem Solving](https://www.coursera.org/learn/creative-problem-solving)\n\n"
        "🔹 *Цифровой маркетинг*\n"
        "— Курс: [Google Digital Workshop](https://learndigital.withgoogle.com/digitalgarage/course/digital-marketing)\n\n"
        "🔹 *Гибкие навыки (soft skills)*\n"
        "— Курс: [Edx — Soft Skills Professional Certificate](https://www.edx.org/professional-certificate/ritx-soft-skills)\n\n"
        "💡 Не обязательно изучать всё сразу. Начни с того, что тебе интересно, и развивайся в своём темпе!"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# Команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("help", help_command))

# Главное меню
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("💡 Как пользоваться сайтом"), guide))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("📅 Календарь событий"), events_calendar))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🔙 Назад"), back_to_main))

# Советы
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("ℹ️ Советы"), tips_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("📌 Как выбрать профессию"), tip_profession))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("🎧 Как эффективно учиться"), tip_learning))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("💼 Как выбрать вуз"), tip_university))

# Поддержка
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*Поддержка.*"), support_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*тревожусь.*"), support_future))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*перегруз.*"), support_overload))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*не получается.*"), support_failure))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*не уверен.*"), support_confidence))

# Обратная связь
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*Обратная связь.*"), feedback_menu))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*Оставить отзыв.*"), leave_review))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*ошибк.*"), report_bug))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*поддержк.*"), support_message))

# Основные разделы
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*Истории успеха.*"), success_stories))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(".*Навыки будущего.*"), future_skills))


# Всё остальное (например, отзыв)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, collect_feedback))



# Запуск
app.run_polling()
