from llm import ask_llm


class ComplianceAgent:

    def check_compliance(self, document_text):

        prompt = f"""
You are a strict legal compliance checker.

Your job is ONLY to identify whether specific clauses
exist in the document.

RULES:
1. Read the document carefully.
2. If a clause or its synonym appears, mark it Present.
3. If not found, mark it Absent.
4. Do NOT explain.
5. Do NOT infer.
6. Return ONLY the required format.

Clause Definitions:

Confidentiality Clause:
Keywords:
confidentiality, confidential, non-disclosure, secrecy

Termination Clause:
Keywords:
termination, terminate, resignation, notice period

Payment Terms:
Keywords:
salary, compensation, remuneration, wages, payment, bonus

Liability Clause:
Keywords:
liability, liable, damages, indemnity

Governing Law Clause:
Keywords:
governing law, jurisdiction, laws of India, applicable law

Non-Compete Clause:
Keywords:
non-compete, competitor, competing company, restrictive covenant

Dispute Resolution Clause:
Keywords:
arbitration, mediation, dispute resolution, court proceedings

Data Privacy Clause:
Keywords:
data privacy, personal data, GDPR, privacy, data protection

Document:
-------------------------
{document_text}
-------------------------

Return exactly:

Confidentiality Clause: Present/Absent
Termination Clause: Present/Absent
Payment Terms: Present/Absent
Liability Clause: Present/Absent
Governing Law Clause: Present/Absent
Non-Compete Clause: Present/Absent
Dispute Resolution Clause: Present/Absent
Data Privacy Clause: Present/Absent
"""

        return ask_llm(prompt)