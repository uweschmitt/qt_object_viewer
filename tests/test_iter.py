from qt_object_viewer import object_iter, Node, Leaf

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

    assert get_output().strip() == """
root(dict)
    a(int) = 3
    b(tuple)
        0(int) = 1
        1(dict)
            c(int) = 7
        2(int) = 3
        3(test_iter.Test)
            i(int) = 3
            j(list)
                0(int) = 1
                1(int) = 2
                2(int) = 3
            k(dict)
                a(int) = 3
                """.strip()
