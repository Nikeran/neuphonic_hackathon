from openai import OpenAI

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

def language_model_chat(text, PROMPT=None):
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(model="gpt-4o",
                                                 messages=[{"role": "system", "content": PROMPT}])
    output = completion.choices[0].message.content
    return output

def OA_chat(text, PROMPT=None):
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(model="gpt-4o",
                                                 messages=messages)
    output = completion.choices[0].message.content
    messages.append(output)
    return output

'''
def language_model_chat(user_input, PROMPT=None):
    model = "llama3.1:latest"
    stream = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_input},
        ],
        stream=True,
    )

    output = ""
    for chunk in stream:
        output += chunk["message"]["content"]
    return output
'''

if __name__ == "__main__":
    text = ""
    user_personality = language_model_chat(text, PROMPT)
    PROMPT2 = f"Here's a psychological profile: \n {user_personality} \n I want you to build an antagonistic personality to the one given, that will be used to simulate a workplace disagreement. The output will look like this: <|personality_type|> \n <|personality_summary|>"
    antagonistic_personality = language_model_chat(text, PROMPT2)
    PROMPT3 = f"Here's a psychological profile of a user: \n {user_personality} and a personality antagonistic to it: \n {antagonistic_personality} \n Build a workplace scenario in which the first personality is tested against the second one to see how the first person would handle the interaction. This scenario will be used in a simulated behavioural online assessment. This is for an ambitious AI startup Neuphonic that focuses on low latency text to speech. The first personality is a new employee and the second one is their manger. Adress the new employee as you, this prompt will be read by the person taking the OA. Don't explicitly mention the personality types in your answer. Output only a short description of the circumstances consisting of a few sentences."
    scenario = language_model_chat(text, PROMPT3)
    PROMPT4 = f"You are tasked with having a natural conversation with a user that's going to be tested on his behavioral performance. Here's a hypothetical scenario: \n {scenario} \n You are the manager with the following personality: {antagonistic_personality} the conversation will start now. If you agree, say OK."
    messages = [{"role": "system", "content": PROMPT4},
            {"role": "assistant", "content": "OK"}]
    out = OA_chat(text, PROMPT4)
    print(user_personality)
    print(antagonistic_personality)
    print(scenario)
    print(out)
    
   while True:
    user_input = input("User Input: ")
    # Append the user's input to the conversation history
    messages.append({"role": "user", "content": user_input})
    
    # Get the assistant's response
    llm_output = OA_chat(user_input, PROMPT4)
    
    # Append the assistant's response to the conversation history
    messages.append({"role": "assistant", "content": llm_output})
    
    # Print the assistant's response
    print(llm_output)

