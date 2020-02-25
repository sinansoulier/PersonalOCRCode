__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2020-02-14'

"""
Prefix Trees homework
2020-02 - S3#
@author: francois.soulier
"""

from algopy import tree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import



##############################################################################
## Measure

#------------------------------------------------------------------------------------

def countwords(T):
    """ count words in tree T
    
    """
    count = 0
    if T.key[1]:
        count += 1
    for C in T.children:
        count += countwords(C)
    return count
    
#------------------------------------------------------------------------------------

def longestwordlength(T):
    """ longest word length
    
    """
    longest = -1
    for C in T.children:
        longest = max(longest, longestwordlength(C))
    return (longest+1)

#------------------------------------------------------------------------------------

# Function that computes the number of character of each word
# and sums all the results
def __sum(T, count=1):
    sum = 0
    for C in T.children:
        rec_sum = __sum(C, count+1)
        if C.key[1]:
            sum += count
        sum += rec_sum
    return sum

    #____________________________________________________

def averagelength(T):
    """ average word length

    """
    sum, nb_words = __sum(T), countwords(T)
    return sum/nb_words
    
###############################################################################
## search and list

#------------------------------------------------------------------------------------

# Function that builds the list 'word_list', which purpose is to countain the words 
# of the tree T
def __treetolist(T, word_list, index_next=0, word=""):
    if T.key[1]:
        word_list.insert(index_next, word+T.key[0])
        index_next += 1
    for C in T.children:
        index_next = __treetolist(C, word_list, index_next, word+T.key[0])
    return index_next

        #____________________________________________________

def wordlist(T):
    """ generate the word list
    
    """
    word_list = []
    __treetolist(T, word_list)
    return word_list

#------------------------------------------------------------------------------------

# Function that contains the main algorithm of the function 
# searchword, using indexing for the parameter 'word'
def __searchword(T, word, index=0):
    if not(T.children):
        if index == len(word):
            return True
        else:
            return False
    else:
        if index == len(word):
            return True
        for C in T.children:
            if C.key[0] == word[index]:
                return __searchword(C, word, index+1)
        return False

def searchword(T, word):
    """ search for a word in a tree
    
    """
    return __searchword(T, word)

#------------------------------------------------------------------------------------

def __completion(T, prefix, len_prefix, lvl):
    if lvl == 0:
        array = []
        i = 0
        if T.key[1]:
            array.insert(0, prefix)
            i += 1
        for child in T.children:
            __treetolist(child, array, i, prefix)
        if not(array):
            return []
        return array
    else:
        for C in T.children:
            if C.key[0] == prefix[len_prefix-lvl]:
                return __completion(C, prefix, len_prefix, lvl-1)

def completion(T, prefix):
    """ generate the list of words with a common prefix
    
    """
    length = len(prefix)
    return __completion(T, prefix, length, length)
###############################################################################
## Build

#-----------------------------------------------------------------------------------------------


def treetofile(T, filename):
    """ save the tree in a file
    
    """
    L = wordlist(T)
    file = open(filename, "w+")
    for line in L:
        file.write(line + "\n")
    file.close


#-----------------------------------------------------------------------------------------------


    # Function that does a binary search of the element x in the list L (here children of a Tree)
def __binary_search(L, x, left, right):
    if left == right:
        return right
    else:
        mid = left + (right - left) // 2
        if x == L[mid].key[0]:
            return mid
        elif x < L[mid].key[0]:
            return __binary_search(L, x, left, mid)
        else:
            return __binary_search(L, x, mid+1, right)

    #____________________________________________________
    
    # Function containing the main algorithm
    # that adds the word 'word' depending on its length,
    # and the index we are on
def __addword(T, word, index, length):
    if index < length:
        i = __binary_search(T.children, word[index], 0, T.nbchildren)
        end_word = index == length-1
        if T.children:
            if i < T.nbchildren:
                if T.children[i].key[0] != word[index]:
                    T.children.insert(i, tree.Tree((word[index], end_word)))
            else:
                T.children.append(tree.Tree((word[index], end_word)))
        else:
            T.children.insert(i, tree.Tree((word[index], end_word)))
        if i >= T.nbchildren:
            i = -1
        __addword(T.children[i], word, index+1, length)    

    #____________________________________________________

def addword(T, word):
    """ add a word in the tree
    
    """
    length = len(word)
    __addword(T, word, 0, length)


#-----------------------------------------------------------------------------------------------


def treefromfile(filename):
    """ build the prefix tree from a file of words
    
    """
    file = open(filename)
    l_s = file.readlines()
    T = tree.Tree(('', False))
    for line in l_s:
        line = line.strip()
        addword(T, line)
    file.close()
    return T