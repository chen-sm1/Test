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
        z.append(ai.display())
    for j in ['J','Q','K']:
        aj=card(j,n)
        z.append(ai.display())
z.append(('king','small'))
z.append(('king','big'))
print(z)

