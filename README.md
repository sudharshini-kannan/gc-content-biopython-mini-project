# GC Content Calculator (Biopython)

This mini project reads many DNA sequences from a FASTA file and calculates the GC content (%) and length for each sequence using Biopython. The results are saved to a CSV file so they can be opened in Excel or used for further analysis. [web:27][web:29][web:35]

## Project goal

- Input: FASTA file with one or more gene sequences.
- Output: CSV table with:
  - sequence ID
  - sequence length
  - GC content in percent.

This is a simple bioinformatics task that shows how to use Biopython for sequence handling.

## Folder structure

- `data/`
  - `genes.fasta` – input FASTA file with DNA sequences.
  - `gc_results.csv` – output file created by the script.
- `src/`
  - `gc_content_calculator.py` – main Python script.

## Requirements

- Python 3
- Biopython
- pandas

Install the dependencies:

```bash
pip install biopython pandas
