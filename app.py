import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Personality trait questions
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

# Streamlit app title
st.title("Personality Profile Comparison")

# Collect user responses through sliders and calculate trait scores
scores = {}
st.write("Please rate each question on a scale from 0 (Not at all) to 10 (Extremely):")

for trait, q_list in questions.items():
    total_score = 0
    for question in q_list:
        score = st.slider(question, 0, 10, 5, key=question)  # Unique key for each question
        total_score += score
    scores[trait] = total_score / len(q_list)  # Average score per trait

# Button to display personality profile
if st.button("Show Personality Profile"):
    # Prepare character data with user's responses
    character_data = [
        {"name": "James (Inspired by Robert Downey Jr.)", "traits": [7, 9, 8, 6, 3]},
        {"name": "Raj (Inspired by Shah Rukh Khan)", "traits": [8, 7, 8, 7, 4]},
        {"name": "Maya (Inspired by Priyanka Chopra)", "traits": [9, 6, 7, 8, 5]},
        {"name": "John (Inspired by Keanu Reeves)", "traits": [6, 7, 6, 9, 2]},
        {"name": "Anjali (Inspired by Kajol)", "traits": [8, 6, 7, 8, 5]},
    ]

    # Convert user's scores to a list for comparison
    user_traits = list(scores.values())

    # Find the closest character match based on Euclidean distance
    closest_character = min(character_data, key=lambda character: np.linalg.norm(np.array(character["traits"]) - np.array(user_traits)))

    # Traits for the 3D bar chart
    traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]
    values = closest_character["traits"]

    # Calculate introversion percentage based on extraversion score
    extraversion_score = scores["Extraversion"]
    introversion_percentage = (10 - extraversion_score) * 10  # Invert and convert to percentage
    st.write(f"Your personality resembles: **{closest_character['name']}**")
    st.write(f"Introversion Level: **{introversion_percentage:.1f}%**")

    # Plot 3D bar chart for the matched character
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(len(traits))
    y = np.zeros(len(traits))
    z = np.zeros(len(traits))
    dx = np.ones(len(traits))
    dy = np.ones(len(traits))
    dz = values
    colors = plt.cm.viridis(np.linspace(0, 1, len(traits)))

    # Plotting the bars
    ax.bar3d(x, y, z, dx, dy, dz, color=colors, alpha=0.8)

    # Set labels and titles with adjustments to avoid overlap
    ax.set_xticks(x)
    ax.set_xticklabels(traits, rotation=15, ha="right")  # Rotate labels slightly to avoid overlap
    ax.set_zlim(0, 10)
    ax.set_xlabel(" ", labelpad=25)
    ax.set_ylabel(" ")
    ax.set_zlabel("Score (0-10)", labelpad=15)
    ax.set_title(f"Personality Profile of {closest_character['name']}")

    # Display the 3D plot in Streamlit
    st.pyplot(fig)
