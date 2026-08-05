from pydantic import BaseModel


class JobRequirement(BaseModel):
    skill: str
    qualification: str
    responsibility: str


class JobRequirementsList(BaseModel):
    requirements: list[JobRequirement]
