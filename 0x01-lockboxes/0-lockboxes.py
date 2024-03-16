#!/usr/bin/python3
""" a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the
        boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
