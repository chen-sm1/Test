class card:                          #定义一个卡牌类
    def __init__(self,a,b):          #初始属性：数字与花色
        self.num=str(a)
        self.color=b
    def display(self):               #显示实例的数字与花色
        return (self.num,self.color)

all_card=[]                          #all_card列表存放总的卡牌
for n in ['spade','heart','club','diamond']:          
    for i in range(1,11):            #添加数字1-10(四种花色)到all_card
        x=card(i,n)
        all_card.append(x)           #添加'J' 'Q' 'K'(四种花色)到all_card
    for j in ['J','Q','K']:
        x=card(j,n)
        all_card.append(x)
all_card.append(card('king','small'))   #添加大小王到all_card
all_card.append(card('king','big'))
y=[i.display() for i in all_card]

import random
player1=random.sample(all_card,17)      #从all_card中随机抽取17张卡牌，放到player1中
for i in all_card:                      #从all_card中删除被抽取的卡牌     
    for j in player1:
        if j in all_card:
            all_card.remove(j)

player2=random.sample(all_card,17)      #继续抽取卡牌，放到player2和player3中
for i in all_card:
    for j in player2:
        if j in all_card:
            all_card.remove(j)
player3=random.sample(all_card,17)
for i in all_card:
    for j in player3:
        if j in all_card:
            all_card.remove(j)

dizhu=random.randint(1,3)               #随处抽取一名玩家为地主
if dizhu==1:
    player1+=all_card                   #若玩家为地主，获得all_card中的地主牌
    print('player1是地主')
elif dizhu==2:
    player2+=all_card
    print('player2是地主')
else:
    player3+=all_card
    print('player3是地主')

player1_display=[x.display() for x in player1]      #用列表显示三个玩家的卡牌
player2_display=[x.display() for x in player2]
player3_display=[x.display() for x in player3]

def sortcard(n):                #卡牌排序
    a=[];b=[];c=[];d=[]
    for x in n:
        if x[0]=='10':          #调用sorted时,'10'<'1',故将'10'转换为'99',使卡牌'10'满足 '10'>'1'
            x=list(x)           #后续再把卡牌中的'99'转换为'10'
            x[0]='99'
            x=tuple(x)
        if x[0]=='K':           #调用sorted时，'K'<'J'<'Q',将'K'转换为'k',使卡牌'K'满足'J'<'Q'<'K'
            x=list(x)           #后续再把卡牌中的'k'转换为'K'
            x[0]='k'
            x=tuple(x)
        if x[1]=='spade':       #将四种花色的卡牌分别放入a,b,c,d
            a.append(x)
        elif x[1]=='heart':
            b.append(x)
        elif x[1]=='club':
            c.append(x)
        else:                   #d中除了'diamond'花色的卡牌，还有大小王
            d.append(x)
    a=sorted(a)                 #a,b,c,d分别进行排序
    b=sorted(b)
    c=sorted(c)
    d=sorted(d)
    n=a+b+c+d

    for x in n:
        if x[0]=='99':          #将卡牌'10'转换为原来的数值
            location=n.index(x)
            x=list(x)
            x[0]='10'
            x=tuple(x)
            n[location]=x
        if x[0]=='k':           #将卡牌'K'转换为原来的数值
            location=n.index(x)
            x=list(x)
            x[0]='K'
            x=tuple(x)
            n[location]=x
        if x[0]=='king':        #将大小王放在n列表的最后
            n.remove(x)
            n.append(x)
            
    print(n,end='\n\n')

sortcard(player1_display)       #按顺序打印三个玩家的卡牌
sortcard(player2_display)
sortcard(player3_display)

print(len(player1_display),len(player2_display),len(player3_display))       #打印三个玩家的卡牌数
