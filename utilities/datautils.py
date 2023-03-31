def flatten_list(items):
    """
    Usecase of 'yield from'
    flattens nested lists
    """
    for i in items:
        if isinstance(i, list):
            yield from flatten_list(i)
        else:
            yield i


def flatten_list2(items):
    stack = [iter(items)]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()
