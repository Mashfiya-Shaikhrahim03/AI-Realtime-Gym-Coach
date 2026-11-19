# from services.config.workout_config import PROMPT


# class LLMCoach:
#     def __init__(self, groq_client):
#         self.client = groq_client
#         self.history = []
#         self.system_prompt = PROMPT

#     def give_feedback(self, event, issue):
#         prompt = f"Event: {event}"

#         if issue:
#             prompt += f" Form Issue: {issue}"

#         messages = [
#             {"role": "system", "content": self.system_prompt},
#             *self.history[-10:],
#             {"role": "user", "content": prompt}
#         ]

#         response = self.client.chat.completions.create(
#             model="openai/gpt-oss-120b",
#             messages=messages,
#             temperature=0.4,
#         )

#         text = response.choices[0].message.content.strip()
#         self.history.append({"role": "assistant", "content": text})

#         return text
    


import logging

from groq import APIConnectionError, APITimeoutError, APIStatusError
from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def get_fallback_feedback(self, event, issue):

        if issue:
            return (
                f"Keep going with your {event}. "
                f"Focus on correcting your form: {issue}. "
                "Move in a controlled manner and prioritize proper technique."
            )

        return (
            f"Good effort with your {event}! "
            "Keep your movements controlled and maintain proper form."
        )

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.4,
                timeout=15.0
            )

            text = response.choices[0].message.content

            if not text or not text.strip():
                raise ValueError("Groq returned empty feedback")

            text = text.strip()

            self.history.append({
                "role": "assistant",
                "content": text
            })

            return text

        except (APIConnectionError, APITimeoutError, APIStatusError):
            logging.exception("Groq API unavailable. Using fallback feedback.")

        except ValueError:
            logging.exception("Invalid or empty Groq response.")

        fallback = self.get_fallback_feedback(event, issue)

        self.history.append({
            "role": "assistant",
            "content": fallback
        })

        return fallback
