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

###🧪 Use Cases

Modell-Vergleich: EleMo-V2 vs. GPT-4 vs. Llama-3 bei der Generierung von Lerngeschichten.
Fine-Tune-Evaluation: Vorher/Nachher-Vergleich nach LoRA-Training.
Prompt-Engineering: Welcher System-Prompt produziert bessere Geschichten?
Qualitätssicherung in Kitas: Objektive Bewertung von Dokumentations-Entwürfen.
Forschung: Standardisiertes Benchmark für pädagogische KI im deutschsprachigen Raum.


### Lizenz

Dieses Tool unterliegt der EleMo Non-Commercial License.
Für kommerzielle Nutzung (z. B. Integration in Kita-Software) kontaktiere uns über [www.ki-insel.de].

### 📚 Zitieren

  title = {EleMo Lerngeschichten-Bench: A Benchmark for Evaluating Learning Stories in Early Childhood Education},
  author = {Sebastian Götz / Kita Digital},
  year = {2026},
  url = {https://github.com/Kita-Digital/Lerngeschichten-Bench}
}

