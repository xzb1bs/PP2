def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Пример использования функции
fahrenheit_temperature = float(input())
celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} градусов по Фаренгейту равны {celsius_result:.2f} градусам по Цельсию")
