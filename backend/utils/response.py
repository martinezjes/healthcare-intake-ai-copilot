def success_response(data=None, message=None, meta=None):
    return {
        "status": "success",
        "message": message,
        "data": data,
        "meta": meta or {}
    }


def error_response(message="An error occurred", data=None):
    return {
        "status": "error",
        "message": message,
        "data": data
    }