import matplotlib.pyplot as plt

H = 11.5
S = 1.8
V = 10000.0
C0 = 0.4
h = 1
Ce = [0, 0.005, 0.02, 0.05, 0.1, 0.14, 0.18, 0.22, 0.26, 0.3, 0.38]
tsr = H * S / V * 3600
ny = 12

nC = list(0 for i in range(ny))

for i in range(ny):
  nC[i] = list(0 for i in range(11))

for i in range (ny):
  nC[i][0] = C0

fC = list(0 for i in range(ny))

for i in range(ny):
  fC[i] = list(0 for i in range(11))
print(fC)
print(nC)


for n in range (ny):
  for i in range (1, 11):
    nC[n][i] = n/tsr * (nC[n][i-1] - nC[n][i])
    fC[n][i] = ((C0 - nC[n][i]) - Ce[i])**2


for i in range(1, ny):
  print("При количестве ячеек =",i, "погрешность составляет", round(sum(fC[i]) * 100, 2), "%")
  if sum(fC[i]) < sum(fC[i-1]):
    fmin = sum(fC[i])
    a = i
print("Минимальная погрешность при", a, "ячеек = ", round(fmin * 100, 2), "%")


F = list(0 for i in range(ny))
for i in range (1, ny):
  F[i] = sum(fC[i]) * 100


plt.figure
plt.xlim(1, 10)
plt.ylim(0, 50)
plt.title("Зависимость ошибки от количества ячеек")
plt.plot(list(i for i in range(ny)), F,  marker='o')
plt.xlabel('Число ячеек')
plt.ylabel('Ошибка, %')
plt.show()