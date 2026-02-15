from fastapi import APIRouter, Depends
from app.models.request import RAGRequest
from app.models.response import RAGResponse
from app.services.rag_service import RAGService
from app.core.auth import verify_jwt
from app.core.tenants import resolve_tenant

router = APIRouter()

@router.post("/rag", response_model=RAGResponse)
def rag_endpoint(
    request: RAGRequest,
    token=Depends(verify_jwt),
    tenant_id=Depends(resolve_tenant)
):
    service = RAGService(tenant_id=tenant_id)
    answer = service.run(query=request.query)
    return RAGResponse(answer=answer)
