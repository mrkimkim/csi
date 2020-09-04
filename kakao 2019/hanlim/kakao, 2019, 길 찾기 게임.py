class Node() :

    def __init__(self, arr) :

        self.index = arr[2]
        self.data = arr[1]
        self.left = None
        self.right = None

    def __str__(self) :

        return str(self.index)



class Tree() :

    def __init__ (self) :

        self.root = None
        

    def insert(self, arr) :

        new_node = Node(arr)

        if self.root == None :

            self.root = new_node


        node = self.root

        while True :

            pre_node = node

            if node.data > new_node.data :

                node = node.left

                if node == None :

                    node = new_node

                    pre_node.left = node

            elif node.data < new_node.data :

                node = node.right

                if node == None :

                    node = new_node

                    pre_node.right = node


    def preorderTraversal(self,node,arr) :

        self.array = arr
        self.array.append(node.index)

        if not node.left == None : self.array = self.preorderTraversal(node.left,self.array)
        if not node.right == None : self.array = self.preorderTraversal(node.right, self.array)

        return self.array


    def postorderTraversal(self, node, arr) :

        self.array = arr

        if not node.left == None : self.array = self.postorderTraversal(node.left, self.array)
        if not node.right == None : self.array = self.postorderTravesal(node.right, self.array)

        self.array.append(node.index)

        return self.array


def switchXY(arr, n) :

    temp = []

    for i in range(n) :

        arr[i].reverse()
        temp.append(arr[i]+[i+1])

    temp.sort()
    temp.reverse()

    return temp


def solution(nodeinfo):

    n = len(nodeinfo)

    switched = switchXY(nodeinfo,n)

    tree = Tree()


    for i in range(n) :

        tree.insert(switched[i])

    print(tree.root.data, tree.root.index)

    answer = []

    answer.append(tree.preorderTraversal(tree.root,[]))
    answer.append(tree.postorderTraversal(tree.root,[]))


    return answer


# Driver Code

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

print(solution(nodeinfo))
