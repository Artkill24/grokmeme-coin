#!/usr/bin/env python3
"""Script per deployare GrokMeme su Supra"""

import os
import subprocess
from pathlib import Path

def deploy_contract():
    print("🚀 Deploy GrokMeme...")
    
    contracts_dir = Path(__file__).parent.parent / "contracts"
    if not contracts_dir.exists():
        print("❌ contracts/ non trovata!")
        return False
    
    os.chdir(contracts_dir)
    
    try:
        print("\n📦 Compilazione...")
        result = subprocess.run(
            ["supra", "move", "compile"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Errore: {result.stderr}")
            return False
        
        print("✅ Compilato!")
        
        print("\n🌐 Deploy testnet...")
        result = subprocess.run(
            ["supra", "move", "publish", "--network", "testnet"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Errore: {result.stderr}")
            return False
        
        print("✅ Deployato!")
        print(result.stdout)
        return True
        
    except FileNotFoundError:
        print("❌ Supra CLI non trovato! Installa da docs.supra.com")
        return False

if __name__ == "__main__":
    print("╔═══════════════════════════╗")
    print("║  GrokMeme Deploy Script  ║")
    print("╚═══════════════════════════╝\n")
    
    if deploy_contract():
        print("\n🎉 Deploy completato!")
        print("\n📋 Prossimi passi:")
        print("1. python scripts/mint.py --amount 1000000")
        print("2. python social/twitter_bot.py --daily")
