import pulp 

def answer():
    model = pulp.LpProblem(name="Optmization Problem", sense=pulp.LpMaximize)

    x_1= pulp.LpVariable(name="x1", lowBound=0,cat='Continuous')
    x_3= pulp.LpVariable(name="x3", lowBound=0,cat='Continuous')
    x_4= pulp.LpVariable(name="x4", lowBound=0,cat='Continuous')
    x_5= pulp.LpVariable(name="x5", lowBound=0,cat='Continuous')
    x_6= pulp.LpVariable(name="x6", lowBound=0,cat='Continuous')
    x_7= pulp.LpVariable(name="x7", lowBound=0,cat='Continuous')

    model+= 2*x_1+3*(x_4-x_5)-x_3

    model+=3*x_1+(x_4-x_5)+5*x_3+x_6==10
    model+=x_1+2*(x_4-x_5)-3*x_3+x_7==5
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


answer()