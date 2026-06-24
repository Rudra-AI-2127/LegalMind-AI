from concurrent.futures import ThreadPoolExecutor

from agents.summary_agent import SummaryAgent
from agents.clause_agent import ClauseAgent
from agents.risk_agent import RiskAgent
from agents.compliance_agent import ComplianceAgent
from agents.report_agent import ReportAgent


class LegalOrchestrator:

    def __init__(self):

        # Initialize Agents

        self.summary_agent = SummaryAgent()

        self.clause_agent = ClauseAgent()

        self.risk_agent = RiskAgent()

        self.compliance_agent = ComplianceAgent()

        self.report_agent = ReportAgent()

    # ---------------------------------------------------
    # Main Analysis Pipeline
    # ---------------------------------------------------

    def analyze_document(self, document_text):

        print("\n[Launching Parallel Agents...]")

        # Run agents in parallel

        with ThreadPoolExecutor(max_workers=4) as executor:

            summary_future = executor.submit(
                self.summary_agent.summarize,
                document_text
            )

            clause_future = executor.submit(
                self.clause_agent.extract_clauses,
                document_text
            )

            risk_future = executor.submit(
                self.risk_agent.analyze_risks,
                document_text
            )

            compliance_future = executor.submit(
                self.compliance_agent.check_compliance,
                document_text
            )

            # Collect Results

            summary = summary_future.result()
            print("[✓] Summary Agent Completed")

            clauses = clause_future.result()
            print("[✓] Clause Agent Completed")

            risks = risk_future.result()
            print("[✓] Risk Agent Completed")

            compliance = compliance_future.result()
            print("[✓] Compliance Agent Completed")

        # Generate Final Report

        print("\n[Generating Final Report...]")

        final_report = self.report_agent.generate_report(
            summary,
            clauses,
            risks,
            compliance
        )

        print("[✓] Report Agent Completed")

        # Return all outputs for UI

        return {
            "summary": summary,
            "clauses": clauses,
            "risks": risks,
            "compliance": compliance,
            "report": final_report
        }