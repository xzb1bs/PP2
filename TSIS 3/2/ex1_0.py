def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Пример использования функции
grams_amount = int(input())
ounces_result = grams_to_ounces(grams_amount)
print(f"{grams_amount} граммов равно {ounces_result:.2f} унции")
