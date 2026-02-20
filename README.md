# Discrete Wronskian Stability of Prime Gaps

**Titan Project — Paper XI**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

We introduce the **discrete Wronskian compression ratio** $q_W$ for prime gaps: for a gap of length $g$ starting at prime $p$, $q_W$ measures how much the $g-1$ consecutive composites share prime factors.

**Key finding:** While gap lengths grow with $\log^2 p$ (Cramér heuristic), the compression $q_W$ does *not* grow. It decays from ~1.6 for small gaps and stabilizes in the band **[1.30, 1.43]** for all 12 record gaps with $g \geq 36$ up to $10^7$.

This stabilization is reported as an empirical phenomenon and open problem. No claims involving the ABC conjecture are made.

## Repository Structure

```
├── paper/
│   ├── Cramer_Wronskian.tex       # LaTeX source (6 pages)
│   └── Cramer_Wronskian.pdf       # Compiled PDF
├── scripts/
│   └── cramer_wronskian_scanner.py  # Record gap scanner
├── data/
│   └── record_gaps.csv            # All 18 record gaps up to 10^7
├── LICENSE
└── README.md
```

## Quick Start

```bash
pip install sympy
python scripts/cramer_wronskian_scanner.py --limit 10000000
```

## Companion Papers (Titan Project)

| # | Title | Link |
|---|-------|------|
| VIII | Legendre's Conjecture in Function Fields | [Zenodo:18705744](https://zenodo.org/records/18705744) |
| IX | Quadratic Residue Asymmetry in Legendre Intervals | [Zenodo:18706876](https://zenodo.org/records/18706876) |
| X | Oppermann's Parity Law | [Zenodo:18707265](https://zenodo.org/records/18707265) |
| **XI** | **Wronskian Stability of Prime Gaps (this repo)** | Zenodo (forthcoming) |

## Citation

```bibtex
@article{chen2026wronskian,
  author  = {Ruqing Chen},
  title   = {The Discrete Wronskian Stability of Prime Gaps: Empirical Observations near the Cram\'er Limit},
  year    = {2026},
  note    = {Titan Project Paper XI}
}
```

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
