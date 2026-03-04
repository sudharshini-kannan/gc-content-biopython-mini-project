from pathlib import Path
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Base project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
PLOTS_DIR = PROJECT_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)


def run_gc_analysis(input_fasta: Path, output_csv: Path):
    """Read sequences from FASTA, compute GC%, save CSV and plot."""
    records = []

    # Read each sequence from FASTA
    for record in SeqIO.parse(str(input_fasta), "fasta"):
        seq_id = record.id
        seq = record.seq
        gc_frac = gc_fraction(seq)          # 0–1 GC fraction [web:27][web:29]
        gc_percent = round(gc_frac * 100, 2)

        records.append(
            {
                "id": seq_id,
                "length": len(seq),
                "gc_percent": gc_percent,
            }
        )

    # Make table
    df = pd.DataFrame(records)

    # Mark GC‑rich sequences (GC >= 60%)
    df["gc_rich"] = df["gc_percent"] >= 60.0

    # Save table to CSV
    df.to_csv(output_csv, index=False)

    # Plot GC% histogram
    plt.figure()
    df["gc_percent"].hist(bins=20)
    plt.xlabel("GC percent")
    plt.ylabel("Number of sequences")
    plt.title("GC% distribution")
    plot_path = PLOTS_DIR / "gc_percent_histogram.png"
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close()

    # Print summary to terminal
    print(df)
    print("\nGC‑rich sequences (GC >= 60%):")
    print(df[df["gc_rich"]])
    print(f"\nSaved results to: {output_csv}")
    print(f"GC% histogram saved to: {plot_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate GC% for sequences in a FASTA file and save results to CSV."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default=str(DATA_DIR / "genes.fasta"),
        help="Path to input FASTA file (default: data/genes.fasta)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=str(DATA_DIR / "gc_results.csv"),
        help="Path to output CSV file (default: data/gc_results.csv)",
    )

    args = parser.parse_args()  # parse command-line options [web:82][web:84]

    run_gc_analysis(Path(args.input), Path(args.output))
