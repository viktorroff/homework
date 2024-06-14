from random import randint, choice
name = ['Walter', 'Jessy', 'Tomas', 'Balbo']
surname = ['Waltering', 'Jessin', 'Tomassy', 'Balby']
def gen_customer() -> dict:
      customer = {
          'neme': choice(name),
          'surename': choice(surname),
          'account': f"{randint(50_000, 200_000)}$"
         }
      return customer
def gen_houses(count: int) -> list[dict]:
    house_list = []
    for _ in range(count):
        house = {
        'price':f"{randint(50_000, 200_000)}$",
        'square':f"{randint(15, 80)}m2"
    }
        house_list.append(house)
    return house_list
def square_to_int(square: str) -> int:
    return int(square[:-1])
def price_to_int(price: str) -> int:
    return int(price[:-1])
def get_recommend(customer, house_list) -> dict:
    customer_account = customer['account']
    res = list(filter(lambda x: x['price'] <= customer_account, house_list))
    res.sort(key=lambda x: x['square'], reverse=True)
    return f"{customer}\n{res}"
print(get_recommend(customer=gen_customer(), house_list=gen_houses(20)))