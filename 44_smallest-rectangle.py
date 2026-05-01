def solution(sizes):
    # w = max(sizes[0])
    # h = max(sizes[1])
    max_width = 0
    max_height = 0
    
    for width, height in sizes :
        width, height = max(width, height), min(width, height)
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    return max_width*max_height