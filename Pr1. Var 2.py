import matplotlib.pyplot as plt
import math

R=8.31
k01=1.686*10**10
k02=4.214*10**8
E1=115140
E2=95240
CAall=[]
CBall=[]
CCall=[]
CDall=[]
CEall=[]
h=0.0005

for T in range(500, 751, 10):
    k1=k01*math.exp(-E1/(R*T))
    k2=k02*math.exp(-E2/(R*T))
    CA_list=[0.3]
    CB_list=[0]
    CC_list=[0]
    CD_list=[0.2]
    CE_list=[0.2]
    for time in range(2000):
        CA=CA_list[-1]+h*(-2*k1*(CA_list[-1]**2))
        CA_list.append(CA)
        CB=CB_list[-1]+h*(k1*(CA_list[-1]**2)+k2*CD_list[-1]*CE_list[-1])
        CB_list.append(CB)
        CC=CC_list[-1]+h*(k1*(CA_list[-1]**2))
        CC_list.append(CC)
        CD=CD_list[-1]+h*(-k2*CD_list[-1]*CE_list[-1])
        CD_list.append(CD)
        CE=CE_list[-1]+h*(-k2*CD_list[-1]*CE_list[-1])
        CE_list.append(CE)

    CAall.append(CA_list)
    CBall.append(CB_list)
    CCall.append(CC_list)
    CDall.append(CD_list)
    CEall.append(CE_list)


plt.figure
x = [i for i in range(2001)]
plt.title("Изменение концентрации при Т=750К")
plt.xlabel("Время")
plt.ylabel("Концентрация")
plt.plot(x, CAall[25], label="CA")
plt.plot(x, CBall[25], label="CB")
plt.plot(x, CCall[25], label="CC")
plt.plot(x, CDall[25], label="CD")
plt.plot(x, CEall[25], label="CE")
plt.legend()
plt.show()