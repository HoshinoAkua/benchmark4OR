import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_Demand Backlogging Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
P = info["P"]
R = info["R"]
c = info["c_i"]
h = info["h_i"]
a = info["a_{i,j}"]
b = info["b_j"]
d = info["d_i"]

x = {}
y = {}
for i in range(P):
    x[i] = model.addVar(name = f"x{i}")
    y[i] = model.addVar(name = f"y{i}")
model.setObjective(sum((x[i]*c[i]+h[i]*y[i]) for i in range(P)))

for i in range(P):
    model.addCons(x[i]+y[i] <= d[i])
for j in range(R):
    model.addCons(sum(x[i]*a[i][j] for i in range(P))<=b[j])

model.writeProblem('../../lp_file/MF_Production Planning Problem_Demand Backlogging Production Planning Problem')