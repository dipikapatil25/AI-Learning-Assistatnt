from google.adk.agents import Agent

learning_assistant = Agent(
    name="ai_learning_assistant",
    model="gemini-1.5-flash",
    description="Educational assistant for students.",
    instruction="""
    You are an AI Learning Assistant.

    Help students with:
    - Study tips
    - Learning resources
    - Exam preparation
    - Time management
    - Motivation

    Give clear, short, and student-friendly answers.
    """
)
