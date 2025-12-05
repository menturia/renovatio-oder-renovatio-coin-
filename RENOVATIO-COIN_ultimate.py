# RENOVATIO-COIN_ultimate.py – RENOVATIO-COINs 2025 – FINAL ULTIMATE EDITION
import hashlib
import time
import json
from datetime import datetime
try:
    from winsound import Beep
except ImportError:
    # Für Nicht-Windows Systeme
    def Beep(frequency, duration):
        print(f"\a", end="", flush=True)  # System bell als Fallback

# === FARBPALETTE ===
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[97m"
F = "\033[1m"
U = "\033[4m"
X = "\033[0m"

# Beep-Frequenzen
def success_beep():
    Beep(1000, 200)
    Beep(1500, 300)

def tick_beep():
    Beep(800, 50)

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = None
    
    def calculate_hash(self):
        data = json.dumps({
            "index": self.index, 
            "transactions": self.transactions, 
            "timestamp": self.timestamp, 
            "previous_hash": self.previous_hash, 
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()
    
    def mine(self, difficulty=4):
        target = "0" * difficulty
        print(f"{G}→ Mining Block {self.index} | Ziel: {target}{X}", end="", flush=True)
        attempts = 0
        start = time.time()
        
        while self.calculate_hash()[:difficulty] != target:
            self.nonce += 1
            attempts += 1
            if attempts % 10000 == 0:
                tick_beep()
            if attempts % 50000 == 10000:
                print(f"{R}♥{Y}♥{B}♥{M}♥{C}♥{W}♥{R}♥{G}♥{X}", end="", flush=True)
            if attempts % 200000 == 0:
                print(f"{Y}→ {attempts:,} Hashes → {self.calculate_hash()[:difficulty+12]}", end="\r", flush=True)
        
        self.hash = self.calculate_hash()
        duration = time.time() - start
        print(f"\n{G}★ BLOCK GEFUNDEN! ★{X}")
        success_beep()
        print(f"{G}Block {self.index} nach {attempts:,} Hashes in {duration:.2f}s")
        print(f"{G}Hash: {self.hash[:64]}{X}")
        return self.hash

def display_heartbeat():
    """Zeigt einen bunten Herzschlag an"""
    colors = [R, Y, G, B, M, C]
    for color in colors:
        print(f"{color}♥{X}", end="", flush=True)
        time.sleep(0.05)
    print()

# === START ===
print(f"{C}╔{'═'*80}╗{X}")
print(f"{C}║{F}RENOVATIO-COINs 2025 – FINAL ULTIMATE EDITION{' ' * 41}{X}{C}║{X}")
print(f"{C}╚{'═'*80}╝{X}")

print(f"\n{Y}★ Genesis-Block wird erstellt...{X}")
genesis = Block(0, [f"{Y}Genesis: 1.000.000 RENOVATIO-COINs → Nick Freund{X}"], "0")
genesis.mine(4)
chain = [genesis]

# Wallet initialisieren
wallet = {"Nick Freund": 1000000}

def update_wallet(sender, receiver, amount):
    """Aktualisiert das Wallet nach einer Transaktion"""
    print(f"{M}{'═'*60}{X}")
    print(f"{M}💰 Wallet-Update: {sender} → {receiver}: {amount:,} RENOVATIO-COINs{X}")
    
    if sender != "genesis":
        if wallet.get(sender, 0) >= amount:
            wallet[sender] -= amount
            wallet[receiver] = wallet.get(receiver, 0) + amount
        else:
            print(f"{R}❌ FEHLER: {sender} hat nicht genug RENOVATIO-COINs!{X}")
            return False
    else:
        wallet[receiver] = wallet.get(receiver, 0) + amount
    
    # Herzschlag anzeigen
    display_heartbeat()
    
    # Wallet-Stände anzeigen
    print(f"{G}✅ Neue Wallet-Stände:{X}")
    for person, balance in wallet.items():
        print(f"   {G}→ {person}: {balance:,} RENOVATIO-COINs{X}")
    
    return True

# Blockchain aufbauen
print(f"\n{Y}★ Erstelle weitere Blöcke...{X}")

# Block 1: Nick Freund → Max
print(f"\n{B}★ Block 1: Nick Freund → Max{X}")
update_wallet("Nick Freund", "Max", 150)
b1 = Block(1, [
    f"{M}Nick Freund → Max: 150 RENOVATIO-COINs{X}",
    f"{G}Transaktionsgebühr: 1 RENOVATIO-COINs{X}"
], chain[-1].hash)
b1.mine(4)
chain.append(b1)
update_wallet("Nick Freund", "Miner", 1)  # Transaktionsgebühr

# Block 2: Max → Lisa
print(f"\n{B}★ Block 2: Max → Lisa{X}")
update_wallet("Max", "Lisa", 70)
b2 = Block(2, [
    f"{R}Max → Lisa: 70 RENOVATIO-COINs{X}",
    f"{G}Mining-Belohnung: 50 RENOVATIO-COINs{X}",
    f"{G}Transaktionsgebühr: 1 RENOVATIO-COINs{X}"
], chain[-1].hash)
b2.mine(5)
chain.append(b2)
update_wallet("system", "Miner", 50)  # Mining-Belohnung
update_wallet("Max", "Miner", 1)  # Transaktionsgebühr

# Block 3: Lisa → Nick Freund
print(f"\n{B}★ Block 3: Lisa → Nick Freund{X}")
update_wallet("Lisa", "Nick Freund", 30)
b3 = Block(3, [
    f"{B}Lisa → Nick Freund: 30 RENOVATIO-COINs{X}",
    f"{G}Mining-Belohnung: 50 RENOVATIO-COINs{X}",
    f"{G}Transaktionsgebühr: 1 RENOVATIO-COINs{X}"
], chain[-1].hash)
b3.mine(5)
chain.append(b3)
update_wallet("system", "Miner", 50)  # Mining-Belohnung
update_wallet("Lisa", "Miner", 1)  # Transaktionsgebühr

# === BLOCKCHAIN ANZEIGEN ===
print(f"\n{Y}{'═'*80}{X}")
print(f"{Y}{F}           RENOVATIO-COIN BLOCKCHAIN – KOMPLETTE ÜBERSICHT{X}")
print(f"{Y}{'═'*80}{X}")

for block in chain:
    print(f"\n{G}╔{'═'*78}╗{X}")
    print(f"{G}║ Block #{block.index:4d} {' ' * 52} ║{X}")
    print(f"{G}╠{'═'*78}╣{X}")
    print(f"{G}║ {Y}Zeit:{X} {datetime.fromtimestamp(block.timestamp):%d.%m.%Y %H:%M:%S} {' ' * 37} {G}║{X}")
    print(f"{G}║ {Y}Hash:{X} {block.hash}{G} ║{X}")
    print(f"{G}║ {Y}Prev Hash:{X} {block.previous_hash}{G} ║{X}")
    print(f"{G}║ {Y}Nonce:{X} {block.nonce:,} {' ' * (68 - len(str(block.nonce)))} {G}║{X}")
    
    print(f"{G}║ {Y}Transaktionen:{X} {' ' * 62} {G}║{X}")
    for tx in block.transactions:
        # Kürze lange Texte für bessere Darstellung
        if len(tx) > 70:
            display_tx = tx[:67] + "..."
        else:
            display_tx = tx
        print(f"{G}║   • {display_tx}{' ' * (74 - len(display_tx))} {G}║{X}")
    
    print(f"{G}╚{'═'*78}╝{X}")

# === FINALE STATISTIKEN ===
print(f"\n{M}{'═'*80}{X}")
print(f"{M}{F}                    FINALE STATISTIKEN{X}")
print(f"{M}{'═'*80}{X}")

print(f"\n{Y}📊 Blockchain-Statistiken:{X}")
print(f"   • Gesamtblöcke: {len(chain)}")
print(f"   • Genesis-Block: Block #{chain[0].index}")
print(f"   • Letzter Block: Block #{chain[-1].index}")
print(f"   • Gesamt-Transaktionen: {sum(len(b.transactions) for b in chain)}")

print(f"\n{Y}💰 Wallet-Stände:{X}")
total_coins = 0
for person, balance in sorted(wallet.items()):
    print(f"   • {person:15s}: {balance:10,d} RENOVATIO-COINs")
    total_coins += balance

print(f"\n{Y}📈 Mining-Statistiken:{X}")
total_nonce = sum(b.nonce for b in chain)
print(f"   • Total Nonce-Versuche: {total_nonce:,}")
print(f"   • Durchschn. Versuche/Block: {total_nonce // len(chain):,}")

print(f"\n{G}✅ Mining abgeschlossen! Du hast eine vollständige Blockchain mit {len(chain)} Blöcken erstellt!{X}")
print(f"{C}✨ Herzlichen Glückwunsch zum erfolgreichen Mining! ✨{X}")

print(f"\n{W}{'═'*80}{X}")
input(f"{W}Drücke Enter zum Beenden...{X}")