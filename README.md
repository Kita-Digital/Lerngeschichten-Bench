# 🧸 EleMo-Pedagogy-Bench-DE

**Professionelle Evaluation von Bildungs- und Lerngeschichten nach Margaret Carr**

EleMo-Pedagogy-Bench-DE ist ein Open-Source-Benchmark-Tool zur objektiven, KI-gestützten Evaluation von pädagogischen Lerngeschichten (Learning Stories). Es vergleicht zwei Geschichten in 5 pädagogischen Qualitätsdimensionen und liefert ein fundiertes Vergleichsurteil.

Das Tool läuft **100 % lokal** über LM Studio – keine Cloud, keine Datenabflüsse.

---

## ✨ Features

- **Vergleicht zwei Lerngeschichten** (z. B. EleMo vs. GPT-4, oder zwei verschiedene Prompts)
- **Bewertet in 5 pädagogischen Dimensionen** (je 1-10 Punkte)
- **Liefert eine Gesamtpunktzahl** (max. 50 Punkte)
- **Gibt eine begründete Analyse**, warum Geschichte X besser ist als Y
- **Epistemische Disziplin:** Bestraft explizit das Erfinden von Gefühlen/Gedanken (Halluzinationen)
- **Wunderschönes Terminal-UI** durch die `rich` Bibliothek

---

## 📊 Bewertungsdimensionen

| # | Dimension | Beschreibung |
|---|-----------|--------------|
| 1 |  Beobachtungstreue | Objektivität, Detailreichtum, "Kamera-Perspektive" |
| 2 | 🔍 Bedeutungsgebung | Sichtbarmachung von Lerndispositionen (Margaret Carr) |
| 3 |  Anschlussfähigkeit | Logische, kindgerechte Next Steps |
| 4 | 💌 Beziehung & Ton | Brief-Form, wertschätzend, keine Fachbegriffe |
| 5 | 🛡️ Epistemische Disziplin | Keine Halluzinationen von inneren Zuständen (Gefühle, Motive) |

---

## ⚙️ Installation & Voraussetzungen

### 1. Python installieren
Stelle sicher, dass Python 3.10+ installiert ist.

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
