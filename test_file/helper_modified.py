import os
import sys
import argparse
import pathlib
import numpy as np
import random
import pyscipopt as scp
import torch
import torch.nn as nn
import pickle


device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
def graph_generator(ins_name):
    
    m = scp.Model()
    m.hideOutput(True)
    m.readProblem(ins_name)
    
    
    nvars = m.getNVars()
    
    mvars = m.getVars()
    
    
    mvars.sort(key=lambda v: v.name)
    
    var_feature = torch.zeros((nvars,2))
   
    
    #得到变量节点的特征
    obj = m.getObjective()
    for n in range(nvars):
        var = mvars[n]
        obj_coeff = obj[var]
        lb = var.getLbOriginal()
        if lb != 0:
            m.addCons(var >=0)
        
        ub = var.getUbOriginal()
        if ub != 1e20:
            m.addCons(var <= 1e20)
        if var.vtype() == 'BINARY':
            bin = 1
        else:
            bin = 0
        m.addCons(var>=lb)
        m.addCons(var <= ub)
        feature = [obj_coeff,bin]
        var_feature[n] = torch.tensor(feature)


    ncons = m.getNConss()
    mcons = m.getConss()
    cons_feature = torch.zeros((ncons,2))
    A = torch.zeros((ncons, nvars))
    #得到约束节点的特征
    for i in range(ncons):
        cons = mcons[i]
        lhs, rhs = m.getLhs(cons), m.getRhs(cons)
        if lhs == rhs:
            sense = 0.0
            b = lhs
        elif lhs == -1e20:
            sense = -1.0
            b = rhs
        elif rhs == 1e20:
            sense = 1.0
            b = lhs
        feature = [b,sense]
        cons_feature[i] = torch.tensor(feature)

    #得到邻接矩阵
    varindx = {}
    for i in range(nvars):
        varindx[mvars[i].name] = i
    A = torch.zeros(ncons,nvars)
    for i in range(ncons):
        row = m.getValsLinear(mcons[i])
        for var in row.keys():
            j = varindx[var]
            value = row[var]
            A[i,j] = value

    return A, var_feature, cons_feature

 
 

