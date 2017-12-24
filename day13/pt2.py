s = """0: 3
1: 2
2: 5
4: 4
6: 4
8: 6
10: 6
12: 6
14: 8
16: 6
18: 8
20: 8
22: 8
24: 12
26: 8
28: 12
30: 8
32: 12
34: 12
36: 14
38: 10
40: 12
42: 14
44: 10
46: 14
48: 12
50: 14
52: 12
54: 9
56: 14
58: 12
60: 12
64: 14
66: 12
70: 14
76: 20
78: 17
80: 14
84: 14
86: 14
88: 18
90: 20
92: 14
98: 18
"""

from itertools import count

lengths = { key: value for key, value in map(lambda x: map(int, x.split(": ")), s.splitlines()) }
state = { key: { 'position': 0, 'step': 1 } for key in lengths }

def tick(state):
    for key, value in state.items():
        value['position'] += value['step']

        if value['position'] == lengths[key] - 1:
            value['step'] = -1
        elif value['position'] == 0:
            value['step'] = 1

success = False
delays = set()

for i in count():
    delays.add(i)
    failures = set()
    for delay in delays:
        if i - delay in state and state[i - delay]['position'] == 0:
            failures.add(delay)
        elif i - delay >= 98:
            print(delay)
            success = True
            break

    delays -= failures

    if success:
        break

    tick(state)
