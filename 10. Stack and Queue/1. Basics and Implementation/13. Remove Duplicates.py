#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    lis = []
	    for ch in s:
	        if ch not in lis:
	            lis.append(ch)
	    return "".join(lis)
