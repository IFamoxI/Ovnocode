import matplotlib.pyplot as plt

k1=0.2  
k2=0.4  
R=8.31
E1=11,514*10**4
E2=9,524*10**4
h=0.0005  #integration step


def next(C, a1, a2, a3, a4):
    Cinext = C + (h / 6) * (a1 + 2 * a2+ 2 * a3 + a4)
    return Cinext


def r1 (A):
    ri1 = k1 * A ** 2
    return ri1


def r2(D,E):
    ri2 = k2 * D * E
    return ri2


CA_list = [0.3]
CB_list = [0]
CC_list = [0]
CD_list = [0.2]
CE_list = [0.2]


for time in range(2000):
    
    Aa1 = h * (-2 * (r1(CA_list[-1])))
    Aa2 = h * (-2 * r1(CA_list[-1] + (Aa1 / 2)))
    Aa3 = h * (-2 * r1(CA_list[-1] + (Aa2 / 2)))
    Aa4 = h * (-2 * r1(CA_list[-1] + Aa3))
    CA = next(CA_list[-1], Aa1, Aa2, Aa3, Aa4)
    CA_list.append(CA)

    Ba1 = h * (r1(CA_list[-1]) + r2(CD_list[-1], CE_list[-1]))
    Ba2 = h * (r1(CA_list[-1] + (Ba1 / 2)) + r2(CD_list[-1] + (Ba1 / 2), CE_list[-1] + (Ba1 / 2)))
    Ba3 = h * (r1(CA_list[-1] + (Ba2 / 2)) + r2(CD_list[-1] + (Ba2 / 2), CE_list[-1] + (Ba2 / 2)))
    Ba4 = h * (r1(CA_list[-1] + Ba3) + r2(CD_list[-1] + Ba3, CE_list[-1] + Ba3))
    CB = next(CB_list[-1], Ba1, Ba2, Ba3, Ba4)
    CB_list.append(CB)

    Ca1 = h * (r1(CA_list[-1]))
    Ca2 = h * (r1(CA_list[-1] + (Ca1 / 2)))
    Ca3 = h * (r1(CA_list[-1] + (Ca2 / 2)))
    Ca4 = h * (r1(CA_list[-1] + Ca1))
    CC = next(CC_list[-1], Ca1, Ca2, Ca3, Ca4)
    CC_list.append(CC)

    Da1 = h * (-r2(CD_list[-1], CE_list[-1]))
    Da2 = h * (-r2(CD_list[-1] + (Da1 / 2), CE_list[-1]))
    Da3 = h * (-r2(CD_list[-1] + (Da2 / 2), CE_list[-1]))
    Da4 = h * (-r2(CD_list[-1] + Da3, CE_list[-1]))
    CD = next(CD_list[-1], Da1, Da2, Da3, Da4)
    CD_list.append(CD)

    Ea1 = h * (-r2(CD_list[-1], CE_list[-1]))
    Ea2 = h * (-r2(CD_list[-1], CE_list[-1] + (Ea1 / 2)))
    Ea3 = h * (-r2(CD_list[-1], CE_list[-1] + (Ea2 / 2)))
    Ea4 = h * (-r2(CD_list[-1], CE_list[-1] + Ea3))
    CE = next(CE_list[-1], Ea1, Ea2, Ea3, Ea4)
    CE_list.append(CE)



plt.figure
x = [i for i in range(2001)]
plt.title("Изменение концентрации по времени")
plt.xlabel("Время")
plt.ylabel("Концентрация")
plt.plot(x, CA_list, label="CA")
plt.plot(x, CB_list, label="CB")
plt.plot(x, CC_list, label="CC")
plt.plot(x, CD_list, label="CD")
plt.plot(x, CE_list, label="CE")
plt.legend()
plt.show()