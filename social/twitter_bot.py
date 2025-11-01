#!/usr/bin/env python3
"""Bot Twitter per GrokMeme"""

import tweepy
import os
import random
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')

class GrokMemeBot:
    def __init__(self):
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_secret = os.getenv('TWITTER_ACCESS_SECRET')
        
        if not all([self.api_key, self.api_secret, self.access_token, self.access_secret]):
            raise ValueError("❌ Credenziali Twitter mancanti in .env")
        
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_secret
        )
        print("✅ Bot inizializzato!")
    
    def post_tweet(self, text):
        try:
            if len(text) > 280:
                text = text[:277] + "..."
            response = self.client.create_tweet(text=text)
            print(f"✅ Tweet postato! ID: {response.data['id']}")
            return response.data['id']
        except Exception as e:
            print(f"❌ Errore: {e}")
            return None
    
    def post_mint(self, amount):
        emoji = random.choice(["🚀", "🔥", "💎", "🌙"])
        text = f"""{emoji} MINT ALERT {emoji}

{amount:,} $GROKME mintati!

📊 Supply: Growing
👥 Holders: Increasing
📈 To the moon!

#GrokMeme #SupraChain #MemeCoins 🐶"""
        return self.post_tweet(text)
    
    def post_daily(self):
        text = """📊 DAILY STATS 📊

$GROKME on Supra Blockchain

💰 Supply: Growing
👥 Holders: Increasing
🔥 Vibes: Immaculate
📈 Direction: Up Only

#GrokMeme #DeFi #Web3 🚀"""
        return self.post_tweet(text)
    
    def post_custom(self, msg):
        tags = "\n\n#GrokMeme #SupraChain"
        text = msg + tags if len(msg + tags) <= 280 else msg
        return self.post_tweet(text)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", choices=["mint"])
    parser.add_argument("--amount", type=int)
    parser.add_argument("--daily", action="store_true")
    parser.add_argument("--custom", type=str)
    args = parser.parse_args()
    
    print("╔═══════════════════════════╗")
    print("║  GrokMeme Twitter Bot    ║")
    print("╚═══════════════════════════╝\n")
    
    try:
        bot = GrokMemeBot()
        
        if args.event == "mint" and args.amount:
            bot.post_mint(args.amount)
        elif args.daily:
            bot.post_daily()
        elif args.custom:
            bot.post_custom(args.custom)
        else:
            print("Usa: --event mint --amount 1000000")
            print("     --daily")
            print("     --custom 'Tuo messaggio'")
    except ValueError as e:
        print(f"\n{e}")
        print("Configura social/.env con le tue API keys!")
