import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Faraz Ahmed's CV")

# Introduction section
st.title("**Faraz Ahmed**")
st.subheader("**Data Scientist**")
st.write("Driven and analytical data scientist with 5+ years of experience in building and deploying machine learning models. Passionate about using data to solve real-world problems.")

# Experience section
st.header("Experience")
job1 = {
    "title": "Senior Data Scientist",
    "company": "Acme Corporation",
    "dates": "2020 - Present",
    "description": "Developed and implemented machine learning models for customer churn prediction, leading to a 15% reduction in churn rate. Built and deployed automated data pipelines for real-time analytics."
}
job2 = {
    "title": "Data Analyst",
    "company": "StartUpX",
    "dates": "2018 - 2020",
    "description": "Analyzed customer behavior data to identify insights and improve marketing campaigns. Created interactive dashboards for data visualization and reporting."
}
st.write(job1)
st.write(job2)

# Skills section
st.header("Skills")
st.write("**Technical Skills:** Python, R, SQL, Machine Learning (Scikit-learn, TensorFlow), Deep Learning (PyTorch), Cloud Computing (AWS, Azure)")
st.write("**Soft Skills:** Communication, Teamwork, Problem-Solving, Critical Thinking, Data Visualization")

# Education section
st.header("Education")
st.write("**Master of Science in Data Science**, University of California, Berkeley - 2018")
st.write("**Bachelor of Science in Computer Science**, Massachusetts Institute of Technology - 2016")

# Projects section (optional)
# st.header("Projects")
# st.write("Add a brief description of your personal projects or contributions to open-source projects.")

# Contact section
st.header("Contact")
st.write("Email:ahmedfaraz5588@mail.com")
st.write("LinkedIn: https://www.linkedin.com/in/johndoe/")

# Interactive elements (optional)
# Add code for charts, maps, media, etc., as needed.

# Run the app
if __name__ == "__main__":
    st.write("**Interactive CV powered by Streamlit**")
