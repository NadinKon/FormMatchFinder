from fastapi import APIRouter, HTTPException, Request
from app.database.database import forms_collection
from app.utils import find_matching_template

router = APIRouter()


@router.post("/get_form")
async def get_form(request: Request):
    # Получение данных формы из POST-запроса
    form_data = await request.form()
    # Преобразование данных формы в словарь
    form_data_dict = {key: value for key, value in form_data.items()}
    # Функция find_matching_template проверяет каждый шаблон в базе данных на соответствие
    # полям и типам данных в form_data_dict
    matching_template_name = await find_matching_template(form_data_dict, forms_collection)
    # Возвращение имени подходящего шаблона, если он был найден
    if matching_template_name:
        return {"template_name": matching_template_name}
    # Если подходящий шаблон не найден, возвращается ошибка 404
    else:
        raise HTTPException(status_code=404, detail="Matching template not found")

@router.post("/insert_form_template/")
async def insert_form_template(form_template: dict):
    # Вставка нового шаблона формы в базу данных
    # form_template должен быть словарем, содержащим структуру шаблона
    result = await forms_collection.insert_one(form_template)
    # Возвращение идентификатора вставленного шаблона
    return {"inserted_id": str(result.inserted_id)}

