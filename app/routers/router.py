from fastapi import APIRouter, Request
from database.database import forms_collection
from utils import find_matching_template, determine_field_type

router = APIRouter()


@router.post("/get_form")
async def get_form(request: Request):
    form_data = await request.json()  # Получение данных
    matching_template_name = await find_matching_template(form_data, forms_collection)

    if matching_template_name:
        return {"template_name": matching_template_name}
    else:
        # Если подходящий шаблон не найден, возвращаем имена полей с их типами
        field_types = {key: determine_field_type(value) for key, value in form_data.items()}
        return field_types


@router.post("/insert_form_template/")
async def insert_form_template(form_template: dict):
    # Вставка нового шаблона формы в базу данных
    # form_template должен быть словарем, содержащим структуру шаблона
    result = await forms_collection.insert_one(form_template)
    # Возвращение идентификатора вставленного шаблона
    return {"inserted_id": str(result.inserted_id)}
