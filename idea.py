import random

TOTAL_TICKETS = 100_000  # 宝くじの総数
WINNING_TICKETS = 100    # 当たりの枚数（例：100枚）

# 宝くじリストを作成し、当たりをランダムに配置
tickets = [0] * TOTAL_TICKETS
winning_indices = random.sample(range(TOTAL_TICKETS), WINNING_TICKETS)
for idx in winning_indices:
    tickets[idx] = 1

# 当たりの枚数をカウント
num_winning = sum(tickets)

print(f"宝くじ{TOTAL_TICKETS}枚中、当たりは{num_winning}枚です。")