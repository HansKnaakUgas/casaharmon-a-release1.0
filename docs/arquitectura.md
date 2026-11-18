# Arquitectura general

## Vista de conjunto

```
            +----------------------+        +----------------------+
            |  Modelo 1 (Jardin)   |        |  Modelo 2 (Indoor)   |
            |  Receptor RF pasivo  |        |  8 nodos + hub mesh  |
            +----------+-----------+        +----------+-----------+
                       |                               |
                       v                               v
            +----------------------+        +----------------------+
            | hub_central.py       |        | hub_mesh.py          |
            | umbral + alerta      |        | ANC audible + A/B    |
            +----------+-----------+        +----------+-----------+
                       |                               |
                       +---------------+---------------+
                                       v
                           Panel local del usuario
```

## Principio comun
Ningun artefacto transmite energia al ambiente: solo sensa (Modelo 1) o
cancela acusticamente en el rango audible (Modelo 2, altavoz dirigido).
