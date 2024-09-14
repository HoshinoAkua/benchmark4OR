import torch
import torch.nn.functional
import numpy as np

class WLtest():
    def __init__(self, g1, w1, v1, g2, w2, v2):#w是约束节点, v是变量节点
        self.g1 = g1
        self.g2 = g2
        #把特征先用numpy的形式存储
        if isinstance(w1, torch.Tensor):
            self.w1 = w1
            self.v1 = v1
        else:
            self.w1 = torch.tensor(w1)
            self.v1 = torch.tensor(v1)
        if isinstance(w2, torch.Tensor):
            self.w2 = w2
            self.v2 = v2
        else:
            self.w2 = torch.tensor(w2)
            self.v2 = torch.tensor(v2)
            
        self.feature1 = torch.vstack((self.w1, self.v1))
        self.feature2 = torch.vstack((self.w2, self.v2))
        
        
    def coloring(self):
        if isinstance(self.feature1, np.ndarray):
            self.feature = np.vstack((self.feature1, self.feature2))
        elif isinstance(self.feature1, torch.Tensor):
            self.feature = torch.vstack((self.feature1, self.feature2)).cpu().numpy() 
        #对全体feature(两个图一起)进行染色
        hash = {}
        N = len(self.feature)
        N1 = len(self.feature1)
        copy = torch.zeros(N)
        for i in range(N):
            if tuple(self.feature[i]) in hash.keys():
                pass
            else:
                hash[tuple(self.feature[i])] = i
            copy[i] = hash[tuple(self.feature[i])]
        copy = copy.to(torch.int64)
        coding = torch.nn.functional.one_hot(copy)
        #染完色之后把两个进行分开
        coding_f1 = coding[:N1]
        coding_f2 = coding[N1:]
        self.color1, self.color2 = coding_f1.to(torch.float), coding_f2.to(torch.float)
    
    def symmetry_detection(self, N1, M1, M2 ,N11, N21):
        J = N1/M1
        #这里N1表示共有N1个节点, M1表示共有M1类节点. 那么每类节点就有 J= N1/M1个
        '''
        在bin-packing问题:
        min y1+y2
        s.t. \\sum_i^4 c_i*x_{i,1} + d1y1 \\le 0
            \\sum_i^4 c_i*x_{i,2} + d2y2 \\le 0
        在这个例子中, 共有10个节点(N1=10), 共有5类节点{x_{i,j} for i=1,2,3,4, y_j} for j={1,2}
        因此 J = 2.
        '''
        if J - int(J) != 0:
            raise Warning('出现了未知的对称性情况')
        color_var1 = self.color1[:N11]
        color_var2 = self.color2[:N21]
        is_g1_blocked = True
        is_g2_blocked = True
        samecolor_cluster1 = {}
        samecolor_cluster2 = {}
        for i,color in enumerate(color_var1):
            if color not in samecolor_cluster1.keys():
                samecolor_cluster1[color] = [i]
            else:
                samecolor_cluster1[color].append(i)#在color_cluster中, 每个特征对应着它们在var_clor中的index们
        for i,color in enumerate(color_var2):
            if color not in samecolor_cluster2.keys():
                samecolor_cluster2[color] = [i]
            else:
                samecolor_cluster2[color].append(i)
        '''
        如果图G1\\in (m,n)可以被分为几个子图 iff 它的邻接矩阵是可以分块的 iff 这个分块的子矩阵维度是J*M1,
        那么对大的矩阵G1的某k行求和 -> v \\in (1,n)则torch.nonzero(v) == J
        '''
        
        var_idx = list(samecolor_cluster1.values())[0] #这个values是一个list, 表示所有具有相同特征的节点们的index
        for idx in var_idx:
            connect_cons_idx = torch.nonzero(self.g1[:,idx]).squeeze() #对应的不同类的constraint
            v = torch.sum(self.g1[connect_cons_idx],dim = 0)
            if len(torch.nonzero(v)) != M1:
                is_g1_blocked = False
                raise Warning('存在图1是不可分割的')
        var_idx = list(samecolor_cluster2.values())[0]
        for idx in var_idx:
            connect_cons_idx = torch.nonzero(self.g2[:,idx]).squeeze()
            if len(torch.nonzero(v)) != M2:
                is_g2_blocked = False
                raise Warning('存在图2是不可分割的')
        return is_g1_blocked == is_g2_blocked
            



    def detection(self):#检测self.coding1和self.coding2是否相同
        N1 = len(self.color1)
        N11 = len(self.w1) #指的是var的数量
        
        N2 = len(self.color2)
        N21 = len(self.w2)
        
        M1 = len(self.color1[0])
        M2 = len(self.color2[0])
        assert M1 == M2, "没有统一编码"
        if N1 != N2 or N11!=N21:
            return False
        elif M1 == N1:
            return True
        else: #出现了对称性
            return self.symmetry_detection(N1, M1, M2, N11, N21)
        #在检测的过程中会只会出现以下几种情况
        #1. 两张图的节点个数不同, 直接不同构
        #2. 节点个数相同, 但是变量节点个数不同, 也是不同构
        #3. 节点个数相同, 变量节点个数相同, 约束节点个数肯定是相同的
        #4. 所有节点个数相同, 但是a图中存在b图中没有的节点, 且没有重复节点, 表现在one-hot上就是编码长度多于节点个数.
        #5. 注意: 不会出现重复节点, 因此第一个图是N11加N12个节点特征, 第二张图要是和第一张图同构也应该是这些特征, 所以可以通过特征的个数判断是否同构. 
    def test(self, maxiter=2):
        for i in range(maxiter):
            #对feature进行染色
            self.coloring() #染色信息存储在self.color
            self.w1 = self.color1[:len(self.w1)] + self.g1@self.color1[len(self.w1):]
            self.v1 = self.color1[len(self.w1):] + self.g1.T@self.color1[:len(self.w1)]
            self.w2 = self.color2[:len(self.w2)] + self.g2@self.color2[len(self.w2):]
            self.v2 = self.color2[len(self.w2):] + self.g2.T@self.color2[:len(self.w2)]
        
        self.coloring()
        if self.detection():
            return "same"
        else:
            return "not same"        
        