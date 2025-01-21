def max_points(test_cases):
    results = []
    
    for case in test_cases:
        n, arr = case
        evens = [x for x in arr if x % 2 == 0]
        odds = [x for x in arr if x % 2 != 0]
        rearranged = evens + odds
        
        s = 0
        points = 0
        
        for num in rearranged:
            s += num
            if s % 2 == 0:
                points += 1
                while s % 2 == 0:
                    s //= 2
        
        results.append(points)
    
    return results

if __name__ == "__main__":
    t = int(input().strip())
    test_cases = []
    
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        test_cases.append((n, arr))
    
    results = max_points(test_cases)
    for res in results:
        print(res)
