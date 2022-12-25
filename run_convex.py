#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, top area = {f.area_top()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")