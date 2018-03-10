from string import *
def constrainedMatchPair(firstMatch,secondMatch,length):
    n = ()
    if len(secondMatch) == 0:
        return firstMatch
    for val_secondMatch in secondMatch:
        if len(firstMatch) > 0:
            for val_firstMatch in firstMatch:
                if val_secondMatch < val_firstMatch:
                    break
                else:
                    if val_firstMatch + length + 1 == val_secondMatch:
                        validStartKey = val_firstMatch
        else:
            if val_secondMatch > 0:
                validStartKey = val_secondMatch-1
            else:
                validStartKey = val_secondMatch
        n = n + (validStartKey,)
    return n


def subStringMatchExact(target,key):
    start = 0
    instances = ()
    for x in xrange(len(target[start:])):
        i = find(target,key,start)
        if i == -1 and start == 0:
            return "Not Found"
        elif i == -1 and start > 0:
            break
        else:
            if len(key) != 0:
                instances = instances + (i,)
            start = i + len(key)
    return instances


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

subStringMatchOneSub(key11,target1)
