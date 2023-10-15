import math
import matplotlib.pyplot as plt



k01=0.4
k02=0.2
R=round(8.31, 2)
E1=round(10.351*10**4, 1)
E2=round(9.180*10**4, 1)
h=0.5  #integration step

CAall=[]
CBall=[]
CCall=[]


for T in range(500, 751, 10):
    CA_list=[round(0.7, 4)]
    CB_list=[0]
    CC_list=[0]
    k1=round(k01*math.exp(-E1/(R*T)), 4)
    k2=round(k02*math.exp(-E2/(R*T)), 4)
    print('k1 ', k1)
    print('k2 ', k2)

    for time in range(20):
        
        F_CA=-k1*CA_list[-1]-k2*CA_list[-1]
        F_CB=k1*CA_list[-1]
        F_CC=k2*CA_list[-1]

        Aa1=h*(F_CA)
        Aa2=h*(F_CA+(Aa1/2))
        Aa3=h*(F_CA+(Aa2/2))
        Aa4=h*(F_CA+Aa3)
        CA=round(CA_list[-1]+h/6*(Aa1+2*Aa2+2*Aa3+Aa4), 4)
        CA_list.append(CA)

        Ba1=h*(F_CB)
        Ba2=h*(F_CB+Ba1/2)
        Ba3=h*(F_CB+Ba2/2)
        Ba4=h*(F_CB+Ba3)
        CB=round(CB_list[-1]+h/6*(Ba1+Ba2*2+Ba3*2+Ba4), 4)
        CB_list.append(CB)

        Ca1=h*(F_CC)
        Ca2=h*(F_CC+Ca1/2)
        Ca3=h*(F_CC+Ca2/2)
        Ca4=h*(F_CC+Ca3)
        CC=round(CC_list[-1]+h/6*(Ca1+Ca2*2+Ca3*2+Ca4), 4)
        CC_list.append(CC)

    CAall.append(CA_list)
    CBall.append(CB_list)
    CCall.append(CC_list)

print('CAall', CAall[-1])
print('CBall', CBall[-1])
print('CCall', CCall[-1])


print('Сумма концентраций продуктов равна ', CAall[-1][-1]+CBall[-1][-1]+CCall[-1][-1])


plt.figure
plt.subplot(1,2,1)
x = [i for i in range(2001)]
plt.title("Изменение концентрации при Т=500К")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(x, CAall[0], color='r', label='CA')
plt.plot(x, CBall[0], color='g', label='CB')
plt.plot(x, CCall[0], color='b', label='CC')
plt.legend()

plt.subplot(1,2,2)
x = [i for i in range(2001)]
plt.title("Изменение концентрации при Т=750К")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(x, CAall[25], color='r', label='CA')
plt.plot(x, CBall[25], color='g', label='CB')
plt.plot(x, CCall[25], color='b', label='CC')
plt.legend()
plt.show()