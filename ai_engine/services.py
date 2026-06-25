import google.generativeai as genai

from django.conf import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)


def generate_roadmap(goal_data):

    model = genai.GenerativeModel(
        'models/gemini-2.5-flash'
    )

    prompt = f"""
    Create a professional learning roadmap.

    Goal Title:
    {goal_data['title']}

    Description:
    {goal_data['description']}

    Goal Type:
    {goal_data['goal_type']}

    Category:
    {goal_data['goal_category']}

    Daily Hours:
    {goal_data['daily_hours']}

    Return only 6 roadmap phases.
    One phase per line.
    No numbering explanation.
    """

    response = model.generate_content(
        prompt
    )

    return response.text

def generate_tasks(goal_title, roadmap_phase):

    model = genai.GenerativeModel(
        'models/gemini-2.5-flash'
    )

    prompt = f"""
    Create actionable learning tasks.

    Goal:
    {goal_title}

    Roadmap Phase:
    {roadmap_phase}

    Return only 6 tasks.

    One task per line.

    No numbering.
    No explanations.
    """

    response = model.generate_content(
        prompt
    )

    return response.text