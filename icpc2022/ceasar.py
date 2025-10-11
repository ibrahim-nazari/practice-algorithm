t=int(input())
for _ in range(t):
    line = input().strip()
    parts = line.split()
    op = parts[0]
    S = int(parts[1])
    T = parts[2]
    
    result = ''
    for c in T:
        base = ord('a')
        shifted = (ord(c) - base + S) % 26
        result += chr(base + shifted)
    
    print(result)
    