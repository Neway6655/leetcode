from collections import deque

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rawPathArray = path.split("/")
        simplifyPathStack = deque([])
        for rawPath in rawPathArray:
            if rawPath == '':
                continue
            if rawPath == '.':
                continue
            if rawPath == '..':
                if len(simplifyPathStack) != 0:
                    simplifyPathStack.pop()
                continue
            simplifyPathStack.append(rawPath)

        if len(simplifyPathStack) == 0:
            return '/'
            
        result = ''
        singlePath = simplifyPathStack.popleft()
        while singlePath != '':
            result = result + '/' + singlePath
            if len(simplifyPathStack) == 0:
                break
            singlePath = simplifyPathStack.popleft()
        
        return result

