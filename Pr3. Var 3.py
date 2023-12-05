import matplotlib.pyplot as plt

L = 11.5
S = 1.8
V = 10000.0
C0 = 0.4
h = 1
Ce = [0, 0.005, 0.02, 0.05, 0.1, 0.14, 0.18, 0.22, 0.26, 0.3, 0.38]
tsr = L * S / V * 3600
fC_list = []

for n in range(2, 12):
    C_list = [C0]
    for time in (1, 11):
        C = n / tsr * (C_list[-1] - C)  
        C_list.append(C)

        fC = ((C0-C)-Ce[time]) ** 2
        fC_list.append(fC)
    C_dict = {n: C}
    fC_dict = {n: fC}

print(C_dict)
print(fC_dict)