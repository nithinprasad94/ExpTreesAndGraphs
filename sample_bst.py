import random
import math

class tree_node(object):

    def __init__(self,val,left,right):
        self.x = val
        self.left = left
        self.right = right

def generate_randomized_trees(num_nodes):

    random.seed(0)

    head1 = None
    head2 = None
    
    for i in range(num_nodes):
        rand_val = round(random.random()*50) #Generates a rounded random number from 1-25

        print(rand_val)
        
        temp_node1 = tree_node(rand_val,None,None)
        temp_node2 = tree_node(rand_val,None,None)
        
        head1 = insert_node_balanced(head1,temp_node1)
        head2 = insert_node_bst(head2,temp_node2)

        #print_tree(head2)
        
    return (head1,head2)

def insert_node_bst(head,node):

    if head == None:
        head = node
        return head

    if head.left == None and node.x < head.x:
        head.left = node
        return head
    
    if head.right == None and node.x >= head.x:
        head.right = node
        return head
    
    inserted = False

    curr = head
    prev = curr
    choix = ""

    while curr != None:

        prev = curr
        
        if node.x >= prev.x:
            curr = curr.right
            choix = "right"

        if node.x < prev.x:
            curr = curr.left
            choix = "left"
            
    if choix == "right":
        prev.right = node
    elif choix == "left":
        prev.left = node

    return head

def insert_node_balanced(head,node):

    if head == None:
        head = node
        return head

    if head.left == None:
        head.left = node
        return head

    if head.right == None:
        head.right = node
        return head
    
    nodes = [head.left,head.right]
    children = []

    while nodes != None:

        leftmost_node = node
        
        for n in nodes:
            if n.left == None:
                n.left = node
                return head
            if n.right == None:
                n.right = node
                return head
            children.append(n.left)
            children.append(n.right)

        nodes = []
        nodes = children[:]
        children = []

    leftmost_node.left = node
    return head

def depth(head):

    if head == None:
        return 0

    else:
        return 1 + max(depth(head.left),depth(head.right))

def print_tree(head):

    if head == None:
        print("--Empty Tree--")
        return

    head = fill_voids(head)

    tree_depth = depth(head)
    
    print("Tree depth: ",tree_depth)

    spaces_count_list = []

    covered_num = int(2**(tree_depth-1)/2)
    for i in range(tree_depth):
        if covered_num > 0:
            spaces_count_list.append(2*(2*covered_num-1))
        else:
            spaces_count_list.append(covered_num)
            
        if covered_num > 1:
            covered_num = int(covered_num/2)
        else:
            covered_num = 0

    #print(spaces_count_list)

    nodes = [head.left,head.right]
    children = []

    curr_depth = 0
    print(' '*spaces_count_list[curr_depth] + str(head.x))

    while nodes != []:
        curr_depth += 1

        node_string = ' '*spaces_count_list[curr_depth]
        
        for n in nodes:
            if (n != None):                        
                node_string = node_string + str(n.x).zfill(2) + ' '*spaces_count_list[curr_depth-1]
                if n.left != None:
                    children.append(n.left)
                if n.right != None:
                    children.append(n.right)

        print(node_string)        
        
        nodes = []
        nodes = children[:]
        children = []

    (head,dummy) = remove_voids(head)
    
def fill_voids(head):
    #Makes a 'complete' BST by filling in empty spaces with garbage data (useful for printing)

    if head == None:
        return head

    tree_depth = depth(head)

    parents = [head]

    for i in range(2,tree_depth+1):

        children = []
        
        for node in parents:
            if node.left == None:
                node.left = tree_node('NA',None,None)
            if node.right == None:
                node.right = tree_node('NA',None,None)
            children.append(node.left)
            children.append(node.right)

        parents = []
        parents = children[:]

    return head

def remove_voids(head):

    if head.left != None:
        (dummy,remove_left) = remove_voids(head.left)
        if remove_left == True:
            head.left = None
    if head.right != None:
        (dummy,remove_right) = remove_voids(head.right)
        if remove_right == True:
            head.right = None

    if head.left == None and head.right == None and head.x == 'NA':
        return (head,True)

    return (head,False)

def balance_bst(head):

    sorted_list = [head.x]
    #print("Building list ...")
    #print(sorted_list)
    #print(head.x)
    sorted_list = build_list(sorted_list,head)
    #print("Just created an unsorted list...")
    #print(sorted_list)

    #print(len(sorted_list))
    #for elem in sorted_list:
    #    print(elem)
    sorted_list.sort()
    #print("Just sorted list...")
    #print(sorted_list)

    list_length = len(sorted_list)

    head_index = math.floor(list_length/2)
    #print("Head index: ",head_index)

    head = tree_node(sorted_list[head_index],None,None)

    left = balance_sub_list(sorted_list[:head_index])
    right = balance_sub_list(sorted_list[head_index+1:])

    head.left = left
    head.right = right

    return head

def balance_sub_list(sorted_sublist):

    list_length = len(sorted_sublist)
    #print("Sorted sublist: ",sorted_sublist)
    #print("List length: ",list_length)

    if list_length == 0:
        return None

    head_index = math.floor(list_length/2)
    if list_length == 1:
        head_index = 0

    #print("head index: ",head_index)
    head = tree_node(sorted_sublist[head_index],None,None)

    #print(sorted_sublist[:head_index])
    #print(sorted_sublist[head_index+1:])
    
    left = balance_sub_list(sorted_sublist[:head_index])
    right = balance_sub_list(sorted_sublist[head_index+1:])

    head.left = left
    head.right = right

    return head

def build_list(sorted_list,head):
    #print("calling build_list",head.x)

    if head.left == None and head.right == None:
        #print("reached leaf ...")
        return sorted_list
    
    if head.left != None:
        #print("adding left")
        sorted_list.append((head.left.x))
        #print(sorted_list)
        sorted_list = build_list(sorted_list,head.left)
    if head.right != None:
        #print("adding right")
        sorted_list.append((head.right.x))
        #print(sorted_list)
        sorted_list = build_list(sorted_list,head.right)

    return sorted_list
        
(head1,head2) = generate_randomized_trees(7)
print("Testing tree...")
print_tree(head1)
print("Testing tree 2...")
print_tree(head2)
head2 = balance_bst(head2)
print_tree(head2)
    
