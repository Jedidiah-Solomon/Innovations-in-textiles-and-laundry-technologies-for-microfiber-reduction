# Microfibre Pollution Review (2020–2025)

This repository contains the code, data files, and visualizations used in the review paper titled:

**“Innovations in Textiles and Laundry Technologies for Microfibre Reduction”**  
Authors: Blessing Odunayo and Jedidiah Solomon  
Date: July 2025

## Summary

This review is based on a comprehensive search and analysis of literature from Web of Science (WOS), Medline, and the Chinese Science Citation Database (CSCD) covering microfibre pollution and mitigation technologies published between January 2020 and July 2025.

We applied keyword-based filtering and deduplication using a Python-based methodology, and visualized trends such as publication years and keyword frequencies.

## Contents

- `/data/` — Raw data files from databases (WOS, Medline, CSCD)
- `/scripts/` — Python scripts used for filtering, cleaning, and visualization
- `/figures/` — Generated charts and graphs (e.g., publication trends)
- `/output/` — Final cleaned datasets (`screened_literature.csv`, `.xlsx`)
- `README.md` — Project overview
- `LICENSE` — MIT License for code

## Methodology Overview

A detailed Python-based filtering script was used to:

- Load and clean literature metadata
- Deduplicate entries by DOI and title
- Apply keyword filtering (`"laundry"`, `"textile"`, `"washing machine"`, etc.)
- Generate publication trend visualizations

## Visualizations

See `/figures/` for visual outputs including:

- Publication trends (2020–2025)
- Keyword frequency distribution

## License

- **Code**: [MIT License](LICENSE)
- **Data, Notebooks, and Figures**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## 🔗 Citation

If you use this work, please cite it properly (see below).
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
