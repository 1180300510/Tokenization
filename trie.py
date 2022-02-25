class Trienode:
    def __init__(self,character=None,child=[],isEnd=False):#参数分别表示当前节点存储的字母，子节点，是否为叶节点
        self.character=character
        self.child={w.character: w for w in child}#hash表
        self.isEnd=isEnd

class Trie:
    def __init__(self):
        self.node=Trienode()

    def insert(self,word):#把单词插入到trie树
        temp=self.node
        for w in word:
            if w not in temp.child:
                temp.child[w]=Trienode(w)
            temp=temp.child[w]
        temp.isEnd=True
    
    def search(self,word):#查找某单词是否在trie树中
        temp=self.node
        for w in word:
            if w not in temp.child:
                return False
            temp=temp.child[w]
        if temp.character:
            return True
        return False
    
    
            
        