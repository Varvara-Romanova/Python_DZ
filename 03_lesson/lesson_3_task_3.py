from address import Address
from mailing import Mailing

address_to = Address("123456", "Оренбург", "Ленинская", "12", "18")
address_from = Address("654321", "Москва", "Малая Бронная", "11", "4")

mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=550,
    track="TR123456789RU"
)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
