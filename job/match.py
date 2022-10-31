from applicant.resume_parser import summarize_resume, calculate_score


def analyze_job_description(data):
    return calculate_score(data)


def calculate_applicant_job_match(skills_required, applicant_skills):
    skills_required_set = set(skills_required)
    applicant_skills_set = set(applicant_skills)

    overlap = applicant_skills_set & skills_required_set
    universe = applicant_skills_set | skills_required_set

    match = (float(len(overlap)) / len(universe)) * 100
    return match


def calculate_match_score(required_technical_skills,
                          applicant_technical_skills):
    technical_skills_match = calculate_applicant_job_match(required_technical_skills, applicant_technical_skills)

    return technical_skills_match

