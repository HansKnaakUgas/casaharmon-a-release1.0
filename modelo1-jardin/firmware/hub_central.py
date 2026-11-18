#!/usr/bin/env python3
"""hub_central.py — Modelo 1 (esqueleto).

Lee mediciones del receptor RF y emite alertas cuando el nivel supera
el umbral configurado. Es un punto de partida: adaptar al hardware real.
"""

import json
import time
from pathlib import Path

CONFIG = Path(__file__).with_name("config.yaml")


def cargar_config() -> dict:
    """Carga umbral y ventana de muestreo (formato simplificado)."""
    cfg = {"umbral_alerta_dbm": -60, "ventana_muestreo_s": 60}
    try:
        for linea in CONFIG.read_text().splitlines():
            if linea.startswith("umbral_alerta_dbm:"):
                cfg["umbral_alerta_dbm"] = float(linea.split(":", 1)[1].strip())
            elif linea.startswith("ventana_muestreo_s:"):
                cfg["ventana_muestreo_s"] = int(linea.split(":", 1)[1].strip())
    except OSError:
        print("⚠️  config.yaml no encontrado, usando valores por defecto")
    return cfg


def leer_medicion() -> float:
    """TODO: reemplazar por lectura real del receptor (puerto serie/USB).

    Retorna nivel en dBm. Por ahora devuelve un valor simulado.
    """
    return -72.5


def evaluar(nivel_dbm: float, umbral: float) -> str:
    if nivel_dbm >= umbral:
        return ("🔴 ALERTA: nivel sobre umbral. Recomendacion pasiva: "
                "aumentar distancia, apantallar fuente o programar apagado.")
    return "🟢 Nivel dentro de rango esperado."


def main() -> None:
    cfg = cargar_config()
    print(f"CasaHarmonia Modelo 1 — umbral {cfg['umbral_alerta_dbm']} dBm")
    try:
        while True:
            nivel = leer_medicion()
            print(json.dumps({"ts": int(time.time()), "dbm": nivel,
                              "estado": evaluar(nivel, cfg['umbral_alerta_dbm'])}))
            time.sleep(cfg["ventana_muestreo_s"])
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
