data = {
        "model": "services.service",
        "pk": 2236,
        "fields": {
            "category": 17,
            "name": "Спецификация отделочных материалов",
            "unit": 3,
            "min_price": 1,
            "max_price": 1000
        }
    }
for k, v in data.items():
    if isinstance(v, dict):
        for k1, v1 in v.items():
            if k1 == 'name':
                print(v1)



