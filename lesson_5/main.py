#km_h={'speed_1': 100, 'speed_2': 92, 'speed_3': 132, 'speed_4': 46}
#for (k,v) in km_h.items():
#    m_h = {k: v * 1.609 for (k, v) in km_h.items()}
#    print(m_h)

#n = int(input('n = '))
#n_factorial = [x for x in range(1, n + 1)]
#res = 1
#for k in n_factorial:
 #   res *=k
#print(res)

a=[4, 6, 7, 5, 4, 5, 5, 6, 5, 5, 5, 5]
start, end = 0, 5
ma_five = set()
for i in range(len(a) - 4):
    prime = a[start:end]
    if 2 not in prime or 3 not in prime:
        ma_five.add(prime.count(5))
    start += 1
    end +=1
print(max(ma_five))
