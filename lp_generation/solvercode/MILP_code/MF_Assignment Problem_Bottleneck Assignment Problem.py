import pyscipopt as scp
import json
with open("../../../data/MILP_data/parameter_Assignment Problem_Bottleneck Assignment Problem.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
M = info["M"]
N = info["N"]
c = info["c_{i j}"]
x = {}
s = {}
for i in range(N):
    for j in range(M):
        x[i,j] = model.addVar(name = f"x{i}{j}", vtype= "B")
s[0] =  model.addVar(name = f"s", lb = None)
model.setObjective(s[0])
for i in range(N):
    model.addCons(sum(x[i,j] for j in range(M))==1)
for j in range(M):
    model.addCons(sum(x[i,j] for i in range(N))==1)
    for i in range(M):
        model.addCons(s[0]>=c[i][j]*x[i,j])

model.writeProblem('../../MILP_file/MF_Assignment Problem_Bottleneck Assignment Problem.lp')
model.writeProblem('../../success/MF_Assignment Problem_Bottleneck Assignment Problem.lp')
