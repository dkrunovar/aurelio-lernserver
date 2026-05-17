#!/bin/bash
# ══════════════════════════════════════════════════════
#  Aurelio Lernserver — Doppelklick zum Starten
#  (Dieses Skript öffnet automatisch ein Terminal)
# ══════════════════════════════════════════════════════

cd "$(dirname "$0")"

echo "🎒 Aurelio Lernserver wird gestartet..."
echo ""

# Python prüfen
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 nicht gefunden!"
    echo "   Bitte installiere Python von: https://python.org"
    read -p "Drücke Enter zum Schließen..."
    exit 1
fi

# anthropic Paket prüfen und installieren
if ! python3 -c "import anthropic" 2>/dev/null; then
    echo "📦 Installiere das 'anthropic' Paket (einmalig)..."
    pip3 install anthropic --quiet
    echo "✅ Installiert!"
    echo ""
fi

# Browser öffnen (kurz warten bis Server läuft)
sleep 1.5 && open "http://localhost:8080" &

# Server starten
python3 server.py
