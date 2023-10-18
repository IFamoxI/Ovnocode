import matplotlib.pyplot as plt
import math


k1=0.45
kn1=0.035
k2=0.33
k3=0.21
kn3=0.1
h=0.02 #integration step

CH2_list=[0.6]
Cz_list=[1.0]
CzH2_list=[0]
CC7H8_list=[0.4]
CzC7H8H2_list=[0]
CCH4_list=[0]
CC6H6_list=[0]



for time in range(2000):
    
    r1=k1*CH2_list[-1]*Cz_list[-1]
    rn1=kn1*CzH2_list[-1]
    r2=k2*CzH2_list[-1]*CC7H8_list[-1]
    r3=k3*CzC7H8H2_list[-1]
    rn3=kn3*Cz_list[-1]*CCH4_list[-1]*CC6H6_list[-1]
    
    
    Cz=round(Cz_list[-1]+h*(-r1+rn1+r3-rn3),4)
    Cz_list.append(Cz)

    CzH2=round(CzH2_list[-1]+h*(r1-rn1-r2), 4)
    CzH2_list.append(CzH2)

    CzC7H8H2=round(CzC7H8H2_list[-1]+h*(r2-r3+rn3), 4)
    CzC7H8H2_list.append(CzC7H8H2)

    CH2=round(CH2_list[-1]+h*(-r1+rn1), 4)
    CH2_list.append(CH2) 

    CC7H8=round(CC7H8_list[-1]+h*(-r2),4)
    CC7H8_list.append(CC7H8)

    CC6H6=round(CC6H6_list[-1]+h*(r3-rn3),4)
    CC6H6_list.append(CC6H6)

    CCH4=round(CCH4_list[-1]+h*(r3-rn3),4)
    CCH4_list.append(CCH4)



plt.figure
plt.title("Изменение концентрации по времени")
plt.xlabel("Время")
plt.ylabel("Концентрация")
t=range(2001)
plt.plot(t, Cz_list, label='z')
plt.plot(t, CzH2_list, label='zH2')
plt.plot(t, CzC7H8H2_list, label='zC7H8H2')
plt.plot(t, CH2_list, label='H2')
plt.plot(t, CC7H8_list, label='C7H8')
plt.plot(t, CC6H6_list, label='C6H6')
plt.plot(t, CCH4_list, label='CH4')
plt.legend()
plt.show()
