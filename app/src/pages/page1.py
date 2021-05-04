import streamlit as st
from ..utils import Page
from matplotlib import pyplot as plt
import seaborn as sns
from ..state import _SessionState

class Page1(Page):
    def __init__(self, state):
        self.state = state

    def plot(self, data, options):
        fig, ax = plt.subplots(1,2,figsize=(10,5))
        ax[0].set_title('Salary distribution(All NBA)')
        sns.histplot(data['salary'].astype(int),ax=ax[0])
        colors = sns.color_palette(n_colors=len(data['Tm'].unique()))
        ax[1].set_title('Salary distribution(by teams)')
        bins = [i for i in range(0,10**7,5*10**6)]
        for counter, tm in enumerate(options):
            sns.histplot(data[data['Tm']==tm]['salary'].astype(int),ax=ax[1],bins=10,binrange=(0,5*10**7),
                        color=colors[counter],alpha=0.4, label=tm)
        plt.legend()
        return fig

    def write(self):
        st.title("Salary distribution")
        data = self.state.data
        teams = data['Tm'].unique()
        options = st.sidebar.multiselect(
        'Pick teams',teams)
        fig = self.plot(data, options)
        st.pyplot(fig)