import gradio as gr
from groq import Groq

# Connect to Groq AI
client = Groq(api_key="YOUR_API_KEY_HERE")

def generate_plan(goal, year, hours, level):
    prompt = f"""
    You are PlanIT, an AI mentor and daily planner for BTech students.
    You don't just give tasks — you guide, teach and roadmap like a senior mentor.
    
    Student profile:
    - Goal: {goal}
    - BTech Year: {year}
    - Available hours today: {hours}
    - Current level: {level}
    
    Generate a focused daily plan with exactly 4 tasks.
    For EACH task provide:
    - The task with time
    - WHY it matters for their goal
    - HOW to do it (specific steps, resources, platforms)
    - What to do TOMORROW to continue
    
    Format exactly like this:
    
    🎯 PLANIT — YOUR DAILY ROADMAP
    ================================
    TASK 1: [task name] ([X] mins)
    📌 Why: [why this matters]
    📖 How: [exact steps]
    ➡️ Tomorrow: [next step]
    
    TASK 2: [task name] ([X] mins)
    📌 Why: [why this matters]
    📖 How: [exact steps]
    ➡️ Tomorrow: [next step]
    
    TASK 3: [task name] ([X] mins)
    📌 Why: [why this matters]
    📖 How: [exact steps]
    ➡️ Tomorrow: [next step]
    
    TASK 4: [task name] ([X] mins)
    📌 Why: [why this matters]
    📖 How: [exact steps]
    ➡️ Tomorrow: [next step]
    
    ================================
    💡 MENTOR TIP: [personalized advice]
    🔥 MOTIVATION: [one powerful line]
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    
    return response.choices[0].message.content

# Build the Gradio interface
demo = gr.Interface(
    fn=generate_plan,
    inputs=[
        gr.Textbox(label="🎯 What is your goal?", placeholder="e.g. Get an AI internship, Crack placements, Learn web dev..."),
        gr.Dropdown(label="📅 What year are you in?", choices=["1st Year", "2nd Year", "3rd Year", "4th Year"]),
        gr.Slider(label="⏰ Hours available today", minimum=1, maximum=10, value=4, step=1),
        gr.Dropdown(label="📊 Your current level", choices=["Beginner", "Intermediate", "Advanced"])
    ],
    outputs=gr.Textbox(label="📋 Your Daily Roadmap", lines=30),
    title="🚀 PlanIT — AI Daily Planner for BTech Students",
    description="Tell PlanIT your goal and get a personalized daily roadmap with tasks, resources and guidance!"
)

demo.launch()
