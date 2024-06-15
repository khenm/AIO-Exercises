def sliding_window(num_list: list[int], k: int):
    """Sliding the window to the right for 1 index, 
    capturing exact k elements. Among those k values, find the
    maximum value and add to the result list.

    Args:
        num_list (list[int]): input list of integers 
        k (int): number of elements to be viewed
    """
    # intialize result list
    result: list[int] = []

    # sliding the window
    n: int = len(num_list) - (k - 1)  # number of times to be looped
    for i in range(n):
        maximum_value: int = max(num_list[i:i+k])
        result.append(maximum_value)
    print(result)


def main():
    num_list: list[int] = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k: int = 3
    sliding_window(num_list=num_list, k=k)


if __name__ == "__main__":
    main()
