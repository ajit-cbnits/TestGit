
import random
import string

class UtilsMethods:

    def randomEmailId(stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.sample(letters, stringLength))

    value = randomEmailId()+"@"+"yopmail.com"

    print("Random String is ", value)
