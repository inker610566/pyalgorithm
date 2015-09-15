
def KMP(s, p):
    '''
        :Args:
            - s : string to be matched
            - p : pattern
        :Return:
            - a list
    '''
    def build_failure(s):
        f, j = [-1], -1
        for i, c in (lambda e: (next(e), e)[1])(enumerate(s)):
            while j != -1 and s[j+1] != c:
                j = f[j]
            if s[j+1] == c: j += 1
            f += [j]
        return f
    p = p + '$' # guard char
    f = build_failure(p)
    print p
    print f
    # match
    j = -1
    ret = []
    for i, c in enumerate(s):
        while j != -1 and p[j+1] != c:
            j = f[j]
        if p[j+1] == c: j += 1
        ret += [j+1]

    return ret

    
if __name__ == '__main__':
    print KMP('aacecaaa'[-1::-1], 'aacecaaa')
