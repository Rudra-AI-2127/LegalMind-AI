from llm import ask_llm


class RiskAgent:

    def analyze_risks(self, document_text):

        prompt = f"""
        You are an expert legal risk analyst.

        Analyze the following legal document and identify:

        1. Potential legal risks.
        2. Unfair or one-sided clauses.
        3. Missing protections.
        4. Overall Risk Level:
           - Low
           - Medium
           - High

        Document:

        {document_text}

        Format your answer like:

        Overall Risk Level: <Level>

        Risks:
        - Risk 1
        - Risk 2

        Recommendations:
        - Recommendation 1
        - Recommendation 2
        """

        response = ask_llm(prompt)

        return response