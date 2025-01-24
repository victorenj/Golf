## Author: Victor E Balasoto
## Last Update: 1/23/25
## Purpose: For PGT golfers use

# ----------------------------------------------------------
# > Open CLI
# > cd C:\Users\PC\Desktop\Golf
# > Scripts\activate
# > streamlit run scorecard.py
# ----------------------------------------------------------

import streamlit as st
import pandas as pd
import tomllib
from pprint import pprint


def load_toml():
    """Load TOML data from file"""
    with open('.streamlit\config.toml', 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data


def main():
    # Title of the app
    st.logo("assets/pgt_logo2_blk.jpg", size="large")
    st.title("Golf Scorecard App")
    
    # Sidebar for player input
    st.sidebar.header("Player Information")
    num_players = st.sidebar.number_input("Number of Players", min_value=1, max_value=4, value=1)
    player_names = []
    
    for i in range(num_players):
        player_name = st.sidebar.text_input(f"Enter name for Player {i + 1}", value=f"Player {i + 1}")
        player_names.append(player_name)
    
    # Main scorecard section
    st.header("Scorecard")
    holes = [f"Hole {i}" for i in range(1, 19)]  # List of holes (1 to 18)
    
    # Initialize a DataFrame to store scores
    score_data = pd.DataFrame(index=holes, columns=player_names)
    
    # Input scores for each hole and player
    # -----------------------------------------------------------------------------------
    columns = st.columns(4, gap="small", vertical_alignment="center")

    for player, column in zip(player_names, columns):
        with column:
            for hole in holes:
                score_data.loc[hole, player] = st.number_input(f"{hole} Score ({player})", min_value=0, max_value=10, value=0, key=f"{player}_{hole}")
    # -----------------------------------------------------------------------------------
    
    # Display the scorecard table
    st.subheader("Scorecard Table")
    st.dataframe(score_data)
    
    # Calculate and display total scores
    st.header("Total Scores")
    total_scores = score_data.astype(int).sum(axis=0)  # Convert data to integers and sum by column (player)
    for player, total in total_scores.items():
        st.subheader(f"Score for {player}")
        st.write(f"{player}: {total} strokes")

if __name__ == '__main__':
    data: dict = load_toml()
    pprint(data, sort_dicts=False)
    main()