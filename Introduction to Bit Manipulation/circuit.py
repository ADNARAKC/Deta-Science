def circuit_output(A, B, C):
    X = (not A) & B
    Y = C | (not X)
    Z = X & Y
    Q = Z
    return Q

print(f"Output for A=0, B=0, C=0: {circuit_output(0, 0, 0)}")
print(f"Output for A=0, B=1, C=0: {circuit_output(0, 1, 0)}")
print(f"Output for A=1, B=0, C=0: {circuit_output(1, 0, 0)}")