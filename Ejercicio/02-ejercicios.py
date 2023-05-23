def no_space(text):
    nuevo_text = ""
    for char in text:
        if char != " ":
            nuevo_text += char
    return nuevo_text


def reverse(text):
    texto_al_reves = ""
    for char in text:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(text):
    text = no_space(text)
    texto_al_reves = reverse(text)
    return text.lower() == texto_al_reves.lower()


es_palindromo("hello")
