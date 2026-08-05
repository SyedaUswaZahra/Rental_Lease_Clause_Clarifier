from typing import TypedDict, List


class GraphState(TypedDict):
    question: str
    retrieved_chunks: List[str]
    graded_chunks: List[str]
    citations: List[str]
    answer: str
    verification_warning: str
    needs_clarification: bool
