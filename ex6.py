def is_sorted(string):
    ordered=True
    for i in string:
        try:
             prev>0
             if  prev>ord(i):
                ordered=False
                break
        except:
            prev=ord(i)
    return ordered

print(is_sorted("zzzdfjfwwfe"))