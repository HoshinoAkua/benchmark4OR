import pyscipopt as scp
import json
with open("../../data/parameter_The Knapsack Problem.json0th_paraminfo.json") as f:
    info = json.load(f)
N = info["N"]
W = info["W"]
w = info["w_{i}"]
v = info["v_{i}"]
model = scp.Model()
x = {}
for i in range(N):
    x[i] = model.addVar(name = f"x{i}", vtype = "C",lb = 0)
    
model.setObjective(sum(v[i]*x[i] for i in range(N)))
model.addCons(sum(w[i]*x[i] for i in range(N))<=W)

model.writeProblem("../../test/knapsck problem.lp")