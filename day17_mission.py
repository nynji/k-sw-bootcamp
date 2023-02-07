import random


class treenode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')


if __name__ == '__main__':
    things = ['바나나맛우유', '레쓰비캔커피', '츄파춥스','도시락','삼다수','코카콜라','삼각김밥']
    sell = [random.choice(things) for _ in range(20)]
    print(f'오늘 판매된 물건(중복O) --> {sell}')
    node = treenode()
    node.data = sell[0]
    root = node

    for name in sell[1:]:
        node=treenode()
        node.data = name

        current = root
        while True:
            if node.data == current.data:
                break
            if node.data < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left

            elif node.data > current.data:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

    print('이진탐색트리 구현 완료')
    print('오늘 판매될 물건(중복X) --> ', end=' ')
    preorder(root)








