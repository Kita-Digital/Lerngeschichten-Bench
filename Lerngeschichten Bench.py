#!/usr/bin/env python3
"""
EleMo-Pedagogy-Bench-DE (Robust Edition)
Vergleicht zwei Lerngeschichten nach Margaret Carr und bewertet sie automatisch.
"""

import json
import sys
import argparse
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# --- 1. DER SYSTEM PROMPT (Verschärft für striktes JSON) ---
SYSTEM_PROMPT = """
Du bist ein erfahrener pädagogischer Experte und spezialisiert auf die Evaluation von Bildungs- und Lerngeschichten nach der Methodik von Margaret Carr.

Deine Aufgabe ist es, zwei Lerngeschichten (Geschichte A und Geschichte B) objektiv zu bewerten.

## Bewertungsdimensionen (je 1-10 Punkte)
1. **Beobachtungstreue**: Ist die Beschreibung objektiv, detailliert und "kameraartig"? Nur wahrnehmbare Fakten?
2. **Bedeutungsgebung**: Werden Lerndispositionen sichtbar gemacht? Ist die Deutung vorsichtig ("Es wirkt auf mich...")?
3. **Anschlussfähigkeit**: Ist die Einladung zum Weiterforschen logisch, kindgerecht und nicht belehrend?
4. **Beziehung & Ton**: Persönlicher Brief an das Kind? Warme Sprache? Keine Überschriften/Fachbegriffe?
5. **Epistemische Disziplin (KRITISCH)**: Behauptet die Geschichte Dinge, die wir nicht wissen können (Gedanken, Gefühle, Motive)? Wenn ja, stark abwerten (1-3 Punkte).

## Ausgabeformat (STRENGES JSON)
Du musst AUSSCHLIESSLICH ein valides JSON-Objekt ausgeben. 
WICHTIG: Nutze EXAKT die Schlüssel "story_a", "story_b" und "comparison". Keine anderen Schlüsselnamen. Gib KEINEN Text vor oder nach dem JSON aus.

{
  "story_a": {
    "scores": {
      "beobachtungstreue": X,
      "bedeutungsgebung": X,
      "anschlussfaehigkeit": X,
      "beziehung_ton": X,
      "epistemische_disziplin": X
    },
    "total_score": X,
    "strengths": ["Punkt 1", "Punkt 2"],
    "weaknesses": ["Punkt 1", "Punkt 2"]
  },
  "story_b": {
    "scores": {
      "beobachtungstreue": X,
      "bedeutungsgebung": X,
      "anschlussfaehigkeit": X,
      "beziehung_ton": X,
      "epistemische_disziplin": X
    },
    "total_score": X,
    "strengths": ["Punkt 1", "Punkt 2"],
    "weaknesses": ["Punkt 1", "Punkt 2"]
  },
  "comparison": {
    "winner": "A" oder "B" oder "Unentschieden",
    "score_difference": X,
    "detailed_reasoning": "Ausführliche, pädagogisch fundierte Begründung (mindestens 3-4 Sätze) mit konkreten Textbeispielen."
  }
}
"""


# --- 2. HILFSFUNKTIONEN ---

def get_multiline_input(prompt_text: str) -> str:
    console.print(f"\n[bold cyan]{prompt_text}[/bold cyan]")
    console.print("[dim](Füge deinen Text ein. Tippe zum Beenden ###END### in eine neue Zeile und drücke Enter.)[/dim]")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "###END###":
                break
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines).strip()


def extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return json.loads(text.strip())


def get_score_color(score: int) -> str:
    if score >= 8: return "bold green"
    if score >= 6: return "yellow"
    if score >= 4: return "orange3"
    return "red"


# --- 3. HAUPTLOGIK ---

