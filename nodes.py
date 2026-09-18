from google import genai

from .prompts import GIFT_RECOMMENDATION_PROMPT


def recommend_gifts(state, client: genai.Client):
    prompt = GIFT_RECOMMENDATION_PROMPT.format(
        recipient=state["recipient"],
        age=state["age"],
        occasion=state["occasion"],
        interests=state["interests"],
        budget=state["budget"],
        relationship=state["relationship"],
        preferences=state["preferences"],
        delivery=state["delivery"],
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {"recommendations": response.text}
