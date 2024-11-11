import asyncio
import websockets
import httpx
import os
from pyneuphonic import Neuphonic, AudioPlayer, TTSConfig
import aioconsole
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import openai
from dotenv import load_dotenv
from os import getenv


API_KEY = "b18280dc613d96becc576c2f0e615554f1f1a6519d7d783465e71113ae3fa794.f0427f49-90b1-4e21-ae9b-fc6ae007f859"

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

holly_voice_id = "8e9c4bc8-3979-48ab-8626-df53befc2090"
# model = 'neu_fast'

async def generate_questions():
    prompt = "Generate a comprehensive list of insightful and challenging questions for a personality test designed for users taking an online assessment. The questions should focus on evaluating the user's behavior and critical thinking skills in various professional scenarios."

async def analyse_personality(answers):
    # Analyse the personality of the user
    prompt = f"Analyse the provided answers to a personality test and build a psychological profile of the user:\n\n{answers}\n\nProfile:"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(inputs.shape, dtype=torch.long)
    outputs = model.generate(
        inputs, 
        max_length=1024,
        num_return_sequences=1,
        attention_mask=attention_mask,
        pad_token_id=tokenizer.eos_token_id
    )
    profile = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return profile

async def chat_with_antagonist(user_input, antagonist_profile):
    # Use OpenAI API to simulate conversation with the antagonist
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"A coworker with profile {antagonist_profile} has a conversation with user: {user_input} while in a professional setting providing the user with scenarios by providing opposite opinions to the user.",
        max_tokens=150
    )
    return response.choices[0].text.strip()

async def main():
    # response = httpx.get(
    #     f'https://eu-west-1.api.neuphonic.com/voices',
    #     headers={'x-api-key': API_KEY},
    # )

    # for object in response.json()['data']['voices']:
    #     print(object)

    # with httpx.stream(
    #     method='POST',
    #     url='https://eu-west-1.api.neuphonic.com/sse/speak/en',
    #     headers={'x-api-key': API_KEY},
    #     json={'text': 'Hello, World!', 'model': {'model': model, 'voice': miles_id}},
    # ) as response:
    #     for message in response.iter_lines():
    #         print(message)

    client = Neuphonic(api_key=API_KEY)
    voices = client.voices.get()  # get's all available voices
    # print(voices)    

    sse = client.tts.AsyncSSEClient()
    tts_config = TTSConfig(speed=1.05)

    # with AudioPlayer() as player:
    #     response = sse.send('Hello, world!', tts_config=tts_config)

    #     async for item in response:
    #         player.play(item.data.audio)

    #     await asyncio.sleep(1)

    with AudioPlayer() as player:
        while True:
            user_text = await aioconsole.ainput(
                "Enter text to speak (or 'quit' to exit): "
            )

            if user_text.lower() == 'quit':
                break

            response = sse.send(user_text, tts_config=tts_config)

            async for item in response:
                player.play(item.data.audio)

            await asyncio.sleep(1)

    # answers = [
    #     "I handle stress by staying calm and focused.",
    #     "I prefer working in a team.",
    #     "I take criticism constructively."
    # ]
    # profile = await analyse_personality(answers)
    # print(profile)


if __name__ == '__main__':
    asyncio.run(main())