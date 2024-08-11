def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        'title': str(todo["title"]),
        'description': str(todo["description"]),
        'created_at': str(todo["created_at"]),
        'done': str(todo["done"]),

    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
