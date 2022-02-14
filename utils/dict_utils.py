def take_duedate(elem):
    return elem['due_on']


def dict_order(d, order_by, reverse=False):
    return sorted(d, key=order_by, reverse=reverse)

