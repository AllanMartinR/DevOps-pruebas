"""Lee resultados.xml y coverage.json y escribe un resumen en la pestaña del run."""
import json
import os
import sys
import xml.etree.ElementTree as ET

modulo = sys.argv[1] if len(sys.argv) > 1 else "todos"

try:
    raiz = ET.parse("resultados.xml").getroot()
    suite = raiz if raiz.tag == "testsuite" else raiz.find("testsuite")
    total = int(suite.get("tests"))
    fallos = int(suite.get("failures")) + int(suite.get("errors"))
    omitidas = int(suite.get("skipped"))
    aprobadas = total - fallos - omitidas
    pct = round(100 * aprobadas / total, 1) if total else 0.0
except (OSError, ET.ParseError, AttributeError, TypeError):
    total = fallos = aprobadas = 0
    pct = 0.0

try:
    with open("coverage.json", encoding="utf-8") as f:
        cobertura = f"{round(json.load(f)['totals']['percent_covered'], 1)}%"
except (OSError, KeyError, ValueError):
    cobertura = "n/d"

if fallos:
    cobertura = "-"  # solo es significativa cuando todo pasa

estado = "VERDE" if total and fallos == 0 else "ROJO"
texto = (
    f"## {estado} - módulo: {modulo}\n\n"
    f"| Pruebas | Aprobadas | Fallidas | % aprobado | Cobertura |\n"
    f"|---|---|---|---|---|\n"
    f"| {total} | {aprobadas} | {fallos} | {pct}% | {cobertura} |\n"
)
print(texto)
destino = os.environ.get("GITHUB_STEP_SUMMARY")
if destino:
    with open(destino, "a", encoding="utf-8") as f:
        f.write(texto)
