"""
樹狀結構定義：
    https://sites.google.com/site/zsgititit/home/python-cheng-shi-she-ji/shu-zhuang-jie-gou-python
    (1)root(根節點)：點1就是root。
    (2)edge(邊)：將點之間連接起來的線就是edge，上圖樹狀結構有8個邊。
    (3)node(節點)：點1到點9都是edge，上圖樹狀結構有9個點。
    (4)parent(雙親節點)：點1是點2、點3與點4的parent。
    (5)children(小孩節點)：點2、點3與點4是點1的children。
    (6)sibling(手足節點)：點3與點4是點2的sibling。
    (7)leaf node(葉節點)或terminal node(終節點)：節點下方沒有其他節點，點5、點6、點7、點8與點9是上圖樹狀結構的leaf，也可以稱為terminal node。
    (8)internal node(內部節點)或nonterminal node(非終節點)：節點不是leaf(葉節點)就是internal node，點1、點2、點3與點4是本圖的internal node，也可以稱為nonterminal node。
    (9)external node(外部節點)：與leaf(葉節點)定義相同，節點下方沒有其他節點，點5、點6、點7、點8與點9是此範例樹狀結構的external node。
    (10)degree(分支度)：節點下有幾個分支，點1的degree為3，點2的degree為2，點7的degree為0。
    (11)level(階層)：若定義root所在level為1，則點1的level為1，點2的level為2，點7的level為3。
    (12)height(高度)或depth(深度)：樹狀結構的所有點的最大level稱作height或depth，此範例樹狀結構的height為3，也可以稱為depth為3。

二元樹：
    - 定義：
        二元樹須符合樹狀結構的定義，且二元樹中每個節點的最大分支度(degree)為2，左邊的分支樹稱作left subtree(左子樹)，右邊的分支樹稱作right subtree(右子樹)。
"""


class Node:
    """
    二元樹需要兩個指標，一個指向左子樹，另一個指向右子樹，
    若子樹是空的時候設定為NULL，NULL就是空指標，程式會以數值0取代，在二元樹走訪時遇到NULL，就不能再走訪下去，必須倒退回去。
    """
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node


p1 = Node('A')
root = p1
p2 = Node('B')
p3 = Node('C')
p4 = Node('D')
p5 = Node('E')
p7 = Node('F')
p1.setLeft(p2)
p1.setRight(p3)
p2.setLeft(p4)
p2.setRight(p5)
p3.setRight(p7)


# 前序走訪
def preorder(p):
  if p:
    print(p.val, ' ', end='')
    preorder(p.left)
    preorder(p.right)


preorder(root)
