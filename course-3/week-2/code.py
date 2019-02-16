#import re
#total = 0
#with open('regex_sum_151103.txt', 'r') as f:
#    for line in f:
#        items = re.findall(r'[0-9]+', line)
#        total += sum([int(i) for i in items])
#print(total)
import re
print(sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_151103.txt', 'r').read())]))
