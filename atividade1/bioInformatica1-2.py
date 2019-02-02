from Bio.Seq import Seq

def verificaSequ(Seq):
	for i in Seq:
		if i =="T":
			print("DNA")
			break
		elif i=="U":
			print("RNA")
			break


Seq1 = "ACTGAACCGGTTTTCCAAGGTTCCAAGGAACCGGTTAGCT"

Seq2 = "ACUGAACCGGUUUUCCAAGGUUCCAAGGAACCGGUUACUG"

print(Seq1)
verificaSequ(Seq1)
print("")
print(Seq2)
verificaSequ(Seq2)


