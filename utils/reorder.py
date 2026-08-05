from schemas.resume_schema import Resume, ResumeSection


class SectionReorderer:
    def __init__(self) -> None:
        pass

    def reorder(self, resume: Resume, requirements: list[str]) -> list[ResumeSection]:
        requirement_lower = [req.lower() for req in requirements]

        scored_sections = []
        for section in resume.sections:
            text_parts = [section.title] + section.bullets
            combined_text = " ".join(text_parts).lower()
            score = sum(1 for req in requirement_lower if req in combined_text)
            scored_sections.append((score, section))

        scored_sections.sort(key=lambda item: item[0], reverse=True)
        return [section for _, section in scored_sections]
