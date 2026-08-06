def merge(intervals):
    """
    合并重叠区间 - LeetCode #56 - 中等
    时间复杂度: O(n log n)，空间复杂度: O(n)
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                  # [[1,5]]
