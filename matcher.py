from parser import get_llm
from langchain_groq import ChatGroq
from models import Resume, JDMatchResult
from prompts import jd_match_prompt

def match_resume_to_jd(resume_text:Resume, job_description:str,  llm:ChatGroq)->JDMatchResult:
    llm = llm or get_llm()
    structured_output =llm.with_structured_output(JDMatchResult, method="function_calling")
    chain= jd_match_prompt | structured_output
    result: JDMatchResult= chain.invoke({
        "jd_text":job_description,
        "resume_json": resume_text.model_dump_json(indent=2)
    })
    return result

