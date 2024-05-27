from fastapi import HTTPException, Request, status


def get_token(request: Request):
    token = request.cookies.get('currency_exchange_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

def get_current_user(token):
    ...