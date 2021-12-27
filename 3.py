import math
from tkinter import *

arrayX1, arrayX2, arrayX3, arrayY, D, ryx = [170,180,170,160,188,200,210,150,174,182,190,170,160,170,180,190,210,225,210,150,186,190], [13,14,13,18,17,16,19,20,21,21,21,18,17,15,15,15,15,16,18,18,14,14], [22,25,30,21,27,24,22,25,26,26,26,26,29,24,24,24,24,22,29,19,25,25], [89.57,91.31,99.49,92.51, 93.31, 86.53, 83.29, 99.8, 96.92, 96.26, 93.53, 96.26, 99.99, 92.57, 90.52, 88.37, 83.77, 78.23, 91.36, 92.36, 90.03, 89.16], [[0]*4,[0]*4,[0]*4,[0]*4], {}

x = [arrayX1,arrayX2,arrayX3]

window = Tk()
window.geometry('400x500')
window.title("Кр2")

n = len(arrayX1)
arrayY0 = [0]*n

yAvr = 0
for i in range(0,n):
    yAvr += arrayY[i]
yAvr /= n

sy = 0
for i in range(0, n):
    sy += (arrayY[i] - yAvr) * (arrayY[i] - yAvr)
sy /= n - 1
sy = math.sqrt(sy)

for i in range(0,n):
    arrayY0[i] = (arrayY[i] - yAvr) / sy

arrayX0 = [[0]*n]*3
arrayXJI = [[0]*n]*3

for j in range(0,n):
    arrayXJI[0][j] = arrayX1[j]
for j in range(0,n):
    arrayXJI[1][j] = arrayX2[j]
for j in range(0,n):
    arrayXJI[2][j] = arrayX3[j]

arrayXAvr = [0]*3

for j in range(0,3):
    for i in range(0,n):
        arrayXAvr[j] += arrayXJI[j][i]
for j in range(0,3):
    arrayXAvr[j] /= n

arraySX = [0]*3
for j in range(0,3):
    for i in range(0,n):
        arraySX[j] += (arrayXJI[j][i] - arrayXAvr[j]) * (arrayXJI[j][i] - arrayXAvr[j])

for j in range(0,3):
    arraySX[j] /= n - 1
    arraySX[j] /= math.sqrt(arraySX[j])

for j in range(0,3):
    for i in range(0,n):
        arrayX0[j][i] = (arrayXJI[j][i] - arrayXAvr[j]) / arraySX[j]

arrayR = [[0]*4,[0]*4,[0]*4]

for l in range(0,3):
    for m in range(0,3):
        sum = 0
        for i in range(0,n):
            sum += arrayX0[l][i] * arrayX0[m][i]
        sum /= n - 1
        arrayR[l][m] = sum

for j in range(0,3):
    sum = 0
    for i in range(0,n):
        sum += arrayY0[i] * arrayX0[j][i]
    sum /= n - 1
    arrayR[j][3] = sum

s = 0
matrix = [[0]*3, [0]*3, [0]*3]
b = [0]*3
a = [0]*3

for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = arrayR[i][j]

for i in range(0,3):
    b[i] = arrayR[i][3]

for k in range(0,2):
    for i in range(k+1,3):
        for j in range(k+1,3):
            matrix[i][j] = matrix[i][j] - matrix[k][j] * (matrix[i][k] / matrix[k][k])
        b[i] = b[i] - b[k] * matrix[i][k] / matrix[k][k]
for i in range(2,-1,-1):
    s = 0
    for j in range(i+1, 3):
        s = s + matrix[i][j] * a[j]
    a[i] = (b[i] - s) / matrix[i][i]

arrayB = [0]*3
for i in range(0,3):
    arrayB[i] = a[i] * (sy / arraySX[i])

b0 = 0
for i in range(0,3):
    b0 += arrayB[i] * arrayXAvr[i]
b0 = yAvr - b0

arrayYp = [0]*n
for i in range(0,n):
    arrayYp[i] = b0 + arrayX1[i] * arrayB[0] + arrayX2[i] * arrayB[1] + arrayX3[i] * arrayB[2]

Label(window, text='Yp').grid(column=5, row=0)
Label(window, text='X1').grid(column=1, row=0)
Label(window, text='X2').grid(column=2, row=0)
Label(window, text='X3').grid(column=3, row=0)
Label(window, text='Y').grid(column=4, row=0)

for i in range(22):
    Label(window, text=str(arrayYp[i])).grid(column=5, row=i+1)
    Label(window, text=str(arrayX1[i])).grid(column=1, row=i+1)
    Label(window, text=str(arrayX2[i])).grid(column=2, row=i+1)
    Label(window, text=str(arrayX3[i])).grid(column=3, row=i+1)
    Label(window, text=str(arrayY[i])).grid(column=4, row=i+1)

window.mainloop()