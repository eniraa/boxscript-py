import numpy


def test_matrix():
    """Test for matrix"""
    from boxscript.utils import matrix

    numpy.testing.assert_array_equal(
        matrix("hello\nworld"),
        numpy.array([["h", "e", "l", "l", "o"], ["w", "o", "r", "l", "d"]]),
    )

    numpy.testing.assert_array_equal(
        matrix("hello\nhi"),
        numpy.array([["h", "e", "l", "l", "o"], ["h", "i", "\0", "\0", "\0"]]),
    )

    numpy.testing.assert_array_equal(
        matrix("a\nbc\ndef"),
        numpy.array([["a", "\0", "\0"], ["b", "c", "\0"], ["d", "e", "f"]]),
    )


def test_neighbors():
    """Test for neighbors"""
    from boxscript.utils import neighbors

    assert neighbors(numpy.array([["a", "b"], ["c", "d"]]), numpy.array([0, 0])) == {
        "N": "\0",
        "E": "b",
        "S": "c",
        "W": "\0",
    }

    assert neighbors(numpy.array([["a"]]), numpy.array([0, 0])) == {
        "N": "\0",
        "E": "\0",
        "S": "\0",
        "W": "\0",
    }

    assert neighbors(
        numpy.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]),
        numpy.array([1, 1]),
    ) == {
        "N": "b",
        "E": "f",
        "S": "h",
        "W": "d",
    }

    assert neighbors(
        numpy.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]),
        numpy.array([100, 100]),
    ) == {
        "N": "\0",
        "E": "\0",
        "S": "\0",
        "W": "\0",
    }

    assert neighbors(numpy.array([]), numpy.array([-75, 32000])) == {
        "N": "\0",
        "E": "\0",
        "S": "\0",
        "W": "\0",
    }
