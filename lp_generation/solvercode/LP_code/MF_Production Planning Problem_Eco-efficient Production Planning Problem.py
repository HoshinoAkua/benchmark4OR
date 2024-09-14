import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_Eco-efficient Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
P= info["P"]
R = info["R"]
E = info["E"]
c = info["c_i"]
a = info["a_{i,j}"]
b = info["b_j"]
g = info["g_i"]
d = info["d_{i,k}"]
e = info["e_k"]
x,y ={},{}
for i in range(P):
    x[i] = model.addVar(name = f'x{i}')
    y[i] = model.addVar(name = f'y{i}')
model.setObjective(sum((x[i]*c[i]+g[i]*y[i]) for i in range(P)))

for j in range(R):
    model.addCons(sum(a[i][j]*x[i] for i in range(P))<=b[j])
for k in range(E):
    model.addCons(sum(d[i][k]*y[i] for i in range(P))<= e[k])

model.writeProblem('../../lp_file/MF_Production Planning Problem_Eco-efficient Production Planning Problem.lp')