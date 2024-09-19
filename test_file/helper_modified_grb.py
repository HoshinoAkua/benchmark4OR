import gurobipy as gp
from gurobipy import GRB
import torch
import numpy as np

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def graph_generator(ins_name):
    # Create a Gurobi model
    m = gp.read(ins_name)
    nvars = m.NumVars
    # Gurobi handles variables and constraints slightly differently
    mvars = m.getVars()
    # Sort variables by name (Gurobi does not guarantee order)
    mvars = sorted(mvars, key=lambda v: v.VarName)
    var_feature = torch.zeros((nvars, 2))

    
    # Obtain variable features
    for n in range(nvars):
        var = mvars[n]
        obj_coeff = var.Obj
        lb = var.LB
        ub = var.UB
        if ub != 1e20:
            m.addConstr(var <= 1e20)
        if lb != 0:
            m.addConstr(var >= 0)
        m.addConstr(var >= lb)
        m.addConstr(var <= ub)
        bin = 1 if var.VType == GRB.BINARY else 0
        feature = [obj_coeff, bin]
        var_feature[n] = torch.tensor(feature)

    # Obtain constraint features
    # for i in range(ncons):
        # cons = mcons[i]
        # sense = cons.Sense
        # rhs = cons.RHS
        # # lhs = -np.inf  # In Gurobi, the lower bound can be implicitly negative infinity
        # b = rhs
        # if sense == GRB.EQUAL:
            
        #     cons_sense = 0.0
        # elif sense == GRB.LESS_EQUAL:
            
        #     cons_sense = -1.0
        # elif sense == GRB.GREATER_EQUAL:
            
        #     cons_sense = 1.0
        # else:
        #     raise NotImplementedError('我只写了大于等于, 小于等于, 等于')
        
        # feature = [b, cons_sense]
        # cons_feature[i] = torch.tensor(feature)
    

    ncons = m.NumConstrs
    mcons = m.getConstrs()
    cons_feature = torch.zeros((ncons, 2))
    A = torch.zeros((ncons, nvars))
    for i in range(ncons):
        cons = mcons[i]
        sense = cons.Sense
        rhs = cons.RHS
        # lhs = -np.inf  # In Gurobi, the lower bound can be implicitly negative infinity
        b = rhs
        if sense == GRB.EQUAL:
            
            cons_sense = 0.0
        elif sense == GRB.LESS_EQUAL:
            
            cons_sense = -1.0
        elif sense == GRB.GREATER_EQUAL:
            
            cons_sense = 1.0
        else:
            raise NotImplementedError('我只写了大于等于, 小于等于, 等于')
        
        feature = [b, cons_sense]
        cons_feature[i] = torch.tensor(feature)
        for j in range(nvars):
            var = mvars[j]
            coeff = m.getCoeff(cons, var)  # Gurobi-specific function for constraint coefficients
            A[i, j] = coeff

    return A, var_feature, cons_feature