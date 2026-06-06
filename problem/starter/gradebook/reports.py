from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: list[dict]) -> str:
    """Build a human-readable, multi-line report using the functions in stats.py."""
    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    top = top_scorer(records)
    passing = passing_students(records)
    
    lines = [
        "=== Gradebook Report ===",
        f"Total records: {len(records)}",
        f"Subjects offered: {', '.join(subjects)}",
        "Averages:"
    ]
    for name in sorted(averages.keys()):
        lines.append(f"  {name} : {averages[name]}")
    lines.append(f"Top scorer: {top[0]} ({top[1]})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passing)}")
    
    return "\n".join(lines)
