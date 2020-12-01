from inputData1 import data
data = data.replace('\n', ',')

dataList = []
tmpList = ''

for i in data:
    if i == ',':
        dataList.append(int(tmpList))
        tmpList = ''

    else:
        tmpList += i

data = dataList; del dataList

canFinish = False

for xcount, x in enumerate(data):

    if canFinish: break

    for ycount, y in enumerate(data):

        if canFinish: break

        if xcount != ycount:

            for zcount, z in enumerate(data):

                if xcount != zcount and ycount != zcount:
                    total = x + y + z

                    if total == 2020:
                        total = x * y * z
                        print(total)
                        canFinish = True
