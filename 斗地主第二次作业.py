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
    print('player1是地主',end='\n\n')
elif dizhu==2:
    player2+=all_card
    print('player2是地主',end='\n\n')
else:
    player3+=all_card
    print('player3是地主',end='\n\n')

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

def sortcard2(n):               #将卡牌中的'10','J','Q','K','1','2',('king','small'),('king','big')变成':',';','<','=','>','?',('@','small'),('A','')并排序
    for x in n:                 #转换后，字符的ascii代码比前一个字符的多1，方便后面顺子的编写
        if x[0]=='10':          #调用sorted时,'10'<'1',故将'10'转换为'99',使卡牌'10'满足 '10'>'1'  
            a=n.index(x)
            x=list(x)           #后续再把卡牌中的'99'转换为'10'
            x[0]=':'
            x=tuple(x)
            n[a]=x
        if x[0]=='J':          
            a=n.index(x)
            x=list(x)           
            x[0]=';'
            x=tuple(x)
            n[a]=x
        if x[0]=='Q':          
            a=n.index(x)
            x=list(x)           
            x[0]='<'
            x=tuple(x)
            n[a]=x 
        if x[0]=='K':          
            a=n.index(x)
            x=list(x)          
            x[0]='='
            x=tuple(x)
            n[a]=x
        if x[0]=='1':          
            a=n.index(x)
            x=list(x)           
            x[0]='>'
            x=tuple(x)
            n[a]=x
        if x[0]=='2':          
            a=n.index(x)
            x=list(x)           
            x[0]='?'
            x=tuple(x)
            n[a]=x
        else:                       #若为大小王
            if x[1]=='small':
                a=n.index(x)
                x=list(x)           
                x[0]='@'
                x=tuple(x)
                n[a]=x
            if x[1]=='big':
                a=n.index(x)
                x=list(x)           
                x[0]='A'
                x=tuple(x)
                n[a]=x
        n=sorted(n)


    return n

def sortcard3(n):               #将卡牌中的'10','J','Q','K','1','2',('king','small'),('king','big')恢复原值
    for x in n:
        if x[0]==':':           #将卡牌'10'转换为原来的数值
            location=n.index(x)
            x=list(x)
            x[0]='10'
            x=tuple(x)
            n[location]=x
        if x[0]==';':          
            location=n.index(x)
            x=list(x)
            x[0]='J'
            x=tuple(x)
            n[location]=x
        if x[0]=='<':          
            location=n.index(x)
            x=list(x)
            x[0]='Q'
            x=tuple(x)
            n[location]=x
        if x[0]=='=':           #将卡牌'K'转换为原来的数值
            location=n.index(x)
            x=list(x)
            x[0]='K'
            x=tuple(x)
            n[location]=x
        if x[0]=='>':          
            location=n.index(x)
            x=list(x)
            x[0]='1'
            x=tuple(x)
            n[location]=x
        if x[0]=='?':          
            location=n.index(x)
            x=list(x)
            x[0]='2'
            x=tuple(x)
            n[location]=x
        if x[0]=='@':
            location=n.index(x)
            x=list(x)
            x[0]='king'
            x=tuple(x)
            n[location]=x
        if x[0]=='A':
            location=n.index(x)
            x=list(x)
            x[0]='king'
            x=tuple(x)
            n[location]=x
    return n

player1_display=sortcard3(sortcard2(player1_display))      #将player1,2,3分别进行排序
player2_display=sortcard3(sortcard2(player2_display))
player3_display=sortcard3(sortcard2(player3_display))
print('player1卡牌',player1_display,sep='\n',end='\n\n')
print('player2卡牌',player2_display,sep='\n',end='\n\n')
print('player3卡牌',player3_display,sep='\n',end='\n\n')
print(len(player1_display),len(player2_display),len(player3_display))       #打印三个玩家的卡牌数

def playcard(n):                                #定义函数playcard(n),若输入的卡牌位于n中，将n中这些卡牌删除
    global out
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



