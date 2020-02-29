import prefixtreesexample
import francoissoulier_prefixtrees
from algopy import tree
from algopy.tree import Tree

TREE1 = francoissoulier_prefixtrees.treefromfile("textFiles/wordList1.txt")
TREE2 = francoissoulier_prefixtrees.treefromfile("textFiles/wordList2.txt")
TREE3 = francoissoulier_prefixtrees.treefromfile("textFiles/list_fr.txt")

print("Number of words (TREE3):", francoissoulier_prefixtrees.countwords(TREE3),"\n")
print("Number of words (TREE1):", francoissoulier_prefixtrees.countwords(TREE1),"\n")
print("Number of words (TREE2):", francoissoulier_prefixtrees.countwords(TREE2),"\n")

print("Found fa?", francoissoulier_prefixtrees.searchword(TREE2, "fa"),"\n")
print("Founc ci?", francoissoulier_prefixtrees.searchword(TREE2, "ci"),"\n")
print("Found castl?", francoissoulier_prefixtrees.searchword(TREE2, "castl"),"\n")

L1 = ['car', 'card', 'cardinal', 'case', 'cast', 'castle', 'casual', 'cinema', 'circle', 'city', 'come', 'could', 'fame', 'famous', 'fan', 'fancy', 'fantastic', 'fantasy']
L1.append("chaperon")










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

