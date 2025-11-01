#!/usr/bin/env python3
"""Script per mintare GrokMeme"""

import argparse
import subprocess

def mint_tokens(amount):
    print(f"🪙 Mintando {amount:,} $GROKME...")
    
    try:
        cmd = [
            "supra", "move", "run",
            "--function-id", "YOUR_ADDRESS::grok_meme::mint",
            "--args", f"u64:{amount * 100_000_000}",
            "--network", "testnet"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Errore: {result.stderr}")
            return False
        
        print("✅ Mintato!")
        print(result.stdout)
        return True
        
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--amount", type=int, required=True)
    args = parser.parse_args()
    
    print("╔══════════════════════╗")
    print("║  GrokMeme Mint      ║")
    print("╚══════════════════════╝\n")
    
    if args.amount <= 0:
        print("❌ Amount deve essere > 0")
    else:
        mint_tokens(args.amount)
