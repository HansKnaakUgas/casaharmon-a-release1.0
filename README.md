# CasaHarmonia — Monitoreo electromagnetico y concienciacion ambiental

[![Docs: CC BY-SA 4.0](https://img.shields.io/badge/Documentacion-CC%20BY--SA%204.0-lightgreen.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Hardware: CERN-OHL-S 2.0](https://img.shields.io/badge/Hardware-CERN--OHL--S%202.0-blue.svg)](https://ohwr.org/cern_ohl_s_v2.txt)
[![Software: GPL-3.0](https://img.shields.io/badge/Software-GPL--3.0-red.svg)](https://www.gnu.org/licenses/gpl-3.0.txt)

> Sistema pasivo automatizado de monitoreo electromagnetico y gestion de
> ruido audible para hogares familiares.
> **No emite radiofrecuencia. No es un jammer.**

## Contenido

- [Filosofia](#filosofia)
- [Artefactos](#artefactos)
- [Consideraciones regulatorias](#regulatorio)
- [Instalacion](#instalacion)
- [Presupuesto](#presupuesto)
- [Licencias](#licencias)

## Filosofia

CasaHarmonia nace de una pregunta: *como hacer visible el ruido
electromagnetico que nos rodea?* No se trata de "apagar" el mundo, sino de
**medir, informar y educar**.

1. **Ecologia profunda** — el hogar como ecosistema.
2. **Principio precautorio** — alerta temprana antes de la certeza de dano.
3. **Diseno para la concienciacion** — el usuario aprende a interpretar su
   entorno electromagnetico.

## Artefactos

### Modelo 1 — Poste de Jardin / Estacion Indoor
Monitoreo pasivo de espectro electromagnetico (1 Hz – 6 GHz) con alerta y
recomendacion de mitigacion pasiva.
📂 [Ver documentacion →](modelo1-jardin/)

### Modelo 2 — Sistema Indoor (Casa 144 m2)
Red mesh de 8 nodos + hub central con cancelacion activa de ruido audible
(ANC) y modo comparacion A/B ("switch de percepcion").
📂 [Ver documentacion →](modelo2-indoor/)

## Regulatorio

> ⚠️ Declaracion del autor, **no validada legalmente**. Verificar con la
> autoridad competente (SUBTEL) antes de cualquier distribucion comercial.

| Norma (Chile) | Consideracion |
| :--- | :--- |
| Ley 18.168 | Receptor pasivo; Modelo 2 opera solo en rango audible |
| Ley 21.720 (2024) | Ningun artefacto es dispositivo de interferencia |
| Res. Ex. N 403/2008 SUBTEL | El sistema mide contra limites; no los genera |
| Ley 19.300 | Referencia al principio precautorio |

## Instalacion

### Modelo 1
```bash
cd modelo1-jardin/firmware
pip install -r requirements.txt
python hub_central.py
```

### Modelo 2
```bash
cd modelo2-indoor/firmware
pip install -r requirements.txt
python hub_mesh.py
```

## Presupuesto

| Item | Costo estimado (CLP) | Estado |
| :--- | :--- | :--- |
| Modelo 1 (BOM completo) | Por definir | En desarrollo |
| Modelo 2 (8 nodos + hub) | Por definir | En desarrollo |

## Licencias

- Documentacion: [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt)
- Hardware: [CERN-OHL-S 2.0](LICENSES/CERN-OHL-S-2.0.txt)
- Software: [GPL-3.0](LICENSES/GPL-3.0.txt)

---
**Estado:** estructura inicial / en desarrollo.
Autor: Hans Knaak Ugas.
