NAME = input()
WAGE = float(input())
SALES = float(input())

MWAGE = WAGE + (SALES * 0.15)

print(f"TOTAL = R$ {MWAGE:0.2f}")