poly = 0xedb88320
startxor = 0xffffffff

def ConstructReverseTable():
	revtable = [0]*256
	for i in range(256):
		rev = i << 24
		for j in range(8):
			rev = ([rev<<1, ((rev^poly)<<1) | 1][rev & 0x80000000 != 0]) & 0xffffffff
		revtable[i] = rev
	return revtable
