# -*- coding：utf-8 -*-

# testDataSet = ['a', 'b', 'b', 'c']
testDataSet = ['a', 'b', 'c', 'd']
#testDataSet = ['a', 'b']


class sub_set:
    def subsets(songmids):
        N = len(songmids)
        prePart = []
        prePart.append(songmids[:1])
        tailPart = songmids[1:]
        for i in range(0, N - 1):
            for j in tailPart:
                lst = []
                for k in prePart[0]:
                    lst.append(k)
                lst.append(j)
                print('{0}\t{1}'.format(lst, 1))
            prePart[0].append(tailPart[:1][0])
            tailPart = tailPart[1:]


    def subsetuse(songmids):
        for ev in songmids:
            print('{0}\t{1}'.format(ev.split(" "), 1))
        for times in range(0, len(songmids)):
            sub_set.subsets(songmids[times:])


if __name__ == '__main__':
    # subSets(testDataSet)
    sub_set.subsetuse(testDataSet)
