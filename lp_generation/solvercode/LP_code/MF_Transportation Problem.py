import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Transportation Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model= scp.Model()
S = info["S"]
D = info["D"]
a = info["a_i"]
b = info["b_j"]
c = info["c_{i,j}"]
x ={}
for i in range(S):
    for j in range(D):
        x[i,j] = model.addVar(name = f"x{i}{j}")
model.setObjective()