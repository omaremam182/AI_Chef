from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="groq"
)

agent = create_agent(
    model=model,
    system_prompt="""
You are a professional cooking assistant.

Your tasks:
- Suggest meals using ONLY the provided ingredients
- Give 3 meal suggestions or more if user asked for more
- Mention cooking time
- Make the response clean and organized 
- Give short easy instructions and sort them by steps in bullet points
- write all instruction bullets in the same table with the meal name and cooking time
- Answer in the same language as the input
- Respond in a friendly and warm tone 
- Use emojis naturally in your responses (🍳🥗🔥😊🔪)
- Be practical and realistic
"""
)

def generate_meals(user_ingredients: str):

    question = HumanMessage(
        content=f"""
        {user_ingredients}
        """
    )

    full_response = ""

    for chunk in agent.stream(
        {"messages": [question]},
        stream_mode="messages"
    ):

        msg = chunk[0]

        if msg.content:
            full_response += msg.content

    return full_response