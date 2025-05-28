# chatbot.py

# 🤖 Welcome Message
bot_name = "CryptoBuddy"
greeting = f"Hey there! I’m {bot_name} 🤖 — your AI-powered crypto sidekick! Ready to make smart and sustainable investment choices? Let’s go! 🚀"
print(greeting)

# 📊 Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# 🧠 Chatbot Logic
def analyze_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"🚀 Trending cryptos: {', '.join(trending)}"

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"📈 {coin} is trending and highly sustainable — a smart long-term choice!"
        return "🔍 No ideal long-term crypto found right now."

    elif "most sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌿 {recommend} is the most sustainable crypto!"

    else:
        return "🤔 I didn’t catch that. Try asking about 'sustainability', 'trending', or 'long-term growth'."

# 💬 Chat Loop
print("💬 Ask me about crypto trends, sustainability, or growth. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print(f"{bot_name}: 👋 Stay savvy! Crypto is risky—always do your own research!")
        break
    response = analyze_query(user_input)
    print(f"{bot_name}: {response}")
