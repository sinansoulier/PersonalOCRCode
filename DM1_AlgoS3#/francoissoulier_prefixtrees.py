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

def countwords(T):
    """ count words in tree T
    
    """
    count = 0
    if T:
        if T.key[1]:
            count += 1
        for C in T.children:
            count += countwords(C)
    return count
    

def longestwordlength(T):
    """ longest word length
    
    """
    longest = -1
    for C in T.children:
        longest = max(longest, longestwordlength(C))
    return (longest+1)


def __sum(T, count=1):
    sum = 0
    for C in T.children:
        rec_sum = __sum(C, count+1)
        if C.key[1]:
            sum += count
        sum += rec_sum
    return sum

def averagelength(T):
    """ average word length

    """
    sum = __sum(T)
    return sum
    
###############################################################################
## search and list

#def __word_list(T, word="", L=[]):
    #if T:
        #if T.key[1]:
          #  word += T.key[0]
          #  L.append(word)
        #for C in T.children:
        #   pass

def wordlist(T):
    """ generate the word list
    
    """
    #FIXME
    pass


def searchword(T, word):
    """ search for a word in a tree
    
    """
    #FIXME
    pass
    
    
def completion(T, prefix):
    """ generate the list of words with a common prefix
    
    """
    #FIXME
    pass


###############################################################################
## Build


def __treetolist(T, s=""):
    pass


def treetofile(T, filename):
    """ save the tree in a file
    
    """
    #FIXME
    pass


def addword(T, word):
    """ add a word in the tree
    
    """
    #FIXME
    pass


def treefromfile(filename):
    """ build the prefix tree from a file of words
    
    """
    file = open(filename)
    l_s = file.readlines()

    