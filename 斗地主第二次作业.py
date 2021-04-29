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
            
    return n

player1_display=sortcard(player1_display)       #将player1,2,3分别进行排序
player2_display=sortcard(player2_display)
player3_display=sortcard(player3_display)
print(player1_display,player2_display,player3_display,sep='\n\n')
print(len(player1_display),len(player2_display),len(player3_display))       #打印三个玩家的卡牌数

def playcard(n):                                #定义函数playcard(n),若输入的卡牌位于n中，将n中这些卡牌删除
    out=[]                                      #用out列表存储成功输入的卡牌
    for x in outcard:                           #遍历输入的卡牌
        for i in n:                             #遍历n
            if x==i[0]:
                out.append(i)
                n.remove(i)
                break
            if x=='kingbig':
                if ('king','big') in n:
                    out.append(('king','big'))
                    n.remove(('king','big'))
            if x=='kingsmall':
                if ('king','small') in n:
                    out.append(('king','small'))
                    n.remove(('king','small'))
    print(out,end='\n\n')                       #打印打出的牌
    print(n,end='\n\n')                         #打印剩余的牌
    print(len(out),len(n))

if dizhu==2:                                    #分情况处理不同地主时的情况
    print('player2是地主')
    print('player2出牌 ')
    outcard=[]                                  #outcard存储所有输入的卡牌
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':                            #输入end时退出循环
            break
    playcard(player2_display)                   #打印出成功打出的卡牌及player2剩余的卡牌
    print('player3出牌 ')                       #同上
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            break
    playcard(player3_display)

if dizhu==3:
    print('player3是地主')
    print('player3出牌: ')
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            break
    playcard(player3_display)

if dizhu==1:
    print('player1是地主')

while 1:                                        #定义出牌顺序，按player1-player2-player3的顺序出牌          
    for pointer in range(1,4):                  #通过改变pointer的值来轮换到下一个玩家
        if pointer==1:
            print('player1出牌 ')
            outcard=[]                          #outcard存储所有输入的卡牌
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':                    #输入end时退出循环
                    break
            playcard(player1_display)           #打印出成功打出的卡牌及player2剩余的卡牌
        if pointer==2:
            print('player2出牌 ')
            outcard=[]
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':
                    break
            playcard(player2_display)
        if pointer==3:
            print('player3出牌 ')
            outcard=[]
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':
                    break
            playcard(player2_display)    
            