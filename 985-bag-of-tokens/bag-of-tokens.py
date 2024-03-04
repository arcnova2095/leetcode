
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens= sorted(tokens)
        score=0
        max_s=0
        left,right=0,len(tokens)-1

        while left<=right:
            if power>= tokens[left]:
                power-=tokens[left]
                score+=1
                left+=1
                max_s= max(max_s,score)
            elif score>0:
                power+=tokens[right]
                score-=1
                right-=1
            else:
                break
        return max_s
