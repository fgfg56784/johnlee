import sys,keyword
from string import ascii_letters, digits
first_list = ascii_letters  + '_' 
all_list = first_list + digits

def check_word(word):
    if keyword.iskeyword(word):
        return '%s是关键字' % word
    if  not  word[0] in first_list:
        return '首字符不合法'
    
    for ind, ch  in enumerate(word[1:]):
        if ch not in all_list:
            return '第%s个字符不合法' % (ind + 2)
    return '%s 是合法的标识符' % word
    
if __name__ == "__main__":
    print(check_word(sys.argv[1]))


   