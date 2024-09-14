## 问题: 图同构 ?$\iff$? 两个优化问题等价

##### 优化问题的一般形式

$$
\min f_0(X)\\
s.t.\quad f_i(X)\le0\\
h_j(X) = 0
$$



两个优化问题之间的转换方式:

1. 对obj function进行变换.

​	假设函数$\phi$单调, 则
$$
\min \phi (f_0(X))\\
s.t.\quad f_i(X)\le0\\
h_j(X) = 0
$$
​	与原问题等价.

2. 对constrain进行变换.

​	只需保证: 若$\phi$作用在$f_i$上时, $\phi(u)\le0\iff u\le0$; 若$\phi$作用在$h_i$, 则$\phi(u)=0\iff u=0$, 那我们就有:
$$
\min f_0(X)\\
s.t.\quad \phi_i(f_i(X))\le0\\
\phi_j(h_j(X)) = 0
$$
​	与原问题等价.

3. 对优化变量进行变换:

​	假设存在一个可逆变换 $\phi$ 有: $\phi(Z)=X$,  这样优化问题:
$$
\min_X f_0(\phi(Z))\\
s.t.\quad f_i(\phi(Z))\le0\\
h_j(\phi(Z)) = 0\\
\phi(Z)=X
$$

4. 添加松弛变量.
   $$
   \min f_0(X)\\
   s.t.\quad f_i(X)+\epsilon_i=0\\
   h_j(X) = 0\\
   \epsilon_i\ge0
   $$



**优化问题的等价:** 

case1. 最广义的定义:

设优化问题($P$)的解集为sol($P$), 那么对于两个优化问题$P_1$和$P_2$, 我们有:
$$
\exist \phi\,,\text{which is invertible},s.t.  \,\forall x^*\in sol(P_1), \phi(x^*)\in sol(P_2); \forall y^*\in sol(P_2), \phi^{-1}(y^*)\in sol(P_1)
$$
case2. 现在考虑一般的MILP或者LP问题, 同时规定这个变换$\phi$仅仅是permutation, 则优化问题的等价可以表述为:
$$
\forall x^*\in sol(P_1), \phi x^*\in sol(P_2); \forall y^*\in sol(P_2), \phi^{-1}y^*\in sol(P_1)
$$


Case3. 等价优化定义:

Claim: 对于我们的benchmark, 我们所有的mathematical formulation是optimal formulation, 即:

1. benchmark中明确规定了优化的变量
2. benchmark中明确规定了优化约束(约束的数量和形式的最优), 如果没有明确说明的都是common sense.
3. 目标函数(目标函数形式的最优)



一个优化问题:

问题: 
$$
C^Tx\\s.t. Ax\circ b
$$
下面定义其等价类:

1. 满足约束数量相同且约束关系顺序可变

2. 对于优化变量进行permutation. 





# 优化置换等价类

设$P_1, P_2\text{为permutation matrix}$: 
$$
1.P_2b=\hat b\\
2.P_1^TC=\hat C\\
3. P_2AP_1=\hat A
$$
那么我们定义新的优化问题:
$$
\hat C^Tx\\
s.t.\,\hat Ax\circ \hat b
$$
与原问题等价.



# 优化问题→二分图

定义优化问题的形式:
$$
C^Tx\\s.t. Ax\circ b
$$
假设有$m$个优化变量, 有$n$个约束, 这样我们设计二分图 $G = (E, V\cup W)$, 其中$E$表示图的边, $V, W$表示节点集合. 

$E$可以视作一个$V\times W\mapsto \mathbb{R}$的映射. 对任意的 $(v,w)\in V\times W$, 我们有$E(v,w):=E_{v,w}\in \mathbb{R}$ .







# 优化问题的置换等价$\iff$ 二分图同构 

 **图同构是否推出来优化问题等价?**

这个问题我倾向于图同构可以推出来优化问题等价. 

首先定义一个优化问题的图:

$G= (E,V\cup W)$, 用$F$表示特征矩阵. 它的邻接带权重矩阵为$A$, 则图同构意味着存在一个permutation $P$, 使得:
$$
P^TA_1P = A_2;P^TF_1=F_2
$$
为了方便说明, 我们再规定邻接矩阵为分块矩阵$A = \begin{bmatrix}0&A^{(1)}\\A^{(1)T}&0\end{bmatrix}$, 其中$A^{(1)}$表示cons对vars的关系(沿行为cons, 沿列为vars). 这样我们可以把特征矩阵写为$F = \begin{bmatrix}F^{(1)}\\F{(2)}\end{bmatrix}$, 上半部分表示cons的特征, 下半部分表示Vars的特征.

这样我们的permutation矩阵一定是分块矩阵$P= \begin{bmatrix}P^{(1)}&0\\0&P^{(2)}\end{bmatrix}$, 上半部分表示对cons进行变换, 下半部分表示对Vars进行变换.

假设一个标准的优化问题:
$$
\min_x C^Tx\\Dx\le b
$$

1. 它的图和优化问题公式一一对应. 

2. 仅对vars进行变换后, 即$\hat A = \begin{bmatrix}0&A^{(1)}P^{(2)}\\P^{(2)T}A^{(2)}&0\end{bmatrix}$, 则这个图对应的优化问题为

   
   $$
   \min_x C^TP^{(2)}x\\
   DP^{(2)}x\le b
   $$

符合我们之前对置换等价类的定义.

3. 对cons或者(cons和var)同时变换, 同理

##### 优化问题等价是否推出来图同构?

优化问题等价, 根据定义可以找出来两个置换矩阵$P_1,P_2$, 其中$P_1$是对vars进行置换, $P_2$​是对cons进行置换, 那么两个优化问题等价意味着

嘻嘻嘻





# 从数学建模到给定参数生成instance的例子

建模相同$\iff$给定任意相同的参数, 他们的instance(即优化问题)置换等价





# 图同构的检测

对于任意两个数学模型, 我们规定了建模相同$\iff$给定任意相同的参数, 他们的instance(即优化问题)置换等价$\iff$ 两个优化问题对应的二分图同构.

目标: 检测图同构.

主流算法: WL-test.

WL-test算法:



WL-test问题: 对于



如果只是sample某个性质的instance, 那么我们是否会

