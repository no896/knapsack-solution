import sys

def solve_knapsack_brute_force():
    # 品物データ (品物番号, 容量, 値段)
    items = [
        (1, 4, 6), (2, 8, 12), (3, 3, 4), (4, 5, 3), (5, 9, 7), (6, 2, 1),
        (7, 3, 3), (8, 1, 2), (9, 5, 7), (10, 2, 3), (11, 4, 4), (12, 2, 2),
        (13, 7, 10), (14, 10, 13), (15, 3, 5), (16, 13, 16), (17, 11, 14), (18, 8, 9)
    ]
    
    max_capacity = 45
    n = len(items)
    
    best_value = 0
    best_combination = []
    best_weight = 0
    
    # 2^18 通りの組み合わせを総当たり
    for i in range(2**n):
        current_weight = 0
        current_value = 0
        current_combination = []
        
        for j in range(n):
            # iのj番目のビットが1なら、その品物を選ぶ
            if (i >> j) & 1:
                current_weight += items[j][1]
                current_value += items[j][2]
                current_combination.append(items[j])
        
        # 容量制限以下、かつこれまでの最高価値を超えていたら更新
        if current_weight <= max_capacity:
            if current_value > best_value:
                best_value = current_value
                best_weight = current_weight
                best_combination = current_combination

    # 結果を確実に画面に出力する
    print("\n=== 探索結果 ===")
    print(f"最高総値段: {best_value}")
    print(f"その時の総容量: {best_weight} / {max_capacity}")
    print("品物番号の組み合わせ:")
    print([item[0] for item in best_combination])
    print("===============\n")

# プログラムを動かす
solve_knapsack_brute_force()