from neuphonic_texttospeech import neuphonic_tts
from ollama_llm import OA_chat
from whisper_speech_recognition import speech_recognition


PROMPT4 = f"You are tasked with having a natural conversation with a user that's going to be tested on his behavioral performance. Here's a hypothetical scenario: \n {scenario} \n You are the manager with the following personality: {antagonistic_personality} the conversation will start now. If you agree, say OK."
messages = [{"role": "system", "content": PROMPT4},
        {"role": "assistant", "content": "OK"}]

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

