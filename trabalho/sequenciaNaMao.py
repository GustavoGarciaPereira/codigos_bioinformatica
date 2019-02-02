from Bio import SeqIO


seqq = "GTGGTGGCCTACGAAGGT"
seqw = "GTAGTGCCTTCGAAGGGT"

seq1 = []
seq2 = []





#for seq_record in SeqIO.parse("sequencia1.fasta", "fasta"):
#	seq1 = seq_record.seq

#for seq_record in SeqIO.parse("sequencia2.fasta", "fasta"):
#	seq2 = seq_record.seq

#seqc = []

#for i in range(len(seq1)):
#	seqc+=seq2[i]

#calcula pontuação nomal

#calcula a pontuação de acordo com as familias
#calcula_pontuacao_familias(seq1, seq2)


calcula_pontuacao_nomal(seq1, seq2)       #com a base teste o esperado como resposta é 4
calcula_pontuacao_familias(seq1, seq2)	  #com a base teste o esperado como resposta é 8

flag = True

for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		#print("i")
		f=3
	elif (seq1[i] =='A' and seq2[i]=='G')or(seq1[i] =='G' and seq2[i]=='A')or(seq1[i] =='T' and seq2[i]=='C')or(seq1[i] =='C' and seq2[i]=='T')or(seq1[i] =='A' and seq2[i]=='T')or(seq1[i] =='T' and seq2[i]=='A'):
		#print("P")
		f=3
	else:
		if flag:
			seq2.insert(i,'-')
			flag=False
		else:
			seq1.insert(i,'-')
			flag=True

calcula_pontuacao_espasos(seq1, seq2)    #com a base teste o esperado como resposta é 9