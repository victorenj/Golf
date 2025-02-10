## Author: Victor E Balasoto
## Last Update: 2/10/25
## Purpose: For PGT golfers use

# ----------------------------------------------------------
# > Open CLI
# > cd C:\Users\PC\Desktop\Golf
# > Scripts\activate
# > streamlit run scorecard_strokeplay.py
# ----------------------------------------------------------

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PGT Scorecard",
    page_icon=":golfer:",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    '''Create scorecard'''

    def total_scores():
        '''Compute total scores for each player'''
        st.subheader("Total Scores")
        total_scores = score_data.astype(int).sum(axis=0)  # Convert data to integers and sum by column (player)
        for player, total in total_scores.items():
            st.write(f"**{player}: {total} strokes**")

    ## Read specific columns by index
    df_names = pd.read_excel('GolfCoursePar.xlsx', usecols=["Knights Play", "Brevofield", "Quaker Creek", "Raleigh Golf", "Zebulon CC"])
    kp = pd.read_excel('GolfCoursePar.xlsx', usecols=[0, 1])
    bf = pd.read_excel('GolfCoursePar.xlsx', usecols=[0, 2])
    qc = pd.read_excel('GolfCoursePar.xlsx', usecols=[0, 3])
    rg = pd.read_excel('GolfCoursePar.xlsx', usecols=[0, 4])
    zc = pd.read_excel('GolfCoursePar.xlsx', usecols=[0, 5])

    # --- Sidebar for player input ---
    st.logo("assets/pgt_logo2_blk.jpg", size="large")
    st.sidebar.header("Player Information")
    num_players = st.sidebar.number_input("Number of Players", min_value=1, max_value=4, value=1)
    player_names = []
    
    for i in range(num_players):
        player_name = st.sidebar.text_input(f"Enter name for Player {i + 1}", value=f"Player {i + 1}")
        player_names.append(player_name)
    # --- Sidebar for player input ---
    # --- Sidebar for course input ---
    course_name = ["Knights Play", "Brevofield", "Quaker Creek", "Raleigh GA", "Zebulon CC", "Custom"]
    golf_course = st.sidebar.selectbox("Golf Course", course_name)

    if golf_course == "Custom":
        custom_input = st.sidebar.text_input("Write the name of Golf Course :")
        if custom_input:
            st.subheader(f'**_{custom_input} Golf Course_**')
    else:
        st.subheader(f'**_{golf_course} Golf Course_**')

    holes = [f"Hole {i}" for i in range(1, 19)]  # List of holes (1 to 18)
    score_data = pd.DataFrame(index=holes, columns=player_names)
    columns = st.columns(18, gap="small", vertical_alignment="top")
    for hole, column in zip(holes, columns):
        with column:
            #st.subheader(f'{player}')
            for player in player_names:
                if golf_course == "Knights Play":
                    score_data.loc[hole, player] = st.number_input(f"{hole} ({player})", min_value=1, max_value=6, value=3, key=f"{player}_{hole}")
                else:
                    score_data.loc[hole, player] = st.number_input(f"{hole} ({player})", min_value=1, max_value=10, value=4, key=f"{player}_{hole}")
    if golf_course == "Knights Play":
        st.sidebar.write(kp)
    elif golf_course == "Brevofield":
        st.sidebar.write(bf)
    elif golf_course == "Quaker Creek":
        st.sidebar.write(qc)
    elif golf_course == "Raleigh GA":
        st.sidebar.write(rg)
    elif golf_course == "Zebulon CC":
        st.sidebar.write(zc)
    # --- Sidebar for course input ---
    # --- Hole & total scores ---
    scol1, scol2 = st.columns(2, gap='small')
    with scol1:
        st.subheader("Scorecard")
        st.dataframe(score_data)
    with scol2:
        total_scores()
    # --- Hole & total scores ---

if __name__ == '__main__':
    main()