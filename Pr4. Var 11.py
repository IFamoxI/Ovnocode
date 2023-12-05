import matplotlib.pyplot as plt
import math

V1 = 2.3 * 10**-4
V2 = 5.1 * 10**-4
p1 = 890
p2 = 1030
C1 = 3000
C2 = 4240
d = 0.02
K = 800
h = 0.01
b1 = (K * math.pi * d) / (V1 * p1 * C1)
b2 = (K * math.pi * d) / (V2 * p2 * C2)
T1 = [190]
T2 = [40]

while T1[-1] - T2[-1] > 2:
    T01 = T1[-1] - h * b1 * (T1[-1] - T2[-1])
    T1.append(T01)
    T02 = T2[-1] + h * b2 * (T1[-1] - T2[-1])
    T2.append(T02)

plt.figure()
plt.subplot(1, 2, 1)
x = range(len(T1))
plt.title("Прямоточный теплообменник")
plt.xlabel("L")
plt.ylabel("Т")
plt.plot(x, T1, label="T1")
plt.plot(x, T2, label="T2")
plt.legend()

T11 = [200]
T22 = [T2[-1]]

while T22[-1] > 35:
    T011 = T11[-1] - h * b1  *(T11[-1] - T22[-1])
    T11.append(T011)
    T022 = T22[-1] - h * b2 * (T11[-1] - T22[-1])
    T22.append(T022)
    
plt.subplot(1, 2, 2)
X = range(len(T11))
plt.title("Противоточный теплообменник")
plt.xlabel("L")
plt.ylabel("Т")
plt.plot(X, T11, label="T1")
plt.plot(X, T22, label="T2")
plt.legend()
plt.show()
print(T11[-1], T22[0])
