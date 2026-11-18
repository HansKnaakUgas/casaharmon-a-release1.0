#!/usr/bin/env python3
"""nodo_sensor.py — Nodo del mesh (esqueleto).

Representa un nodo de sensado ambiental. La lectura es simulada hasta
integrar el hardware real.
"""


class NodoSensor:
    """Un nodo de la red mesh de Modelo 2."""

    def __init__(self, nodo_id: int) -> None:
        self.id = nodo_id

    def leer(self) -> float:
        """Retorna nivel de ruido en dB (simulado)."""
        return 40.0 + (self.id % 3)
