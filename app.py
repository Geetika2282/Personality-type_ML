import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Sample data for training the model
data = {
    'openness': [7, 4, 8, 3, 5, 6, 9, 5, 2, 8, 4, 7, 6, 5, 8],
    'conscientiousness': [6, 3, 7, 2, 5, 4, 8, 5, 3, 7, 4, 6, 7, 3, 6],
    'extraversion': [8, 3, 9, 2, 5, 4, 7, 4, 2, 8, 3, 7, 6, 3, 8],  # Fixed spelling
    'agreeableness': [7, 6, 8, 3, 5, 5, 9, 6, 3, 7, 5, 7, 8, 4, 6],
    'neuroticism': [4, 7, 3, 8, 5, 6, 2, 7, 8, 3, 6, 4, 3, 7, 5],
    'is_introvert': [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Fit the logistic regression model
X = df[['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']]
y = df['is_introvert']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

# Streamlit UI
st.title("Personality Type Predictor")

# User input
openness = st.slider("Rate your openness to experience (0.0 - 10.0):", 0.0, 10.0, 5.0)
conscientiousness = st.slider("Rate your conscientiousness (0.0 - 10.0):", 0.0, 10.0, 5.0)
extraversion = st.slider("Rate your extraversion (0.0 - 10.0):", 0.0, 10.0, 5.0)
agreeableness = st.slider("Rate your agreeableness (0.0 - 10.0):", 0.0, 10.0, 5.0)
neuroticism = st.slider("Rate your neuroticism (0.0 - 10.0):", 0.0, 10.0, 5.0)

if st.button("Predict Personality Type"):
    user_data = pd.DataFrame({
        'openness': [openness],
        'conscientiousness': [conscientiousness],
        'extraversion': [extraversion],
        'agreeableness': [agreeableness],
        'neuroticism': [neuroticism]
    })

    # Scale user data
    user_data_scaled = scaler.transform(user_data)
    probability = model.predict_proba(user_data_scaled)[:, 1][0] * 100  # Probability of being an Introvert

    # Display result
    st.success(f"Probability you are an Introvert: {probability:.2f}%")

    # Plotting
    features = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    user_values = user_data.values.flatten()

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(user_values, labels=features, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)  # Display the plot in Streamlit
