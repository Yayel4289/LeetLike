class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
graphs = set()
n, m = map(int, input().split())
for i in range(m):
    a, op, b = input().split()
    cl = None
    match op:
        case '>':
            cl = Node(set(a), Node(set(b)))
            break
        case '<':
            cl = Node(set(b), Node(set(a)))
            break
        case '=':
            cl = Node(set((a, b)))
            break
    graphs.add(cl)

