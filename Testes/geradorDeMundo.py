import random
import sys

def criaMundo(linhas, colunas):
	mundo = []
	print "linhas:",linhas,"colunas:",colunas
	for i in range(0, linhas):
		aux1 = []
		for j in range(0, colunas):
			if((i == 0) or (i == linhas -1) or (j == 0) or (j == colunas - 1)):
				aux1.append("#")
			else:
				aux1.append("-")
		mundo.append(aux1[:])
	numeroParedes = random.randint(0, (linhas * colunas) - 15)

	print "Preenchendo o mundo com paredes aleatorias."

	for i in range(1, numeroParedes + 1):
		linha = random.randint(1, linhas - 1)
		coluna = random.randint(1, colunas - 1)

		while(mundo[linha][coluna] == "#"):
			
			linha = random.randint(1, linhas - 1)
			coluna = random.randint(1, colunas - 1)
		mundo[linha][coluna] = "#"
	pastilhaL = random.randint(1, linhas - 2)
	pastilhaC =random.randint(1, colunas - 2)
	mundo[pastilhaL][pastilhaC] = "0"
	return mundo

linhas = random.randint(5,30)
colunas = random.randint(5,30)
mundo = criaMundo(linhas, colunas)

saida = open(sys.argv[1], "w")

string = str(linhas) + " " + str(colunas)
saida.write(string + "\n")

for i in mundo:
	string = ""
	for j in i:
		string += j
	saida.write(string + "\n")
saida.close()