## Author: Victor E Balasoto
## Last Update: 1/23/25
## Purpose: For PGT golfers use

# ----------------------------------------------------------
# > Open CLI
# > cd C:\Users\PC\Desktop\Golf
# > Scripts\activate
# > streamlit run scorecard_stableford.py
# ----------------------------------------------------------

import streamlit as st
import pandas as pd

# Title of the app
st.title("Golf Scorecard App with Stableford Scoring")

# Sidebar for player input
st.sidebar.header("Player Information")
num_players = st.sidebar.number_input("Number of Players", min_value=1, max_value=4, value=1)
player_names = []

for i in range(num_players):
    player_name = st.sidebar.text_input(f"Enter name for Player {i + 1}", value=f"Player {i + 1}")
    player_names.append(player_name)

# Sidebar for course information
st.sidebar.header("Course Information")
par_values = []
for i in range(1, 19):
    par_values.append(st.sidebar.number_input(f"Par for Hole {i}", min_value=3, max_value=5, value=4))

# Main scorecard section
st.header("Scorecard")
holes = [f"Hole {i}" for i in range(1, 19)]  # List of holes (1 to 18)

# Initialize a DataFrame to store scores and points
score_data = pd.DataFrame(index=holes, columns=player_names)
stableford_points = pd.DataFrame(index=holes, columns=player_names)

# Stableford scoring rules
def calculate_stableford_points(score, par):
    if score <= par - 4:  # Four strokes under par
        return 6
    elif score == par - 3:  # Three strokes under par (albatross)
        return 5
    elif score == par - 2:  # Two strokes under par (eagle)
        return 4
    elif score == par - 1:  # One stroke under par (birdie)
        return 3
    elif score == par:      # Par
        return 2
    elif score == par + 1:  # One stroke over par (bogey)
        return 1
    else:                   # Two or more strokes over par (double bogey or worse)
        return 0

# Input scores for each hole and player
for player in player_names:
    st.subheader(f"Scores for {player}")
    for i, hole in enumerate(holes):
        score = st.number_input(f"{hole} Score ({player})", min_value=0, max_value=10, value=0, key=f"{player}_{hole}")
        score_data.loc[hole, player] = score
        
        # Calculate Stableford points for the hole
        stableford_points.loc[hole, player] = calculate_stableford_points(score, par_values[i])

# Display the scorecard table
st.subheader("Scorecard Table")
st.dataframe(score_data)

# Display Stableford points table
st.subheader("Stableford Points Table")
stableford_points = stableford_points.astype(int)  # Ensure points are integers
st.dataframe(stableford_points)

# Calculate and display total Stableford points for each player
st.header("Total Stableford Points")
total_stableford_points = stableford_points.sum(axis=0)  # Sum points by column (player)
for player, total in total_stableford_points.items():
    st.write(f"{player}: {total} points")
