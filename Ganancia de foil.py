import math

P = 4  # positivos antes
N = 4  # negativos antes
p = 3  # positivos después
n = 0  # negativos después

fraccion_despues = p / (p + n)
fraccion_antes = P / (P + N)

log_despues = math.log2(fraccion_despues)
log_antes = math.log2(fraccion_antes)

foil_gain = p * (log_despues - log_antes)

print("Condición: nivel_educativo == 'terciario'")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p}")
print(f"n (negativos después) = {n}")
print(f"p / (p + n) = {fraccion_despues:.3f}")
print(f"P / (P + N) = {fraccion_antes:.3f}")
print(f"log2(p / (p + n)) = {log_despues:.3f}")
print(f"log2(P / (P + N)) = {log_antes:.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")