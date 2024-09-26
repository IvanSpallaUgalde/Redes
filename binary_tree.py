from graphviz import Digraph

class TreeNode:
    def __init__(self, final):
        self.final = final
        self.path = ''
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = TreeNode(False)

    def insert(self, value):
        actual_node = self.root
        father = None
        for i in range(len(value)):
            if value[i] == '0':
                if i == len(value) - 1:
                    if actual_node.right is None:
                        actual_node.right = TreeNode(True)
                        if father is None:
                            actual_node.right.path = '0'
                        else:
                            actual_node.right.path = father.path + '0'
                    else:
                        actual_node.right.final = True
                else:
                    if actual_node.right is None:
                        actual_node.right = TreeNode(False)
                        if father is None:
                            actual_node.right.path = '0'
                        else:
                            actual_node.right.path = father.path + '0'
                    father = actual_node
                    actual_node = actual_node.right
            
            elif value[i] == '1':
                if i == len(value) - 1:
                    if actual_node.left is None:
                        actual_node.left = TreeNode(True)
                        if father is None:
                            actual_node.left.path = '1'
                        else:
                            actual_node.left.path = father.path + '1'
                    else:
                        actual_node.left.final = True
                else:
                    if actual_node.left is None:
                        actual_node.left = TreeNode(False)
                        if father is None:
                            actual_node.left.path = '1'
                        else:
                            actual_node.left.path = father.path + '1'
                    actual_node = actual_node.left

    '''
    def draw(self):
        
        def height(node):
            return 1 + max(height(node.left), height(node.right)) if node else -1
        
        nlevels = height(self.root)
        width = pow(2,nlevels+1)

        q=[(self.root,0,width,'c')]
        levels=[]

        while(q):
            node,level,x,align= q.pop(0)
            if node:
                if len(levels)<=level:
                    levels.append([])

                levels[level].append([node,level,x,align])
                seg= width//pow(2,level+1)
                q.append((node.left,level+1,x-seg,'l'))
                q.append((node.right,level+1,x+seg,'r'))

        for i, l in enumerate(levels):
            pre=0
            preline=0
            linestr=''
            pstr=''
            seg = width//(pow(2,i+1))
            for n in l:
                valstr = str(n[0].path)
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2]
                if n[3] =='l':
                    linesrt+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)
                    preline = n[2] + seg + seg//2
                pstr+=' '*(n[2]-pre-len(valstr))+valstr
                pre = n[2]
            print(linestr)
            print(pstr)
    '''
    def plot():

        dot = Digraph(comment='Binary Tree')
        