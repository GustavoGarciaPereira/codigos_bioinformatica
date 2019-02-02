from Bio import SeqIO

seqq = "GTGGTGGCCTACGAAGGT"
seqw = "GTAGTGCCTTCGAAGGG"

seq1 = []
seq2 = []

for i in range(len(seqq)):
	seq1.append(seqq[i])

for i in range(len(seqw)):
	seq2.append(seqw[i])

def calcula_pontuacao_normal(seq1, seq2):
	cont = 0

	if seq1>seq2:
		x=len(seq2)
	else:
		x=len(seq1)

	for i in range(x):
		if seq1[i] == seq2[i]:
			cont +=1
			#print("iguamal      seq1{} seq2{} cont{}".format(seq1[i],seq2[i],cont))
		else:
			cont -=1
			#print("diferente      seq1{} seq2{} cont{}".format(seq1[i],seq2[i],cont))
		
	print("calcula_pontuacao_nomal >>>>   cont",cont)

def calcula_pontuacao_familias(seq1, seq2):
	cont = 0
	#a-g
	#c-t
	if seq1>seq2:
		x=len(seq2)
	else:
		x=len(seq1)

	for i in range(x):
		if seq1[i] == seq2[i]:
			cont +=1
			#print("iguamal      seq1{} seq2{} cont{}".format(seq1[i],seq2[i],cont))
		elif (seq1[i] =='A' and seq2[i]=='G')or(seq1[i] =='G' and seq2[i]=='A')or(seq1[i] =='T' and seq2[i]=='C')or(seq1[i] =='C' and seq2[i]=='T'):
			#print("familias iguais      seq1{} seq2{} cont{}".format(seq1[i],seq2[i],cont))
			cont+=0
		else:
			cont -=1
			#print("familias diferente      seq1{} seq2{} cont{}".format(seq1[i],seq2[i],cont))

	print("calcula_pontuacao_familias >>>> cont",cont)

def calcula_pontuacao_espasos(seq1, seq2):
	cont = 0

	if seq1>seq2:
		x=len(seq2)
	else:
		x=len(seq1)

	for i in range(x):
		if seq1[i] == seq2[i]:
			cont +=1
		elif seq1[i] == '-' or seq2[i] == '-':
			cont -=2
		else:
			cont -=1
			
	print("calcula_pontuacao_espasos >>>> cont",cont)

calcula_pontuacao_normal(seq1, seq2)       #com a base teste o esperado como resposta é 4
calcula_pontuacao_familias(seq1, seq2)	  #com a base teste o esperado como resposta é 8

flag = True

for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		#print("i")
		f=0
	elif (seq1[i] =='A' and seq2[i]=='G')or(seq1[i] =='G' and seq2[i]=='A')or(seq1[i] =='T' and seq2[i]=='C')or(seq1[i] =='C' and seq2[i]=='T')or(seq1[i] =='A' and seq2[i]=='T')or(seq1[i] =='T' and seq2[i]=='A'):
		#print("P")
		f=0
	else:
		if flag:
			seq2.insert(i,'-')
			flag=False
		else:
			seq1.insert(i,'-')
			flag=True

calcula_pontuacao_espasos(seq1, seq2)    #com a base teste o esperado como resposta é 9