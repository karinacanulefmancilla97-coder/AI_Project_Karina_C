# Sistema simple de recomendaciones por categoría de interés.
# El usuario selecciona una categoría y recibe tres productos relacionados.

PRODUCTS_BY_CATEGORY = {
    "tecnología": [
        "Smartphone de gama media",
        "Laptop para estudio",
        "Auriculares inalámbricos",
    ],
    "deportes": [
        "Bicicleta de montaña",
        "Yude deportivo",
        "Malla de fútbol",
    ],
    "música": [
        "Guitarra eléctrica",
        "Bajo eléctrico",
        "Studio de grabación portátil",
    ],
}


def recommend_products(category):
    """Devuelve los tres productos disponibles para una categoría."""
    # Normalizamos la respuesta del usuario para que coincida con las claves.
    category = category.strip().lower()

    if category in PRODUCTS_BY_CATEGORY:
        return PRODUCTS_BY_CATEGORY[category]

    return []


def main():
    """Pregunta por una categoría y muestra recomendaciones al usuario."""
    print("Selecciona una categoría de interés:")
    print("1. Tecnología")
    print("2. Deportes")
    print("3. Música")

    # Se espera una respuesta numérica del usuario.
    choice = input("Tu elección: ").strip()

    categories = {
        "1": "tecnología",
        "2": "deportes",
        "3": "música",
    }

    # Si la opción no es válida, se muestra un mensaje de error.
    if choice not in categories:
        print("Por favor, selecciona una de las opciones mostradas.")
        return

    selected_category = categories[choice]
    recommendations = recommend_products(selected_category)

    print(f"\nRecomendaciones para {selected_category.title()}:")
    for index, product in enumerate(recommendations, start=1):
        print(f"{index}. {product}")


if __name__ == "__main__":
    main()
