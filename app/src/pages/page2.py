import streamlit as st
from ..utils import Page
from matplotlib import pyplot as plt
import seaborn as sns
from ..state import _SessionState

class Page2(Page):
    def __init__(self, state):
        self.state = state

    def plot(self, data, optionx, optiony, hue):
        fig, ax = plt.subplots(1,1)
        sns.scatterplot(data=data, x=optionx, y=optiony,ax=ax,hue=hue, s=50)
        plt.legend()
        return fig

    def write(self):
        st.title("By stats")
        data = self.state.data
        tar = data.copy()
        colors = sns.color_palette(n_colors=len(data['Tm'].unique()))

        team = data['Tm'].unique()
        pos = data['Pos'].unique()

        optionx = st.sidebar.selectbox(
        'choose for x',
        ('G','GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
        'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK','TOV', 'PF', 'PTS', 'salary'),
        1)
        optiony = st.sidebar.selectbox(
        'choose for y',
        ('G','GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
        'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK','TOV', 'PF', 'PTS', 'salary'),
        24)

        optionhue = st.sidebar.selectbox(
        'Which hues do you want to use?',
        ('All','Team','Position'))

        x = optionx
        y = optiony
        hue = None

        if optionhue == 'All':
            tar = data.copy()
            hue = None
        if optionhue == 'Team':
            team1 = st.sidebar.selectbox(
            'choose team1',
            (team)
            )
            team2 = st.sidebar.selectbox(
            'choose team2',
            (team)
            )
            tar = data[(data['Tm']==team1) | (data['Tm']==team2)]
            hue='Tm'
        if optionhue == 'Position':
            pos1 = st.sidebar.selectbox(
            'choose Pos1',
            (pos)
            )
            pos2 = st.sidebar.selectbox(
            'choose Pos2',
            (pos)
            )
            tar = data[(data['Pos']==pos1) | (data['Pos']==pos2)]
            hue='Pos'
        # fig, ax = plt.subplots(1,1,figsize=(15,10))
        # sns.scatterplot(data=tar, x=optionx, y=optiony,ax=ax,hue=hue, s=100)
        # plt.legend()
        fig = self.plot(tar, optionx, optiony, hue)
        st.pyplot(fig)