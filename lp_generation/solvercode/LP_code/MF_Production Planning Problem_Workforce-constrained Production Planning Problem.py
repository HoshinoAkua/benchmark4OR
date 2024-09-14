import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_Workforce-constrained Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
P = info["P"]
R = info["R"]
W = info["W"]

c = info["c_i"]
f = info["f_i"]
a = info["a_{i,j}"]
b = info["b_j"]
d = info["d_{i,j}"]
e = info["e_j"]
x,w = {},{}
for i in range(P):
    x[i] = model.addVar(name = f"x{i}")
    w[i] = model.addVar(name = f"w{i}")
for j in range(R):
    model.addCons(sum(a[i][j]*x[i] for i in range(P)) <= b[j])
for j in range(W):
    model.addCons(sum(d[i][j]*x[i] for i in range(P))<= e[j]*w[j])
    
model.writeProblem("../../lp_file/MF_Production Planning Problem_Workforce-constrained Production Planning Problem.lp")
