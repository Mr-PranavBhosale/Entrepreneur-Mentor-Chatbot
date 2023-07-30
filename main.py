import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    
    if state is None:
        state = {}

    # Extract the latest user message
    if message_history:
        user_message = message_history[-1].content.lower()
    else:
        user_message = ""


    # Check if the user input contains keywords to trigger specific actions
    if "hi" in user_message or "hello" in user_message or "hey" in user_message:
        bot_response = " Hello! I'm your friendly chatbot here to help you with anything related to startups and business. Feel free to ask any questions or share your ideas, and I'll do my best to assist you."
    elif "business" in user_message:
        bot_response = "Hello there! Looking to start a business? I can help you with that. Just let me know what you're curious about, and I'll guide you through the process step-by-step."
    elif "startup" in user_message:
        bot_response = "Hey, startups are my jam! I can offer you advice on everything from idea validation to funding strategies. What aspect of startups are you interested in exploring?"
    elif "entrepreneurship" in user_message:
        bot_response = "Entrepreneurship is a thrilling journey! If you have any questions about being an entrepreneur, I'm all ears. Just ask away!"
    elif any(keyword in user_message for keyword in ["launch", "start", "kickstart"]):
        bot_response = "Ready to launch your dream venture? I'm here to provide guidance at every step of the way. Share your vision with me, and let's make it happen!"
    elif any(keyword in user_message for keyword in ["legal", "registration", "incorporation"]):
        bot_response = "Legal processes can be tricky, but don't worry! I can assist you with company registration, legal documentation, and compliance. How can I support you?"
    elif any(keyword in user_message for keyword in ["next step", "how to", "success", "achieve"]):
        bot_response = "Let's talk about your next move to achieve success! Whether it's scaling your business or overcoming challenges, I'm here to provide insights and encouragement."
    elif any(keyword in user_message for keyword in ["funding", "investors", "capital", "fundraising"]):
        bot_response = "Funding your startup can be challenging but rewarding. Whether you need angel investors, venture capital, or crowdfunding tips, I've got your back."
    elif any(keyword in user_message for keyword in ["marketing", "branding", "promotion", "advertising"]):
        bot_response = "A strong marketing strategy is essential for business success. Let's discuss marketing techniques, branding ideas, and effective ways to promote your venture."
    elif any(keyword in user_message for keyword in ["innovation", "ideas", "creativity", "out-of-the-box"]):
        bot_response = "Innovation is the heart of entrepreneurship. Share your ideas, and I'll help you nurture creativity and think outside the box."
    elif any(keyword in user_message for keyword in ["team", "cofounder", "hiring", "human resources"]):
        bot_response = "Building a strong team is vital for a thriving startup. Whether you need advice on hiring, cofounders, or managing HR, I'm here to support you."
    elif any(keyword in user_message for keyword in ["scaling", "growth", "expansion", "global", "market penetration"]):
        bot_response = "Scaling your business can be a game-changer. Let's explore growth strategies, expanding into new markets, and penetrating the global landscape."
    elif any(keyword in user_message for keyword in ["failure", "challenge", "obstacle", "learn from mistakes"]):
        bot_response = "It's okay to face challenges and learn from failures. We can discuss overcoming obstacles and learning valuable lessons from mistakes."
    elif any(keyword in user_message for keyword in ["mentorship", "guidance", "support", "advice"]):
        bot_response = "Mentorship is essential for personal and professional growth. Consider me your virtual mentor, providing guidance and support every step of the way."
    elif any(keyword in user_message for keyword in ["technology", "innovative solutions", "automation"]):
        bot_response = "Leveraging technology can give your startup a competitive edge. Let's explore innovative solutions and automation tools to streamline your business."
    elif "roadmap" in user_message:
        bot_response = "Creating a roadmap is a critical step in achieving your startup goals. To assist you better, could you tell me which area of business or startup you're focusing on? For example, product development, marketing, funding, or any other specific domain."
    elif any(keyword in user_message for keyword in ["product development", "product roadmap", "innovation strategy"]):
        bot_response = "Great! Let's map out the product development process and plan an innovation strategy to stay ahead in the market."
    elif any(keyword in user_message for keyword in ["marketing strategy", "branding roadmap", "promotion plan"]):
        bot_response = "Awesome! Let's create a comprehensive marketing strategy to build a strong brand and promote your products or services effectively."
    elif any(keyword in user_message for keyword in ["funding roadmap", "investor pitch", "fundraising plan"]):
        bot_response = "Fantastic! We'll work on a funding roadmap and prepare you for successful investor pitches to secure funding for your startup."
    elif any(keyword in user_message for keyword in ["legal compliance", "regulatory roadmap", "intellectual property strategy"]):
        bot_response = "Excellent! We'll focus on ensuring legal compliance and developing an intellectual property strategy to protect your innovations."
    
    else:
        
    # # Generate GPT-3.5 Turbo response
     bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state
