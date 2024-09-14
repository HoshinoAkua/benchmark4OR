import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_Capacity-constrained Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
I = info["I"]
T = info["T"]
c = info["c_i"]
h = info["h_i"]
q = info["q_{i,t}"]
d = info["d_{i,t}"]
s = info["s_{i,t}"]

x = {}
y = {}
for i in range(I):
    for t in range(T):
        x[i,t] = model.addVar(name = f"x{i}{t}", vtype = "C",ub=q[i][t])
        y[i,t] = model.addVar(name = f"y{i}{t}", vtype = "C")
obj = sum(c[i]*sum(x[i,t] for t in range(T)) + h[i] *sum(y[i,t] for t in range(T)) for i in range(I))
model.setObjective(obj)
for i in range(I):
    for t in range(1, T):
        model.addCons(x[i,t]+y[i,t-1] == d[i][t]+y[i,t])
    model.addCons(y[i])
    
    