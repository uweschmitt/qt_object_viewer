from qt_object_viewer import Node, Leaf

from contextlib import contextmanager
import cStringIO


@contextmanager
def capture_output():
    import sys
    fp = cStringIO.StringIO()
    try:
        sys.stdout = fp
        yield lambda fp=fp: fp.getvalue()
    finally:
        sys.stdout = sys.__stdout__

def test_0():

    class Test(object):

        i = 3
        j = list((1, 2, 3))
        k = dict(a=3)

    obj = dict(a=3, b=(1, dict(c=7), 3, Test()))
    tree = Node.from_("root", obj)
    with capture_output() as get_output:
        tree.print_()

    print get_output()
    assert get_output().strip() == """
at -1: root(dict)
    at 0: a(int) = 3
    at 1: b(tuple)
        at 0: (int) = 1
        at 1: (dict)
            at 0: c(int) = 7
        at 2: (int) = 3
        at 3: (test_iter.Test)
            at 0: i(int) = 3
            at 1: j(list)
                at 0: (int) = 1
                at 1: (int) = 2
                at 2: (int) = 3
            at 2: k(dict)
                at 0: a(int) = 3
                """.strip()
