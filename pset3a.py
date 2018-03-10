#divide and conquer
from string import *
def countSubStringMatch(target,key):
    start = 0
    inst = []
    found = True
    for x in target:
        i = find(target,key,start)
        if i == -1 and start == 0:
            print "No instance of \"%s\" found"%(key)
            found = False
            break
        elif i == -1 and start > 0:
            break
        else:
            inst.append(i)
            start = i + len(key)
    if found:
        return "%i instances found" % len(inst)
    else:
        return "No Instances found"
        
instances = 0
def countSubStringMatchRecursive(target,key,start=0):
    global instances
    if len(target) < len(key):
        return "Search term can't be bigger than search string"
    end = len(key) + start
    i = find(target[start:end],key)
    if i == -1:
        countSubStringMatchRecursive(target[start+1:],key)
    else:
        instances += 1
        countSubStringMatchRecursive(target[start+end:],key)
    return "%i instances found" % instances
    
DNA_strand = "atgacatgcacaagtatgcat"
sequence = "at"
print "-"*51
print "Searching for \"%s\" from \"%s\"" % (sequence,DNA_strand)
print "-"*51
print "Using countSubStringMatchRecursive(): ",
print countSubStringMatchRecursive(DNA_strand,sequence)

print "Using countSubStringMatch(): ",
print countSubStringMatch(DNA_strand,sequence)
    
