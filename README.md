# GC Content Calculator (Biopython)

This mini project reads multiple DNA sequences from a FASTA file and calculates the GC content (%) and length for each sequence using Biopython. The results are saved as a CSV table and a GC% histogram plot, which are common first steps in sequence quality checks and exploratory genomics analysis. [web:27][web:36][web:85][web:87]

## Project goal

- Input: one FASTA file containing one or more DNA sequences (genes, contigs, etc.).
- Output:
  - A CSV file with sequence ID, length, GC percent, and a GC‑rich flag.
  - A PNG image showing the distribution of GC% across all sequences.

This project shows how to combine Biopython, pandas, and matplotlib to perform simple, reproducible bioinformatics analysis in Python. [web:27][web:85][web:87]

## Folder structure

- `data/`
  - `genes.fasta` – input FASTA file with DNA sequences.
  - `gc_results.csv` – output table (created by the script).
- `plots/`
  - `gc_percent_histogram.png` – histogram of GC% for all sequences.
- `src/`
  - `gc_content_calculator.py` – main Python script.

## Requirements

- Python 3
- Biopython (for sequence parsing and GC calculation) [web:27][web:36][web:85]
- pandas (for tabular data handling) [web:87][web:89]
- matplotlib (for plotting the GC% histogram) [web:75][web:87]

Install the dependencies:

```bash
pip install biopython pandas matplotlib

## Why this project is useful

- Demonstrates practical use of Biopython for real DNA sequence handling, not just toy examples. [page:1][web:24]
- Produces ready-to-use CSV tables and a GC% histogram, which are common first steps in genomics QC and gene analysis. [page:1][web:75][web:79]
- Includes a simple command-line interface so it can be integrated into larger pipelines or scripts.

