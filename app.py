import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Function to collect user responses to personality questions
def ask_questions():
    questions = {
        "Openness": [
            "How curious are you about trying new things or exploring new ideas?",
            "Do you enjoy activities that stimulate your imagination and creativity?",
            "How willing are you to adapt to different lifestyles or cultural experiences?"
        ],
        "Conscientiousness": [
            "How organized and reliable do you consider yourself in daily life?",
            "Do you often plan things in advance rather than going with the flow?",
            "How important is it to you to meet deadlines or stay on top of your responsibilities?"
        ],
        "Extraversion": [
            "How energized do you feel after spending time with a group of people?",
            "Do you enjoy being the center of attention in social settings?",
            "How often do you seek excitement or engage in lively activities?"
        ],
        "Agreeableness": [
            "How often do you find yourself sympathizing with others’ emotions or needs?",
            "How likely are you to prioritize harmony over winning in a conflict?",
            "How willing are you to help others, even if it requires extra effort?"
        ],
        "Neuroticism": [
            "How often do you feel anxious or worried about potential problems?",
            "How easily do you get stressed or overwhelmed by challenges?",
            "How likely are you to react strongly to situations that don’t go your way?"
        ]
    }

    scores = {trait: 0 for trait in questions.keys()}
    
    print("Please rate each question on a scale from 0 (Not at all) to 10 (Extremely):\n")
    for trait, q_list in questions.items():
        for question in q_list:
            while True:
                try:
                    score = float(input(f"{question} (0-10): "))
                    if 0 <= score <= 10:
                        scores[trait] += score / len(q_list)  # Average score per trait
                        break
                    else:
                        print("Please enter a number between 0 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    
    return scores

# Get user personality scores
personality_scores = ask_questions()

# Character profiles for comparison
character_data = [
    {"name": "James (Inspired by Robert Downey Jr.)", "traits": [7, 9, 8, 6, 3]},
    {"name": "Raj (Inspired by Shah Rukh Khan)", "traits": [8, 7, 8, 7, 4]},
    {"name": "Maya (Inspired by Priyanka Chopra)", "traits": [9, 6, 7, 8, 5]},
    {"name": "John (Inspired by Keanu Reeves)", "traits": [6, 7, 6, 9, 2]},
    {"name": "Anjali (Inspired by Kajol)", "traits": [8, 6, 7, 8, 5]},
    {"name": "User (You!)", "traits": list(personality_scores.values())},
]

# Trait labels
traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

# Set up the figure and 3D subplot for the animation
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# Function to update the chart for each character
def update(frame):
    ax.clear()
    character = character_data[frame]
    values = character["traits"]
    
    # Set up 3D bars for each trait
    x = np.arange(len(traits))
    y = np.zeros(len(traits))
    z = np.zeros(len(traits))
    dx = np.ones(len(traits))
    dy = np.ones(len(traits))
    dz = values
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(traits)))
    
    # Plotting the bars
    ax.bar3d(x, y, z, dx, dy, dz, color=colors, alpha=0.8)
    
    # Set labels and titles
    ax.set_xticks(x)
    ax.set_xticklabels(traits)
    ax.set_zlim(0, 10)
    ax.set_xlabel("Traits")
    ax.set_ylabel(" ")
    ax.set_zlabel("Score (0-10)")
    ax.set_title(f"Personality Profile of {character['name']}")

# Animate the chart, cycling through each character
ani = FuncAnimation(fig, update, frames=len(character_data), repeat=True, interval=2000)

# Show the animated chart
plt.show()
