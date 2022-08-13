import matplotlib.pyplot as plt
import curves
 
# 1 para cada lista em curves, precisamos de um energyList e um countList
# 2 para cada lista em curves, precisamos de iterar sobre os dicts e fazer um for in para energy e um para count
# 3 para cada lista em curves, precisamos chamar o ax.plot com a energyList e a countList como parametro

fig, ax = plt.subplots()
legendsList = []

for curve in curves.curves.values():
    energyList = []
    countList = []

    for x in curve:
        energyList.append(x['energy'])

    for y in curve:
        countList.append(y['count'])

    ax.plot(energyList, countList, color='lightgreen')

# for legends in curves.curves.keys():
#     legendsList.append(legends)

# plt.legend(legendsList)
plt.show()