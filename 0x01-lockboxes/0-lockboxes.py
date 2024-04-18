#!/usr/bin/python3
'''module for working with lockboxes.
'''


def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return True
    unlocked = [False] * n
    unlocked[0] = True
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)
