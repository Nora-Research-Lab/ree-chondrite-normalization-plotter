![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# REE Chondrite Normalization Plotter
 
*For geochemists and petrologists: enter whole-rock rare-earth-element concentrations in ppm and instantly get a chondrite-normalized spider plot plus Ce and Eu anomaly ratios.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geochemistry
 
This tool performs deterministic rare-earth-element (REE) normalization for whole-rock geochemical data. (a) The user provides 14 numeric inputs, all in ppm, for La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, and Lu. Missing or zero values are treated as invalid and should show a warning instead of a plot. (b) The core logic uses built-in CI chondrite reference values from Sun and McDonough 1989: La 0.237, Ce 0.613, Pr 0.0928, Nd 0.457, Sm 0.148, Eu 0.0563, Gd 0.199, Tb 0.0361, Dy 0.246, Ho 0.0546, Er 0.160, Tm 0.0247, Yb 0.161, Lu 0.0246. For each element, normalized value = input_ppm / chondrite_ppm. Anomaly ratios are computed as Ce/Ce* = Ce_N / sqrt(La_N * Pr_N) and Eu/Eu* = Eu_N / sqrt(Sm_N * Gd_N). (c) The Gradio interface shows a single-screen layout with 14 Number inputs grouped in rows and labelled by element symbol and ppm, a Submit button, a line plot, a data table, and a download button. (d) Outputs are a matplotlib line chart with elements ordered from La to Lu on the x-axis, normalized values on a log-scale y-axis, a horizontal reference line at 1, plus a table showing element, input ppm, and normalized value. Ce/Ce* and Eu/Eu* are displayed as text. A CSV file of the table is available for download. (e) No AI/ML component is used; the logic is a clean geochemical normalization and ratio calculation.
 
## Run it
 
```bash
docker build -t ree-chondrite-normalization-plotter .
docker run -p 7860:7860 ree-chondrite-normalization-plotter
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-19.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
