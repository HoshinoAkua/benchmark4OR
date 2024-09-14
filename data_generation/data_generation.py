from rolling import auto_param
import json
import numpy as np

import os
K  = 1#生成K个数据
path = './set covering var/parameters'
path_list = os.listdir(path)

def recursive_to_list(arr):
    if not isinstance(arr,np.ndarray):
        if isinstance(arr, np.int32) or isinstance(arr,np.int64): # type: ignore
            return int(arr)
        elif isinstance(arr,np.float64): # type: ignore
            return float(arr)
        else: 
            return arr
    else:
        return [recursive_to_list(i) for i in arr]
    

for filename in path_list:
    with open(os.path.join(path,filename),'r') as f:#注意VM这个数据, 在生成origintask的过程应该设计subparameter, 之后要补上
        data = json.load(f)
    for i in range(K):
        hyparinfo, parainfo = auto_param(data)
        #print(hyparinfo)

        for key in parainfo.keys():
            parainfo[key] = recursive_to_list(parainfo[key])
        for key in hyparinfo.keys():
            hyparinfo[key] = recursive_to_list(hyparinfo[key])
        hyparinfo.update(parainfo)
        with open(f'./data/{filename}{i}th_paraminfo.json','w') as f:
            f.write(json.dumps(hyparinfo,indent=2))
            
