# Regex library
import re
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
# replace capital leters
new = re.sub('[A-Z]', '', string)
print(new)

# replace special characters
new = re.sub('[.,\']', '', string)
print(new)

# replace capital leters and spaces
new = re.sub('[.,\'A-Z+" "]', '', string)
print(new)

# replace anything except numbers
string = string + '6 298 - 345'
new = re.sub('[^0-9]', '', string)
print(new)
