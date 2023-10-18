import math
import matplotlib.pyplot as plt

k1=0.2  #20000000000
k2=0.4  #40000000000
R=8.31
E1=11,514*10**4
E2=9,524*10**4
h=0.00000005  #integration step

CA_list=[0.3]
CB_list=[0]
CC_list=[0]
CD_list=[0.2]
CE_list=[0.2]


for time in range(2000):
    F_CA=-2*k1*(CA_list[-1])**2
    F_CB=k1*CA_list[-1]**2+k2*CD_list[-1]*CE_list[-1]
    F_CC=k1*CA_list[-1]**2
    F_CD=-k2*CD_list[-1]*CE_list[-1]
    F_CE=-k2*CD_list[-1]*CE_list[-1]

    Aa1=h*(F_CA)
    Aa2=h*(F_CA+(Aa1/2))
    Aa3=h*(F_CA+(Aa2/2))
    Aa4=h*(F_CA+Aa3)
    CA=CA_list[-1]+h/6*(Aa1+2*Aa2+2*Aa3+Aa4)
    CA_list.append(CA)

    Ba1=h*(F_CB)
    Ba2=h*(F_CB+Ba1/2)
    Ba3=h*(F_CB+Ba2/2)
    Ba4=h*(F_CB+Ba3)
    CB=CB_list[-1]+h/6*(Ba1+Ba2*2+Ba3*2+Ba4)
    CB_list.append(CB)

    Ca1=h*(F_CC)
    Ca2=h*(F_CC+Ca1/2)
    Ca3=h*(F_CC+Ca2/2)
    Ca4=h*(F_CC+Ca3)
    CC=CC_list[-1]+h/6*(Ca1+Ca2*2+Ca3*2+Ca4)
    CC_list.append(CC)

    Da1=h*(F_CD)
    Da2=h*(F_CD+Da1/2)
    Da3=h*(F_CD+Da2/2)
    Da4=h*(F_CD+Da3)
    CD=CD_list[-1]+h/6*(Da1+Da2*2+Da3*2+Da4)
    CD_list.append(CD)

    Ea1=h*(F_CE)
    Ea2=h*(F_CE+Ea1/2)
    Ea3=h*(F_CE+Ea2/2)
    Ea4=h*(F_CE+Ea3)
    CE=CE_list[-1]+h/6*(Ea1+Ea2*2+Ea3*2+Ea4)
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