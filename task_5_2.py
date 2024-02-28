# Завдання

# Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, 
# де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент,
# який є більшим або рівним заданому значенню.

def binary_search_with_bounds(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            # Знайдено точне значення, виходимо з циклу
            upper_bound = arr[mid]
            break
    
    # Якщо точне значення не знайдено, визначаємо верхню межу
    if upper_bound is None:
        if low < len(arr):
            upper_bound = arr[low]
        else:
            # Якщо всі елементи менші за x, верхньої межі не існує
            upper_bound = None

    return (iterations, upper_bound)

# Відсортований масив з дробовими числами
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
x = 5.5

# Викликаємо функцію і друкуємо результат
result = binary_search_with_bounds(arr, x)
print(result)
