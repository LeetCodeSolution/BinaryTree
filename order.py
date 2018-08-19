def pre_order(root):
    if not root:
        return
    print(root.value, end=' ')
    
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    
    in_order(root.left)
    print(root.value, end=' ')
    in_order(root.right)


def end_order(root):
    if not root:
        return
    
    end_order(root.left)
    end_order(root.right)
    print(root.value, end=' ')
