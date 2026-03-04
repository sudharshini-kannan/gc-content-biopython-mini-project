from pathlib import Path
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt  # new


# Find the project and data folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
PLOTS_DIR = PROJECT_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)


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

# Mark GC‑rich sequences (GC >= 60%)
df["gc_rich"] = df["gc_percent"] >= 60.0

# Save table
df.to_csv(OUTPUT_CSV, index=False)

# --- Plot GC% histogram ---
plt.figure()
df["gc_percent"].hist(bins=20)
plt.xlabel("GC percent")
plt.ylabel("Number of sequences")
plt.title("GC% distribution")
plot_path = PLOTS_DIR / "gc_percent_histogram.png"
plt.savefig(plot_path, dpi=150, bbox_inches="tight")
plt.close()
# ---------------------------

print(df)
print("\nGC‑rich sequences (GC >= 60%):")
print(df[df["gc_rich"]])
print(f"\nSaved results to: {OUTPUT_CSV}")
print(f"GC% histogram saved to: {plot_path}")

