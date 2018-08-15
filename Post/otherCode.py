def GetRowCount(PostCount):
    AllNumber = PostCount / 3
    FloatPart = AllNumber - int(AllNumber)

    if FloatPart != 0:
        AllNumber = AllNumber - FloatPart + 1

    return int(AllNumber)

def GetPostList(Posts):
    Count = Posts.count()
    RowCount = GetRowCount(Count)
    ListPost = []
    for number in range(RowCount):
        number += 1
        ListPost.append(Posts[number * 3 - 3:number * 3])
    return ListPost

def GetPageCount(PostCount):
    AllNumber = PostCount / 12
    FloatPart = AllNumber - int(AllNumber)

    if FloatPart != 0:
        AllNumber = AllNumber - FloatPart + 1

    return int(AllNumber)


#def GetPostPage(Posts):
#    Count = Posts.count()
#    PageCount =
    