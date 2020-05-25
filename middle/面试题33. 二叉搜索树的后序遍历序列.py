def verifyPostorder(postorder: list) -> bool:
    length = len(postorder)
    if length == 0:
        return False
    root = postorder[length - 1]
    i = 0
    while i < length - 1 and postorder[i] < root:
        i += 1
    j = i
    while j < length - 1 and postorder[j] > root:
        j += 1
    if j < length - 1:
        return False
    left = True
    if i > 0:
        left = verifyPostorder(postorder[0:i])
    right = True
    if j < length - 1:
        right = verifyPostorder(postorder[i:length - 1])
    return left and right