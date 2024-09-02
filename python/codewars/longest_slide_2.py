class Node:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None


class Tree:
    def __init__(self, pyra):
        if not pyra:
            return

        self.root = Node(pyra[0][0])
        last_lvl = [self.root]

        for lvl_i, arr in enumerate(pyra[1:], 1):
            this_lvl = []
            for i, val in enumerate(arr):
                node = Node(val)
                this_lvl.append(node)

                if i == 0:
                    last_lvl[i].left = node
                elif i == len(arr) - 1:
                    last_lvl[-1].right = node
                else:
                    last_lvl[i].left = node
                    last_lvl[i - 1].right = node
            last_lvl = this_lvl


def longest_slide_down(p):
    tree = Tree(p)

    longest = 0

    def walk(node, s):
        nonlocal longest
        s += node.value

        if node.left and node.right:
            walk(node.left, s)
            walk(node.right, s)
        elif s > longest:
            longest = s

    walk(tree.root, 0)

    return longest


if __name__ == "__main__":
    pyra = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    res = longest_slide_down(pyra)
    print(res)
    print(res == 1074)
