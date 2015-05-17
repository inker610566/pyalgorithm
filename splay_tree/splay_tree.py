'''
    A minimal implementation of splay tree.
'''
class SplayTree:

    def __init__(self):
        self.ch[0] = self.ch[1] = None
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
        x = self.ch[not lr]
        assert x
        self.ch[not lr] = x.ch[lr]
        x.self.ch[lr] = self


    def _splay(self, rpath):
        '''
            Apply splay to self according to rpath

            :Args:
             - rpath : list of node path from root to parent of self(not including self)
        '''
        for p in reversed(rpath):
            self._rotate(p.ch[0] == self)



