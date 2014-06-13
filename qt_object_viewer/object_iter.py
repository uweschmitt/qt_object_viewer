import re
import sys
import types


def type_to_str(t):
    match = re.match("<type '(.*)'>", str(t))
    if match is None:
        match = re.match("<class '(.*)'>", str(t))
        if match is None:
            return str(t)
    return match.groups()[0]


def interesting_attributes(obj):
    for name in dir(obj):
        value = getattr(obj, name)
        if name.startswith("_"):
            continue
        if isinstance(value, types.MethodType):
            continue
        yield name, value


class Node(object):

    def __init__(self, type_, name, children):
        self.type_ = type_
        self.name = name
        self.children = children

    def get_children(self):
        return self.children

    def get_num_children(self):
        return len(self.children)

    def get_name(self):
        self.name

    @classmethod
    def from_(clz, name, obj):
        type_as_str = type_to_str(type(obj))
        if isinstance(obj, (int, float, basestring)):
            return Leaf(type_as_str, name, obj)
        elif isinstance(obj, (list, tuple)):
            children = [clz.from_(str(i), item) for i, item in enumerate(obj)]
            return clz(type_as_str, name, children)
        elif isinstance(obj, set):
            children = [clz.from_(None, item) for item in obj]
            return clz(type_as_str, name, children)
        elif isinstance(obj, dict):
            children = [clz.from_(key, value) for key, value in obj.items()]
            return clz("dict", name, children)
        else:
            children = [clz.from_(key, value) for key, value in interesting_attributes(obj)]
            if children:
                return clz(type_as_str, name, children)
            else:
                return Leaf(type_as_str, name, obj)

    def print_(self, indent=0):
        sys.stdout.write(" " * indent)
        print "%s(%s)" % (self.name, self.type_)
        for child in self.children:
            child.print_(indent + 4)


class Leaf(Node):

    def __init__(self, type_, name, value):
        super(Leaf, self).__init__(type_, name, [])
        self.value = value

    def get_children(self):
        return None

    def get_num_children(self):
        return 0

    def print_(self, indent=0):
        sys.stdout.write(" " * indent)
        print "%s(%s) = %r" % (self.name, self.type_, self.value)


def object_iter():
    pass
