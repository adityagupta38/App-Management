#Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).

import re

prob1='''{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},
{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[
PHP Warning #2] count(): Parameter must be an array or an object that
implements Countable (153)"}]}'''
                                                                              

'''In first part we will identify the patt & fetch the required data through re module'''                                                                            
print('First Part')
patt=re.compile(r':[0-9]+')
matchli=re.findall(patt,prob1)
print(matchli)
print()
'''In  Second Part We have filterd required regex Using slicing'''
print('RegEx List')
print()
regexlist=[]
for s in matchli:
    regexlist.append(s[1:])

print(regexlist)
    

