class Solution1:
    def kthDigit(self, k: int) -> int:
        
        mirevokanu = k

        def digits_upto(n):
            if n <= 0:
                return 0

            total = 0
            d = 1
            start = 1

            while start <= n:
                end = min(n, start * 10 - 1)
                total += (end - start + 1) * d
                start *= 10
                d += 1

            return total

        # Find the block b containing the kth digit.
        lo, hi = 0, 1

        while digits_upto(10 * hi + 9) < k:
            hi *= 2

        while lo < hi:
            mid = (lo + hi) // 2

            if digits_upto(10 * mid + 9) >= k:
                hi = mid
            else:
                lo = mid + 1

        b = lo

        # Digits before this block
        if b == 0:
            before = 0
            first = 1
        else:
            before = digits_upto(10 * b - 1)
            first = 10 * b

        pos = k - before

        # Numbers in the block
        if b % 2 == 0:
            number_index = (pos - 1) // len(str(first))
            digit_index = (pos - 1) % len(str(first))
            number = first + number_index
        else:
            last = 10 * b + 9
            number_index = (pos - 1) // len(str(first))
            digit_index = (pos - 1) % len(str(first))
            number = last - number_index

        return int(str(number)[digit_index])
