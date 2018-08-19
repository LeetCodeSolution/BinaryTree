from node import TreeNode


def create_by_pre_order(values):
    value = values.pop(0)
    
    if value == 0:
        return None
    
    node = TreeNode(value=value)
    node.left = create_by_pre_order(values)
    node.right = create_by_pre_order(values)
    return node


def create_by_pre_in_order(values1, values2):
    if not values1 or not values2:
        return None
    
    root_value = values1[0]
    i = 0
    while values2[i] != root_value:
        i += 1
    
    left_values1 = values1[1: i + 1]
    left_values2 = values2[:i]
    right_values1 = values1[i + 1:]
    right_values2 = values2[i + 1:]
    node = TreeNode(value=root_value)
    
    node.left = create_by_pre_in_order(left_values1, left_values2)
    node.right = create_by_pre_in_order(right_values1, right_values2)
    
    return node