def compare(m,n):                      #若return1,n要重新输入
    m=sortcard2(m)
    n=sortcard2(n)
    if not len(m)==len(n):             #如果m和n长度不相等
        if m[0]=='pass':
            return 0
        if n[0][0]=='@' and n[1][0]=='A':       #若n出的卡牌为王炸
            return 0
        if n[0][0]==n[1][0]==n[2][0]==n[3][0]:      #若n出的卡牌为炸弹
            return 0
        
        else:
            return 1
    if len(m)==len(n)==1:
        if m[0]=='pass':
            return 0
        if m[0][0]>n[0][0] or m[0][0]==n[0][0]:
            return 1 
    if len(m)==len(n)==2:                           #两张的情况只有对子和王炸
        if not m[0][0]==m[1][0]:
            return 0
        else:
            if not n[0][0]==n[1][0]:
                return 1
            else:
                if m[0][0]>n[0][0] or m[0][0]==n[0][0]:
                    return 1
    if len(m)==len(n)==3:                           #三张的情况只有三张一样
        if not m[0][0]==m[1][0]==m[2][0]:
            return 0
        else:
            if not n[0][0]==n[1][0]==n[2][0]:
                return 1
            else:
                if m[0][0]>n[0][0]:
                    return 1
    if len(m)==len(n)==4:                           #四张的情况有炸和三带一
        if not (m[0][0]==m[1][0]==m[2][0]==m[3][0] or m[0][0]==m[1][0]==m[2][0] or m[1][0]==m[2][0]==m[3][0]):
            return 0
        else:
            if m[0][0]==m[1][0]==m[2][0]==m[3][0]:
                if not n[0][0]==n[1][0]==n[2][0]==n[3][0]:
                    return 1
                else:
                    if m[0][0]>n[0][0]:
                        return 1
            if m[0][0]==m[1][0]==m[2][0]:
                if not (n[0][0]==n[1][0]==n[2][0] or n[1][0]==n[2][0]==n[3][0]):
                    return 1
                if n[0][0]==n[1][0]==n[2][0]:
                    if m[0][0]>n[0][0]:
                        return 1
                if n[1][0]==n[2][0]==n[3][0]:
                    if m[0][0]>n[1][0]:
                        return 1
            if m[1][0]==m[2][0]==m[3][0]:
                if not (n[1][0]==n[2][0]==n[3][0] or n[0][0]==n[1][0]==n[2][0]):
                    return 1
                if n[0][0]==n[1][0]==n[2][0]:
                    if m[1][0]>n[0][0]:
                        return 1
                if n[1][0]==n[2][0]==n[3][0]:
                    if m[1][0]>n[1][0]:
                        return 1                 
                        
                        #截止到这里，前面代码多检测了m,n的输入是否符合卡牌规则
    if len(m)==len(n)==5:                        #五张的情况有 顺子 和 三带一对
        if (m[0][0]==m[1][0]==m[2][0] and m[3][0]==m[4][0]):    #m的前三张卡牌为三张，后两张为对子
                if not (n[0][0]==n[1][0]==n[2][0] or n[2][0]==n[3][0]==n[4][0]):
                    return 1
                else:
                    if n[0][0]==n[1][0]==n[2][0]:
                        if not n[3][0]==n[4][0]:
                            return 1
                        else:
                            if m[0][0]>n[0][0] or m[0][0]==n[0][0]:
                                return 1
                    if n[2][0]==n[3][0]==n[4][0]:
                        if not n[0][0]==n[1][0]:
                            return 1
                        else:
                            if m[0][0]>n[2][0] or m[0][0]==n[2][0]:
                                return 1     #差m后三位为一样的情况
        if (m[2][0]==m[3][0]==m[4][0] and m[0][0]==m[1][0]):    #m的前两张卡牌为对子，后三张卡牌为三张
                if not (n[0][0]==n[1][0]==n[2][0] or n[2][0]==n[3][0]==n[4][0]):
                    return 1
                else:
                    if n[0][0]==n[1][0]==n[2][0]:
                        if not n[3][0]==n[4][0]:
                            return 1
                        else:
                            if m[2][0]>n[0][0] or m[2][0]==n[0][0]:
                                return 1
                    if n[2][0]==n[3][0]==n[4][0]:
                        if not n[0][0]==n[1][0]:
                            return 1
                        else:
                            if m[2][0]>n[2][0] or m[2][0]==n[2][0]:
                                return 1 
        if ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]):  #m为顺子
            if not (ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
                return 1
            else:
                if m[4][0]>n[4][0] or m[4][0]==n[4][0]:
                    return 1
    if len(m)==len(n)==6:
        if not (ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[5][0]>n[5][0] or m[5][0]==n[5][0]:
                return 1
    if len(m)==len(n)==7:
        if not (ord(n[6][0])-ord(n[5][0])==ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[6][0]>n[6][0] or m[6][0]==n[6][0]:
                return 1
    if len(m)==len(n)==8:
        if not (ord(n[7][0])-ord(n[6][0])==ord(n[6][0])-ord(n[5][0])==ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[7][0]>n[7][0] or m[7][0]==n[7][0]:
                return 1
    if len(m)==len(n)==9:
        if not (ord(n[8][0])-ord(n[7][0])==ord(n[7][0])-ord(n[6][0])==ord(n[6][0])-ord(n[5][0])==ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[8][0]>n[8][0] or m[8][0]==n[8][0]:
                return 1
    if len(m)==len(n)==10:
        if not (ord(n[9][0])-ord(n[8][0])==ord(n[8][0])-ord(n[7][0])==ord(n[7][0])-ord(n[6][0])==ord(n[6][0])-ord(n[5][0])==ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[9][0]>n[9][0] or m[9][0]==n[9][0]:
                return 1
    if len(m)==len(n)==11:
        if not (ord(n[10][0])-ord(n[9][0])==ord(n[9][0])-ord(n[8][0])==ord(n[8][0])-ord(n[7][0])==ord(n[7][0])-ord(n[6][0])==ord(n[6][0])-ord(n[5][0])==ord(n[5][0])-ord(n[4][0])==ord(n[4][0])-ord(n[3][0])==ord(n[3][0])-ord(n[2][0])==ord(n[2][0])-ord(n[1][0])==ord(n[1][0])-ord(n[0][0])):
            return 1
        else:
            if m[10][0]>n[10][0] or m[10][0]==n[10][0]:
                return 1
    m=sortcard3(m)
    n=sortcard3(n)
    print(m,n,sep='\n\n')



def check(m):                           #检查m是否符合卡牌规则. 若符合，返回0与m;否则返回1与m
    m=sortcard2(m)
    if len(m)==1:                       #按卡牌长度进行检查
        m=sortcard3(m)
        return 0,m
    if len(m)==2:
        if not (m[0][0]==m[1][0] or (m[0][0]=='@' and m[1][0]=='A')):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==3:
        if not m[0][0]==m[1][0]==m[2][0]:
            m=sortcard3(m)           
            return 1,m                          #赋值时m,n=check(m)
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==4:
        if not (m[0][0]==m[1][0]==m[2][0]==m[3][0] or m[0][0]==m[1][0]==m[2][0] or m[1][0]==m[2][0]==m[3][0]):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==5:                        #五张的情况有 顺子 和 三带一对
        if not((m[0][0]==m[1][0]==m[2][0] and m[3][0]==m[4][0]) or      #此处注意验证是否会出错
                (m[2][0]==m[3][0]==m[4][0] and m[0][0]==m[1][0]) or
                (ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0])) and (ord(m[4][0])<63)):    #这里ord小于63是因为卡牌‘2’转换成了‘？’，对应的ascii代码为63，而顺子最大不能达到‘2’
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m                    
    if len(m)==6:
        if not (ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[5][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==7:
        if not (ord(m[6][0])-ord(m[5][0])==ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[6][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==8:
        if not (ord(m[7][0])-ord(m[6][0])==ord(m[6][0])-ord(m[5][0])==ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[7][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==9:
        if not (ord(m[8][0])-ord(m[7][0])==ord(m[7][0])-ord(m[6][0])==ord(m[6][0])-ord(m[5][0])==ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[8][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==10:
        if not (ord(m[9][0])-ord(m[8][0])==ord(m[7][0])-ord(m[6][0])==ord(m[6][0])-ord(m[5][0])==ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[9][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m
    if len(m)==11:
        if not (ord(m[10][0])-ord(m[9][0])==ord(m[9][0])-ord(m[8][0])==ord(m[7][0])-ord(m[6][0])==ord(m[6][0])-ord(m[5][0])==ord(m[5][0])-ord(m[4][0])==ord(m[4][0])-ord(m[3][0])==ord(m[3][0])-ord(m[2][0])==ord(m[2][0])-ord(m[1][0])==ord(m[1][0])-ord(m[0][0]) and (ord(m[10][0])<63)):
            m=sortcard3(m)
            return 1,m
        else:
            m=sortcard3(m)
            return 0,m

passcard=0                                      #用passcard记录过牌的次数，passcard能被2整除时，玩家可自由出牌
if dizhu==1:                                    #分情况处理不同地主时的情况
    print('player1出牌 ')
    print('player1卡牌：',player1_display,sep='\n')
    outcard=[]                                  #outcard存储所有输入的卡牌
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':                            #输入end时判断是否符合出牌规则
            playcard(player1_display)           #打印出成功打出的卡牌及player2剩余的卡牌
            player1_out=out
            n,player1_out=check(player1_out)    #n,player2_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player1_out:
                    player1_display.append(x)   #将成功打出的卡牌重新加入player2_display
                print('player1的牌')
                print(player1_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                print('符合出牌规则')
                break
        
    print('player2出牌 ')                       #同上
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            playcard(player2_display)           #打印出成功打出的卡牌及player2剩余的卡牌
            player2_out=out
            n,player2_out=check(player2_out)    #n,player2_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player2_out:
                    player2_display.append(x)
                print('player2的牌')
                print(player2_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                n=compare(player1_out,player2_out)
                if n:
                    print('违反出牌规则')
                    for x in player2_out:
                        player2_display.append(x)
                    print('player2的牌')
                    print(player2_display)
                    outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                    continue
                else:
                    print('符合出牌规则')
                    break
        if a=='pass':
            player2_out=player1_out
            passcard+=1                                 #pass计数加一
            break

    print('player3出牌 ')                       #同上
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            playcard(player3_display)           #打印出成功打出的卡牌及player3剩余的卡牌
            player3_out=out
            n,player3_out=check(player3_out)    #n,player3_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player3_out:
                    player3_display.append(x)
                print('player3的牌')
                print(player3_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                n=compare(player2_out,player3_out)
                if n:
                    print('违反出牌规则')
                    for x in player3_out:
                        player3_display.append(x)
                    print('player3的牌')
                    print(player3_display)
                    outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                    continue
                else:
                    print('符合出牌规则')
                    break
        if a=='pass':
            player3_out=player2_out
            passcard+=1
            break

if dizhu==2:                                    #分情况处理不同地主时的情况
    print('player2是地主')
    print('player2出牌 ')
    outcard=[]                                  #outcard存储所有输入的卡牌
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':                            #输入end时判断是否符合出牌规则
            playcard(player2_display)           #打印出成功打出的卡牌及player2剩余的卡牌
            player2_out=out
            n,player2_out=check(player2_out)    #n,player2_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player2_out:
                    player2_display.append(x)   #将成功打出的卡牌重新加入player2_display
                print('player2的牌')
                print(player2_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                print('符合出牌规则')
                break   

    print('player3出牌 ')                       #同上
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            playcard(player3_display)           #打印出成功打出的卡牌及player3剩余的卡牌
            player3_out=out
            n,player3_out=check(player3_out)    #n,player3_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player3_out:
                    player3_display.append(x)
                print('player3的牌')
                print(player3_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                n=compare(player2_out,player3_out)
                if n:
                    print('违反出牌规则')
                    for x in player3_out:
                        player3_display.append(x)
                    print('player3的牌')
                    print(player3_display)
                    outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                    continue
                else:
                    print('符合出牌规则')
                    break
        if a=='pass':
            player3_out=player2_out
            passcard+=1
            break

if dizhu==3:
    print('player3出牌 ')                       #同上
    outcard=[]
    while 1:
        a=input('请出牌： ')
        outcard.append(a)
        if a=='end':
            playcard(player3_display)           #打印出成功打出的卡牌及player3剩余的卡牌
            player3_out=out
            n,player3_out=check(player3_out)    #n,player3_out收集check函数返回的值
            if n:
                print('违反出牌规则')
                for x in player3_out:
                    player3_display.append(x)
                print('player3的牌')
                print(player3_display)
                outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                continue
            else:
                print('符合出牌规则')
                break
    
while 1:                                        #定义出牌顺序，按player1-player2-player3的顺序出牌          
    for pointer in range(1,4):                  #通过改变pointer的值来轮换到下一个玩家
        if pointer==1:
            print('player1卡牌',player1_display,sep='\n',end='\n\n')
            print('player1出牌 ')                       
            outcard=[]
            if passcard%2==0:
                player3_out=['pass']
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':
                    playcard(player1_display)           #打印出成功打出的卡牌及player1剩余的卡牌
                    player1_out=out
                    n,player1_out=check(player1_out)    #n,player1_out收集check函数返回的值
                    if n:
                        print('违反出牌规则')
                        for x in player1_out:
                            player1_display.append(x)
                        print('player1的牌')
                        print(player1_display)
                        outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                        continue
                    else:
                        n=compare(player3_out,player1_out)
                        if n:
                            print('违反出牌规则')
                            for x in player1_out:
                                player1_display.append(x)
                            print('player1的牌')
                            print(player1_display)
                            outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                            continue
                        else:
                            print('符合出牌规则')
                            break
                if a=='pass':
                    player1_out=player3_out
                    passcard+=1
                    break    
        if pointer==2:
            print('player2卡牌',player2_display,sep='\n',end='\n\n')
            print('player2出牌 ')                       
            outcard=[]
            if passcard%2==0:
                player1_out=['pass']    
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':
                    playcard(player2_display)           #打印出成功打出的卡牌及player2剩余的卡牌
                    player2_out=out
                    n,player2_out=check(player2_out)    #n,player2_out收集check函数返回的值
                    if n:
                        print('违反出牌规则')
                        for x in player2_out:
                            player2_display.append(x)
                        print('player2的牌')
                        print(player2_display)
                        outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                        continue
                    else:
                        n=compare(player1_out,player2_out)
                        if n:
                            print('违反出牌规则')
                            for x in player2_out:
                                player2_display.append(x)
                            print('player2的牌')
                            print(player2_display)
                            outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                            continue
                        else:
                            print('符合出牌规则')
                            break
                if a=='pass':
                    player2_out=player1_out
                    passcard+=1
                    break    
        if pointer==3:
            print('player3卡牌',player3_display,sep='\n',end='\n\n')
            print('player3出牌 ')                       #同上
            outcard=[]
            if passcard%2==0:
                player2_out=['pass']
            while 1:
                a=input('请出牌： ')
                outcard.append(a)
                if a=='end':
                    playcard(player3_display)           #打印出成功打出的卡牌及player3剩余的卡牌
                    player3_out=out
                    n,player3_out=check(player3_out)    #n,player3_out收集check函数返回的值
                    if n:
                        print('违反出牌规则')
                        for x in player3_out:
                            player3_display.append(x)
                        print('player3的牌')
                        print(player3_display)
                        outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                        continue
                    else:
                        n=compare(player2_out,player3_out)
                        if n:
                            print('违反出牌规则')
                            for x in player3_out:
                                player3_display.append(x)
                            print('player3的牌')
                            print(player3_display)
                            outcard=[]                      #此处要将outcard清空，不然重新输入时会加上前一次的输入
                            continue
                        else:
                            print('符合出牌规则')
                            break
                if a=='pass':
                    player3_out=player2_out
                    passcard+=1
                    break
    if player1_display==[]:
        if dizhu==1:
            print('地主player1赢了')
            break
        if dizhu==2:
            print('农民player1和player3赢了')
            break
        else:
            print('农民player1和player2赢了')
            break
    if player2_display==[]:
        if dizhu==2:
            print('地主player2赢了')
            break
        if dizhu==1:
            print('农民player2和player3赢了')
            break
        else:
            print('农民player1和player2赢了')
            break
    if player3_display==[]:
        if dizhu==3:
            print('地主player3赢了')
            break
        if dizhu==2:
            print('农民player1和player3赢了')
            break
        else:
            print('农民player2和player3赢了')
            break