from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone", "+79123456789"),
    Smartphone("Samsung", "Galaxy", "+79987654321"),
    Smartphone("Xiaomi", "Redmi", "+79012345678"),
    Smartphone("Google", "Pixel 7 Pro", "+79555555555"),
    Smartphone("POCO", "F7  Ultra", "+79666666666")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
