#!/usr/bin/env python3
"""Revisión editorial semanal de la guía pública, sin escrituras ni publicaciones."""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
DETAILS: list[str] = []

def read_text(relative: str) -> str:
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        ERRORS.append(f"Ruta fuera del repositorio: {relative}")
        return ""
    if not path.is_file():
        ERRORS.append(f"Archivo faltante: {relative}")
        return ""
    text = path.read_text(encoding="utf-8")
    DETAILS.append(f"Encontrado: {relative}")
    return text

def main() -> int:
    raw = read_text("VERSION.json")
    try:
        data = json.loads(raw)
    except (ValueError, TypeError) as exc:
        ERRORS.append(f"VERSION.json inválido: {exc}")
        data = {}
    release = data.get("release") or {}
    version = str(release.get("version") or "")
    date = str(release.get("published_on") or "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        ERRORS.append("Versión no semántica X.Y.Z")
    try:
        published = dt.date.fromisoformat(date)
        if published > dt.date.today():
            WARNINGS.append("Fecha de publicación posterior al día del control")
        if (dt.date.today() - published).days > 60:
            WARNINGS.append("Más de 60 días sin una versión nueva: revisar si hay aprendizajes pendientes")
    except ValueError:
        ERRORS.append("Fecha de publicación inválida")
    docs = data.get("documentation") or {}
    if data.get("consumer_guidance", {}).get("automatic_application_allowed") is not False:
        ERRORS.append("VERSION.json debe prohibir la aplicación automática en proyectos de terceros")
    for key in ("readme", "changelog", "release_notes", "continuous_improvement"):
        relative = docs.get(key)
        if not isinstance(relative, str) or not relative:
            ERRORS.append(f"documentación sin ruta {key}")
        else:
            read_text(relative)
    changelog = read_text("CHANGELOG.md")
    readme = read_text("README.md")
    notes = read_text("ACTUALIZACION_2026-11-13.md")
    # Una versión nueva debe actualizar el registro de cambios y la portada.
    major_minor = ".".join(version.split(".")[:2])
    if not re.search(r"^##\s+" + re.escape(major_minor) + r"\b", changelog, re.M):
        ERRORS.append(f"CHANGELOG no registra la versión {major_minor}")
    if not re.search(r"versión\s+" + re.escape(major_minor) + r"\b", readme, re.I):
        ERRORS.append(f"README no identifica la versión {major_minor}")
    if "13/11/2026" not in notes:
        WARNINGS.append("Notas originales 13/11/2026 no encontradas como se esperaba")
    read_text("plantilla-proyecto/REVISION_SEMANAL_GUIA.md")
    read_text("plantilla-proyecto/automatizaciones/revisar_novedades_semanal.yml")
    issues = "No consultadas (Issues deshabilitadas o token insuficiente)"
    if os.environ.get("GH_TOKEN") and os.environ.get("GITHUB_REPOSITORY"):
        result = subprocess.run(
            ["gh", "issue", "list", "--repo", os.environ["GITHUB_REPOSITORY"],
             "--state", "open", "--limit", "10", "--json", "number,title,url"],
            capture_output=True, text=True, check=False,
        )
        if result.returncode == 0:
            try:
                pending = json.loads(result.stdout)
                issues = f"{len(pending)} Issues abiertas en la muestra de 10"
                for item in pending[:5]:
                    DETAILS.append(f"Issue #{item['number']}: {item['title']}")
            except (ValueError, KeyError):
                WARNINGS.append("No se pudo interpretar lista de Issues")
        else:
            WARNINGS.append("No fue posible consultar Issues; no se interpretan como 0")
    summary = [
        "# Revisión semanal de la guía pública",
        f"- Versión publicada: **{version or 'no verificable'}**",
        f"- Fecha: **{date or 'no verificable'}**",
        f"- Estado del control estructural: **{'ERROR' if ERRORS else 'APROBADO'}**",
        f"- Propuestas: {issues}",
        "",
        "## Hallazgos",
        *(f"- ERROR: {item}" for item in ERRORS),
        *(f"- Aviso: {item}" for item in WARNINGS),
        *((f"- {item}" for item in DETAILS[:25]) if not ERRORS and not WARNINGS else []),
        "",
        "**Límite:** este trabajo verifica estructura y pendientes públicos; "
        "no revisa semánticamente mejoras, no crea publicaciones ni cambia proyectos de colegas.",
        "La evaluación editorial humana/asistida es un paso separado.",
    ]
    output = "\n".join(summary) + "\n"
    print(output)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
            stream.write(output)
    return 1 if ERRORS else 0

if __name__ == "__main__":
    raise SystemExit(main())
