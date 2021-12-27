import math
import numpy
import copy
from tkinter import *

x1, x2, x3, y, D, ryx = [170,180,170,160,188,200,210,150,174,182,190,170,160,170,180,190,210,225,210,150,186,190], [13,14,13,18,17,16,19,20,21,21,21,18,17,15,15,15,15,16,18,18,14,14], [22,25,30,21,27,24,22,25,26,26,26,26,29,24,24,24,24,22,29,19,25,25], [89.57,91.31,99.49,92.51, 93.31, 86.53, 83.29, 99.8, 96.92, 96.26, 93.53, 96.26, 99.99, 92.57, 90.52, 88.37, 83.77, 78.23, 91.36, 92.36, 90.03, 89.16], [[0]*4,[0]*4,[0]*4,[0]*4], {}

x = [x1,x2,x3]

window = Tk()
window.geometry('400x500')
window.title("Кр2")

def sumy(y):
    sum = 0
    for i in range(len(y)):
        sum += y[i]
    return sum


def sumsqr(y):
    sum = 0
    for i in range(len(y)):
        sum += math.pow(y[i],2)
    return sum


def xnay(x,y):
    sum = 0
    for i in range(len(y)):
        sum += x[i]*y[i]
    return sum


def r(x,y):
    r = (len(x1)*xnay(x,y)-sumy(x)*sumy(y))/math.sqrt((22*sumsqr(x)-math.pow(sumy(x),2))*(len(x1)*sumsqr(y)-math.pow(sumy(y),2)))
    return r


def Dmk(col, row):
    dc = copy.deepcopy(D)
    dc.pop(row-1)
    for i in range(len(dc)):
        for j in range(len(dc[i])):
            if j == col-1:
                dc[i].pop(j)
    return dc


for i in range(len(D)):
    for j in range(len(D[i])):
        if i == j:
            D[i][j] = 1
        elif j == len(D[i])-1:
            D[i][j] == r(x[i],y)
        elif i == len(D)-1:
            D[i][j] = r(y,x[j])
        else:
            D[i][j] = r(x[i],x[j])

for i in range(0,3):
    ryx[i+1] = numpy.linalg.det(Dmk(4,i+1))/math.sqrt(numpy.linalg.det(Dmk(4,4))*numpy.linalg.det(Dmk(i+1,i+1)))
sorted_ryx = {}
sorted_values = sorted(ryx.values(), reverse=True)

for i in sorted_values:
    for k in ryx.keys():
        if ryx[k] == i:
            sorted_ryx[k] = ryx[k]
            break


ye0i = []
for i in range(len(y)):
    ye0i.append((y[i]*len(y))/sumy(y))

aryp = [0]*22

funcarr = [[0]*22, [0]*22, [0]*22]

xCount = 0

for key in sorted_ryx:
    if key == 1:
        arrayX = copy.deepcopy(x1)
    elif key == 2:
        arrayX = copy.deepcopy(x2)
    elif key == 3:
        arrayX = copy.deepcopy(x3)
    sxy, sx, sy, sx2, syy = 0, 0, 0, 0, 0
    for i in range(len(arrayX)):
        sxy += arrayX[i]*ye0i[i]
        sx += arrayX[i]
        sy += ye0i[i]
        sx2 += arrayX[i] * arrayX[i]
    a = (len(arrayX) * sxy - sx * sy) / (len(arrayX) * sx2 - sx * sx)
    b = (sx2 * sy - sx * sxy) / (len(arrayX) * sx2 - sx * sx)
    SumForm = {}
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = a*arrayX[i] + b
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula0'] = syy
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = 1 / (a * arrayX[i] + b)
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula1'] = syy
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = (a / arrayX[i]) + b
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula2'] = syy
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = b * math.pow(arrayX[i], a)
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula3'] = syy
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = b * math.exp(a * arrayX[i])
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula4'] = syy
    syy = 0
    for i in range(len(arrayX)):
        aryp[i] = a * math.log(arrayX[i]) + b
        syy += (ye0i[i] - aryp[i]) * (ye0i[i] - aryp[i])
    SumForm['Formula5'] = syy

    print(SumForm)

    sorted_values = sorted(SumForm.values(), reverse=True)
    sorted_form = {}

    for i in sorted_values:
        for k in SumForm.keys():
            if SumForm[k] == i:
                sorted_form[k] = SumForm[k]
                break
    print (sorted_form)
    for key in sorted_form:
        if key == 'Formula0':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = a * arrayX[i] + b
                ye0i[i] = ye0i[i] /(a * arrayX[i] + b)
        if key == 'Formula1':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = 1 / (a * arrayX[i] + b)
                ye0i[i] = ye0i[i] /(1 / (a * arrayX[i] + b))
        if key == 'Formula2':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = (a / arrayX[i]) + b
                ye0i[i] = ye0i[i] /((a / arrayX[i]) + b)
        if key == 'Formula3':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = b * math.pow(arrayX[i], a)
                ye0i[i] = ye0i[i] /(math.pow(arrayX[i], a))
        if key == 'Formula4':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = b * math.exp(a * arrayX[i])
                ye0i[i] = ye0i[i] /(b * math.exp(a * arrayX[i]))
        if key == 'Formula5':
            for i in range(len(arrayX)):
                funcarr[xCount][i] = a * math.log(arrayX[i]) + b
                ye0i[i] = ye0i[i] /(math.log(arrayX[i]) + b)
    xCount += 1

for i in range(len(arrayX)):
    aryp[i] = sumy(y)/len(arrayX) * funcarr[0][i] * funcarr[1][i] * funcarr[2][i]

Label(window, text='Yp').grid(column=5, row=0)
Label(window, text='X1').grid(column=1, row=0)
Label(window, text='X2').grid(column=2, row=0)
Label(window, text='X3').grid(column=3, row=0)
Label(window, text='Y').grid(column=4, row=0)

for i in range(len(arrayX)):
    Label(window, text=str(aryp[i])).grid(column=5, row=i+1)
    Label(window, text=str(x1[i])).grid(column=1, row=i+1)
    Label(window, text=str(x2[i])).grid(column=2, row=i+1)
    Label(window, text=str(x3[i])).grid(column=3, row=i+1)
    Label(window, text=str(y[i])).grid(column=4, row=i+1)

window.mainloop()