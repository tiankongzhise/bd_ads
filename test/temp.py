def chunk_list(lst, size=100):
    """将列表按指定大小分块
    :param lst: 原始列表
    :param size: 每块大小（默认100）
    :return: 分块后的二维列表
    """
    return [lst[i:i+size] for i in range(0, len(lst), size)]

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21]
    # chunks = chunk_list(lst, size=10)
    chunks = lst[20:30000]
    print(chunks)
