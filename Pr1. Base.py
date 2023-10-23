import matplotlib.pyplot as plt
import math


R=round(8.31, 4)
CA0=round(0.2, 4)
CC0=round(0.1, 4)
T=(500)
E1=(113540)
E2=(95920)
E3=(94310)
k01=(2.529*10**10)
k02=(2.622*10**8)
k03=round((2.26*10**8), 1)
CAall=[]
CBall=[]
CCall=[]
CDall=[]
k1_list=[]
k2_list=[]
k3_list=[]
XA_list=[]
XC_list=[]
h=0.0016 #integration step

for T in range(500,751,10):
    
  CA_list=[round(0.2, 4)]
  CB_list=([0])
  CC_list=[round(0.1, 4)]
  CD_list=([0])
  k1=k01*math.exp(-E1/(R*T))
  k1_list.append(k1)
  k2=k02*math.exp(-E2/(R*T))
  k2_list.append(k2)
  k3=k03*math.exp(-E3/(R*T))
  k3_list.append(k3)

  for time in range(2000):
    CA_memes=((-k1*CA_list[-1]*(CC_list[-1])**2)+(k2*CB_list[-1]))
    CA_memes_list=[]
    CA_memes_list.append(CA_memes)
    CA=CA_list[-1]+h*CA_memes
    CA_list.append(CA)
    CB=CB_list[-1]+h*((k1*CA_list[-1]*(CC_list[-1])**2)-(k2*CB_list[-1])-(k3*CB_list[-1]))
    CB_list.append(CB)
    CC=CC_list[-1]+h*((-2*k1*CA_list[-1]*(CC_list[-1])**2)+(k2*CB_list[-1]))
    CC_list.append(CC)
    CD=(CD_list[-1]+h*(2*k3*CB_list[-1]))
    CD_list.append(CD)
  
  CAall.append(CA_list)
  CBall.append(CB_list)
  CCall.append(CC_list)
  CDall.append(CD_list)



plt.figure
plt.subplot(1,2,1)
x = [i for i in range(2001)]
plt.title("Изменение концентрации при Т=750К")
plt.xlabel("Время")
plt.ylabel("КОнцентрация, моль/л")
plt.plot(x, CAall[25], label="CA")
plt.plot(x, CBall[25], label="CB")
plt.plot(x, CCall[25], label="CC")
plt.plot(x, CDall[25], label="CD")
plt.legend()

plt.subplot(1,2,2)
plt.title("Степень превращение от температуры")
plt.xlabel("Температура, К")
plt.ylabel("Степень превращения, %")
i=0
while i <= len (CAall)-1:
    XA=1-(CAall[i][-1]/CAall[i][0])
    XC=1-(CCall[i][-1]/CCall[i][0])
    i+=1
    XA_list.append(XA)
    XC_list.append(XC)
T=range(500,751,10)
plt.plot(T, XA_list, label="XA")
plt.plot(T,  XC_list, label="XC")
plt.legend()
plt.show()

