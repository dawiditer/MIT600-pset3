def subStringMatchExactlyOneSub(target,key):
    subs_only = ()
    for val in key:
        if val not in target:
            subs_only = subs_only + (val,)
    return subs_only
