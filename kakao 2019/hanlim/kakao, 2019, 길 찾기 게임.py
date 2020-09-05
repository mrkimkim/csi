import sys
sys.setrecursionlimit(10**6)  # 파이썬의 경우 재귀 깊이가 1000으로 제한이 되어 있다.
                              # 그런데 nodeinfo의 길이는 1 ~ 1000 이고
                              # 아래의 preorder, postorder 재귀의 경우 각각 1000번은 재귀하므로 상한선을 바꿔줄 필요가 있다.

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

            else : return  # 이거 없으면 루프가 안 끝난다.


    def preorderTraversal(self,node,arr) :

        self.array = arr
        self.array.append(node.index)

        if not node.left == None : self.array = self.preorderTraversal(node.left,self.array)
        if not node.right == None : self.array = self.preorderTraversal(node.right, self.array)

        return self.array


    def postorderTraversal(self, node, arr) :

        self.array = arr

        if not node.left == None : self.array = self.postorderTraversal(node.left, self.array)
        if not node.right == None : self.array = self.postorderTraversal(node.right, self.array)

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

    answer = []

    answer.append(tree.preorderTraversal(tree.root,[]))
    answer.append(tree.postorderTraversal(tree.root,[]))


    return answer


# Driver Code

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

print(solution(nodeinfo))
