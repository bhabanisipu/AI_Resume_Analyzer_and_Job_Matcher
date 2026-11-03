import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("Groq_TOKEN")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGSMITH_PROJECT")

def analyze_resume(
    resume_text,
    job_description,
    matched_skills,
    missing_skills
):
    """Analyze a resume using a hosted Groq language model."""

    try:
        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing from the .env file."
            )

        # Initialize the Groq model
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            groq_api_key=GROQ_API_KEY,
            temperature=0.3,
            max_tokens=1000
        )

        # Create chat prompt
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are an experienced AI resume analyzer.

                Analyze resumes professionally.
                Give practical and accurate suggestions.
                Do not invent qualifications or experience.
                """
            ),
            (
                "human",
                """
                Analyze the candidate's resume for the given job.

                RESUME:
                {resume_text}

                JOB DESCRIPTION:
                {job_description}

                MATCHED SKILLS:
                {matched_skills}

                MISSING SKILLS:
                {missing_skills}

                Provide your analysis using these headings:

                1. Resume Strengths
                2. Skills to Improve
                3. Resume Improvement Suggestions
                4. Interview Preparation Questions
                """
            )
        ])

        # Create LangChain pipeline
        chain = prompt | llm

        # Execute the chain
        result = chain.invoke({
            "resume_text": resume_text[:8000],
            "job_description": job_description[:5000],
            "matched_skills": ", ".join(matched_skills),
            "missing_skills": ", ".join(missing_skills)
        })

        return result.content

    except ValueError:
        raise

    except Exception as error:
        raise RuntimeError(
            f"Resume analysis failed: {error}"
        ) from error
