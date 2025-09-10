import sys 
sys.setrecursionlimit(1_000_000)

class Tree:
    def __init__(self, cat) -> None:
        self.cat = cat 
        self.related = set()

    def add_relation(self, tree):
        self.related.add(tree)
        tree.related.add(self)

n, m = map(int, input().split())
inp = input()
a = []
for i in range(0, len(inp), 2):
    a.append(int(inp[i]))

root = Tree(a[0])
trees = {1: root}
for _ in range(n - 1):
    t1_num, t2_num = map(int, input().split())
    t1 = trees.setdefault(t1_num, Tree(a[t1_num - 1]))
    t2 = trees.setdefault(t2_num, Tree(a[t2_num - 1]))
    t1.add_relation(t2)
   
def count_ok_paths(t: Tree, m, parent=None, acc=0):
    t.related.discard(parent)
    acc = acc + t.cat if t.cat != 0 else 0
    if acc > m:
        return 0 
    elif not len(t.related):
        return 1

    res = 0
    for child in t.related:
        res += count_ok_paths(child, m, t, acc)
    return res

print(count_ok_paths(root, m))

