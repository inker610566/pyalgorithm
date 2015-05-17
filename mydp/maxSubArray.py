#sm => sum
#rtn => return value

def maxSubArray(A):
	sm = rtn = 0
	for i in A:
		sm = max(0, sm + i)
		rtn = max(sm, rtn)
	return rtn
