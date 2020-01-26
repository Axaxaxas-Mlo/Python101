import random

class player():
    def __init__ (self, HP):
        self.HP = HP

    def powerUp(self):
        if int(self.HP) < 1:
            print('ya estas muerto')
        elif int(self.HP) > 100:
            print('ya llegaste al limite (HP = %s)' %str(self.HP))
        else:
            self.HP += random.randint(1,20)
            print('ahora tienes',str(self.HP),'de vida\n\n')

    def takeDamage(self):
        self.HP -= random.randint(1,10)
        if int(self.HP) > 0:
            print('ahora tienes',str(self.HP),'de vida\n\n')
        else:
            print('ya estas muerto')
            
    def tellHealth(self):
        print('Tienes',str(self.HP),'de vida\n\n')


HP = int(input ('Inicio del juego, define la vida inicial de tu jugador \n\n'))
player1 = player(HP)

while True:
    accion = int(input('\npresiona 1 para subir de vida \n 2 para tomar dano \n 3 para ver tu vida \n\n'))
    if accion == 1:
        player1.powerUp()
    elif accion == 2:
        player1.takeDamage()
    elif accion == 3:
        player1.tellHealth()
    else:
        print('Esa accion no esta reconocida, intenta de nuevo \n\n')