import random

# 有名人の名前リスト（男女）
famous_men = ["ウサイン・ボルト", "カール・ルイス", "朝原宣治", "桐生祥秀", "山縣亮太"]
famous_women = ["福島千里", "ジャマイカ・フレイザー", "アリソン・フェリックス", "市川華菜", "土井杏南"]

# 一般的な日本人男性名
men_names = [
    "佐藤健", "鈴木大輔", "高橋翔", "田中悠斗", "伊藤直樹",
    "渡辺陽介", "山本健太", "中村優", "小林誠", "加藤亮",
    "吉田拓海", "山田航", "佐々木悠", "松本大地", "斎藤翼",
    "清水優斗", "山口大輝", "森本悠真", "石井颯太", "池田悠人"
]

# 一般的な日本人女性名
women_names = [
    "佐藤美咲", "鈴木彩花", "高橋優奈", "田中美穂", "伊藤彩香",
    "渡辺真央", "山本美月", "中村彩乃", "小林優衣", "加藤美咲",
    "吉田彩", "山田美咲", "佐々木彩花", "松本美優", "斎藤美咲",
    "清水彩花", "山口美咲", "森本彩花", "石井美咲", "池田美咲"
]

# 男性25人、女性25人
men = famous_men + random.sample(men_names, 20)
women = famous_women + random.sample(women_names, 20)

# タイムをランダム生成
def generate_time():
    return round(random.uniform(9.56, 12.99), 2)

# 選手リスト作成
runners = []

for name in men:
    runners.append({"name": name, "gender": "男性", "time": generate_time()})

for name in women:
    runners.append({"name": name, "gender": "女性", "time": generate_time()})

# タイムが良い順にソート
runners_sorted = sorted(runners, key=lambda x: x["time"])

# 結果表示
for i, runner in enumerate(runners_sorted, 1):
    print(f"{i:2d}位: {runner['name']}（{runner['gender']}） - {runner['time']}秒")