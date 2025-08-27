P1C, P1U, P1P = [float(x) for x in input().split(" ")]
P2C, P2U, P2P = [float(x) for x in input().split(" ")]

P1 = P1U * P1P
P2 = P2U * P2P

TOTAL = P1 + P2

print(f"VALOR A PAGAR: R$ {TOTAL:0.2f}")