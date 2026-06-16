import streamlit as st
import plotly.express as px

from analyzer import *

st.title("GitHub Profile Analyzer")

username = st.text_input("GitHub Username")

if username:

    profile = get_profile(username)
    repos = get_repos(username)

    st.image(profile["avatar_url"], width=150)

    st.subheader(profile["name"])

    if profile.get("bio"):
        st.write(profile["bio"])

    st.write(f"Followers: {profile['followers']}")
    st.write(f"Public Repos: {profile['public_repos']}")

    score = developer_score(profile, repos)

    st.metric("Developer Score", score)

    langs = language_stats(repos)

    fig = px.pie(
        names=list(langs.keys()),
        values=list(langs.values()),
        title="Languages Used"
    )

    st.plotly_chart(fig)

    st.subheader("Top Repositories")

    for repo in top_repositories(repos):
        st.write(
            f"⭐ {repo['stargazers_count']} - {repo['name']}"
        )

    st.link_button(
        "Open GitHub Profile",
        profile["html_url"]
    )