def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0

    max_height = 0
    for b in branches(t):
        max_height = max(max_height, height(b))
    return 1 + max_height


def max_path_sum(t):
    """Return the maximum path sum of the tree."""
    if is_leaf(t):
        return label(t)

    sums = []
    for b in branches(t):
        sums += [label(t) + max_path_sum(b)]
    return max(sums)


def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    None
    """
    path = []
    if is_leaf(t):
        if label(t) == x:
            path += [label(t)]
            return path
        else:
            return None

    path += [label(t)]
    for b in branches(t):
        if find_path(b, x):
            path += find_path(b, x)
            return path


def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]),tree(6)])
    >>> sum_tree(t)
    15
    """
    if is_leaf(t):
        return label(t)

    sum = 0
    for b in branches(t):
        sum += sum_tree(b)
    return label(t) + sum


def balanced(t):
    """
    Checks if each branch has same sum of all elements and if each branch is balanced
    >>> t = tree(1, [tree(3), tree(1,[tree(2)]), tree(1,[tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    sum_branches = []
    for b in branches(t):
        sum_branches += [sum_tree(b)]
    curr_b = sum_branches[0]
    for b in sum_branches:
        if b != curr_b:
            return False

    if is_leaf(t):
        return True
    for b in branches(t):
        if not balanced(b):
            return False
    return True


def sprout_leaves(t, leaves):
    """Sprout new leaves containing data in leaves at each leaf in the original tree t and return the resulting tree"""
    if is_leaf(t):
        sprout_branch = [tree(leaf) for leaf in leaves]
        return tree(label(t), sprout_branch)
    new_tree = tree(label(t))
    for b in branches(t):
        new_tree += tree(sprout_leaves(b, leaves))
    return new_tree


# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with a label and a list of branches."""
    return [label] + branches


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, otherwise returns False"""
    return not branches(tree)
