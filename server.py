#!/usr/bin/env python3
"""
Aurelio Lernserver — läuft auf dem Mac Mini
Startet einen lokalen Webserver auf Port 8080
"""

import json
import os
import sys
import http.server
import anthropic

# ── API KEY ────────────────────────────────────────────────────────────────
# Entweder hier eintragen ODER als Umgebungsvariable setzen:
#   export ANTHROPIC_API_KEY="sk-ant-..."
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "HIER_API_KEY_EINTRAGEN")

SYSTEM_PROMPT = """Du bist LEO, Aurelios freundlicher KI-Lernbegleiter.
Aurelio ist 8 Jahre alt und geht in die 2. Klasse Volksschule in Wien.

Was Aurelio gerade lernt:
- DEUTSCH: Lernwörter mit ai/ei (Hai, Mai, Kaiser), C-Laut (Cent, Comic, Clown),
  Vorsilben ver-, ab-, auf-, vor-, zusammengesetzte Nomen, Bildergeschichten
- MATHE: Addition und Subtraktion bis 100 mit Übergang (36+27, 71-35),
  Malreihen 1-10, Sachaufgaben, Schaubilder lesen
- Aurelio übt auch mit der ANTON-App

Deine Regeln:
- Sprich IMMER einfaches, klares Deutsch — wie ein netter Lehrer mit 8-Jährigen
- Sei geduldig und ermutigend. Fehler sind toll — daraus lernt man!
- Erkläre mit konkreten Beispielen aus dem Alltag (Fußball, Tiere, Essen...)
- Stelle nach jeder Erklärung eine einfache Übungsfrage
- Wenn Aurelio eine Aufgabe zeigt: löse sie SCHRITTWEISE und erkläre jeden Schritt
- Verwende Emojis und sei fröhlich 😊
- Antworte IMMER auf Deutsch
- Halte Antworten kurz (max 5-6 Sätze) — Aurelio ist 8!
- Wenn er "Hilfe" oder "ich verstehe nicht" schreibt: erkläre nochmal anders
- Lobe Fortschritt, nicht nur Ergebnisse ("Toll, du versuchst es!")"""

PORT = 8080

class AurelioHandler(http.server.SimpleHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/chat":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = json.loads(self.rfile.read(length))
                messages = body.get("messages", [])

                client = anthropic.Anthropic(api_key=API_KEY)
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=600,
                    system=SYSTEM_PROMPT,
                    messages=messages
                )
                result = {"reply": response.content[0].text}
                self._json(200, result)
            except Exception as e:
                self._json(500, {"error": str(e)})
        else:
            self.send_response(404)
            self.end_headers()

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # Einfache Log-Ausgabe
        print(f"  {args[0]} {args[1]}")


if __name__ == "__main__":
    if API_KEY == "HIER_API_KEY_EINTRAGEN":
        print("⚠️  ACHTUNG: API Key fehlt!")
        print("   Öffne server.py und trage deinen Anthropic API Key ein.")
        print("   Oder: export ANTHROPIC_API_KEY='sk-ant-...' vor dem Start")
        print()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(("", PORT), AurelioHandler)
    print(f"🎒 Aurelio Lernserver läuft!")
    print(f"   → Öffne im Browser: http://localhost:{PORT}")
    print(f"   → Im Heimnetz:      http://DEINE-IP:{PORT}")
    print(f"   Zum Beenden: Ctrl+C")
    print()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ Server gestoppt.")
