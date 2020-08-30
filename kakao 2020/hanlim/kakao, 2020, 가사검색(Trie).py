class Node(object) :

    def __init__(self, key, data = None) :

        self.key = key
        self.data = data
        self.children = {}


class Trie(object) :

    def __init__ (self) :

        self.head = Node(None) # 루트는 비어있음.

    def insert(self, string) :

        curr_node = self.head


        for char in string :

            if char not in curr_node.children :  # 자식 노드에 해당 글자가 없다면 추가

                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]  # 있다면 트리를 타고 감


        curr_node.data = string  # 노드의 마지막에 데이터 값으로 문자열 자체 지정


    def search(self, string) :

        curr_node = self.head

        for char in string :

            if char in curr_node.children : # 자식 노드에 해당 글자가 있다면 노드를 타고 감. 

                curr_node = curr_node.children[char]

            else :

                return False

        if curr_node.data != None :  # 해당 글자가 있다면 마지막 글자의 data 값이 비어 있으면 안 됨. 

            return True


    def starts_with(self, prefix) :

        curr_node = self.head

        result = []

        subtrie = None


        for char in prefix :

            if char in curr_node.children :

                curr_node = curr_node. children[char]

                subtrie = curr_node # prefix의 마지막 글자까지 노드를 타고 감.

            else :

                return None


        queue = list(subtrie.children.values())

            
        while queue :

            curr = queue.pop()

            if curr.data != None :

                result.append(len(curr.data))

            queue += list(curr.children.values()) # 노드를 타고 가면서 마지막 자손부터 처음순으로 글자 탐색

        return result


def solution(words, queries) :


    order = Trie()
    reverse = Trie()

    for word in words :

        order.insert(word)
        reverse.insert(word[::-1])


    answer = [] 
    for query in queries :

        k = query.count('?')
        
        if query[0] == '?' :

            a = reverse.starts_with(query[:k-1:-1])

        else :

            a = order.starts_with(query[:len(query)-k])

        if a != None : 
            answer.append(a.count(len(query)))

        else :

            answer.append(0)


    return answer        

# driver program
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))
