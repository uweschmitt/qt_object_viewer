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


_do_not_recurse_into = (types.MethodType, types.BuiltinMethodType, types.UnboundMethodType,
                        types.MemberDescriptorType, types.ClassType, types.TypeType)


def interesting_attributes(obj):
    for name in dir(obj):
        value = getattr(obj, name)
        if name.startswith("_"):
            continue
        if isinstance(value, _do_not_recurse_into):
            continue
        yield name, value


class Node(object):

    def __init__(self, parent, type_, name):
        self.parent = parent
        self.type_ = type_
        self.name = name
        self.index = -1
        self.children = []

    def set_children(self, children):
        self.children = children
        for i, child in enumerate(children):
            child.index = i

    def get_children(self):
        return self.children

    def get_num_children(self):
        return len(self.children)

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_parent(self):
        return self.parent

    @classmethod
    def from_(clz, name, obj, parent=None):
        type_as_str = type_to_str(type(obj))
        if isinstance(obj, (int, float, basestring)):
            return Leaf(parent, type_as_str, name, obj)
        else:
            if isinstance(obj, _do_not_recurse_into):
                return Leaf(parent, type_as_str, name, obj)
            result = clz(parent, type_as_str, name)
            children = []
            if isinstance(obj, (list, tuple)):
                children = [clz.from_("", item, parent=result) for i, item in enumerate(obj)]
            elif isinstance(obj, set):
                children = [clz.from_("", item, parent=result) for item in obj]
            elif isinstance(obj, dict):
                children = [clz.from_(key, value, parent=result) for key, value in obj.items()]
            else:
                children = [clz.from_(key, value, parent=result) for key, value in interesting_attributes(obj)]
                if not children:
                    return Leaf(parent, type_as_str, name, obj)
            result.set_children(children)
            return result

    def print_(self, indent=0):
        sys.stdout.write(" " * indent)
        print "at %d: %s(%s)" % (self.index, self.name, self.type_)
        for child in self.children:
            child.print_(indent + 4)


class Leaf(Node):

    def __init__(self, parent, type_, name, value):
        super(Leaf, self).__init__(parent, type_, name)
        self.value = value

    def get_children(self):
        return None

    def get_num_children(self):
        return 0

    def print_(self, indent=0):
        sys.stdout.write(" " * indent)
        print "at %d: %s(%s) = %r" % (self.index, self.name, self.type_, self.value)
