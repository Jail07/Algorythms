def can_reach_target(instructions, x, y):
    # Simulate one full sequence
    positions = set()
    current_x, current_y = 0, 0
    positions.add((current_x, current_y))

    for move in instructions:
        if move == 'U':
            current_y += 1
        elif move == 'D':
            current_y -= 1
        elif move == 'L':
            current_x -= 1
        elif move == 'R':
            current_x += 1
        positions.add((current_x, current_y))

    # Compute net change after one full sequence
    dx, dy = current_x, current_y

    # Check if target is reachable
    for (x0, y0) in positions:
        if dx == 0 and dy == 0:
            # Robot returns to (0, 0) after each sequence
            if x0 == x and y0 == y:
                return True
        else:
            # Solve x = x0 + k * dx, y = y0 + k * dy
            if dx == 0:
                if x != x0:
                    continue
                if dy == 0:
                    if y != y0:
                        continue
                    else:
                        return True
                else:
                    if (y - y0) % dy == 0 and (y - y0) // dy >= 0:
                        return True
            else:
                if (x - x0) % dx != 0:
                    continue
                k = (x - x0) // dx
                if k < 0:
                    continue
                if y == y0 + k * dy:
                    return True
    return False


# Example usage
instructions = "UR"
x, y = 2, 2
print(can_reach_target(instructions, x, y))  # Output: True