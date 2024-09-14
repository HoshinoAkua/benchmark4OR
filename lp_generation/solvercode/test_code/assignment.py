import pyscipopt as scp
import json
with open("../../../data/test_data/parameter_Assignment Problem.json0th_paraminfo.json") as f:
    info = json.load(f)
I = info["I"]
J = info["J"]
c = info["c_{i j}"]
model = scp.Model()
x = {}
for i in range(I):
    for j in range(J):
        x[i,j] = model.addVar(name = f"x{i}{j}", vtype = "B")
model.setObjective(sum(c[i][j] * x[i,j] for i in range(I) for j in range(J)))
for i in range(I):
    model.addCons(sum(x[i,j] for j in range(J))==1)
for j in range(J):
    model.addCons(sum(x[i,j] for i in range(I))==1)

model.writeProblem("../../test/assignment.lp")