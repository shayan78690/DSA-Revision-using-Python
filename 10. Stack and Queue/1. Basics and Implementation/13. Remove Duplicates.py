#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    lis = []
	    for ch in s:
	        if ch not in lis:
	            lis.append(ch)
	    return "".join(lis)


#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    seen = set()
	    lis = []
	    for ch in s:
	        if ch not in seen:
	            seen.add(ch)
	            lis.append(ch)
	    return "".join(lis)
