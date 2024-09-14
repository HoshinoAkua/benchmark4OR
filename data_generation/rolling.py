import json
import random
import numpy as np

infinite = 10

def function(bound):
    N1 = np.random.randint(0, bound)
    N2 = np.random.randint(0,bound)
    low = min(N1, N2)
    upper = max(N1, N2)
    return np.array([i for i in range(low, upper+1)])
def element_wise(bound):
    bound = int(bound)
    number = np.random.randint(0,bound)
    
    target = list(range(bound))
    return np.random.choice(target,number,replace=False)


def auto_param(param_info):
    #初始化超参数
    hyperparameterinfo = {}
    for type,range_,name in zip(param_info['hyperparametertype'],
                            param_info['hyperparameterrange'],param_info['hyperparametername']):
        if range_[1] == 'infinite':
            range_[1] = infinite
        if type == 'int':
            data = random.randint(range_[0],range_[1])
            
        elif type == 'float':
            data = random.uniform(range_[0],range_[1])
        #先假设不会在超参数上出现range型数据
        elif type == 'intrange':
            pass
        elif type == 'floatrange':
            pass
        hyperparameterinfo[name] = data
        #初始化一般参数:
    parameterinfo = {}
    for type, range_, name, dependecy, dependecy_type in zip(param_info['parametertype'],
                                            param_info['parameterrange'],
                                            param_info['parametername'],
                                            param_info['parameterdependency'],
                                            param_info['dependencytype']):
        if range_[1] == 'infinite':
            range_[1] = infinite
        if range_[0] == '-infinite':
            range_[0] = -infinite
        count = []
        
        for d,t in zip(dependecy, dependecy_type):
            if t == 'circulate':
                count.append(hyperparameterinfo[d])#count 存放的是角标的参数,
            elif t == 'bound':
                bound = hyperparameterinfo[d]
                assert isinstance(bound, int) or isinstance(bound, list) or isinstance(bound, float), f"bound类型的数据必须是列表, 浮点数或者整数, 目前的类型为{type(bound)}"
                if isinstance(bound, int) or isinstance(bound, float) :
                    range_[0] = 0
                    range_[1] = bound
                else:
                    range_ = bound
        #对于每一个参数, 他有多少个存放在count中, len(count)代表了下角标的长度, bound存放了参数的取值范围. 
        #且所有的bound都以列表的形式存在.
        # if count == []: #假如我只需要生成一个随机数,那么在参数里面可能不会写circulate约束, 而只有bound约束. 因此需要给count一个值, 否则会生成一个numpy整数.
        #     count.append(1)
            
        if type == 'int':
            param = np.random.randint(range_[0], range_[1]+1, size=count)
        elif type == 'float':
            param = np.random.uniform(range_[0],range_[1],size=count)
        elif type == 'intrange':
            param = np.zeros(shape=count)
            delta = range_[1]-range_[0]
            param = param+delta
            f1 = np.frompyfunc(function, 1,1)
            param = f1(param)+range_[0]
        elif type == 'discrete':#浮点数范围数据先不管
            param = np.zeros(shape=count)+(range_[1]-range_[0])
            f1 = np.frompyfunc(element_wise,1,1)
            param = f1(param)+range_[0]
        # 每一个参数都被一个numpy矩阵存起来了.
        if len(param.shape) == 0:
            parameterinfo[name] = param.item()
        else:
            parameterinfo[name] = param
    return hyperparameterinfo, parameterinfo