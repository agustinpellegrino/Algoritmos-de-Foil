datos = [
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

# Separar ejemplos positivos y negativos
positivos = [d for d in datos if d["en_formacion"]]
negativos = [d for d in datos if not d["en_formacion"]]

# Analizar los atributos
atributos = ["departamento", "nivel_educativo", "edad"]

for atributo in atributos:
    valores_positivos = {d[atributo] for d in positivos}
    valores_negativos = {d[atributo] for d in negativos}

    exclusivos = valores_positivos - valores_negativos

    print(f"{atributo}: {exclusivos}")

# Regla inducida
print("\nRegla inducida:")
print("SI edad <= 24 ENTONCES en_formacion = True")