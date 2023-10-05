#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def look_next_opened_box(opened_boxes):
    """Find the next opened box to check.

    Args:
        opened_boxes (dict): A dictionary that keeps track of boxes we have opened.

    Returns:
        list: The keys inside the next box we should check.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if we can open all the boxes.

    Args:
        boxes (list): A list containing all the boxes and their keys.

    Returns:
        bool: True if we can open all the boxes, otherwise, False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') == 'checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Entry point."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
