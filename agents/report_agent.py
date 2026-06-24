class ReportAgent:

    def generate_report(
            self,
            summary,
            clauses,
            risks,
            compliance):

        report = f"""
# Legal Analysis Report

## 1. Executive Summary

{summary}

---

## 2. Key Clauses

{clauses}

---

## 3. Risk Assessment

{risks}

---

## 4. Compliance Status

{compliance}

---

## 5. Recommendations

- Review all identified risks carefully.
- Add missing clauses wherever necessary.
- Clarify ambiguous terms.
- Ensure compliance with applicable laws.
- Consult a legal professional before signing.

---

## 6. Disclaimer

This report is AI-generated for educational and informational purposes only and should not be considered legal advice.

Consult a qualified legal professional before making legal decisions.
"""

        return report