class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return str(self.value)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)


class TreeBuilder:
    def __init__(self):
        self.tree = Tree()

    def add_root(self, value):
        self.tree.root = Node(value)
        return self

    def add_child(self, parent_value, child_value):
        parent = self._find_node(self.tree.root, parent_value)
        if parent:
            parent.add_child(Node(child_value))
        return self

    def _find_node(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            result = self._find_node(child, value)
            if result:
                return result
        return None

    def build(self):
        return self.tree


# Создаем дерево с помощью TreeBuilder
builder = TreeBuilder()
tree = (
    builder
    .add_root("A")
    .add_child("A", "B")
    .add_child("A", "C")
    .add_child("B", "D")
    .add_child("B", "E")
    .add_child("C", "F")
    .build()
)

# Выводим дерево
print(tree)