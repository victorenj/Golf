## Author: Victor E Balasoto
## Last Update: 1/23/25
## Purpose: For PGT golfers use

# ----------------------------------------------------------
# > Open CLI
# > cd C:\Users\PC\Desktop\Golf
# > Scripts\activate
# > streamlit run scorecard_strokeplay.py
# ----------------------------------------------------------

import streamlit as st
import pandas as pd


def main():
    '''Create scorecard'''
    
    def total_scores():
        '''Compute total scores for each player'''
        st.header("Total Scores")
        total_scores = score_data.astype(int).sum(axis=0)  # Convert data to integers and sum by column (player)
        for player, total in total_scores.items():
            st.subheader(f"Score for {player}")
            st.write(f"{player}: {total} strokes")

    # Title of the app
    st.logo("assets/pgt_logo2_blk.jpg", size="large")
    st.title("PGT Scorecard")
    st.subheader("*Pinoy Golf Tour*")
    
    # Sidebar for player input
    st.sidebar.header("Player Information")
    num_players = st.sidebar.number_input("Number of Players", min_value=1, max_value=4, value=1)
    player_names = []
    
    for i in range(num_players):
        player_name = st.sidebar.text_input(f"Enter name for Player {i + 1}", value=f"Player {i + 1}")
        player_names.append(player_name)
    
    course_par = st.sidebar.selectbox(
            "Golf Course Par Score",
            ("Par 3 Course", "Par 4 Course"),
            index=0
        )

    # Main scorecard section
    holes = [f"Hole {i}" for i in range(1, 19)]  # List of holes (1 to 18)
    
    # Initialize a DataFrame to store scores
    score_data = pd.DataFrame(index=holes, columns=player_names)
    
    # Input scores for each hole and player
    # -----------------------------------------------------------------------------------
    columns = st.columns(4, gap="small", vertical_alignment="center")

    for player, column in zip(player_names, columns):
        with column:
            st.subheader(f'{player}')
            for hole in holes:
                if course_par == "Par 3 Course":
                    score_data.loc[hole, player] = st.number_input(f"{hole} Score ({player})", min_value=1, max_value=6, value=3, key=f"{player}_{hole}")
                if course_par == "Par 4 Course":
                    score_data.loc[hole, player] = st.number_input(f"{hole} Score ({player})", min_value=1, max_value=10, value=4, key=f"{player}_{hole}")
    # -----------------------------------------------------------------------------------
    
    scol1, scol2 = st.columns(2, gap='large')
    with scol1:
        # Display the scorecard table
        st.subheader("Scorecard Table")
        st.dataframe(score_data)
    with scol2:
        total_scores()


if __name__ == '__main__':
    main()