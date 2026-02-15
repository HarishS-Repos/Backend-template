from fastapi import Depends

def resolve_tenant(token=Depends(lambda: {"tenant": "demo"})):
    return token["tenant"]
