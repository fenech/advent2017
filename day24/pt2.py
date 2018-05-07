s = """14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14
"""

bridges = set(tuple(map(int, line.split("/"))) for line in s.splitlines())

def recurse(port, bridges, strength, length):
    steps = set(b for b in bridges if port in b)
    for b in steps:
        left, right = b
        next_port = right if left == port else left
        for l, s in recurse(next_port, bridges - {b}, strength + left + right, length + 1):
            yield l, s
    yield length, strength

print(max(recurse(0, bridges, 0, 0)))
