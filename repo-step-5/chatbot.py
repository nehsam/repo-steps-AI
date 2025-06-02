import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Custom logic for chatbot
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
