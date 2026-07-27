from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        hashset = set(wordList)
        if endWord not in hashset:
            return 0
        q = deque()
        q.append((beginWord, 1))
        hashset.remove(beginWord) if beginWord in hashset else None
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + ch + word[i+1:]
                    if newword in hashset:
                        hashset.remove(newword)
                        q.append((newword, step+1))
        
        return 0
        
