"""gradebook.stats — aggregate statistics over grade records."""

def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    scores_by_student = {}
    for r in records:
        scores_by_student.setdefault(r["name"], []).append(r["score"])
    return {name: round(sum(scores)/len(scores), 2) for name, scores in scores_by_student.items()}

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    return {r["subject"] for r in records}

def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    return max(averages.items(), key=lambda kv: kv[1])

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    return sorted([name for name, avg in averages.items() if avg >= threshold])
