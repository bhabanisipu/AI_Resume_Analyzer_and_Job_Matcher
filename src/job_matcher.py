from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Receive two inputs
# resume_text comes from resume_parser.py, while job_description is supplied by the user.

# 2. Calculate similarity
# TF-IDF converts the texts into numerical vectors. Cosine similarity measures their textual similarity.

# 3. Compare skills
# The code identifies which listed skills appear in the job description, which are mentioned in the resume, and which required skills are missing.

# 4. Return results
# A Python dictionary contains the similarity score, skill coverage, matched skills, and missing skills.

def match_resume_to_job(resume_text,job_description):
    try:
        if not isinstance(resume_text,str) or not resume_text.strip():
            raise ValueError("resume text cannot be empty. ")
        if not isinstance(job_description,str) or not job_description.strip():
            raise ValueError("job descrition cannot be empty. ")
        if not resume_text or not job_description:
            raise ValueError("Resume and job description are required. ")
        vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,2))
        tfidf_matrix = vectorizer.fit_transform([
            resume_text.lower(),
            job_description.lower()
        ])

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]
        similarity_score = round(similarity*100,2)
        skills = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "nlp",
            "generative ai",
            "langchain",
            "tensorflow",
            "pytorch",
            "pandas",
            "numpy",
            "fastapi",
            "flask",
            "docker",
            "git",
            "aws"
        ]

        required_skills = []

        for skill in skills:
            if skill in job_description.lower():
                required_skills.append(skill)

        # Find matched skills in resume
        matched_skills = []

        for skill in required_skills:
            if skill in resume_text.lower():
                matched_skills.append(skill)

        # Find missing skills
        missing_skills = []

        for skill in required_skills:
            if skill not in matched_skills:
                missing_skills.append(skill)

        # Calculate skill match percentage
        if len(required_skills) > 0:
            skill_match_score = round(
                len(matched_skills) / len(required_skills) * 100,
                2
            )
        else:
            skill_match_score = 0

        return {
            "similarity_score": similarity_score,
            "skill_match_score": skill_match_score,
            "required_skills": required_skills,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }
    except ValueError:
        raise
    except Exception as e:
        raise RuntimeError(
            f"resume matching Failed: {e}"
        )from e
    