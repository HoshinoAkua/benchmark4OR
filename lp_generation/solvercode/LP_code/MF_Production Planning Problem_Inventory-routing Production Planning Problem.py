import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_Inventory-routing Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()

I = info["I"]
J = info["J"]
T = info["T"]
c = info["c_{ij}"]
d = info["d_{ij}"]
e = info["e_{ij}"]
p = info["p_{i}"]
q = info["q_{j,t}"]
r = info["r_{ij}"]
x = {}
y = {}
z = {}
for i in range(I):
    for t in range(T):
        x[i,t] = model.addVar(name = f"x{i}{t}")
        for j in range(J):
            y[i,j,t] = model.addVar(name = f"y{i}{j}{t}")
for i in range(I):
    for j in range(J):
        z[i,j] = model.addVar(name = f"z{i}{j}")
exp1 = sum(sum(c[i][j]*x[i,t] for i in range(I) for j in range(J)) for t in range(T))
exp2 = sum(sum(d[i][j]*y[i,j,t] for i in range(I) for j in range(J)) for t in range(T))
exp3 = sum(e[i][j]*z[i,j] for i in range(I) for j in range(J))

model.setObjective(exp1+exp2+exp3)

for j in range(J):
    for t in range(T):
        model.addCons(sum(p[i]*x[i,t] for i in range(I))<=q[j][t])
for i in range(I):
    for j in range(J):
        model.addCons(sum(y[i,j,t] for t in range(T))<= r[i][j])
for t in range(T):
    model.addCons(sum(x[i,t] for i in range(I))== sum(y[i,j,t] for i in range(I) for j in range(J)))
    for i in range(I):
        for j in range(J):
            model.addCons(z[i,j]-y[i,j,t] >= 0)
model.writeProblem("../../lp_file/MF_Production Planning Problem_Inventory-routing Production Planning Problem.lp")