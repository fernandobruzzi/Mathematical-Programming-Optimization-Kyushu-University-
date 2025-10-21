number_to_letter = {0:'A', 1:'B' , 2:'C' , 3:'D' , 4: 'E' ,  5:'F' , 6: 'G', 7:'H', 8:'I', 9:'J' , 10:'K'}

def djikstra(initial_node, final_node, ll):
    g_cost = [float('inf')]*len(ll)
    g_cost[initial_node]=0
    ol_list = [initial_node]
    cl_list= []
    pp_list = [-1]*len(ll)
    id = 0
    while len(ol_list)>0:
        s = ol_list.pop(id)
        if s == final_node:break
        for i in range(len(ll[s])):
            v, cost_v = ll[s][i][0],ll[s][i][1]
            if not(v in cl_list):
                ol_list.append(v)
                prev_cost = g_cost[v]
                g_cost[v] = min(prev_cost,g_cost[s]+cost_v)
                if prev_cost!=g_cost[v]: pp_list[v]=s
        cl_list.append(s)

        min_val = g_cost[id]
        for index in ol_list:
            if g_cost[index]<min_val: 
                min_val= g_cost[index]
                id = index
    if g_cost[final_node]<float('inf'): 
        print("There is an answer!")
        path = []
        i = final_node
        while i!= initial_node:
            path.insert(0,number_to_letter[i])
            i = pp_list[i]
        path.insert(0,number_to_letter[i])
        print(f"The path is {path}")
        print(f"The cost associated to this path is {g_cost[final_node]}")

    else: print("There is no answer!")
    return

# A = 0, B = 1, C = 2, D = 3, E = 4, F = 5, G = 6, H = 7, I = 8, J = 9, K = 10
ll = [[(1,3),(2,5)],
      [(3, 1),(6,10)],
      [(3,4)],
      [(4,9),(5,8)],
      [(7,1),(8,3)],
      [(9,4)],
      [(9,2)],
      [(8,1),(10,5)],
      [(10,1)],
      [(8,1),(10,9)],
      [()]]


djikstra(0,10,ll)