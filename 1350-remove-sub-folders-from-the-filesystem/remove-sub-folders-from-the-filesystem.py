class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result=[]
        for i in folder:
            if not result or not i.startswith(result[-1]+'/'):
                result.append(i)
        return result