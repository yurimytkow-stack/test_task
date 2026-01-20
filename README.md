# Address Service

сервіс для валідації та парсингу адрес

## що тут є

два ендпоінти:
- `POST /addres/addresses/validate` - валідація адрес
- `PUT /addres/addresses/recognize` - парсинг адреси з тексту

## як запустити

1. переходимо в папку проекту:
```bash
cd src
```

2. піднімаємо базу:
```bash
docker-compose up -d
```

3. накатуємо міграції:
```bash
alembic upgrade head
```

4. запускаємо сервер:
```bash
uvicorn main:app --reload
```

все, працює на http://127.0.0.1:8000/docs

## як це працює

### валідація адреси

**запит:**
```json
POST /addres/addresses/validate
[
  {
    "name": "John Doe",
    "phone": "+1234567890",
    "email": "user@example.com",
    "company_name": "My Company",
    "address_line1": "123 Main St",
    "address_line2": "Apt 4B",
    "city_locality": "Kyiv",
    "state_province": "Kyivska",
    "postal_code": "01001",
    "country_code": "UA"
  }
]
```

**відповідь:**
```json
[
  {
    "status": "verified",
    "original_address": { ... },
    "matched_address": { ... },
    "messages": []
  }
]
```

### парсинг адреси

**запит:**
```json
PUT /v1/addresses/recognize
{
  "text": "John Doe at 123 Main St Apt 4B in Kyiv",
  "address": {
    "country_code": "UA"
  }
}
```

**відповідь:**
```json
{
  "score": 0.91,
  "address": {
    "name": "John Doe",
    "address_line1": "123 Main St",
    "address_line2": "Apt 4B",
    "city_locality": "Kyiv",
    ...
  },
  "entities": [
    {
      "type": "person",
      "score": 0.95,
      "text": "John Doe",
      "start_index": 0,
      "end_index": 8
    },
    ...
  ]
}
```

## важливо

зараз queries використовують мок дані, бо ShipEngine API потребує ключ

коли буде API ключ - просто змінити `AddressValidationQueries` та `AddressRecognitionQueries` на реальні виклики, решта коду залишається без змін

## архітектура і патернам

все по SOLID:
- **Service** - тільки оркестрація
- **Queries** - робота з API
- **Factory** - створення об'єктів
- **Repository** - збереження в БД
- **Serializer** - серіалізація response
- **Utils** - допоміжні функції

ніяких хардкодів, все через інтерфейси, легко підміняється та тестується

## dependencies

```
fastapi
sqlalchemy
asyncpg
pydantic
```

---
