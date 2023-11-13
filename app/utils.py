import re
from datetime import datetime


def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def validate_phone(phone: str) -> bool:
    return re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", phone) is not None


def validate_date(date_str: str) -> bool:
    formats = ("%d.%m.%Y", "%Y-%m-%d")
    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            pass
    return False


def validate_field(field_name: str, field_value: str) -> bool:
    if "email" in field_name:
        return validate_email(field_value)
    elif "phone" in field_name:
        return validate_phone(field_value)
    elif "date" in field_name:
        return validate_date(field_value)
    else:  # для текстовых полей
        return True


# проверяет каждый шаблон в базе данных на соответствие
# полям и типам данных в form_data_dict
async def find_matching_template(form_data_dict: dict, forms_collection):
    templates = await forms_collection.find().to_list(length=100)
    for template in templates:
        if all(field in form_data_dict for field in template["fields"]):
            if all(validate_field(field["field_name"], form_data_dict[field["field_name"]]) for field in template["fields"]):
                return template["name"]
    return None
