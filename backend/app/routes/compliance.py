from fastapi import APIRouter, HTTPException
from backend.app.models import ComplianceCheck
from backend.app.schemas import ComplianceCheckSchema

router = APIRouter()

@router.post("/compliance", response_model=ComplianceCheckSchema)
def create_compliance_check(compliance_check: ComplianceCheckSchema):
    compliance_check_obj = ComplianceCheck(**compliance_check.dict())
    compliance_check_obj.save()
    return compliance_check_obj

@router.get("/compliance/{compliance_id}", response_model=ComplianceCheckSchema)
def get_compliance_check(compliance_id: int):
    compliance_check = ComplianceCheck.get(compliance_id)
    if not compliance_check:
        raise HTTPException(status_code=404, detail="Compliance check not found")
    return compliance_check