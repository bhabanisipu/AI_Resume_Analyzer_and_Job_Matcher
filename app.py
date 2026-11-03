
import streamlit as st

from src.resume_parser import extract_resume_text
from src.job_matcher import match_resume_to_job
from src.ai_analyzer import analyze_resume


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)


# Application Title
st.title("AI Resume Analyzer and Job Matcher")

st.write(
    "Upload your resume and enter a job description to analyze "
    "your skills, identify gaps, and get AI-powered suggestions."
)


# Resume Upload
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)


# Job Description
job_description = st.text_area(
    "Enter the Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)


if st.button("Analyze Resume", type="primary"):

    if uploaded_file is None:
        st.error("Please upload your resume PDF.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:
        try:

            with st.spinner("Analyzing your resume..."):

                # Step 1: Extract resume text
                uploaded_file.seek(0)

                resume_text = extract_resume_text(uploaded_file)


                # Step 2: Match resume with job description
                match_results = match_resume_to_job(
                    resume_text,
                    job_description
                )


                # Step 3: Analyze resume using Groq AI
                ai_results = analyze_resume(
                    resume_text=resume_text,
                    job_description=job_description,
                    matched_skills=match_results["matched_skills"],
                    missing_skills=match_results["missing_skills"]
                )


            st.success("Resume analysis completed!")


            # Step 4: Display matching scores
            st.subheader("Resume Matching Results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Text Similarity",
                    f'{match_results["similarity_score"]}%'
                )

            with col2:
                st.metric(
                    "Skill Match",
                    f'{match_results["skill_match_score"]}%'
                )

            st.caption(
                "These scores measure text similarity and listed skill "
                "overlap. They are not probabilities of getting hired."
            )


            # Step 5: Display required skills
            st.subheader("Skills Analysis")

            st.write("**Required Skills:**")

            if match_results["required_skills"]:
                st.write(", ".join(match_results["required_skills"]))
            else:
                st.info(
                    "No supported skills were detected in the job description."
                )


            st.write("**Matched Skills:**")

            if match_results["matched_skills"]:
                for skill in match_results["matched_skills"]:
                    st.success(skill)
            else:
                st.write("No matching skills detected.")


            st.write("**Skills to Develop:**")

            if match_results["missing_skills"]:
                for skill in match_results["missing_skills"]:
                    st.warning(skill)
            else:
                st.write(
                    "No missing skills detected from the supported skill list."
                )


            # Step 6: Display AI-generated analysis
            st.subheader("AI Resume Analysis")

            st.markdown(ai_results)


            # Step 7: Display extracted resume text
            with st.expander("View Extracted Resume Text"):
                st.text(resume_text)


        except Exception as error:

            st.error(f"An error occurred: {error}")

            st.info(
                "Check that your PDF contains selectable text, "
                "your Groq API key is valid, and the hosted model "
                "is available."
            )
