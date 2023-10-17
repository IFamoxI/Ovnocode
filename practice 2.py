import math
import matplotlib.pyplot as plt



k1=0.4
k2=0.2
T580 = 580
R=round(8.31, 2)
E1=round(10.351*10**4, 1)
E2=round(9.180*10**4, 1)
h=0.00000005  #integration step

CAall=[]
CBall=[]
CCall=[]


for T in range(500, 751, 10):
    CA_list=[round(0.7, 2)]
    CB_list=[0]
    CC_list=[0]
    k1=k1*math.exp((E1/R)*((1/T580)-(1/T)))
    k2=k2*math.exp((E2/R)*((1/T580)-(1/T)))
    print(T)
    print('k1 ', k1)
    print('k2 ', k2)

    for time in range(200):
        
        F_CA=-k1*CA_list[-1]-k2*CA_list[-1]
        F_CB=k1*CA_list[-1]
        F_CC=k2*CA_list[-1]

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

    CAall.append(CA_list)
    CBall.append(CB_list)
    CCall.append(CC_list)

print('CAall', CAall[24])
print('CBall', CBall[24])
print('CCall', CCall[24])


print('Сумма концентраций продуктов равна ', CAall[-1][-1]+CBall[-1][-1]+CCall[-1][-1])

plt.figure
plt.subplot(1,2,1)
x = [i for i in range(201)]
plt.title("Изменение концентрации при Т=500К")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(x, CAall[24], color='r', label='CA')
plt.plot(x, CBall[24], color='g', label='CB')
plt.plot(x, CCall[24], color='b', label='CC')
plt.legend()

plt.subplot(1,2,2)
x = [i for i in range(201)]
plt.title("Изменение концентрации при Т=750К")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(x, CAall[25], color='r', label='CA')
plt.plot(x, CBall[25], color='g', label='CB')
plt.plot(x, CCall[25], color='b', label='CC')
plt.legend()
plt.show()