from typing import Literal

from pydantic import BaseModel


class GapAnalysisItem(BaseModel):
    requirement: str
    status: Literal['met', 'partially_met', 'missing']
    evidence: str


class GapAnalysisResult(BaseModel):
    items: list[GapAnalysisItem]
