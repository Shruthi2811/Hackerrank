n=int(input())
nos=list( map(int, input().split()) )
weights=list( map(int, input().split()) )
wm=0;
for i in range(0,n):
    wm=wm+nos[i]*weights[i]
print(round((wm/sum(weights)),1))
