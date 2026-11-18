#!/usr/bin/env python3
"""hub_mesh.py — Modelo 2 (esqueleto).

Coordina los nodos de la red mesh, calcula el perfil de ruido y controla
el ANC audible. Punto de partida: adaptar al hardware real.
"""

import json
import time
from pathlib import Path

from nodo_sensor import NodoSensor

CONFIG = Path(__file__).with_name("config.yaml")
NUM_NODOS = 8


def cargar_config() -> dict:
    return {"num_nodos": NUM_NODOS, "anc_habilitado": False, "umbral_ruido_db": 45}


def main() -> None:
    cfg = cargar_config()
    print(f"CasaHarmonia Modelo 2 — {cfg['num_nodos']} nodos, "
          f"ANC {'ON' if cfg['anc_habilitado'] else 'OFF'}")
    nodos = [NodoSensor(i) for i in range(cfg["num_nodos"])]
    try:
        while True:
            lecturas = {n.id: n.leer() for n in nodos}
            promedio = sum(lecturas.values()) / len(lecturas)
            estado = "🟢" if promedio < cfg["umbral_ruido_db"] else "🔴"
            print(json.dumps({"ts": int(time.time()), "promedio_db": round(promedio, 1),
                              "estado": estado}))
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
