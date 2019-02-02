from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment



seqq = "GTGGTGGCCTACGAAGGT"
seqw = "GTAGTGCCTTCGAAGGGT"

seq11 = []
seq22 = []


#for seq_record in SeqIO.parse("sequencia1.fasta", "fasta"):
#	seq1 = seq_record.seq

#for seq_record in SeqIO.parse("seq2.fasta", "fasta"):
#	seq2 = seq_record.seq

#for i in range(len(seq1)):
#	seq11.append(seq1[i])

#for i in range(len(seq2)):
#	seq22.append(seq2[i])




# seqc = []
# for i in range(len(seq1)):
# 	seqc+= seq2[i]
	

#calcula pontuação nomal

#calcula a pontuação de acordo com as familias
#calcula_pontuacao_familias(seq1, seq2)
#print("!",len(seqc))

alignments = pairwise2.align.globalms(seqq, seqw,1,-1,-2,0)

print(alignments)
for i in range(len(alignments)):
	print(format_alignment(*alignments[i]))
# print(len(seq1))
# print(len(seq2))
# print(len(seqc))

# flag = True

# print(flag)

# for i in range(len(seqc)):
# 	if seq2[i] != seqc[i]:
# 		flag = False
# print(flag)
