a=int(input('请输入层数(n>2且n为奇数)：'))
for i in range(1,a+1-(a//2)):
    print(' '*(a-(a//2)-i),'+'*(2*i-1))
for n in range(1,(a//2)+1):
    print(' '*n,'+'*(a-2*n))
