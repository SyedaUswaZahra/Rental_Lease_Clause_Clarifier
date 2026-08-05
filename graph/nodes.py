from typing import Any, Dict, List

from schemas.state import GraphState
from utils.loader import load_lease_text
from chains.splitter import split_lease_text
from chains.vectorstore import build_vectorstore, retrieve_top_k
from chains.grader import grade_chunks
from chains.generator import generate_answer
from chains.verifier import verify_answer


def loader_node(state: GraphState, source: str, is_pdf: bool) -> Dict[str, Any]:
    """Loads raw lease text into state."""
    raw_text = load_lease_text(source, is_pdf=is_pdf)
    return {"raw_text": raw_text}


def splitter_node(state: GraphState, raw_text: str) -> Dict[str, Any]:
    """Splits raw text into clause chunks."""
    chunks = split_lease_text(raw_text)
    return {"chunks": chunks}


def vectorstore_node(state: GraphState, chunks: List[str]) -> Dict[str, Any]:
    """Builds the FAISS vectorstore from chunks."""
    vectorstore = build_vectorstore(chunks)
    return {"vectorstore": vectorstore}


def retrieve_node(state: GraphState, vectorstore: Any, question: str) -> Dict[str, Any]:
    """Retrieves top-k chunks into state.retrieved_chunks."""
    retrieved_chunks = retrieve_top_k(vectorstore, question, k=5)
    return {"retrieved_chunks": retrieved_chunks}


def grade_node(state: GraphState, llm: Any, question: str, chunks: List[str]) -> Dict[str, Any]:
    """Grades chunks and updates state.graded_chunks."""
    graded_chunks = grade_chunks(llm, question, chunks)
    return {"graded_chunks": graded_chunks}


def generate_node(
    state: GraphState,
    llm: Any,
    question: str,
    chunks: List[str],
    callbacks: List[Any],
) -> Dict[str, Any]:
    """Generates answer and citations into state."""
    answer = generate_answer(llm, question, chunks, callbacks)
    citations = chunks
    return {"answer": answer, "citations": citations}


def verify_node(
    state: GraphState,
    llm: Any,
    answer: str,
    clauses: List[str],
) -> Dict[str, Any]:
    """Verifies answer and sets state.verification_warning."""
    verification_warning = verify_answer(llm, answer, clauses)
    return {"verification_warning": verification_warning}


def clarify_node(state: GraphState) -> Dict[str, Any]:
    """Sets needs_clarification=True."""
    return {"needs_clarification": True}
