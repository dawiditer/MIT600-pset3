from string import *
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

print subStringMatchExact(target1,key10)
print subStringMatchExact(target1,key11)
print subStringMatchExact(target1,key12)
print subStringMatchExact(target1,key13)
print
print subStringMatchExact(target2,key10)
print subStringMatchExact(target2,key11)
print subStringMatchExact(target2,key12)
print subStringMatchExact(target1,key13)
