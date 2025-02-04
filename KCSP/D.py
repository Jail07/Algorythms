def max_productivity(n, e, s, p):
    max_sum = 0
    current_sum = sum(p[:e])  # Начальное окно длины e
    max_sum = current_sum
    i = e  # Начинаем с минуты e

    while i < n:
        # Найти лучший возможный интервал работы после отдыха
        best_next_sum = 0
        best_index = -1

        for j in range(i, min(n - e + 1, i + s + 1)):  # Ищем новый отрезок
            next_sum = sum(p[j:j + e])  # Считаем сумму e минут
            if next_sum > best_next_sum:
                best_next_sum = next_sum
                best_index = j

        if best_index == -1:  # Если больше работать нельзя
            break

        max_sum += best_next_sum
        i = best_index + e + s  # Переход на новую работу + отдых

    return max_sum


# Читаем входные данные
n, e, s = map(int, input().split())
p = list(map(int, input().split()))

# Выводим результат
print(max_productivity(n, e, s, p))
