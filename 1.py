import math

def sumx(t):
    sumx=0.0
    for i in range(7):
        sumx+=1/t[i]
    return sumx


def sumy(k):
    sumy=0.0
    for i in range(7):
        sumy+=math.log(k[i])
    return sumy


def sumx2(t):
    sumx2=0.0
    for i in range(7):
        sumx2+=math.pow(1/t[i],2)
    return sumx2


def sumxy(t,k):
    sumxy=0.0
    for i in range(7):
        sumxy+=(1/t[i])*math.log(k[i])
    return sumxy


t=[400,415,455,505,530,595,605]
k=[0.4,0.5,0.8,1.6,2.2,4.3,4.7]
a = 0
b=0
R=8.315

a=(7*sumxy(t,k)-sumx(t)*sumy(k))/(7*sumx2(t)-pow(sumx(t),2))
b=(sumx2(t)*sumy(k)-sumx(t)*sumxy(t,k))/(7*sumx2(t)-pow(sumx(t),2))
k0=math.exp(b)
E=-a*R
print("k0 = {}, E = {}".format(k0,E))
kpi=[]
for i in range(7):
    kpi.append((-E)/R*t[i])
print(kpi)