"""Workflow outline for a human-reviewed short-form content pipeline.

This module describes workflow stages only; it does not claim to execute
external agents, web research, media generation, publishing, or analytics.
"""

from dataclasses import dataclass

WORKFLOW_STAGES = (
    "brief",
    "research_and_fact_check",
    "audience_analysis",
    "scriptwriting",
    "editorial_review",
    "platform_optimization",
    "production_package",
    "performance_evaluation",
)

SPECIALISTS = (
    "Research & Fact Checker",
    "Audience Intelligence Specialist",
    "Lead Content Writer",
    "Senior Editorial Director",
    "SEO & Content Optimization Specialist",
)


@dataclass(frozen=True)
class ContentBrief:
    topic: str
    audience: str = ""
    goal: str = ""
    pillar: str = ""
    duration_seconds: int = 45

    def validate(self) -> list[str]:
        issues: list[str] = []
        if not self.topic.strip():
            issues.append("Topic is required.")
        if not 10 <= self.duration_seconds <= 180:
            issues.append("Duration must be between 10 and 180 seconds.")
        return issues


def workflow_overview() -> str:
    return " → ".join(WORKFLOW_STAGES)
