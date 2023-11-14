from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_DETAILS = "mongodb://mongodb:27017"
MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)


# Подключение к базе данных и получение доступа к коллекции форм
database = client["My_database"]
forms_collection = database["forms_collection"]

# Шаблоны формы для начальной вставки в базу данных
form_template = [
    {
        "name": "ContactForm",
        "fields": [
            {"field_name": "user_email", "field_type": "email"},
            {"field_name": "user_phone", "field_type": "phone"}
        ]
    },
    {
        "name": "RegistrationForm",
        "fields": [
            {"field_name": "username", "field_type": "text"},
            {"field_name": "email", "field_type": "email"},
            {"field_name": "birth_date", "field_type": "date"}
        ]
    },
    {
        "name": "OrderForm",
        "fields": [
            {"field_name": "product_name", "field_type": "text"},
            {"field_name": "order_date", "field_type": "date"}
        ]
    }
]


async def init_db():
    # Вставка шаблона формы в коллекцию
    await forms_collection.insert_many(form_template)
    print("Database initialized with one template.")
    client.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())
