import matplotlib.pyplot as plt
import math


R=round(8.31, 4)
CA0=round(0.2, 4)
CC0=round(0.1, 4)
T=(500)
k1=round(0.42, 4)
k2=round(0.2, 4)
k3=round(0.25, 4)
E1=(113540)
E2=(95920)
E3=(94310)
k01=(2.529*10**10)
k02=(2.622*10**8)
k03=(2.26*10**8)
CA_list=[round(0.2, 4)]
CB_list=([0])
CC_list=[round(0.1, 4)]
CD_list=([0])
CAall=[]
CBall=[]
CCall=[]
CDall=[]
k1_list=[]
k2_list=[]
k3_list=[]
h=2 #integration step

for T in range(500,751,10):
    k1=k01*math.exp(-E1/(R*T))
    k1_list.append(k1)
    k2=k02*math.exp(-E2/(R*T))
    k2_list.append(k2)
    k3=k03*math.exp(-E3/(R*T))
    k3_list.append(k3)
    for time in range(2000):
      CA=CA_list[-1]+h*((-k1*CA_list[-1]*(CC_list[-1])**2)+(k2*CB_list[-1]))
      CA_list.append(CA)
      CB=CB_list[-1]+h*((-k1*CA_list[-1]*(CC_list[-1])**2)-(k2*CB_list[-1])-(k3*CB_list[-1]))
      CB_list.append(CB)
      CC=CC_list[-1]+h*((-2*k1*CA_list[-1]*(CC_list[-1])**2)+(2*k2*CB_list[-1]))
      CC_list.append(CC)
      CD=2*k3*CB_list[-1]
      CD_list.append(CD) 
    CAall.append(CA_list)
    CBall.append(CB_list)
    CCall.append(CC_list)
    CDall.append(CD_list)
    CA_list=[round(0.2, 4)]
    CB_list=([0])
    CC_list=[round(0.1, 4)]
    CD_list=([0])
    
    
print(CAall[-1])
#print(k1_list)
#print(k2_list)
#print(k3_list)


