import matplotlib.pyplot as plt

k1 = 0.38
kn1 = 0.13
k2 = 0.33
k3 = 0.29
kn3 = 0.07
h = 0.02

CC4H8_list = [0.72]
Cz_list = [1]
CzC4H8_list = [0]
CzC8H10_list = [0]
CH2_list = [0]
CC8H10_list = [0]

for time in range(2000):

    r1 = k1 * CC4H8_list[-1] * Cz_list[-1]
    rn1 = kn1 * CzC4H8_list[-1]
    r2 = k2 * CzC4H8_list[-1] * CC4H8_list[-1]
    r3 = k3 * CzC8H10_list[-1]
    rn3 = kn3 * Cz_list[-1] * CC8H10_list[-1]

    CC4H8 = CC4H8_list[-1] + h * (-r1 + rn1 - r2)
    Cz = Cz_list[-1] + h * (-r1 + rn1 + r3 - rn3)
    CzC4H8 = CzC4H8_list[-1] + h * (r1 - rn1 - r2)
    CzC8H10 = CzC8H10_list[-1] + h * (r2 - r3 + rn3)
    CH2 = CH2_list[-1] + h * r2
    CC8H10 = CC8H10_list[-1] + h * (r3 - rn3)

    CC4H8_list.append(CC4H8)
    Cz_list.append(Cz)
    CzC4H8_list.append(CzC4H8)
    CzC8H10_list.append(CzC8H10)
    CH2_list.append(CH2)
    CC8H10_list.append(CC8H10)

plt.figure
plt.subplot(1,2,1)
plt.title("Изменение концентрации по времени основных продуктов")
plt.xlabel("Время")
plt.ylabel("Концентрация, моль/л")
t=range(2001)
plt.plot(t, CC4H8_list, label='C4H8')
plt.plot(t, CC8H10_list, label='C8H10')
plt.plot(t, CH2_list, label='H2')
plt.legend()

plt.subplot(1,2,2)
plt.title("Изменение концентрации по времени побочных продуктов")
plt.xlabel("Время")
plt.ylabel("Концентрация, моль/л")
plt.plot(t, Cz_list, label='z')
plt.plot(t, CzC4H8_list, label='zC4H8')
plt.plot(t, CzC8H10_list, label='zC8H10')
plt.legend()
plt.show()