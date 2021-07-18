import numpy
cimport numpy


cpdef numpy.ndarray matrix(str code):
    """Converts a string into a matrix.

    Args:
        code (str): The input string to convert to a matrix

    Returns:
        numpy.ndarray: The 2D matrix of the string's chars.
    """
    cdef list lines
    cdef int length

    lines = code.splitlines()
    length = max(map(len, lines))
    return numpy.array([[*line.ljust(length, "\0")] for line in lines], dtype="str")


cpdef dict neighbors(numpy.ndarray characters, numpy.ndarray pos):
    """Finds the characters neighboring a position

    Args:
        text (str): The text to use when finding neighbors
        pos (list[int]): The location in the form [row, column]

    Returns:
        dict[str, str]: A dictionary of neighbors of the form
            {"N": `chr`, "S": `chr`, "E": `chr`, "W": `chr`}.
            If there is no neighboring character in a cardinal direction,
            then that `chr` will be \0.
    """
    cdef dict directions, neighboring

    directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    neighboring = {}

    for location in directions:
        loc = pos + directions[location]
        if 0 <= loc[0] < characters.shape[0] and 0 <= loc[1] < characters.shape[1]:
            neighboring[location] = characters[loc[0], loc[1]]
        else:
            neighboring[location] = "\0"

    return neighboring
