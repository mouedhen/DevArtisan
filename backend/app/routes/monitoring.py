from fastapi import APIRouter, HTTPException
from backend.app.models import MonitoringData
from backend.app.schemas import MonitoringDataSchema

router = APIRouter()

@router.post("/monitoring", response_model=MonitoringDataSchema)
def create_monitoring_data(monitoring_data: MonitoringDataSchema):
    monitoring_data_obj = MonitoringData(**monitoring_data.dict())
    monitoring_data_obj.save()
    return monitoring_data_obj

@router.get("/monitoring/{data_id}", response_model=MonitoringDataSchema)
def get_monitoring_data(data_id: int):
    monitoring_data = MonitoringData.get(data_id)
    if not monitoring_data:
        raise HTTPException(status_code=404, detail="Monitoring data not found")
    return monitoring_data