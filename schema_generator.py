def generate_schema(intent, design):

    return {
        "app_name": intent["app_name"],
        "pages": design["pages"],
        "roles": design["roles"],
        "database_tables": design["entities"]
    }