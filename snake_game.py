import random

snake = [5]
food = random.randint(1, 10)
score = 0

print("🐍 Snake Game (1-10 board)")
print("Controls: a = left, d = right")

while True:
    print(f"Snake at {snake[-1]} | Food at {food}")
    move = input("Move: ")

    if move == 'a':
        snake.append(snake[-1] - 1)
    elif move == 'd':
        snake.append(snake[-1] + 1)
    else:
        print("Invalid move")
        continue

    if snake[-1] == food:
        score += 1
        food = random.randint(1, 10)
        print("🍎 Food eaten!")
    else:
        snake.pop(0)

    if snake[-1] < 1 or snake[-1] > 10:
        print("💀 Game Over")
        print("Score:", score)
        break
