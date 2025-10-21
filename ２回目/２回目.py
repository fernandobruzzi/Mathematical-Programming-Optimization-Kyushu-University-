import numpy as np

def problem_2():
    x=[8,11,13,10,15,19,17,20]
    y= [115,124,138,120,151,186,169,193]

    x = np.array(x)
    y = np.array(y)
    n= x.size

    b_1 = np.sum(y) - ((np.sum(x*y)*np.sum(x))/np.sum(x*x))
    b_2 = n - ((np.sum(x)*np.sum(x))/np.sum(x*x)) 
    b = b_1/b_2
    a = (np.sum(x*y)-b*np.sum(x))/np.sum(x*x)
    print(f"a = {round(a,4)}, and b ={round(b,4)}")
    return

import pulp 

def problem_3():
    model = pulp.LpProblem(name="Production_Planning", sense=pulp.LpMaximize)

    x_1= pulp.LpVariable(name="x1", lowBound=0,cat='Integer')
    x_2= pulp.LpVariable(name="x2", lowBound=0,cat='Integer')

    model+=x_1+x_2
    model+=3*x_1+2*x_2<=12
    model+=x_1+2*x_2<=8

    model.solve()
    print(f"ステータス: {pulp.LpStatus[model.status]}")
    print("--- 最適な生産計画 ---")
    print(f"ケチャップ (x1) の生産量: {pulp.value(x_1):.4f} 単位")
    print(f"トマトジュース (x2) の生産量: {pulp.value(x_2):.4f} 単位")
    print("--------------------")
    print(f"合計の最大生産量: {pulp.value(model.objective):.4f} 単位")
    return

problem_3()

def lpprob():
    model = pulp.LpProblem(name="Optmization Problem", sense=pulp.LpMaximize)

    x_1= pulp.LpVariable(name="x1", lowBound=0,cat='Continuous')
    x_3= pulp.LpVariable(name="x3", lowBound=0,cat='Continuous')
    x_4= pulp.LpVariable(name="x4", lowBound=0,cat='Continuous')
    x_5= pulp.LpVariable(name="x5", lowBound=0,cat='Continuous')
    x_6= pulp.LpVariable(name="x6", lowBound=0,cat='Continuous')
    x_7= pulp.LpVariable(name="x7", lowBound=0,cat='Continuous')

    model+= 2*x_1+3*(x_4-x_5)-x_3

    model+=3*x_1+(x_4-x_5)+5*x_3+x_6==10
    model+=x_1+2*(x_4-x_5)+5*x_3+x_7==5
    model+=4*x_1-2*(x_4-x_5)-x_3==7

    model.solve()
    print(f"ステータス: {pulp.LpStatus[model.status]}")
    print("--- 最適解 ---")
    print(f"x1: {pulp.value(x_1):.4f}")
    print(f"x2: {pulp.value(x_4-x_5):.4f}")
    print(f"x3: {pulp.value(x_3):.4f}")
    print(f"x4: {pulp.value(x_4):.4f}")
    print(f"x5: {pulp.value(x_5):.4f}")
    print(f"x6: {pulp.value(x_6):.4f}")
    print(f"x7: {pulp.value(x_7):.4f}")

    print("--------------------")
    print(f"max数値: {pulp.value(model.objective):.4f} ")
    return


lpprob()