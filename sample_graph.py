import random

class neighbour(object):

    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

class graph_node(object):

    def __init__(self,node,val,neighbour_nodes,weights):
        self.node = node
        self.val = val
        if len(neighbour_nodes) != len(weights):
            print("Error with edge weights!")
        self.neighbours = {}
        self.num_neighbours = 0
        if len(neighbour_nodes) > 0:
            #print(neighbour_nodes)
            #print(weights)
            for i in range(len(weights)):
                node = neighbour_nodes[i]
                weight = weights[i]
                self.neighbours[node] = weight
        self.colour = 0

    def update_neighbours(self,neighbour,weight):
        self.neighbours[neighbour] = weight

    def remove_neighbours(self,neighbour):
        rem = self.neighbours.popitem(neighbour)
        
def create_random_graph(num_nodes):

    random.seed(0)

    graph_nodes = []
    
    for i in range(num_nodes):

        #print(i)

        node_value = round(1 + random.random()*49)

        num_neighbours = 0 + round(random.random()*min(i,3))

        neigh_nodes = []
        edge_weights = []
        
        if num_neighbours == 0:
            graph_nodes.append(graph_node(i,node_value,[],[]))

        else:
            for j in range(num_neighbours):

                new_node_acq = False

                while not new_node_acq:
                    node = round(0 + random.random()*(i-1))
                    if node not in neigh_nodes:
                        neigh_nodes.append(node)
                        weight = round(1 + random.random()*8)
                        edge_weights.append(weight)

                        graph_nodes[node].update_neighbours(i,weight)

                        new_node_acq = True
            #print(num_neighbours)
            #print(neigh_nodes)
            #print(edge_weights)
            graph_nodes.append(graph_node(i,node_value,neigh_nodes,edge_weights))

    return graph_nodes

def print_graph(graph_nodes):

    num_nodes = len(graph_nodes)

    for i in range(len(graph_nodes)):
        print("Node: ",graph_nodes[i].node)
        print("Value: ",graph_nodes[i].val)
        print("Neighbours: ",graph_nodes[i].neighbours,"\n")

def add_random_node(graph_nodes,val,neighbour_nodes,weights):

    node = len(graph_nodes)
    graph_nodes.append(graph_node(node,val,neighbour_nodes,weights))

    for i in range(len(neighbour_nodes)):
        graph_nodes[neighbour_nodes[i]].update_neighbours(node,weights[i])

    return graph_nodes

def del_node(graph_nodes,node):

    pass    

def traversal_bfs(graph_nodes):

    traversed_nodes = []
    traversed_ids = []
    
    elem_list = [graph_nodes[0]]

    future_nodes = []
    
    while len(elem_list) != 0:
        for elem in elem_list:

            traversed_nodes.append(elem)
            traversed_ids.append(elem.node)

            elem.colour = 2 #2 means visited, 0 is unmarked, 1 is marked

            neighbour_list = list(elem.neighbours.keys())
            print(neighbour_list)
            
            for neighbour in neighbour_list:

                if graph_nodes[neighbour].colour == 0:

                    future_nodes.append(graph_nodes[neighbour])
                    graph_nodes[neighbour].colour = 1

        elem_list = []
        elem_list = future_nodes[:]
        future_nodes = []

    for node_ref in graph_nodes:
        node_ref.colour = 0 #Once BFS is done, unmark all nodes

    return [traversed_nodes,traversed_ids]
    

def traversal_dfs(graph_nodes):

    traversed_nodes = []
    traversed_ids = []

    if len(graph_nodes) == 0:
        return [None,None]
    
    (traversed_nodes,traversed_ids) = dfs_rec(graph_nodes,graph_nodes[0])

    for node_ref in graph_nodes:
        node_ref.colour = 0
    
    return [traversed_nodes,traversed_ids]

def dfs_rec(graph_nodes,node):

    traversed_nodes = []
    traversed_ids = []
    
    if node.colour != 2:

        traversed_nodes.append(node)
        traversed_ids.append(node.node)
        
        node.colour = 2

        node_id = node.node
        
        neighbours = list(graph_nodes[node_id].neighbours.keys())

        for neighbour in neighbours:

            if graph_nodes[neighbour].colour == 0:
                graph_nodes[neighbour].colour = 1

                [int_nodes,int_ids] = dfs_rec(graph_nodes,graph_nodes[neighbour])

                traversed_nodes.extend(int_nodes)
                traversed_ids.extend(int_ids)

        return [traversed_nodes,traversed_ids]

    else:
        return [traversed_nodes,traversed_ids]

#graph1 = create_random_graph(10)
#print_graph(graph1)

graph2 = create_random_graph(1)
#print_graph(graph2)
graph2 = add_random_node(graph2,20,[0],[3])
#print_graph(graph2)
graph2 = add_random_node(graph2,12,[0,1],[9,2])
#print_graph(graph2)
graph2 = add_random_node(graph2,7,[0,1,2],[7,4,1])
#print_graph(graph2)
graph2 = add_random_node(graph2,13,[2,3],[3,8])
#print_graph(graph2)
graph2 = add_random_node(graph2,33,[1],[5])
#print_graph(graph2)
graph2 = add_random_node(graph2,19,[1],[7])
#print_graph(graph2)
graph2 = add_random_node(graph2,39,[3,6],[8,4])
#print_graph(graph2)
graph2 = add_random_node(graph2,18,[6],[1])
#print_graph(graph2)
graph2 = add_random_node(graph2,3,[8],[6])
#print_graph(graph2)
graph2 = add_random_node(graph2,10,[8],[2])
#print_graph(graph2)
graph2 = add_random_node(graph2,29,[7],[4])
#print_graph(graph2)
graph2 = add_random_node(graph2,44,[11],[3])
print_graph(graph2)

[nodes_t,ids_t] = traversal_bfs(graph2)
print(ids_t)

[nodes_t,ids_t] = traversal_dfs(graph2)
print(ids_t)
