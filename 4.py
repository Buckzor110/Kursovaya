import math

arrayX1 = [3, 1, 4, 2]
arrayX2 = [0.5, 0.4, 0.9, 0.1]
arrayX3 = [60, 15, 75, 45]
arrayPlanX1 = [-1, 1, -1, 1, -1, 1, -1, 1]
arrayPlanX2 = [-1, -1, 1, 1, -1, -1, 1, 1]
arrayPlanX3 = [-1, -1, -1, -1, 1, 1, 1, 1]
arrayY = [2710, 1400, 3070, 1257, 2360, 1980, 2920, 1100]
s2y = 11890
fy = 4

n = len(arrayPlanX1)

b0 = b1 = b2 = b3 = b12 = b13 = b23 = 0

for i in range(n):
    b0 += arrayY[i]
b0 /= n

for i in range(n):
    b1 += arrayPlanX1[i] * arrayY[i]
b1 /= n

for i in range(n):
    b2 += arrayPlanX2[i] * arrayY[i]
b2 /= n

for i in range(n):
    b3 += arrayPlanX3[i] * arrayY[i]
b3 /= n

for i in range(n):
    b12 += arrayPlanX1[i] * arrayPlanX2[i] * arrayY[i]
b12 /= n

for i in range(n):
    b13 += arrayPlanX1[i] * arrayPlanX3[i] * arrayY[i]
b13 /= n

for i in range(n):
    b23 += arrayPlanX2[i] * arrayPlanX3[i] * arrayY[i]
b23 /= n

s2b = s2y / n
tt = 2.45

t0 = t1 = t2 = t3 = t12 = t13 = t23 = 0

t0 = abs(b0) / math.sqrt(s2b)
t1 = abs(b1) / math.sqrt(s2b)
t2 = abs(b2) / math.sqrt(s2b)
t3 = abs(b3) / math.sqrt(s2b)
t12 = abs(b12) / math.sqrt(s2b)
t13 = abs(b13) / math.sqrt(s2b)
t23 = abs(b23) / math.sqrt(s2b)

valuableCount = 7

if t0 < tt:
    valuableCount -= 1
    b0 = 0

if t1 < tt:
    valuableCount -= 1
    b1 = 0

if t2 < tt:
    valuableCount -= 1
    b2 = 0

if t3 < tt:
    valuableCount -= 1
    b3 = 0

if t12 < tt:
    valuableCount -= 1
    b12 = 0

if t13 < tt:
    valuableCount -= 1
    b13 = 0

if t23 < tt:
    valuableCount -= 1
    b23 = 0

arrayYp = [0] * n

for i in range(n):
    arrayYp[i] = b0 + b1 * arrayPlanX1[i] + b2 * arrayPlanX2[i] + b3 * arrayPlanX3[i] + b12 * arrayPlanX1[i] * \
                 arrayPlanX2[i] + b13 * arrayPlanX1[i] * arrayPlanX3[i] + b23 * arrayPlanX2[i] * arrayPlanX3[i]

s2ad = 0
for i in range(n):
    s2ad += (arrayY[i] - arrayYp[i]) * (arrayY[i] - arrayYp[i])
s2ad /= n - valuableCount

F = s2ad / s2y

temp1 = str(round((b0 + (b1 * -arrayX1[0]) / arrayX1[1] + (b2 * -arrayX2[0]) / arrayX2[1] + (b3 * -arrayX3[0]) / arrayX3[1] + (b12 * -arrayX1[0] * -arrayX2[0]) / (arrayX1[1] * arrayX2[1]) + (b13 * -arrayX1[0] * -arrayX3[0]) / (arrayX1[1] * arrayX3[1]) + (b23 * -arrayX2[0] * -arrayX3[0]) / (arrayX2[1] * arrayX3[1])), 3))
temp2 = str(round((b1 / arrayX1[1] + (b12 * arrayX2[0]) / (arrayX1[1] * arrayX2[1]) + (b13 * arrayX3[0]) / (arrayX1[1] * arrayX3[1])), 3))
temp3 = str(round((b2 / arrayX2[1] + (b12 * arrayX1[0]) / (arrayX1[1] * arrayX2[1]) + (b23 * arrayX3[0]) / (arrayX2[1] * arrayX3[1])), 3))
temp4 = str(round((b3 / arrayX3[1] + (b13 * arrayX1[0]) / (arrayX1[1] * arrayX3[1]) + (b23 * arrayX2[0]) / (arrayX2[1] * arrayX3[1])), 3))
temp5 = str(round(b12 / (arrayX1[1] * arrayX2[1]), 3))
temp6 = str(round(b13 / (arrayX1[1] * arrayX3[1]), 3))
temp7 = str(round(b23 / (arrayX2[1] * arrayX3[1]), 3))
temp8 = "\nYp = " + temp1 + " + " + temp2 + " x1 + " + temp3 + " x2 + " + temp4 + " x3 + " + temp5 + " x1x2 + " + temp6 + " x1x3 + " + temp7 + " x2x3 "
temp9 = temp8.replace("+ -", "- ")

if "+ 0.0 x1 " in temp9:
    temp9 = temp9.replace("+ 0.0 x1 ", "")
elif "- 0.0 x1 " in temp9:
    temp9 = temp9.replace("- 0.0 x1 ", "")
if "+ 0.0 x2 " in temp9:
    temp9 = temp9.replace("+ 0.0 x2 ", "")
elif "- 0.0 x2 " in temp9:
    temp9 = temp9.replace("- 0.0 x2 ", "")
if "+ 0.0 x3 " in temp9:
    temp9 = temp9.replace("+ 0.0 x3 ", "")
elif "- 0.0 x3 " in temp9:
    temp9 = temp9.replace("- 0.0 x3 ", "")
if "+ 0.0 x1x2 " in temp9:
    temp9 = temp9.replace("+ 0.0 x1x2 ", "")
elif "- 0.0 x1x2 " in temp9:
    temp9 = temp9.replace("- 0.0 x1x2 ", "")
if "+ 0.0 x1x3 " in temp9:
    temp9 = temp9.replace("+ 0.0 x1x3 ", "")
elif "- 0.0 x1x3 " in temp9:
    temp9 = temp9.replace("- 0.0 x1x3 ", "")
if "+ 0.0 x2x3 " in temp9:
    temp9 = temp9.replace("+ 0.0 x2x3 ", "")
elif "- 0.0 x2x3 " in temp9:
    temp9 = temp9.replace("- 0.0 x2x3 ", "")

print('Расчётное значение критерия Фишера:\n', round(F, 3), sep = '')
print('Уравнение регрессии физических переменных:', temp9)