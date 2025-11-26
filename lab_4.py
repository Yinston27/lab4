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
LENGTH = 2
WIDTH = 4

def gen_memo_table(items, max_weight, required_item=None, basic_point=20):
    list_change = None
    if required_item in items:
        list_change = items.pop(required_item)
        max_weight -= list_change['weight']
        basic_point += list_change['price']

    table = [[0 for col in range(max_weight)] for row in range(len(items))]
    iterator = enumerate(items.keys())
    return_iterator = enumerate(items.keys())
    for i, item in iterator:
        price = items[item]['price']
        weight = items[item]['weight']
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
    # for row in table:
    #     print(row)
    return [items, table, return_iterator, max_weight, required_item, basic_point, list_change]


def return_list(items, table, return_iterator, max_weight, required_item, basic_point, list_change=None):
    if required_item:
        prev_bag = [required_item for i in range(list_change['weight'])]
    else:
        prev_bag = []

    item_idx, limit_weight = len(items)-1, max_weight-1
    negative_point = 0
    d = [0 for i in range(len(items))]
    for i, j in return_iterator:
        d[i] = j

    while item_idx >= 0:
        weight = items[d[item_idx]]['weight']
        price = items[d[item_idx]]['price']
        if max_weight > 0:
            if item_idx != 0 and table[item_idx-1][limit_weight] != table[item_idx][limit_weight] or (item_idx == 0 and table[item_idx][limit_weight] > 0):
                for i in range(weight):
                    prev_bag.append(d[item_idx])
                max_weight -= weight
                basic_point += price
                limit_weight -= weight
            else:
                negative_point += price
            
        else:
            negative_point += price
        item_idx -= 1

    return_bag = [[[] for i in range(WIDTH)] for j in range(LENGTH)]
    for i in range(len(prev_bag)):
        return_bag[i // WIDTH][i % WIDTH].append(prev_bag[i])
    for row in return_bag:
        print(row)
    
    print(f'Очки выживания: {basic_point - negative_point}')
  

if __name__ == '__main__':
    res = gen_memo_table(item, WIDTH*LENGTH)
    # for i in res[1]:
    #     print(i)
    return_list(res[0], res[1], res[2], res[3], res[4], res[5], res[6])
