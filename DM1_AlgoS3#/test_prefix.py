import prefixtreesexample
import francoissoulier_prefixtrees
from algopy import tree
from algopy.tree import Tree

print("Number of words (Tree1):", francoissoulier_prefixtrees.countwords(prefixtreesexample.Tree1),"\n")
print("Longest word length (Tree1):", francoissoulier_prefixtrees.longestwordlength(prefixtreesexample.Tree1),"\n")
print("Average word length (Tree1):", francoissoulier_prefixtrees.averagelength(prefixtreesexample.Tree1),"\n")


TREE1 = francoissoulier_prefixtrees.treefromfile("textFiles/wordList1.txt")
TREE2 = francoissoulier_prefixtrees.treefromfile("textFiles/wordList2.txt")
#TREE3 = francoissoulier_prefixtrees.treefromfile("textFiles/list_fr.txt")

"""print("Number of words (TREE1):", francoissoulier_prefixtrees.countwords(TREE1),"\n")
print("Longest word length (TREE1):", francoissoulier_prefixtrees.longestwordlength(TREE1),"\n")
print("Average length (TREE1):", francoissoulier_prefixtrees.averagelength(TREE1),"\n")

print("Number of words (TREE2):", francoissoulier_prefixtrees.countwords(TREE2),"\n")
print("Longest word length (TREE2):", francoissoulier_prefixtrees.longestwordlength(TREE2),"\n")
print("Average length (TREE2):", francoissoulier_prefixtrees.averagelength(TREE2),"\n")

print("Number of words (TREE3):", francoissoulier_prefixtrees.countwords(TREE3),"\n")
print("Longest word length (TREE3):", francoissoulier_prefixtrees.longestwordlength(TREE3),"\n")
print("Average length (TREE3):", francoissoulier_prefixtrees.averagelength(TREE3),"\n")
"""

print("List of words (Tree1):", francoissoulier_prefixtrees.wordlist(prefixtreesexample.Tree1),"\n")
print("List of words (TREE2):", francoissoulier_prefixtrees.wordlist(TREE2))

francoissoulier_prefixtrees.treetofile(prefixtreesexample.Tree1, "my_putain_de_txt_file.txt")
francoissoulier_prefixtrees.treetofile(TREE2, "my_putain_de_txt_file2.txt")

L1 = ['car', 'card', 'cardinal', 'case', 'cast', 'castle', 'casual', 'cinema', 'circle', 'city', 'come', 'could', 'fame', 'famous', 'fan', 'fancy', 'fantastic', 'fantasy']
L1.append("chaperon")
for e in L1:
    print(e, "in TREE2:", francoissoulier_prefixtrees.searchword(TREE2, e),"\n")

print(francoissoulier_prefixtrees.completion(prefixtreesexample.Tree1, "fan"),"\n")

print(francoissoulier_prefixtrees.completion(prefixtreesexample.Tree1, "ci"),"\n")

print(francoissoulier_prefixtrees.completion(prefixtreesexample.Tree1, "what"),"\n")

Tree2 = Tree(('', False), 

    [Tree(('c', False), 

        [Tree(('a', False), 

            [Tree(('r', True), 

                [Tree(('d', True), 

                    [Tree(('i', False), 

                        [Tree(('n', False), 

                            [Tree(('a', False), 

                                [Tree(('l', True))
                                ])
                            ])
                        ])
                    ])
                ]), 

            Tree(('s', False), 

                [Tree(('e', True)), 

                Tree(('t', True), 

                    [Tree(('l', False), 

                        [Tree(('e', True))
                        ])
                    ]),

                Tree(('u', False), 

                    [Tree(('a', False), 

                        [Tree(('l', True))
                        ])
                    ])
                ])
            ]),

        Tree(('i', False), 

            [Tree(('t', False), 

                [Tree(('y', True))]),

            Tree(('n', False), 

                [Tree(('e', False),

                    [Tree(('m', False), 

                        [Tree(('a', True))
                        ])
                    ])
                ]),

            Tree(('r', False), 
                [Tree(('c', False), 
                    [Tree(('l', False), 
                        [Tree(('e', True))
                        ])
                    ])
                ])
            ]),

        Tree(('o', False), 

            [Tree(('m', False), 

                [Tree(('e', True))
                ]),
            Tree(('u', False), 

                [Tree(('l', False), 

                    [Tree(('d', True))
                    ])
                ])
            ])
        ]),
Tree(('f',False),

    [Tree(('a', False), 

        [Tree(('m', False), 

            [Tree(('e', True)),

            Tree(('o', False), 

                [Tree(('u', False), 

                    [Tree(('s', True))
                    ])
                ])
            ]),

        Tree(('n', True), 

            [Tree(('c', False), 

                [Tree(('y', True))
                ]),

            Tree(('t', False), 

                [Tree(('a', False), 

                    [Tree(('s', False), 

                        [Tree(('t', False), 

                            [Tree(('i', False), 

                                [Tree(('c', True))
                                ])
                            ]),

                        Tree(('s', False), 

                            [Tree(('y', True)
                            )]
                        )]
                    )]
                )]
            )]
        )]
    )]
    
)])

