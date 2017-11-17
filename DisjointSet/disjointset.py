class DJNode:
    def __init__(self,data):
        self.data=data
        self.rank = 1
        self.parent = self

class DJset:
    def __init__(self,set_A):
        self.entries = {x:DJNode(x) for x in set_A}

        def merge(self, u, v):
            u = self.entries[u]
            v = self.entries[v]
            p_u = find_parent(u)
            p_v = find_parent(v)

            elif p_u > p_v:
                p_v.parent = p_u
                p_u.rank+=p_v.rank
            else:
                p_u.parent = p_v
                p_v.rank += p_u.rank

        def find_parent(a):
            current = a
            while current != current.parent:
                current = current.parent
            return current


