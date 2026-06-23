def repair_schema(schema):

    if "roles" not in schema:
        schema["roles"] = ["User"]

    if "pages" not in schema:
        schema["pages"] = ["Home"]

    return schema