# 🎒 Aurelio Lernserver — Setup-Anleitung

## Einmalige Einrichtung (5 Minuten)

### Schritt 1: API Key holen
1. Gehe auf: https://console.anthropic.com
2. Registriere dich (kostenlos)
3. Gehe auf "API Keys" → "Create Key"
4. Kopiere den Key (beginnt mit `sk-ant-...`)

### Schritt 2: API Key eintragen
Öffne die Datei `server.py` mit einem Texteditor und ersetze:
```
API_KEY = "HIER_API_KEY_EINTRAGEN"
```
durch:
```
API_KEY = "sk-ant-dein-key-hier"
```

### Schritt 3: Server starten
**Einfachste Methode:**
- Doppelklick auf `START.command`
- Falls Warnung erscheint: Rechtsklick → Öffnen → Öffnen

**Oder im Terminal:**
```bash
cd /Pfad/zum/Ordner
python3 server.py
```

### Schritt 4: Im Browser öffnen
- http://localhost:8080  ← auf dem Mac Mini selbst
- http://DEINE-IP:8080  ← von anderen Geräten im Heimnetz

---

## Dateien im Ordner

| Datei | Beschreibung |
|-------|-------------|
| `index.html` | Haupt-Lernhub (Wochenplan, Lernwörter, Mathe) |
| `leo.html` | KI-Lernbegleiter Leo (Aurelio tippt Fragen) |
| `server.py` | Server-Skript (hält API Key sicher) |
| `START.command` | Doppelklick-Starter für Mac |

---

## Kosten
- Anthropic API: ca. €0.003 pro Gespräch mit Leo (sehr günstig)
- 100 Gespräche ≈ €0.30

---

## Tipps
- Server läuft im Hintergrund, solange das Terminal offen ist
- Zum Beenden: Ctrl+C im Terminal, oder Terminal schließen
- Fehler-Tracking in index.html wird im Browser gespeichert (bleibt erhalten)
- Aurelio kann Leo auf jedem Gerät im Heimnetz öffnen (iPad, iPhone, etc.)

---

## ANTON App
ANTON und dieser Lernserver ergänzen sich:
- **ANTON**: Strukturierte Übungen, viele Fächer, gamifiziert
- **Lernserver**: Gezielte Lernwörter von Carina + Fehler-Tracking für Eltern
- **Leo**: Erklärungen auf Aurelios Niveau wenn er etwas nicht versteht
