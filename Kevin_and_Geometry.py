def solve_single_test():
    n = int(input())
    nums = sorted(map(int, input().split()))
    
    # First find duplicates quickly
    prev = nums[0]
    dup = None
    for i in range(1, n):
        if nums[i] == prev:
            if not dup:  # First duplicate found
                dup = nums[i]
            elif nums[i] != dup:  # Second duplicate found
                print(f"{min(prev, dup)} {max(prev, dup)} {min(prev, dup)} {max(prev, dup)}")
                return
        prev = nums[i]
    
    if not dup:  # No duplicates found
        print("-1")
        return
    
    # If we're here, we have exactly one duplicate number
    # We need to find two numbers x and y where y < x + 2*dup
    dup_count = 0
    remaining = []
    
    # Get remaining numbers (excluding two instances of duplicate)
    for num in nums:
        if num == dup and dup_count < 2:
            dup_count += 1
            continue
        remaining.append(num)
    
    # Check pairs
    for i in range(len(remaining)-1):
        if remaining[i+1] < remaining[i] + 2*dup:
            print(f"{min(remaining[i], remaining[i+1])} {max(remaining[i], remaining[i+1])} {dup} {dup}")
            return
    
    print("-1")

def main():
    t = int(input())
    for _ in range(t):
        solve_single_test()

if __name__ == "__main__":
    main()