import pyscipopt as scp
import json
with open("../../../data/MILP_data/MF_Facility Location Problem_Uncapacitated Facility Location Problem (UFLP)_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
F = info["F"]
C = info["C"]
f = info["f_{i}"]
c = info["c_{ij}"]

x = {}
y = {}
for i in range(F):
    for j in range(C):
        x[i,j] = model.addVar(name = f"x{i}{j}", vtype ="B")
    y[i] = model.addVar(name = f"y{i}", vtype = "B")
model.setObjective(sum(f[i]*y[i] for i in range(F))+sum(c[i][j]*x[i,j] for j in range(C) for i in range(F)))

for j in range(C):
    model.addCons(sum(x[i,j] for i in range(F))==1)

model.writeProblem('../../MILP_file/MF_Facility Location Problem_Uncapacitated Facility Location Problem (UFLP).lp')
model.writeProblem('../../success/MF_Facility Location Problem_Uncapacitated Facility Location Problem (UFLP).lp')