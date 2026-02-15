from fastapi import Header, HTTPException

def verify_jwt(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    # Token verification would happen here
    return {"sub": "user-id", "tenant": "demo"}
