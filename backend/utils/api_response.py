def api_response(data=None, message="", meta=None):
    return {
        "success": True,
        "data": data,
        "message": message,
        "meta": meta or {}
    }