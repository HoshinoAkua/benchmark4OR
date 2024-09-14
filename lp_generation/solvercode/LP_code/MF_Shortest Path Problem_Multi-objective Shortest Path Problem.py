import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Shortest Path Problem_Multi-objective Shortest Path Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
N = info["N"]
d = info["d_{i,j}"]
t_ = info["t_{i,j}"]
s = info["s"]-1
t = info["t"]-1

x = {}
for i in range(N):
    for j in range(N):
        x[i,j] = model.addVar(name = f"x{i}{j}")
model.setObjective(sum(d[i][j]*x[i,j] for i in range(N) for j in range(N))+sum(t_[i][j]*x[i,j] for i in range(N) for j in range(N)))

for i in range(N):
    if i not in [s,t]:
        model.addCons(sum(x[i,j] for j in range(N))-sum(x[j,i] for j in range(N))==0)
    elif i == s:
        model.addCons(sum(x[i,j] for j in range(N))-sum(x[j,i] for j in range(N))==1)
    elif i == t:
        model.addCons(sum(x[i,j] for j in range(N))-sum(x[j,i] for j in range(N))==-1)
model.writeProblem('../../lp_file/MF_Shortest Path Problem_Multi-objective Shortest Path Problem.lp')
model.writeProblem('../../success/MF_Shortest Path Problem_Multi-objective Shortest Path Problem.lp')
