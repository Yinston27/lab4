item = {
    'r':{'price':25, 'weight':3},
    'p':{'price':15, 'weight':2},
    'a':{'price':15, 'weight':2},
    'm':{'price':20, 'weight':2},
    'i':{'price':5, 'weight':1},
    'k':{'price':15, 'weight':1},
    'x':{'price':20, 'weight':3},
    't':{'price':25, 'weight':1},
    'f':{'price':15, 'weight':1},
    'd':{'price':10, 'weight':1},
    's':{'price':20, 'weight':2},
    'c':{'price':20, 'weight':2},
    
}

def gen_memo_table(items, max_weight, basic_point=20, required_item=None):
    if required_item in items:
        max_weight -= items.pop(required_item)['weight']
        
    table = [[0 for col in range(max_weight)] for row in range(len(items))]
    for i, item in enumerate(items.values()):
        price = item['price']
        weight = item['weight']
        for limit_weught in range(1, max_weight+1):
            limit_idx = limit_weught - 1
            if i == 0:
                res = 0 if limit_weught < weight else price
                table[i][limit_idx] = res
            else:
                prev_price = table[i - 1][limit_idx]
                if weight > limit_weught:
                    table[i][limit_idx] = prev_price
                else:
                    if limit_idx < weight:
                        prev_without_current = 0
                    else:
                        prev_without_current = table[i - 1][limit_idx - weight]
                    res = prev_without_current + price
                    table[i][limit_idx] = max(res, prev_price)
    for row in table:
        print(row)






if __name__ == '__main__':
    gen_memo_table(item, 9, 'd')