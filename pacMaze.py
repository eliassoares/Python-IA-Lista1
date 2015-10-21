import math
import heapq

class PacMaze(object):	
	#No = (acao, (no atual), custo, (pai))
	def __init__(self, fileName):
		info = self.__readFile(fileName)
		self.lines = info[0][0]
		self.collunm = info[0][1]
		self.world = info[1]
		self.fronteira = []
		self.__pontoSolucao = None
		self.explorados = []
		self.caminho = []
		for i in range(0, self.lines):
			aux1 = []
			aux2 = []
			for j in range(0, self.collunm):
				aux1.append(False)
				aux2.append(None)
			self.explorados.append(aux1[:])
			self.caminho.append(aux2[:])
		
		
	def __readFile(self,fileName):
		fil = open(fileName,"r")
		world = []
		lines = 0
		collunm = 0
		i = 0
		for line in fil:
			if(i == 0):
				lines = int(line.split(" ")[0])
				collunm = int(line.split(" ")[1])
				i += 1
			else:
				posicaoPastilha = line.find("0")
				if(posicaoPastilha > -1):
					#Para poder calcular a heuristica:
					self.linhaPastilha = i - 1
					self.colunaPastilha = posicaoPastilha
				world.append(line)
				i += 1

		return (lines, collunm), world

	def sucessor(self,estado):
		estados = []
		#cima, baixo, direita e esquerda
		possibilidades = [False, False, False, False]
		if(((estado[0] - 1) > 0) and (self.world[estado[0] - 1][estado[1]] != "#")): 
			possibilidades[0] = True
		if(((estado[0] + 1) < (self.lines -1)) and (self.world[estado[0] + 1][estado[1]] != "#")): 
			possibilidades[1] = True
		if(((estado[1] + 1) < (self.collunm) -1) and (self.world[estado[0]][estado[1] + 1] != "#")): 
			possibilidades[2] = True
		if(((estado[1] - 1) > 0) and (self.world[estado[0]][estado[1] - 1] != "#")): 
			possibilidades[3] = True

		if(possibilidades[0]):
			estados.append(("acima", estado[0] - 1, estado[1]))
		if(possibilidades[1]):
			estados.append(("abaixo", estado[0] + 1, estado[1]))
		if(possibilidades[2]):
			estados.append(("direita", estado[0], estado[1] + 1))
		if(possibilidades[3]):
			estados.append(("esquerda", estado[0], estado[1] - 1))

		return estados

	def expande(self, noAtual):
			sucessores = self.sucessor(noAtual[1])
			#print noAtual
			nosSucessores = []
			for sucessor in sucessores:
						 	#custo					estado 				acao		pai
				noFilho = noAtual[0] + 1, (sucessor[1], sucessor[2]),  sucessor[0], noAtual[1]
				nosSucessores.append(noFilho)
			return nosSucessores

	def testaSolucao(self, no):
		if(self.world[no[1][0]][no[1][1]] == "0"):
			return True
		else:
			return False

	def caminhoInverso(self, noInicial, noFinal):
		noAtual = noFinal
		custoTotal = noFinal[0]
		expansoes = 0
		for i in self.explorados:
			for j in i:
				if(j):
					expansoes += 1

		acoes = ""
		#No = (custo, (no atual), acao, (pai))
		while(noAtual != noInicial):
			acoes = noAtual[2] + " " + acoes
			#voltando pelo caminho:
			noAtual = self.caminho[noAtual[3][0]][noAtual[3][1]]
		print "custo:",custoTotal,"expansoes:",expansoes
		return acoes

	#Para debug e visualizacao:
	def mostraPac(self, no):
		aux = []
		for i in self.world:
			j = i[:]
			if(i == self.world[no[1][0]]):
				j = j[:no[1][1]] + "p" + j[no[1][1]+1:]
			aux.append(j)
		return aux

	def mostraPassoAPasso(self, no, algoritmo):
		if(algoritmo == 1):
			saida = self.solucaoBFS(no)
		elif(algoritmo == 2):
			saida = self.solucaoDFS(no)
		else:
			saida = self.solucaoAStar(no)

		saida = saida.split(" ")
		noAtual = self.__pontoSolucao


		i = 0
		aux = []
		while(noAtual != no):
			aux.append(self.mostraPac(noAtual))
			noAtual = self.caminho[noAtual[3][0]][noAtual[3][1]]
		
		print "Inicio: "
		for i in range(len(aux) -1, -1, -1):
			k = ""
			for j in aux[i]:
				print j
			print "\n"
			a = raw_input("Aperte Enter para visualizar o proximo passo.")
			print "\n",saida[len(aux) - i]
		print "Fim!"

	def mostraMundo(self):
		for linha in self.world:
			print linha

	#--------------------------------------------------------------
	# Funcoes do BFS:
	def insereBFS(self, no):
		self.fronteira.append(no)
		self.caminho[no[1][0]][no[1][1]] = no

	def removeBFS(self):
			try:
				primeiro = self.fronteira.pop(0)
				return primeiro
			except ValueError:
				iLovePython = 0

	def insere_listaBFS(self, listaNo):
		for no in listaNo:
			if(self.explorados[no[1][0]][no[1][1]] == False):
				
				#tem que verificar se o no jao nao estar na fronteira:
				naoEsta = True
				for i in self.fronteira:
					if(i[1] == no[1]): # O no ja esta na fronteira:
						naoEsta = False
						break
				if(naoEsta):
					self.fronteira.append(no)
					self.caminho[no[1][0]][no[1][1]] = no

	def solucaoBFS(self, noInicial):
		self.insereBFS(noInicial)

		while(len(self.fronteira) != 0):
			no = self.removeBFS()

			if(self.testaSolucao(no)):
				self.__pontoSolucao = no
				return self.caminhoInverso(noInicial, no)
			
			if(self.explorados[no[1][0]][no[1][1]] == False):
				self.explorados[no[1][0]][no[1][1]] = True
				self.insere_listaBFS(self.expande(no))
			
	#--------------------------------------------------------------
	#Funcoes do DFS:
	def insereDFS(self, no):
		self.fronteira.append(no)
		self.caminho[no[1][0]][no[1][1]] = no

	def removeDFS(self):
		try:
			ultimo = self.fronteira.pop(len(self.fronteira) - 1)
			return ultimo
		except ValueError:
			iLovePython = 0

	def insere_listaDFS(self, listaNo):
		for no in listaNo:
			if(self.explorados[no[1][0]][no[1][1]] == False):
				
				#tem que verificar se o no ja nao estar na fronteira:
				naoEsta = True
				for i in self.fronteira:
					if(i[1] == no[1]): # O no ja esta na fronteira:
						naoEsta = False
						break
				if(naoEsta):
					self.fronteira.append(no)
					self.caminho[no[1][0]][no[1][1]] = no
	
	def solucaoDFS(self, noInicial):
		
		self.insereDFS(noInicial)

		while(len(self.fronteira) != 0):
			no = self.removeDFS()
			
			if(self.testaSolucao(no)):
				self.__pontoSolucao = no
				return self.caminhoInverso(noInicial, no)
			
			if(self.explorados[no[1][0]][no[1][1]] == False):
				self.insere_listaDFS(self.expande(no))
				self.explorados[no[1][0]][no[1][1]] = True


	#--------------------------------------------------------------
	#Funcoes A*:

	def insereAStar(self, no):
		heapq.heappush(self.fronteira, no)
		self.caminho[no[1][1][0]][no[1][1][1]] = no[1]

	def removeAStar(self):
		return heapq.heappop(self.fronteira)

	#Heuristica de movimentos minimos
	def heuristica2(self, no):
		d1 = math.fabs(self.linhaPastilha - no[1][0])
		d2 = math.fabs(self.colunaPastilha - no[1][1])
		return d1+d2

	#Distancia Euclidiana
	def heuristica1(self, no):
		d1 = math.pow((self.linhaPastilha - no[1][0]), 2)
		d2 = math.pow((self.colunaPastilha - no[1][1]), 2)
		return math.sqrt(d1 + d2)

	def solucaoAStar(self, noInicial):
		f = self.heuristica2(noInicial)
		self.insereAStar((f, noInicial))
		aberto = []
		for i in range(0, self.lines):
			aux1 = []
			for j in range(0, self.collunm):
				aux1.append(False)
			aberto.append(aux1[:])

		while(len(self.fronteira) != 0):

			no = self.removeAStar()
			
			if(self.testaSolucao(no[1])):
				self.__pontoSolucao = no[1]
				return self.caminhoInverso(noInicial, no[1])

			self.explorados[no[1][1][0]][no[1][1][1]] = True

			for i in self.expande(no[1]):
				if(not self.explorados[i[1][0]][i[1][1]]):
					if(not aberto[i[1][0]][i[1][1]]):
						g = i[0]
						f = g + self.heuristica2(i)
						aberto[i[1][0]][i[1][1]] = True
						self.insereAStar((f, i))
