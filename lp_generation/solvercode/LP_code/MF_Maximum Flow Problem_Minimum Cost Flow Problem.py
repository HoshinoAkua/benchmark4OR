import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Maximum Flow Problem_Minimum Cost Flow Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
N= info["N"]
d = info["d"]
a = info["a_{i, j}"]
c = info["c_{i, j}"]
s = info["s"]-1
t = info["t"]-1

f={}
for i in range(N):
    for j in range(N):
        f[i,j] = model.addVar(name = f"f{i}{j}" ,vtype = "C",ub=c[i][j])
model.setObjective(sum(a[i][j]*f[i,j] for i in range(N) for j in range(N)))

for i in range(N):
    for j in range(N):
        model.addCons((f[i,j]+f[j,i])==0)
   
    
for i in range(N):
    if i not in [s,t]:
        model.addCons(sum(f[i,j] for j in range(N))==0)
    elif i == s:
        model.addCons(sum(f[i,j] for j in range(N))==d)
    elif i == t:
        model.addCons(sum(f[j,i] for j in range(N))==d)
model.writeProblem("../../lp_file/MF_Maximum Flow Problem_Minimum Cost Flow Problem.lp")