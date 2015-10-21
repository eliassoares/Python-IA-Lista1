import sys
from pacMaze import PacMaze

#print sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
pac = PacMaze(sys.argv[2])
estado = (int(sys.argv[3]), int(sys.argv[4]))
funcaoChamada = int(sys.argv[1])

if(funcaoChamada == 1):
	sucessores = pac.sucessor(estado)
	saida = ""
	for sucessor in sucessores:
		saida += "(" + sucessor[0] + ";" + str(sucessor[1]) + "," + str(sucessor[2]) + ") "
	print saida[ : len(saida) - 1]

elif(funcaoChamada == 2):	#Expande:
	custo = int(sys.argv[5])
	expande = pac.expande((custo, estado, None, None))
	saida = ""
	for i in expande:
		saida += "(" + i[2] + ";"+ str(i[1][0]) + "," + str(i[1][1]) + ";" + str(i[0]) + ";" + str(i[3][0]) + "," + str(i[3][1]) + ") "
	print saida[ : len(saida) - 1]

elif(funcaoChamada == 3):	#BSF:
	solucao = pac.solucaoBFS((0, estado, None, None))
	print solucao

elif(funcaoChamada == 4):	#DFS:
	solucao = pac.solucaoDFS((0, estado, None, None))
	print solucao

elif(funcaoChamada == 5):
	solucao = pac.solucaoAStar((0, estado, None, None))
	print solucao
elif(funcaoChamada == 6):	#Debug:
	pac.mostraMundo()

elif(funcaoChamada == 7):	#Mostra BSF Passo a Passo:
	pac.mostraPassoAPasso((0, estado, None, None), 1)

elif(funcaoChamada == 8):	#Mostra DSF Passo a Passo:
	pac.mostraPassoAPasso((0, estado, None, None), 2)

elif(funcaoChamada == 9):	#Mostra A* Passo a Passo:
	pac.mostraPassoAPasso((0, estado, None, None), 8)

else:
	print "Nunca deveria ter chegado aqui!!!"