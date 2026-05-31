class Solution:

	def anagram(self, s, t):
	    count = [0] * 26
	    for i in range(len(s)):
	        count[ord(s[i])-ord('a')] += 1
	        count[ord(t[i])-ord('a')] -= 1
	       
	    for i in range(len(count)):
	        if count[i] != 0:
	            return False
	    return True
	    
	def search(self,pat, txt):
	    n = len(txt)
	    m = len(pat)
	    count = 0
	    left = 0
	    right = 0
	    while right < n:
	        if right-left+1 > m:
	            left += 1
	        if right-left+1 == m:
	            if self.anagram(txt[left:right+1], pat):
	                count += 1




	        right += 1
	    return count
	            
