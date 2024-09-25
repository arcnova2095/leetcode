class trie:
    def __init__(self):
        self.next=[None]*26
        self.count=0

class Solution:
    def __init__(self):
            self.root= trie()
    def insert(self,word):
        node= self.root
        for i in word:
            if node.next[ord(i)- ord('a')]== None:
                node.next[ord(i)- ord('a')]= trie()
            node.next[ord(i)- ord('a')].count+=1
            node = node.next[ord(i) - ord("a")]

        
    def count(self,s):
        node= self.root
        ans=0
        for i in s:
            ans+=node.next[ord(i) - ord("a")].count
            node=node.next[ord(i) - ord("a")]
        return ans
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for i in words:
            self.insert(i)
        scores=[]
        for i in range(len(words)):
            scores.append(self.count(words[i]))
        return scores