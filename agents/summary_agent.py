from llm import ask_llm


class SummaryAgent:

    def summarize(self, document_text):

        prompt = f"""
        You are an expert legal assistant.

        Read the following legal document and provide:

        1. A concise summary.
        2. Important parties involved.
        3. Main obligations.
        4. Important dates if present.

        Document:

        {document_text}

        Return the answer in clear sections.
        """

        response = ask_llm(prompt)

        return response