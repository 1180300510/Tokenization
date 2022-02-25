#分词效果分析
fmm_list=[]
bmm_list=[]
corpus_list=[]

with open('./divide/Lab1/seg_FMM.txt','r') as fmm:
    for line in fmm.readlines():
        line=line.strip('/ \n')#去除掉最后的\_和换行符
        line=line.split('/ ')
        fmm_list.append(line)

with open('./divide/Lab1/seg_BMM.txt','r') as bmm:
    for line in bmm.readlines():
        line=line.strip('/ \n')
        line=line.split('/ ')
        bmm_list.append(line)

with open('./divide/Lab1/199801_seg&pos.txt') as corpus:
    for line in corpus.readlines():
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
        corpus_list.append(line)

success_fmm=0#匹配成功的数目
success_bmm=0
num_corpus=0#语料库中分词数目
num_fmm=0#fmm方法分词数目
num_bmm=0#bmm方法分词数目

for i in range(len(corpus_list)):
    num_corpus+=len(corpus_list[i])
    num_fmm+=len(fmm_list[i])
    num_bmm+=len(bmm_list[i])
    
    for j in range(len(fmm_list[i])):
        for k in range(len(corpus_list[i])):
            if fmm_list[i][j]==corpus_list[i][k]:
                success_fmm+=1
                break
    
    for j in range(len(bmm_list[i])):
        for k in range(len(corpus_list[i])):
            if bmm_list[i][j]==corpus_list[i][k]:
                success_bmm+=1
                break    

print(success_fmm)
print(num_corpus)
print(num_fmm)
print("正向匹配的准确率,召回率和F值：")
precesion_fmm=success_fmm/num_corpus
recall_fmm=success_fmm/num_fmm
F1_fmm=2*precesion_fmm*recall_fmm/(precesion_fmm+recall_fmm)
print(precesion_fmm)
print(recall_fmm)
print(F1_fmm)


print(success_bmm)
print(num_corpus)
print(num_bmm)
print("逆向匹配的准确率,召回率和F值：")
precesion_bmm=success_bmm/num_corpus
recall_bmm=success_bmm/num_bmm
F1_bmm=2*precesion_bmm*recall_bmm/(precesion_bmm+recall_bmm)
print(precesion_bmm)
print(recall_bmm)     
print(F1_bmm)   


