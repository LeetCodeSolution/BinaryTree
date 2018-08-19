from create import create_by_pre_order
from order import pre_order, in_order, end_order
from create import create_by_pre_in_order

values = [1, 2, 4, 0, 7, 0, 0, 0, 3, 5, 0, 0, 6, 8, 0, 0, 0]

root = create_by_pre_order(values)

pre_order(root)

print()

in_order(root)

print()

end_order(root)

print()

values1 = [1, 2, 4, 7, 3, 5, 6, 8]
values2 = [4, 7, 2, 1, 5, 3, 8, 6]
root = create_by_pre_in_order(values1, values2)

pre_order(root)
