def find_prefix(List):
    if len(List) == 0:
        return ""
    prefix = List[0]
    for i in range(1,len(List)):
        while List[i].find(prefix) != 0 :
            prefix = prefix[:-1]
    return prefix

List = ["dog","flow","float"]
print(find_prefix(List))