frase = input("Escreva uma frase: ")

letras = {}

for letra in frase:
    if letra.isalpha():
        letra = letra.lower()
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

for letra in sorted(letras):
    print(f"'{letra}': {letras[letra]}")