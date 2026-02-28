Structured Questionnaire Answering Tool
🚀 Overview

This project is a secure, AI-powered web application that automates structured questionnaire answering using internal reference documentation.

It simulates how companies respond to security reviews, compliance audits, vendor assessments, and operational questionnaires in a structured and grounded way.

The system:

Authenticates users

Stores questionnaires and reference documents

Retrieves relevant internal documentation

Generates grounded answers with citations

Provides confidence scores and coverage summary

Exports a structured document preserving original format

🏢 Industry & Fictional Company
Industry

Cybersecurity SaaS

Fictional Company

ShieldOps AI is a fictional cybersecurity SaaS company providing cloud-native threat detection, compliance automation, and security posture monitoring for enterprise clients operating in regulated environments.

The system uses internal documents such as:

Security policy

Compliance reports

Backup policies

Infrastructure documentation

Incident response procedures

These act as the "source of truth" for answering questionnaires.

🧠 What This System Does
1️⃣ User Authentication

JWT-based authentication

Secure signup and login

Protected endpoints

2️⃣ Questionnaire Upload

Upload text-based questionnaire

Automatically parses into individual questions

Stores questions in database

3️⃣ Reference Document Upload

Upload multiple internal documents

Stored per-user

Acts as ground truth for answer generation

4️⃣ AI-Powered Answer Generation

Retrieves relevant content using keyword-based mock RAG

Generates structured answers

Attaches citation (source filename)

Returns "Not found in references." if unsupported

5️⃣ Confidence Score

Each answer includes a confidence level:

High

Medium

Low

Based on retrieval match strength.

6️⃣ Coverage Summary

Each run provides a summary:

Total questions

Questions answered

Questions not found

7️⃣ Export Functionality (Phase 2)

Preserves original questionnaire structure

Keeps questions unchanged

Inserts answers below each question

Includes citations

Downloads structured .docx file

🏗 Architecture
Backend

FastAPI

Database

SQLite

SQLAlchemy ORM

Authentication

JWT (JSON Web Tokens)

Password hashing using Passlib

Retrieval Logic

Keyword-based matching (mock RAG)

Citation metadata stored with documents

Document Export

python-docx

🔄 User Workflow

User signs up / logs in

Uploads questionnaire

Uploads reference documents

Clicks Generate Answers

Reviews answers with citations & confidence

Exports structured document

This ensures a complete workflow from upload → review → export.

📊 API Response Structure
Generate Answers Response
{
  "summary": {
    "total_questions": 10,
    "answered": 9,
    "not_found": 1
  },
  "results": [
    {
      "question": "...",
      "answer": "...",
      "citation": "security_policy.txt",
      "confidence": "High"
    }
  ]
}
📌 Assumptions

Questionnaire is plain text (each line = one question)

Reference documents are plain text files

Retrieval is keyword-based (mock AI stage)

Each user operates on their own dataset

Only latest questionnaire is processed for generation

⚖ Trade-offs

Used keyword-based retrieval instead of embeddings for simplicity

SQLite used instead of production-grade PostgreSQL

No frontend UI (Swagger used for demonstration)

No chunk-level retrieval segmentation

Answers are snippet-based rather than summarized

These trade-offs were made to ensure end-to-end completeness within scope.

🔮 What I Would Improve With More Time

If extended further, I would:

Replace keyword retrieval with embedding-based semantic search

Use a vector database (e.g., Chroma or Pinecone)

Implement document chunking

Add partial regeneration per question

Add answer editing UI

Add version history tracking

Add async background processing

Deploy on cloud (Render / AWS)

Implement citation snippet highlighting

Add evaluation metrics for retrieval quality

🔐 Grounding & Reliability

The system ensures reliability by:

Retrieving answers strictly from reference documents

Attaching explicit citations

Returning "Not found in references." when unsupported

Providing confidence scores

Preventing hallucinated content

This ensures structured, explainable AI outputs.

📂 Project Structure
structured-qa-tool/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── auth.py
│   ├── rag.py
│   ├── utils.py
│   ├── app.db
│   └── venv/
│
├── mock_data/
│   ├── questionnaire.txt
│   ├── security_policy.txt
│   ├── compliance_report.txt
│   ├── backup_policy.txt
│   ├── incident_response.txt
│   └── infrastructure_overview.txt
│
└── README.md
▶ How To Run

Create virtual environment

Install dependencies

pip install fastapi uvicorn sqlalchemy passlib python-jose python-multipart python-docx

Run server

python -m uvicorn main:app --reload

Open Swagger UI

http://127.0.0.1:8000/docs
✅ Assignment Criteria Coverage

✔ User authentication
✔ Persistent storage
✔ Structured upload → generation → export flow
✔ AI-based retrieval logic
✔ Citation grounding
✔ "Not found in references" logic
✔ Review before export
✔ Document export preserving structure
✔ Two Nice-to-Have features implemented

🧾 Final Note

This project demonstrates practical system design thinking for building grounded AI workflows in real-world enterprise scenarios involving structured documentation and compliance processes.

It prioritizes:

Reliability

Explainability

Clear workflow

Structured outputs

Trade-off awareness