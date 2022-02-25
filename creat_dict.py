bigline=set()#使用set集合存储词
def creat_list(line):
    line=line.strip(' \n')
    line=line.split('  ')
    line=line[1:]#去掉时间
    for i in range(len(line)):
        string=line[i]
        string=string[::-1]
        for j in range(len(string)):
            if(string[j]=='/'):
                string=string[j+1:]
                break

        string=string[::-1]
        if len(string)>0 and string[0]=='[':
            string=string[1:]    
        line[i]=string
    for i in range(len(line)):
        string=line[i]
        bigline.add(string)
 
        

with open('./divide/Lab1/199801_seg&pos.txt','r') as f:
    for line in f.readlines():
        creat_list(line)

with open('./divide/Lab1/dict_second.txt','w') as file:
    for i in bigline:
        file.write(i)
        file.write('\n')
    