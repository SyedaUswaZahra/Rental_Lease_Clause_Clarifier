from pydantic import BaseModel


class ResumeSection(BaseModel):
    title: str
    bullets: list[str]


class Resume(BaseModel):
    sections: list[ResumeSection]


class RewrittenBullet(BaseModel):
    original: str
    rewritten: str
    matched_requirement: str
