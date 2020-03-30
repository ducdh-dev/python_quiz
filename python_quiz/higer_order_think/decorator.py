def merging_arr(arr, n):
    def n_times(n):
        def func_decor(func):
            def func_wrapper(arr):
                for _ in range(n):
                    arr = func(arr)
                return arr

            return func_wrapper

        return func_decor

    @n_times(n)
    def sum_once(arr):
        res = [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1, 2)]
        if len(arr) % 2 == 1:
            res.append(arr[-1])
        return res

    return sum_once(arr)


print(merging_arr([3, 5, 1, 6, 2, 4, 3, 7], 2))
# => [ 3+5, 1+6, 2+4, 3+7 ] n = 1
# => [ 8+7, 6+10] n = 2
# => [15, 16]
