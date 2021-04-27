class card:
    def __init__(self,a,b):
        self.num=a
        self.color=b
    def display(self):
        return (self.num,self.color)

z=[]
for n in ['spade','heart','club','diamond']:
    for i in range(1,11):
        ai=card(i,n)
        z.append(ai)
    for j in ['J','Q','K']:
        aj=card(j,n)
        z.append(aj)
z.append(card('king','small'))
z.append(card('king','big'))
y=[i.display() for i in z]

import random
player1=random.sample(z,17)
for i in z:
    for j in player1:
        if j in z:
            z.remove(j)
print(len(z),len(player1))
player2=random.sample(z,17)
for i in z:
    for j in player2:
        if j in z:
            z.remove(j)
player3=random.sample(z,17)
for i in z:
    for j in player3:
        if j in z:
            z.remove(j)
print(len(player1),len(player2),len(player3),len(z))
print([x.display() for x in z])
