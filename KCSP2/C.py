import sys
from collections import deque


def process_events(n, q, r, events):
    queue_x = deque()  # Очередь X
    queue_y = deque()  # Очередь Y

    finish_x = 0  # Время завершения последнего посетителя в X
    finish_y = 0  # Время завершения последнего посетителя в Y
    count_x = 0  # Количество обработанных посетителей в X
    count_y = 0  # Количество обработанных посетителей в Y
    last_op_x = None  # Последняя операция в X
    last_op_y = None  # Последняя операция в Y

    results = []

    for event in events:
        parts = event.split()

        if len(parts) == 3:  # Посетитель
            t, op, w = int(parts[0]), parts[1], int(parts[2])

            # Выбираем, в какое окно идёт посетитель
            if len(queue_x) <= len(queue_y):
                queue_x.append((t, op, w))
            else:
                queue_y.append((t, op, w))

        else:  # Вопрос Славы
            d, c = int(parts[0]), parts[1]

            # Обрабатываем очередь X
            while queue_x and finish_x <= d:
                t, op, w = queue_x.popleft()
                if count_x > 0 and last_op_x != op:
                    finish_x += r  # Переключение между задачами
                finish_x = max(finish_x, t) + w
                count_x += 1
                last_op_x = op

            # Обрабатываем очередь Y
            while queue_y and finish_y <= d:
                t, op, w = queue_y.popleft()
                if count_y > 0 and last_op_y != op:
                    finish_y += r  # Переключение между задачами
                finish_y = max(finish_y, t) + w
                count_y += 1
                last_op_y = op

            # Формируем ответ на запрос
            if c == "X":
                results.append(f"{count_x} {finish_x if finish_x <= d else 0}")
            else:
                results.append(f"{count_y} {finish_y if finish_y <= d else 0}")

    sys.stdout.write("\n".join(results) + "\n")


# Чтение входных данных
if __name__ == "__main__":
    n, q, r = map(int, sys.stdin.readline().split())
    events = [sys.stdin.readline().strip() for _ in range(n + q)]
    process_events(n, q, r, events)
