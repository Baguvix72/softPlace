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
    
def GetPagePost(Posts, numPage):
    PostsPage = Posts[numPage * 12 - 12:numPage * 12]
    ListPost = GetListPosts(PostsPage)
    return ListPost

def GetListPagin(countPage, numPage):
    ListNumPage = [numPage]
    CurrentNum = numPage - 1
    i = 0

    while CurrentNum > 0 and i < 3:
        ListNumPage.insert(0, CurrentNum)
        i += 1
        CurrentNum -= 1

    CurrentNum = numPage + 1
    i = 0

    while CurrentNum <= countPage and i < 3:
        ListNumPage.append(CurrentNum)
        i += 1
        CurrentNum += 1

    return ListNumPage

def GetSpoiler(Text):
    SpoilerList = []
    id = 1

    while Text.find('~~~name=') != -1:
        spoilerName_NumBegin = Text.find('~~~name=')
        spoilerName_NumEnd = Text.find("~~~", spoilerName_NumBegin + 8)
        SpoilerName = Text[spoilerName_NumBegin + 8:spoilerName_NumEnd]
        Text = Text[spoilerName_NumEnd + 3:]
        spoilerText_NumEnd = Text.find('~~~end~~~')
        SpoilerText = Text[0:spoilerText_NumEnd]
        NameAndSpoiler = {"name":SpoilerName, "text":SpoilerText, "id":id}
        SpoilerList.append(NameAndSpoiler)
        id += 1

    return SpoilerList

