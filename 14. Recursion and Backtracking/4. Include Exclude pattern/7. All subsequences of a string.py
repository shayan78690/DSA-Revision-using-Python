class Solution:
	def powerSet(self, s):
		n = len(s)
		result = []
		self.func(s, n, result, "", 0)
		result.sort()
		return result
	def func(self, s, n, result, string, idx):
	    if idx == n:
	        result.append(string)
	        return
	    self.func(s, n, result, string+s[idx], idx+1)
	    self.func(s, n, result, string, idx+1)

