import prefixtreesexample
import francoissoulier_prefixtrees
from algopy import tree
from algopy.tree import Tree

print("Number of words (Tree1):", francoissoulier_prefixtrees.countwords(prefixtreesexample.Tree1),"\n")
print("Longest word length (Tree1):", francoissoulier_prefixtrees.longestwordlength(prefixtreesexample.Tree1),"\n")
print("Average word length (Tree1):", francoissoulier_prefixtrees.averagelength(prefixtreesexample.Tree1),"\n")


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


print("Average word length (Tree2):", francoissoulier_prefixtrees.averagelength(Tree2),"\n")

s = "carcardcardinalcasecastcastlecasualcitycinemacirclecomecouldfamefamousfanfancyfantasticfantasy"
print(len(s))