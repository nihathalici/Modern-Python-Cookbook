# Exer-07-Removing-items-from-a-set-remove-pop-and-difference

log = '''
   [2016-03-05T09:29:31-05:00] INFO: Processing ruby_block[print IP]
   action run (@recipe_files::/home/slott/ch4/deploy.rb line 9)
   [2016-03-05T09:29:31-05:00] INFO: Installed IP: 111.222.111.222
   [2016-03-05T09:29:31-05:00] INFO: ruby_block[print IP] called
   
     - execute the ruby block print IP
    [2016-03-05T09:29:31-05:00] INFO: Chef Run complete in 23.233811181
   seconds
   
    Running handlers:
    [2016-03-05T09:29:31-05:00] INFO: Running report handlers
    Running handlers complete
    [2016-03-05T09:29:31-05:00] INFO: Report handlers complete
    Chef Client finished, 2/2 resources updated in 29.233811181 seconds
'''

import re

pattern = re.compile(r"IP: \d+\.\d+\.\d+\.\d+")
matches = set(pattern.findall(log))
#print(matches)

###

to_be_ignored = {'IP: 0.0.0.0', 'IP: 1.2.3.4'}
matches = {'IP: 111.222.111.222', 'IP: 1.2.3.4'}

#print(matches - to_be_ignored)
#print(matches.difference(to_be_ignored))

valid_matches = matches - to_be_ignored
#print(valid_matches)

valid_matches = matches.copy()
valid_matches.difference_update(to_be_ignored)
print(valid_matches)

###

valid_matches = matches.copy()
for item in to_be_ignored:
    if item in valid_matches:
        valid_matches.remove(item)
print(valid_matches)