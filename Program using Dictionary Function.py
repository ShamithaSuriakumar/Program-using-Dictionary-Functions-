W= "mississippi"
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

m= (most_frequent(W))
k=( sorted(m.items(), key=lambda item: item[1],reverse=True))
for i in k:
    print(*i,sep="=")
