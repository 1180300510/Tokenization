import re
import trie
#测试集需注意的事：跨系统的文件读取，比如换行符，文字的编码 
#最长匹配长度
maxLength=0
Trie=trie.Trie()#初始化trie树



with open('./divide/Lab1/dict_second.txt','r') as f:#将词典中词插入Trie树中
    for line in f.readlines():
        line=line.strip('\n')

        if(len(line)>maxLength):
            maxLength=len(line)
        Trie.insert(line)

def time_match(string):#用正则表达式匹配时间，并将其从字符串中删去
    pattern='\\d\\d\\d\\d\\d\\d\\d\\d-\\d\\d-\\d\\d\\d-\\d\\d\\d'
    result=re.sub(pattern,'',string)
    return result

def forward_match(string):#前向匹配
    temp_list=[]
    while len(string)>0:
        length=maxLength
        if len(string)<length:
            length=len(string)
        word=string[0:length]
        while not Trie.search(word):
            if len(word)==1:
                break
            else:
                length-=1
                word=word[0:length]
        temp_list.append(word)
        string=string[len(word):]
    return temp_list

def backward_match(string):#逆向匹配
    temp_list=[]
    while len(string)>0:
        length=maxLength
        if len(string)<length:
            length=len(string)
        word=string[len(string)-length:len(string)]
        while not Trie.search(word):
            if len(word)==1:
                break
            else:
                length-=1
                word=string[len(string)-length:len(string)]
        temp_list.append(word)
        string=string[0:len(string)-len(word)]
    return temp_list



fmm=open('./divide/Lab1/seg_FMM.txt','w')
bmm=open('./divide/Lab1/seg_BMM.txt','w')

n=0

with open('./divide/Lab1/199801_sent.txt','r') as input:
    for line in input.readlines():
        line=line.strip('\n')
        line=time_match(line)
        forward_list=forward_match(line)
        backward_list=backward_match(line)
        #print(forward_list)
        #print(backward_list)
        n+=1
        print(n)
        for i in range(len(forward_list)):
            fmm.write(forward_list[i])
            fmm.write('/ ')
        fmm.write('\n')

        for i in range(len(backward_list)):
            bmm.write(backward_list[i])
            bmm.write('/ ')
        bmm.write('\n')


fmm.close()
bmm.close()
