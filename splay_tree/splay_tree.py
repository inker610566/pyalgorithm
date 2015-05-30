'''
    A minimal implementation of splay tree.
'''
class SplayTree:

    def __init__(self):
        self.ch[0] = self.ch[1] = self.p = None
        self.value = None

    def __getitem__(self, qValue):
        if self.value == qValue:
            return self
        if self.value == None:
            return None
        comp = self.value > qValue
        return self.ch[comp][qValue] if self.ch[comp] else None
 
    def Left(self):
        return self.ch[0]

    def Right(self):
        return self.ch[1]

    def _rotate(self, lr):
        '''
            Apply rotation to self

            :Args:
             - lr : rotate direction, right if lr else left
        '''
        def set_r(p, s, lr):
            if p: p.ch[lr] = s
            if s: s.p = p
        x = self.ch[not lr]
        assert x
        y = x.ch[lr]
        set_r(self, y, not lr)
        set_r(x, self, lr)

    def _splay(self):
        while self.p and self.p.p:
            p, pp = self.p, self.p.p
            d = p.ch[0] == self
            if d == (pp.ch[0] == p.ch[0]):
                pp._rotate(not d)
                p._rotate(not d)
            else:
                p._rotate(not d)
                p._rotate(d)

        if self.p:
            self.p._rotate(self.p.ch[0] == self)

