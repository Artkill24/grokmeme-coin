# 📘 Guida Deployment GrokMeme

## 🎯 Prerequisiti

1. **Supra Wallet (StarKey)** - Scarica da supra.com
2. **Python 3.8+** - python3 --version
3. **Supra CLI** - Installa da docs.supra.com
4. **Twitter Developer Account** - developer.twitter.com

## 🚀 Step 1: Installa Dipendenze
```bash
# Crea ambiente virtuale
python3 -m venv venv
source venv/bin/activate

# Installa requirements
pip install -r requirements.txt
```

## 🔑 Step 2: Configura Twitter
```bash
# Copia template
cp social/config.example.env social/.env

# Modifica con le tue keys
nano social/.env
```

Inserisci:
- TWITTER_API_KEY
- TWITTER_API_SECRET
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_SECRET

## 🌐 Step 3: Setup Supra
```bash
# Inizializza wallet
supra init

# Connetti al testnet
supra config set-network testnet

# Verifica indirizzo
supra account list

# Richiedi testnet tokens
# Vai su faucet.supra.com
```

## 📝 Step 4: Personalizza Coin

Modifica `contracts/sources/GrokMeme.move`:
```move
string::utf8(b"TuoNome")     // Cambia il nome
string::utf8(b"SIMBOLO")     // Cambia il simbolo
```

Modifica `contracts/Move.toml`:
```toml
grokmeme = "0xTUO_INDIRIZZO"
```

## 🚢 Step 5: Deploy Contratto
```bash
cd contracts

# Compila
supra move compile

# Deploy
supra move publish --network testnet

# Salva il contract address!
```

## 🪙 Step 6: Mint Token
```bash
cd ..

# Minta 1 milione
python scripts/mint.py --amount 1000000
```

## 🐦 Step 7: Avvia Bot
```bash
# Tweet personalizzato
python social/twitter_bot.py --custom "🚀 Launched!"

# Annuncio mint
python social/twitter_bot.py --event mint --amount 1000000

# Stats giornaliere
python social/twitter_bot.py --daily
```

## ✅ Verifica

- SupraScan: testnet.suprascan.io
- Wallet: Controlla balance
- Twitter: Verifica tweet postati

## 🆘 Troubleshooting

**Errore compilazione?**
- Controlla sintassi Move
- Verifica dipendenze in Move.toml

**Bot non funziona?**
- Verifica credenziali in .env
- Controlla permessi API Twitter

**Gas insufficiente?**
- Richiedi più token dal faucet

---

**Per supporto: Apri issue su GitHub**
