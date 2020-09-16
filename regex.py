import re
phoneregex = re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
no = phoneregex.search('My number is 91-9920288028')
print(no.group(1))
print(no.group(2))