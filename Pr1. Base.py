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
h=0.016 #integration step

for T in range(500,751,10):
    
  CA_list=[round(0.2, 4)]
  CB_list=([0])
  CC_list=[round(0.1, 4)]
  CD_list=([0])
  k1=round(k01*math.exp(-E1/(R*T)), 4)
  k1_list.append(k1)
  k2=round(k02*math.exp(-E2/(R*T)), 4)
  k2_list.append(k2)
  k3=round(k03*math.exp(-E3/(R*T)), 4)
  k3_list.append(k3)

  for time in range(2000):
    CA_memes=((-k1*CA_list[-1]*(CC_list[-1])**2)+(k2*CB_list[-1]))
    CA_memes_list=[]
    CA_memes_list.append(CA_memes)
    CA=round(CA_list[-1]+h*CA_memes, 4)
    CA_list.append(CA)
    CB=round(CB_list[-1]+h*((k1*CA_list[-1]*(CC_list[-1])**2)-(k2*CB_list[-1])-(k3*CB_list[-1])), 4)
    CB_list.append(CB)
    CC=round(CC_list[-1]+h*((-2*k1*CA_list[-1]*(CC_list[-1])**2)+(k2*CB_list[-1])), 4)
    CC_list.append(CC)
    CD=round((CD_list[-1]+h*(2*k3*CB_list[-1])), 4)
    CD_list.append(CD)
  
  CAall.append(CA_list)
  CBall.append(CB_list)
  CCall.append(CC_list)
  CDall.append(CD_list)



plt.figure
plt.subplot(1,2,1)
x = [i for i in range(2001)]
plt.title("Изменение концентрации при Т=750К")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(x, CAall[25], label="CA")
plt.plot(x, CBall[25], label="CB")
plt.plot(x, CCall[25], label="CC")
plt.plot(x, CDall[25], label="CD")
plt.legend


plt.subplot(1,2,2)
plt.title("Степень превращение от температуры")
X=0.2-CAall[0][-1],0.2-CAall[1][-1],0.2-CAall[2][-1],0.2-CAall[3][-1],0.2-CAall[4][-1],0.2-CAall[5][-1],0.2-CAall[6][-1],0.2-CAall[7][-1],0.2-CAall[8][-1],0.2-CAall[9][-1],0.2-CAall[10][-1],0.2-CAall[11][-1],0.2-CAall[12][-1],0.2-CAall[13][-1],0.2-CAall[14][-1],0.2-CAall[15][-1],0.2-CAall[16][-1],0.2-CAall[17][-1],0.2-CAall[18][-1],0.2-CAall[19][-1],0.2-CAall[20][-1],0.2-CAall[21][-1],0.2-CAall[22][-1],0.2-CAall[23][-1],0.2-CAall[24][-1],0.2-CAall[25][-1]
TT=range(500,751,10)
plt.plot(TT, X)
plt.show()

