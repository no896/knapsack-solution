import sys

def solve_knapsack_dp():
    # 品物データ (品物番号, 容量, 値段)
    items = [
        (1, 4, 6), (2, 8, 12), (3, 3, 4), (4, 5, 3), (5, 9, 7), (6, 2, 1),
        (7, 3, 3), (8, 1, 2), (9, 5, 7), (10, 2, 3), (11, 4, 4), (12, 2, 2),
        (13, 7, 10), (14, 10, 13), (15, 3, 5), (16, 13, 16), (17, 11, 14), (18, 8, 9)
    ]
    
    max_capacity = 45
    n = len(items)
    
    # dp[w] は「容量 w のときの最高値段」を記録するメモ帳
    dp = [0] * (max_capacity + 1)
    
    # どの容量のときに、どの品物を選んだかを追跡するためのメモ帳
    # (後から「選んだ品物番号の組み合わせ」を復元するために使います)
    chosen_items = [[] for _ in range(max_capacity + 1)]
    
    # 品物を1つずつ順番にループして考えていく
    for j in range(n):
        item_id = items[j][0]
        weight  = items[j][1]
        value   = items[j][2]
        
        # 容量 max_capacity から weight まで、後ろ向きにメモ帳を更新していく
        for w in range(max_capacity, weight - 1, -1):
            # もし「この品物を入れた場合」の方が値段が高くなるなら
            if dp[w - weight] + value > dp[w]:
                # メモ帳の最高値段を更新する
                dp[w] = dp[w - weight] + value
                # その時の組み合わせも更新する（過去の組み合わせに、今の品物を追加）
                chosen_items[w] = chosen_items[w - weight] + [item_id]

    # 結果を確実に画面に出力する（課題1と同じフォーマット）
    print("\n=== 【課題2：動的計画法】 探索結果 ===")
    print(f"最高総値段: {dp[max_capacity]}")
    
    # 選ばれた品物から総容量を再計算
    best_weight = sum(item[1] for item in items if item[0] in chosen_items[max_capacity])
    print(f"その時の総容量: {best_weight} / {max_capacity}")
    
    print("品物番号の組み合わせ:")
    print(chosen_items[max_capacity])
    print("=======================================\n")

# プログラムを動かす
solve_knapsack_dp()