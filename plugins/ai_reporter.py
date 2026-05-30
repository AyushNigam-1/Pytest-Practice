# plugins/ai_reporter.py


def pytest_report_header(config):
    """
    This hook fires at the very beginning of the test session.
    It allows you to inject custom strings into the terminal header.
    """
    return [
        "==================================================",
        "🤖 AI SECURITY TEST SUITE INITIATED",
        "🎯 Target Model : Gemini-1.5-Pro",
        "🛡️ Mode         : Strict Validation",
        "==================================================",
    ]
