def GetIntCount(ObjectCount, divider):
    AllNumber = ObjectCount / divider
    FloatPart = AllNumber - int(AllNumber)

    if FloatPart != 0:
        AllNumber = AllNumber - FloatPart + 1

    return int(AllNumber)

def GetListPosts(Posts):
    Count = Posts.count()
    RowCount = GetIntCount(Count, 3)
    ListPost = []
    for number in range(RowCount):
        number += 1
        ListPost.append(Posts[number * 3 - 3:number * 3])
    return ListPost
    

    