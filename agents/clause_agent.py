from llm import ask_llm


class ClauseAgent:

    def extract_clauses(self, document_text):

        prompt = f"""
        You are a legal clause extraction expert.

        Extract the following clauses if present:

        - Payment Terms
        - Confidentiality Clause
        - Termination Clause
        - Liability Clause
        - Non-Compete Clause
        - Governing Law Clause

        Document:

        {document_text}

        Return only the extracted clauses.
        """

        response = ask_llm(prompt)

        return response