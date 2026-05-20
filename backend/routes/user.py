from fastapi import APIRouter, Depends
from backend.utils.api_response import api_response
from backend.services.deps import get_current_user


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return api_response(
        data={
            "id": current_user.id,
            "email": current_user.email,
            "is_admin": current_user.is_admin
        },
        message="User profile retrieved successfully"
    )

