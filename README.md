# 🧸 EleMo-Pedagogy-Bench-DE (v2)

**Wissenschaftliche Evaluation von Bildungs- und Lerngeschichten nach Margaret Carr**

EleMo-Pedagogy-Bench-DE ist ein hochpräzises, Open-Source-Benchmark-Tool zur objektiven, KI-gestützten Evaluation von pädagogischen Lerngeschichten (Learning Stories). Es evaluiert Texte in 5 pädagogischen Qualitätsdimensionen und schützt durch harte Python-Validierungen vor KI-typischen Halluzinationen.

Das Tool läuft **100 % lokal** (z. B. über LM Studio) – keine Cloud, keine Datenabflüsse, volle DSGVO-Konformität.

---

## ✨ Neue Features in v2

- **3 Ausführungsmodi:** A/B-Vergleich, Batch-Modus (JSONL für N>1) und detaillierte Einzelanalyse.
- **Swap-and-Average (Bias-Kontrolle):** Eliminiert den LLM-Primacy-Effekt im A/B-Vergleich, indem die KI den Vergleich zweimal mit vertauschten Positionen durchführt und die Ergebnisse mittelt.
- **Harte Zitat-Verifikation:** Jede Bewertung *muss* mit einem echten Zitat aus dem Originaltext belegt werden. Halluziniert die KI ein Zitat, wird der Versuch von Python verworfen.
- **Striktes K.O.-Kriterium:** Fällt die *Epistemische Disziplin* (Interpretation ohne Beleg) in einem Durchlauf auf ≤ 3 Punkte, fällt die Geschichte mit dem Status "NICHT BESTANDEN" komplett durch.
- **Logik-Zwang & Auto-Retry:** Die KI wird gezwungen, Punkte und qualitative Urteile (z. B. 9-10 = "Exzellent") logisch zu verknüpfen. Bei Fehlern wiederholt das Skript die API-Anfrage bis zu dreimal automatisch (Self-Healing).
- **"Keine Evidenz"-Erkennung:** Fehlen Kriterien (z. B. Partizipation) situativ völlig, wird dies logisch sauber mit 1-2 Punkten und dem Zitat "Keine Evidenz" geahndet.
- **Widescreen Terminal-UI:** Wunderschöne, bildschirmfüllende `rich`-Tabellen für perfekte Lesbarkeit.

---

## 📊 Bewertungsdimensionen

Das Modell evaluiert strikt nach folgenden Kriterien (je 1–10 Punkte):

| # | Dimension | Beschreibung |
|---|-----------|--------------|
| 1 | 👁️ **Beobachtung vs. Interpretation** | Klare Trennung von dem, was faktisch passiert ist, und der pädagogischen Deutung. |
| 2 | 🌱 **Ressourcenorientierung** | Fokus auf die Stärken, Interessen und Lerndispositionen des Kindes. Keine Defizitorientierung. |
| 3 | 🤝 **Partizipation** | Sichtbarmachung der kindlichen Perspektive, Absichten und aktiven Mitgestaltung. |
| 4 | 💌 **Adressatenorientierung** | Persönliche, wertschätzende Briefform an das Kind, verständliche Sprache ohne Fachjargon. |
| 5 | 🛡️ **Epistemische Disziplin** | Verzicht auf unbegründete psychologische/kausale Zuschreibungen. Keine erfundenen Gefühle/Motive. |

---

## 💻 Nutzung

Starte das Skript einfach in deinem Terminal. Es öffnet sich ein interaktives Menü:

```bash
python elemo_bench.py
