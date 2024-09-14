import pyscipopt as scp
import json
with open("../../../data/test_data/parameter_Facility Location Problem.json0th_paraminfo.json") as f:
    info = json.load(f)
F = info["F"]
C = info["C"]
f = info["f_{i}"]
c = info["c_{i j}"]
M = info["M_{i}"]
D = info["d_{j}"]
model = scp.Model()
x,y = {},{}
for i in range(F):
    y[i] = model.addVar(name = f"y{i}", vtype = "B")
    for j in range(C):
        x[i,j] = model.addVar(name = f"x{i}{j}", vtype = "B")

model.setObjective(sum(f[i]*y[i] for i in range(F))+sum(c[i][j]*x[i,j] for i in range(F) for j in range(C)))
for j in range(C):
    model.addCons(sum(x[i,j] for i in range(F)) == D[j])
for i in range(F):
    model.addCons(sum(x[i,j] for j in range(C))-M[i]*y[i]>=0)
for i in range(F):
    for j in range(C):
        model.addCons(x[i,j]>=D[j]*y[i])
model.writeProblem("../../test/facility location.lp")