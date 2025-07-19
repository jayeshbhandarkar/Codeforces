def sample(length, bin_str):
    one_count = sum(1 for bit in bin_str if bit == '1')
    flip_gain = length - 2 * one_count
    return length * one_count + flip_gain

t = int(input())
for _ in range(t):
    size = int(input())
    orig = input().strip()
    res = sample(size, orig)
    print(res)
