import logging
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.schemas import pic_requests_schema as prs
from src.models import models
from datetime import datetime


class PicRequestsRepo:
    def __init__(self, db: Session):
        self.db = db
        self.logger = logging.getLogger(__name__)

    def register_recyclable_material(self, material: prs.RecyclableMaterial) -> models.RecyclableMaterial:
        db_material = models.RecyclableMaterial(
            type=material.type,
            description=material.description
        )
        self.db.add(db_material)
        self.db.commit()
        self.db.refresh(db_material)
        
        self.logger.info(f"Registered recyclable material with ID {db_material.id}")
        return db_material
    
    def get_all_recyclable_materials(self):
        return self.db.query(models.RecyclableMaterial).all()

    def create_pickup_request(self, pickup_request: prs.PickupRequest) -> models.PickupRequest:
        db_pickup_request = models.PickupRequest(
            producer_id=pickup_request.producer_id,
            address_id=pickup_request.address_id,
            scheduled_time=pickup_request.scheduled_time
        )
        self.db.add(db_pickup_request)
        self.db.commit()
        self.db.refresh(db_pickup_request)

        for item in pickup_request.items:
            db_item = models.PickupRequestItem(
                request_id=db_pickup_request.id,
                material_id=item.id,
                quantity=item.quantity,
                weight_kg=item.weight_kg
            )
            self.db.add(db_item)

        self.db.commit()
        self.logger.info(f"Created pickup request with ID {db_pickup_request.id}")
        return db_pickup_request

    def get_pickup_requests_by_producer(self, producer_id: int):
        return self.db.query(models.PickupRequest).filter(models.PickupRequest.producer_id == producer_id).all()
    
    def get_all_pickup_requests(self):
        return self.db.query(models.PickupRequest).all()
    
    