from Bio import SeqIO

seq = []

for seq_record in SeqIO.parse("teste.fasta", "fasta"):
    #print(seq_record.seq)
	seq = seq_record.seq
    #print(repr(seq_record.seq))
    #print(len(seq_record))



# for i in range(0,len(seq)):
# 	#print("po>",i)
# 	if seq[i]!='A' and seq[i]!='C' and seq[i]!='G'and seq[i]!='T':
# 		print("po>",i)
# 		print(seq[i])

contA = 0
contC = 0
contT = 0
contG = 0
contL = 0

baseNaovalida = []

for i in range(0,len(seq)):
	if seq[i]=='A':
		contA+=1
	elif seq[i]=='C':
		contC+=1
	elif seq[i]=='G':
		contG+=1
	elif seq[i]=='T':
		contT+=1
	else:
		contL+=1
		#baseNaovalida.append(seq[i])
		if not(seq[i] in baseNaovalida):
			baseNaovalida.append(seq[i])

		print("po>",i)
		print(seq[i])
print("C A",contA)
print("C C",contC)
print("C G",contG)
print("C T",contT)
print("C L",contL)
print("Soma Das Bases: {}\nSoma Das Bases + base não definida: {}".format((contA+contT+contG+contC),(contA+contT+contG+contC+contL)))
for i in baseNaovalida:
	if i == 'W':
		print("A ou T")
print("base não valida: ",baseNaovalida)
