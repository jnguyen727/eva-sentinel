# models/track.py
from pydantic import BaseModel, Field
from datetime import datetime

class Track(BaseModel):
    """
    Canonical representation of one radar/ADS-B sample.
    All validations run automatically on every API call.
    """
    lat:   float = Field(..., ge=-90,  le=90,  description="Latitude in degrees")
    lon:   float = Field(..., ge=-180, le=180, description="Longitude in degrees")
    alt_m: float = Field(..., gt=0,                 description="Altitude above MSL (m)")
    speed_ms: float = Field(..., ge=0,              description="Ground speed (m/s)")
    timestamp: datetime
