import os


class Exporter:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def export_resume(self, resume_text: str) -> str:
        path = os.path.join(self.output_dir, "tailored_resume.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(resume_text)
        return path

    def export_cover_letter(self, cover_letter: str) -> str:
        path = os.path.join(self.output_dir, "cover_letter.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(cover_letter)
        return path
