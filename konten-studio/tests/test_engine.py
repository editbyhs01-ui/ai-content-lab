from konten_studio.engine import ContentBrief, WORKFLOW_STAGES, workflow_overview


def test_workflow_has_all_expected_stages():
    assert len(WORKFLOW_STAGES) == 8
    assert "research_and_fact_check" in WORKFLOW_STAGES
    assert "editorial_review" in WORKFLOW_STAGES


def test_overview_is_readable():
    assert "brief" in workflow_overview()
    assert "performance_evaluation" in workflow_overview()


def test_brief_validation():
    assert ContentBrief(topic="Refleksi sabar").validate() == []
    assert "Topic is required." in ContentBrief(topic=" ").validate()
    assert ContentBrief(topic="Topik", duration_seconds=200).validate()
