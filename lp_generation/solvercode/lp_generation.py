import pyscipopt as scp
import json
with open('../data/1th_hyperparaminfo.json','r') as f:
    hyperinfo = json.load(f)
with open('../data/1th_paraminfo.json','r') as f:
    paraminfo = json.load(f)
machinenum = hyperinfo['machinenumber']
tasknum = hyperinfo['tasknumber']
resourcenum = hyperinfo['resourcenum']

machineavailabletask = paraminfo['machineavailabletask']
resourceconsuming = paraminfo['resourceconsuming']
totalresource = paraminfo['totalresource']
conficttask = paraminfo['conficttask']
#origintask = paraminfo['origintask']
print(len(conficttask),machinenum)
model = scp.Model()#建立模型
#创建变量
x = {}
y = {}
for j in range(machinenum):
    y[j] = model.addVar(name=f"y{j}",vtype = "B")
    for i in range(tasknum):
        x[i,j] = model.addVar(name = f"x{i}_{j}",vtype = "B")

#创建目标函数  
model.setObjective(sum(y[j] for j in range(machinenum)),"minimize")

#添加约束
for j in range(machinenum):
    model.addCons(sum(x[i,j] for i in range(tasknum))==1)
    for d in range(resourcenum):
        model.addCons(y[j]*totalresource[j][d]>=sum(x[i,j]*resourceconsuming[i][d] for i in range(tasknum)) )
        cons = [x[i,j] for i in conficttask[d]]
        if cons !=[] and j%2==0:
            model.addCons(-1*sum(cons)>=-1)

model.writeProblem("model4.lp")
