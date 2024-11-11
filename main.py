from neuphonic_texttospeech import neuphonic_tts
from ollama_llm import OA_chat
from whisper_speech_recognition import speech_recognition


PROMPT4 = f"You are tasked with having a natural conversation with a user that's going to be tested on his behavioral performance. Here's a hypothetical scenario: \n {scenario} \n You are the manager with the following personality: {antagonistic_personality} the conversation will start now. If you agree, say OK."
messages = [{"role": "system", "content": PROMPT4},
        {"role": "assistant", "content": "OK"}]



PROMPT = """
Here's some answers for the MBTI test:

Extrovert (E) vs. Introvert (I):
b) One-on-one conversations
b) Having some alone time to relax and unwind
b) Working through it independently
b) Quieter activities at home
b) Find it somewhat awkward or draining
a) Rely on own instincts and feelings
b) Approach them with caution
b) Individual workspaces
b) Prefer to avoid being the center of attention
b) Quiet time for yourself
b) Wait for others to approach you
Sensing (S) vs. Intuition (N):
b) Explore possibilities and potential meanings
b) Enjoy exploring theories and concepts
b) Future possibilities and patterns
b) Leave room for spontaneous experiences and changes
b) Consider potential outcomes and future possibilities
b) Overall vision and goals
b) Contribute ideas and theories
b) Adapt well to changes and enjoy the flexibility
b) Overall impressions and meanings
b) Deeper meanings and symbolism
b) Rich with possibilities and potential connections
b) Innovative and creative solutions
b) Imaginative, out-of-the-box concepts
b) Approaching with creativity and openness
Thinking (T) vs. Feeling (F):
a) Logical analysis and objective criteria
a) Focus on the facts and seek constructive solutions
a) Head and reason
a) Based on logical importance and efficiency
a) Logical and rational choice
a) Objective analysis
a) Emphasize facts, evidence, and logical reasoning
a) Prioritize efficiency and effectiveness
a) Objective performance metrics and results
a) Focus on finding logical solutions and compromises
a) Logical steps and timeline
a) Analyze the situation logically and strategize a plan
a) Objective data and analysis
a) Constructive criticism and improvement suggestions
Judging (J) vs. Perceiving (P):
b) Prefer flexibility and spontaneity, dislike strict schedules
b) Like to explore possibilities and figure it out as you go
b) Tend to work better under pressure and close to the deadline
b) Comfortable with a more flexible and adaptable environment
b) Pack on the fly, throwing in what feels right
b) Adapt well to unexpected changes and enjoy the flexibility
b) Go with the flow and see where it takes you
b) Enjoy being flexible and adapting as the situation evolves
b) Keep it open-ended and see where the day takes you
b) Dislike routine and enjoy spontaneity
b) Prefer to keep options open and gather more information

Fit this person into a personality type. Build a psychological profile for this user. Here's a few examples:

Example personality_type: <|INFJ|>
Example personality_summary: <|This person is an independent and visionary thinker who thrives on exploring possibilities and making logical, well-informed decisions. They value flexibility and creativity in their environment and prefer deep, meaningful interactions over superficial connections. While their introspective nature allows for thoughtful reflection, their adaptability ensures they can navigate unexpected changes with ease.|>

You answer will look like this:

<|personality_type|>
<|personality_summary|>
"""

if __name__ == "__main__":
    '''
    neuphonic_tts(
        "Hello! Welcome to our dental surgery in Kings Cross. How can I assist you today?"
    )
    '''
    conversation_history = " "
    # Initialize conversation history and messages list

    while True:
        # Get the user's transcribed speech input
        transcribed_text = speech_recognition()
        print("Final transcription:", transcribed_text)
        
        # Add the user's input to the messages list
        messages.append({"role": "user", "content": transcribed_text})
        
        # Get the assistant's response
        llm_output = OA_chat(transcribed_text, messages)
        
        # Add the assistant's response to the messages list
        messages.append({"role": "assistant", "content": llm_output})
        
        # Update conversation history
        print(f"Conversation: {messages}")
        
        # Convert the assistant's output to speech using TTS
        neuphonic_tts(llm_output)

