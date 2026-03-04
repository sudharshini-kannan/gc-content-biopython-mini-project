from pathlib import Path
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd

# Find the project and data folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FASTA_FILE = DATA_DIR / "genes.fasta"
OUTPUT_CSV = DATA_DIR / "gc_results.csv"


records = []

# Go through each sequence in the FASTA file
for record in SeqIO.parse(str(FASTA_FILE), "fasta"):
    seq_id = record.id
    seq = record.seq
    gc_frac = gc_fraction(seq)          # GC as 0–1
    gc_percent = round(gc_frac * 100, 2)

    records.append({
        "id": seq_id,
        "length": len(seq),
        "gc_percent": gc_percent,
    })

# Turn list into a table and save
df = pd.DataFrame(records)
df.to_csv(OUTPUT_CSV, index=False)

print(df)
print(f"\nSaved results to: {OUTPUT_CSV}")