def run_benchmark(story_a: str, story_b: str, model_name: str, api_url: str):
    console.print("\n[bold yellow]⏳ KI analysiert die Lerngeschichten... (bitte warten)[/bold yellow]\n")

    client = OpenAI(base_url=api_url, api_key="lm-studio")

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Geschichte A:\n---\n{story_a}\n---\n\nGeschichte B:\n---\n{story_b}\n---"}
            ],
            temperature=0.1,  # WICHTIG: Sehr niedrig für stabiles JSON
            max_tokens=4096
        )
        raw_output = response.choices[0].message.content
        results = extract_json(raw_output)

    except json.JSONDecodeError as e:
        console.print("[bold red]Fehler: Das Modell hat kein gültiges JSON zurückgegeben.[/bold red]")
        console.print(Panel(raw_output, title="Raw Output des Modells", border_style="red"))
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]API-Fehler:[/bold red] {e}")
        sys.exit(1)

    # --- 4. ROBUSTE VALIDIERUNG (Verhindert den KeyError) ---
    if "story_a" not in results or "story_b" not in results or "comparison" not in results:
        console.print("[bold red]Fehler: Das JSON ist gültig, aber die Schlüssel sind falsch.[/bold red]")
        console.print("[dim]Das Modell hat eigene Schlüssel erfunden. Hier ist der Output zur Analyse:[/dim]")
        console.print(Panel(raw_output, title="Falsches JSON-Format", border_style="yellow"))
        console.print(
            "\n[dim]Tipp: Erhöhe in LM Studio die 'Repeat Penalty' oder senke die 'Temperature' auf 0.1[/dim]")
        sys.exit(1)

    # --- 5. AUSGABE ---
    table = Table(title=" Evaluierungsergebnis", box=box.DOUBLE_EDGE, show_lines=True, title_style="bold cyan")
    table.add_column("Dimension", style="bold", width=35)
    table.add_column("Geschichte A", justify="center", width=12)
    table.add_column("Geschichte B", justify="center", width=12)
    table.add_column("Differenz", justify="center", width=12)

    dim_labels = {
        "beobachtungstreue": "📷 Beobachtungstreue",
        "bedeutungsgebung": "🔍 Bedeutungsgebung",
        "anschlussfaehigkeit": "🚀 Anschlussfähigkeit",
        "beziehung_ton": "💌 Beziehung & Ton",
        "epistemische_disziplin": "🛡️ Epistemische Disziplin"
    }

    scores_a = results["story_a"]["scores"]
    scores_b = results["story_b"]["scores"]

    for key, label in dim_labels.items():
        s_a = scores_a.get(key, 0)
        s_b = scores_b.get(key, 0)
        diff = s_b - s_a

        diff_text = f"[green]+{diff}[/green]" if diff > 0 else (f"[red]{diff}[/red]" if diff < 0 else "[dim]0[/dim]")

        table.add_row(
            label,
            f"[{get_score_color(s_a)}]{s_a}/10[/{get_score_color(s_a)}]",
            f"[{get_score_color(s_b)}]{s_b}/10[/{get_score_color(s_b)}]",
            diff_text
        )

    total_a = results["story_a"]["total_score"]
    total_b = results["story_b"]["total_score"]
    total_diff = total_b - total_a
    winner = results["comparison"]["winner"]

    table.add_row(
        "[bold]🏆 GESAMTPUNKTZAHL[/bold]",
        f"[bold]{total_a}/50[/bold]",  # Angepasst auf 5 Dimensionen * 10 = 50
        f"[bold]{total_b}/50[/bold]",
        f"[bold green]{total_diff:+d} → {winner}[/bold green]"
    )
    console.print(table)

    for key, name in [("story_a", "Geschichte A"), ("story_b", "Geschichte B")]:
        data = results[key]
        strengths = "\n".join([f"  • {s}" for s in data.get("strengths", [])])
        weaknesses = "\n".join([f"  • {w}" for w in data.get("weaknesses", [])])

        console.print(Panel(
            f"[bold green]✅ Stärken:[/bold green]\n{strengths}\n\n[bold red]⚠️ Schwächen:[/bold red]\n{weaknesses}",
            title=f"[bold]{name}[/bold] ({data['total_score']}/50 Punkte)",
            border_style="green" if data['total_score'] >= 40 else "yellow"
        ))

    reasoning = results["comparison"]["detailed_reasoning"]
    console.print(Panel(
        f"[bold]🏆 Urteil:[/bold] Geschichte {winner} ist besser.\n\n[bold] Begründung:[/bold]\n{reasoning}",
        title="[bold cyan]Vergleichsurteil[/bold cyan]",
        border_style="cyan"
    ))


def main():
    parser = argparse.ArgumentParser(description="EleMo-Pedagogy-Bench-DE")
    parser.add_argument("--file-a", help="Pfad zu Textdatei für Geschichte A")
    parser.add_argument("--file-b", help="Pfad zu Textdatei für Geschichte B")
    parser.add_argument("--model", default="eleMo-v2-q6", help="Name des Modells in LM Studio")
    parser.add_argument("--url", default="http://localhost:1234/v1", help="LM Studio API URL")
    args = parser.parse_args()

    console.print(Panel.fit(
        "[bold cyan]🧸 EleMo-Pedagogy-Bench-DE[/bold cyan]\n[dim]Evaluation von Lerngeschichten nach Margaret Carr[/dim]",
        border_style="cyan"
    ))

    if args.file_a and args.file_b:
        with open(args.file_a, 'r', encoding='utf-8') as f:
            story_a = f.read()
        with open(args.file_b, 'r', encoding='utf-8') as f:
            story_b = f.read()
    else:
        story_a = get_multiline_input("📝 Bitte Geschichte 1 einfügen:")
        story_b = get_multiline_input("📝 Bitte Geschichte 2 einfügen:")

    if not story_a or not story_b:
        console.print("[bold red]Fehler: Beide Geschichten müssen Text enthalten![/bold red]")
        sys.exit(1)

    run_benchmark(story_a, story_b, args.model, args.url)


if __name__ == "__main__":
    main()