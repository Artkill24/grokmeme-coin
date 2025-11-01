# 🚀 GrokMeme - Meme Coin su Supra.com

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Supra](https://img.shields.io/badge/blockchain-Supra-orange.svg)
![Move](https://img.shields.io/badge/language-Move-red.svg)

**$GROKME non è solo un meme. È un esperimento di crescita virale su blockchain, dove i social diventano il motore di adozione.**

## 📖 Descrizione

GrokMeme è una meme coin deployata su **Supra.com** (Layer 1 blockchain ad alte performance) con integrazione automatica sui social media per crescita virale organica.

## ✨ Features

- ✅ Smart contract in Move (standard Fungible Asset)
- ✅ Bot Twitter automatico per promozione 24/7
- ✅ Sistema di airdrop community-driven
- ✅ Completa trasparenza on-chain
- ✅ Open source e forkable

## 🎯 Utilità di $GROKME

| Funzione | Utilità |
|----------|---------|
| **Bot X automatico** | Marketing 24/7 gratuito |
| **Tweet-to-Earn** | Distribuzione virale |
| **Meme Contest** | Engagement community |
| **Trasparenza on-chain** | Fiducia e longevità |

## 🚀 Quick Start
```bash
# Installa dipendenze
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configura Twitter
cp social/config.example.env social/.env
nano social/.env

# Deploy
cd contracts && supra move publish --network testnet

# Mint
python scripts/mint.py --amount 1000000

# Bot
python social/twitter_bot.py --daily
```

## 📚 Documentazione

- [Guida Deployment](docs/deployment.md)
- [Supra Docs](https://docs.supra.com)

## ⚠️ Disclaimer

Progetto sperimentale educativo. Le meme coin sono speculative.

## 📄 Licenza

MIT License

---

**Se ti piace il progetto, lascia una ⭐ su GitHub!**
