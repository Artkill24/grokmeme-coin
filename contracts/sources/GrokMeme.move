module grokmeme::grok_meme {
    use std::string::{Self, String};
    use std::option;
    use std::signer;
    use aptos_framework::coin::{Self, Coin, MintCapability, BurnCapability};
    use aptos_framework::account;

    /// Errori
    const ENOT_AUTHORIZED: u64 = 1;
    const EALREADY_INITIALIZED: u64 = 2;
    const EINSUFFICIENT_BALANCE: u64 = 3;

    /// Struttura della coin GrokMeme
    struct GrokMeme {}

    /// Capabilities per gestire la coin (mint, burn)
    struct Capabilities has key {
        mint_cap: MintCapability<GrokMeme>,
        burn_cap: BurnCapability<GrokMeme>,
    }

    /// Informazioni sulla coin
    struct CoinInfo has key {
        total_supply: u64,
        decimals: u8,
    }

    /// Inizializza la coin (chiamata una sola volta dal creatore)
    public entry fun initialize(account: &signer) {
        let account_addr = signer::address_of(account);
        
        assert!(!exists<Capabilities>(account_addr), EALREADY_INITIALIZED);

        let (burn_cap, freeze_cap, mint_cap) = coin::initialize<GrokMeme>(
            account,
            string::utf8(b"GrokMeme"),
            string::utf8(b"GROKME"),
            8,
            true,
        );

        move_to(account, Capabilities {
            mint_cap,
            burn_cap,
        });

        move_to(account, CoinInfo {
            total_supply: 0,
            decimals: 8,
        });

        coin::destroy_freeze_cap(freeze_cap);
        coin::register<GrokMeme>(account);
    }

    /// Minta nuovi token
    public entry fun mint(
        admin: &signer,
        amount: u64
    ) acquires Capabilities, CoinInfo {
        let admin_addr = signer::address_of(admin);
        assert!(exists<Capabilities>(admin_addr), ENOT_AUTHORIZED);
        
        let capabilities = borrow_global<Capabilities>(admin_addr);
        let coin_info = borrow_global_mut<CoinInfo>(admin_addr);
        
        let coins = coin::mint<GrokMeme>(amount, &capabilities.mint_cap);
        coin::deposit<GrokMeme>(admin_addr, coins);
        
        coin_info.total_supply = coin_info.total_supply + amount;
    }

    /// Trasferisci token
    public entry fun transfer(
        from: &signer,
        to: address,
        amount: u64
    ) {
        coin::transfer<GrokMeme>(from, to, amount);
    }

    /// Brucia token
    public entry fun burn(
        account: &signer,
        amount: u64
    ) acquires Capabilities, CoinInfo {
        let account_addr = signer::address_of(account);
        
        let capabilities = borrow_global<Capabilities>(account_addr);
        let coin_info = borrow_global_mut<CoinInfo>(account_addr);
        
        let coins = coin::withdraw<GrokMeme>(account, amount);
        coin::burn<GrokMeme>(coins, &capabilities.burn_cap);
        
        coin_info.total_supply = coin_info.total_supply - amount;
    }

    /// Registra un account
    public entry fun register(account: &signer) {
        coin::register<GrokMeme>(account);
    }

    #[view]
    public fun balance_of(account: address): u64 {
        coin::balance<GrokMeme>(account)
    }

    #[view]
    public fun total_supply(creator: address): u64 acquires CoinInfo {
        if (exists<CoinInfo>(creator)) {
            borrow_global<CoinInfo>(creator).total_supply
        } else {
            0
        }
    }

    #[view]
    public fun decimals(creator: address): u8 acquires CoinInfo {
        if (exists<CoinInfo>(creator)) {
            borrow_global<CoinInfo>(creator).decimals
        } else {
            8
        }
    }

    #[view]
    public fun name(): String {
        string::utf8(b"GrokMeme")
    }

    #[view]
    public fun symbol(): String {
        string::utf8(b"GROKME")
    }
}
