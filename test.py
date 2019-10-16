import random

# おみくじリストの作成
paper = ["大吉","中吉","小吉","吉","末吉","凶"]

# おみくじを引いた結果をresultに
result = random.choice(paper)

# おみくじを出力
print("今日の運勢は"f'{result}'"です。")

# 追加メッセージ
if result == paper[0]:
    print('おめでとうございます！')
elif result == paper[5]:
    print('そんなときもあるさ')

    print("渡部")
    print("桑原")

    #倉持