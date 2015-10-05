class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def deepSearch(root, pathSum, pathList, sum, result):
    	if root == None:
    		return
    	currentPathSum = root.val + pathSum
    	newPathList = list(pathList)
        if currentPathSum == sum and root.left == None and root.right == None:
        	newPathList.append(root.val)
        	print "find path!!!" + str(newPathList)
        	result.append(newPathList)
        	return
        else:
    		newPathList.append(root.val)
        	deepSearch(root.left, currentPathSum, newPathList, sum, result)
        	deepSearch(root.right, currentPathSum, newPathList, sum, result)
        	return

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        deepSearch(root, 0, [], sum, result)

        return result