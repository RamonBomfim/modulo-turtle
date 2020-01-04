#Escopo de importações
from turtle import *
from time import sleep
from random import randint

#Escopo de funções e classes
# -- classe tartaruga
class Tartaruga(Turtle):
	#construtor
	def __init__(self, numero, cor, x,y):
		super().__init__()
		
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.color(cor)
		self.setpos(x,y)
		self.shape('turtle')
		self.shapesize(2)
		self.pendown()
		self.showturtle()
		self.numero = numero #id da tartaruga
		
	#função correr	
	def correr(self, x, y):
		self.goto(x,y)

#Escopo de variáveis globais
x = -220
y = 160
cores = ['red', 'yellow', 'blue', 'gray', 'green']
tartarugas = []



#criando janela
janela = Screen()
janela.setup(500, 400)
janela.title('Corrida de Tartarugas')
janela.bgcolor('white')

#criando linha de chegada
linha = Turtle()
linha.hideturtle()
linha.penup()
linha.speed(0)
linha.setposition(235,195)
linha.color('red')
linha.width(2)
linha.pendown()
linha.goto(235,-195)

#criando as tartarugas
for i in range(5):
	tartarugas.append(Tartaruga(i, cores[i], x,y))
	y -= 75
	
#loop do jogo
while True:
	if tartarugas[0].xcor() >= 200 or tartarugas[1].xcor() >= 200 or tartarugas[2].xcor() >= 200 or tartarugas[3].xcor() >= 200 or tartarugas[4].xcor() >= 200:
		break
	else:
		for i in range(len(tartarugas)):
			tartarugas[i].correr(tartarugas[i].xcor() + randint(0, 5), tartarugas[i].ycor())
			print(f'{tartarugas[i].numero} = {tartarugas[i].xcor()}')

janela.mainloop()
