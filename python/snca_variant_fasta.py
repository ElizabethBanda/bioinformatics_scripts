"""
This script was used to define SNCA missense variants by amino acid substitution.
Objective: Generate FASTA sequences of SNCA variants from a reference protein sequence for structural analysis
Dependencies: Python & Biopython
Output: FASTA file containing one sequence per variant.
"""


# Import required SeqIO modules
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# The wildtype sequence is defined as a string and obtained from UniProt Accession: P37840
wildtype_seq = (
    "MDVFMGKSLGAKEGVAATEKTQGVAEAGKTKGVLYGSKTKEGVHGVAYTAEKTKEQVNTVG"
    "GAVTGVTAKQVTGEAGSIAAATGFWKDQLGKNEEGAEOPDPEA"
)

# Create SeqRecord objects for each sequence and set the id to the variant name
records = [
    SeqRecord(
        Seq(wildtype_seq),
        id="SNCA_Wildtype",
        description=""
    ),
    # A30P Variant (Alanine to Proline at position 30)
    SeqRecord(
        Seq(wildtype_seq.replace("AAG", "APG")),
        id="SNCA_A30P",
        description=""
    ),
    # A53T Variant (Alanine to Threonine at position 53)
    SeqRecord(
        Seq(wildtype_seq.replace("GVA", "GVT")),
        id="SNCA_A53T",
        description=""
    ),
    # H50Q Variant (Glutamic Acid to Lysine at position 50)
    SeqRecord(
        Seq(wildtype_seq.replace("GVH", "QVH")),
        id="SNCA_H50Q",
        description=""
    ),
    # E46K Variant (Glutamic Acid to Lysine at position 46)
    SeqRecord(
        Seq(wildtype_seq.replace("KTKE", "KTKK")),
        id="SNCA_E46K",
        description=""
    ),
    # G51D Variant (Glycine to Aspartic Acid at position 51)
    SeqRecord(
        Seq(wildtype_seq.replace("VHG", "VHD")),
        id="SNCA_G51D",
        description=""
    )
]

# Write the sequences to one FASTA file and each sequence in one line
with open("SNCA_variants.fasta", "w") as output_file:
    for record in records:
        output_file.write(f">{record.id}\n{str(record.seq)}\n")
