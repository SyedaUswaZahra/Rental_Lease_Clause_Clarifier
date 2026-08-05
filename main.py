import argparse

from graph.workflow import build_workflow
from utils.disclaimer import append_disclaimer
from langchain_core.language_models import BaseChatModel


def main(source: str, is_pdf: bool = True, question: str = None) -> str:
    """Loads doc, runs workflow, streams answer, appends disclaimer.

    Args:
        source: If is_pdf is True, a file path to the PDF; otherwise pasted lease text.
        is_pdf: Whether the source is a PDF file path.
        question: The user's question about the lease.

    Returns:
        The final answer string with the legal disclaimer appended.
    """
    # Build the workflow graph (llm and vectorstore are built inside the graph nodes)
    workflow = build_workflow(llm=None, vectorstore=None)

    # Invoke the workflow with the source, question, and streaming callbacks
    # The graph nodes handle loading, splitting, vectorstore building, retrieval,
    # grading, generation, and verification internally.
    result = workflow.invoke(
        {
            "question": question,
            "source": source,
            "is_pdf": is_pdf,
        }
    )

    # Capture the final answer
    answer = result.get("answer", "")

    # Append the disclaimer
    final_answer = append_disclaimer(answer)

    # Print and return the final answer
    print(final_answer)
    return final_answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lease agreement Q&A assistant. Provide a PDF path or pasted text and a question."
    )
    parser.add_argument(
        "--pdf",
        type=str,
        default=None,
        help="Path to the lease agreement PDF file.",
    )
    parser.add_argument(
        "--text",
        type=str,
        default=None,
        help="Pasted lease agreement text (use when --pdf is not provided).",
    )
    parser.add_argument(
        "--question",
        type=str,
        required=True,
        help="The question to ask about the lease agreement.",
    )

    args = parser.parse_args()

    if args.pdf and args.text:
        parser.error("Provide either --pdf OR --text, not both.")
    elif args.pdf:
        main(source=args.pdf, is_pdf=True, question=args.question)
    elif args.text:
        main(source=args.text, is_pdf=False, question=args.question)
    else:
        parser.error("Provide either --pdf or --text with the lease content.")
