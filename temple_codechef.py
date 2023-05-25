MOD = 1000000007

def solve(k):
    # calculate minimum x for given k
    x = (2**k - 1) % MOD
    
    # calculate y such that x and y satisfy the condition
    y = (2**k - 2) % MOD
    
    return x, y

# read number of test cases
t = int(input())

for i in range(t):
    # read k for current test case
    k = int(input())
    
    # solve for current test case
    x, y = solve(k)
    
    # print output
    print(x, y)

# MOD = 10**9 + 7

# def solve(k, f):
#     S = sum(f)
#     min_x = float('inf')
#     for y in range(1, 2**k):
#         x = (2**k - 1) * y - S // 2**k
