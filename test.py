import math

source = [4, 3, 5]
elm=len(set(source))				# к-во элементов, n
cells=2			    # к-во положений, m
res=[]				# результирующий список
arrang = math.factorial(elm)/(math.factorial(elm-cells) * math.factorial(cells))# расчёт к-ва сочетаний
for i in range(int(arrang)):
    res.append([])
    tempsource = list(set(source))	# массив ещё не задействованных элементов
    for j in range(cells):
        p=i//math.factorial(cells-1-j)%len(tempsource)
        res[len(res)-1].append(tempsource[p])
        tempsource.pop(p)
for i in range(len(res)):
    print(*res[i], i, end = '\n')