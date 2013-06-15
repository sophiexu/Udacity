# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    element_num = 0
    keyword_in_index = False
    while element_num < len(index):
        element = index[element_num]
        if keyword in element:
            element[1].append(url)
            keyword_in_index = True
        element_num = element_num + 1
    if keyword_in_index == False:
        index.append([keyword, [url]])
    return index

def add_page_to_index(index,url,content):
    new_keywords = content.split()
    for keyword in new_keywords:
        add_to_index(index, keyword, url)
 
#add_to_index(index,'udacity','http://udacity.com')
#add_to_index(index,'computing','http://acm.org')
#add_to_index(index,'udacity','http://npr.org')
#print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


