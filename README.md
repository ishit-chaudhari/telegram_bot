# telegram_bot
This project is a simple yet functional Telegram FAQ Bot designed to provide quick, automated responses to common queries. Built using the Python Telegram Bot API (python-telegram-bot library), it acts as a direct assistant for users, eliminating the need for manual reply handling.
When a user starts a conversation with the bot by sending the /start command, it greets them with a friendly message:

"Hi! I am your FAQ Bot. Ask me anything."

The bot then listens for incoming messages and processes them in real time. It uses basic keyword detection to identify the nature of a user’s question:

If the message contains the word "price", the bot responds with:
"Our services start at ₹1,000 per bot."
If the message contains "contact", it replies with the official contact email:
"You can reach us at example@email.com."
If the word "ishit" is mentioned, it responds with:
"Mr. Ishit Chaudhari is the owner of this bot."
If the bot cannot recognize the query, it politely informs the user:
"Sorry, I do not understand. Please ask something else!"
The architecture of this bot is simple and efficient. It uses CommandHandler to manage commands like /start and MessageHandler with filters to process general text messages. By using asynchronous functions (async def), the bot can handle multiple user requests smoothly without delays.
This bot operates using the polling method (app.run_polling()), which continuously checks for updates from Telegram servers and processes them instantly. The token authentication system ensures that only authorized access is possible.

Overall, this project demonstrates how a minimal codebase can still create a practical, user-friendly Telegram bot capable of interacting with users, providing instant information, and serving as the foundation for more advanced automation features in the future.
