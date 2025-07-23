t = int(input())
for _ in range(t):
    s = input()
    s_sorted = ''.join(sorted(s))
    if "FFT" in s_sorted or "NTT" in s_sorted:
        s_sorted = s_sorted[::-1]
    print(s_sorted)
