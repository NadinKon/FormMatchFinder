import re


def determine_field_type(value):
    type_x = 'text'
    if value is not None:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", value) or re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
            type_x = "date"
        if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
            type_x = "phone"
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            type_x = "email"

    return type_x


# проверяет каждый шаблон в базе данных на соответствие
# полям и типам данных в form_data_dict
async def find_matching_template(form_data_dict: dict, forms_collection):
    templates = await forms_collection.find().to_list(length=100)
    print(templates)

    for template in templates:
        template_fields = template.get("fields", [])
        is_matching_template = all(
            field["field_name"] in form_data_dict and
            determine_field_type(form_data_dict[field["field_name"]]) == field["field_type"]
            for field in template_fields
        )

        if is_matching_template:
            return template["name"]

    return None
