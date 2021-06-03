

def max_segments(segments, start):
    """
    >>> max_segments([(5,8),(0,2),(4,7)],0)
    3
    """
    for down, up in segments:
        if down <= start and up >= start:
            return max_segments(segments,up+1)
    return start

def get_max_in_file(name_file):
    """
    >>> get_max_in_file('small_input.txt')
    3

    >>> get_max_in_file('input.txt')
    23923783

    :param name_file:
    :return:
    """
    with open(name_file) as f:
        segments = []
        start = 0

        for line in f:
            a,b = [int(a) for a in line.split("-")]
            segments.append((a,b))

        now_max = max_segments(segments,start)
        return now_max

def merge_segments(name_file):
    """
    >>> merge_segments("small_input.txt")
    [(0, 2), (4, 8)]

    """
    with open(name_file) as f:
        segments = []
        for line in f:
            a,b = [int(a) for a in line.split("-")]
            segments.append((a,b))
    merged = True
    while merged:
        merged = False
        segments.sort()
        for i,segment in enumerate(segments):
            start,end = segment
            for next_start,next_end in segments[i+1:]:
                if next_start >= start and next_end <= end:
                    # segment 1 is larger than this segment
                    segments.remove((next_start,next_end))
                elif next_start >= start and next_start <= end:
                    segments.append((start,next_end))
                    segments.remove((start,end))
                    segments.remove((next_start,next_end))
                    merged = True
                    break
            if merged:
                break
    return segments

if __name__ == "__main__":
    segments = merge_segments('input.txt')
    segments.sort()
    print(segments)
    numbers_available = segments[0][0]

    for i in range(len(segments)-1):
        numbers_available+=segments[i+1][0]-segments[i][1]-1
        print(numbers_available)
    numbers_available += 4294967295 - segments[-1][1]
    print(numbers_available)
