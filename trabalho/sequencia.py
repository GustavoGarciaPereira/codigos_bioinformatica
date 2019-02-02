from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

for seq_record in SeqIO.parse("sequencia1.fasta", "fasta"):
	seq1 = seq_record.seq

for seq_record in SeqIO.parse("seq2.fasta", "fasta"):
	seq2 = seq_record.seq



alignments = pairwise2.align.globalms(seq1, seq2,1,-1,-2,0)

for i in range(len(alignments)):
	print(format_alignment(*alignments[i]))

print(alignments)