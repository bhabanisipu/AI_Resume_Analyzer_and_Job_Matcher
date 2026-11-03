# AI Resume Analyzer and Job Matcher

## Project Overview

AI Resume Analyzer and Job Matcher is an AI-powered application that analyzes PDF resumes and compares them with job descriptions. It identifies matched and missing skills, calculates resume similarity scores, and generates personalized improvement suggestions and interview questions using LangChain and Groq LLMs.

## Business Problem

Manual resume screening is time-consuming for recruiters, while job seekers often struggle to identify skill gaps and understand how well their resumes match specific job requirements.

This project automates preliminary resume analysis and helps candidates improve their resumes according to job requirements.

## Features

- **Resume Upload:** Upload PDF resumes for analysis.
- **Resume Text Extraction:** Extract resume content using PyMuPDF.
- **Resume Matching:** Compare resumes with job descriptions using TF-IDF and Cosine Similarity.
- **Skill Gap Analysis:** Identify matched and missing skills.
- **AI Resume Analysis:** Generate resume strengths and improvement suggestions using Groq LLM.
- **Interview Preparation:** Generate job-related interview questions.
- **AI Monitoring:** Track model execution and responses using LangSmith.
- **Interactive Interface:** User-friendly application built with Streamlit.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | LLM Integration |
| Groq API | Hosted Language Model |
| GPT-OSS 20B | AI Resume Analysis |
| LangSmith | LLM Monitoring and Tracing |
| PyMuPDF | PDF Text Extraction |
| Scikit-learn | TF-IDF and Cosine Similarity |
| python-dotenv | Environment Variable Management |

## Project Structure

```text
AI_Resume_Analyzer/
│
├── src/
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── ai_analyzer.py
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 2. Navigate to the Project Directory

```bash
cd AI_Resume_Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv ana
```

Activate the environment on Windows:

```bash
ana\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

### 6. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## How It Works

1. Upload a PDF resume.
2. Enter the target job description.
3. Extract resume text using PyMuPDF.
4. Calculate text similarity using TF-IDF and Cosine Similarity.
5. Identify matched and missing skills.
6. Send resume information to the Groq LLM through LangChain.
7. Generate AI-powered resume feedback and interview questions.
8. Monitor LLM execution through LangSmith.

## Sample Output

The application provides:

- Text Similarity Score
- Skill Match Score
- Required Skills
- Matched Skills
- Missing Skills
- Resume Strengths
- Skills to Improve
- Resume Improvement Suggestions
- Interview Preparation Questions

## Future Enhancements

- Support for DOCX resumes.
- OCR support for scanned PDF resumes.
- Advanced skill extraction using NLP.
- Multiple job description comparison.
- Resume improvement and rewriting functionality.
- Downloadable resume analysis reports.
- Recruiter dashboard for preliminary candidate screening.

## Limitations

- Currently supports PDF resumes containing selectable text.
- Skill matching uses a predefined list of supported skills.
- Similarity scores indicate textual similarity, not the probability of getting hired.
- AI-generated suggestions should be reviewed by candidates or recruiters.

## Author

**Bhabani Sankar Sahoo**

B.Tech – Computer Science and Engineering (AIML)

## License

This project is developed for educational and portfolio purposes.
