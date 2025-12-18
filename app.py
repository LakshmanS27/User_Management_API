import streamlit as st
import requests

# Base URL of your FastAPI server
BASE_URL = "http://127.0.0.1:8000"

st.title("User Management UI")

menu = ["Create User", "Get Users", "Delete User"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create User":
    st.subheader("Create New User")
    name = st.text_input("Username")
    age = st.text_input("Age")
    email = st.text_input("Email")
    city = st.text_input("City")
    phone_number = st.text_input("Phone Number")
    
    if st.button("Add User"):
        data = {"name": name,"age": age ,"email": email, "city": city, "phone_number": phone_number}
        response = requests.post(f"{BASE_URL}/users", json=data)
        if response.status_code == 201:
            st.success("User created successfully!")
        else:
            st.error(f"Error: {response.text}")

elif choice == "Get Users":
    st.subheader("Get User by ID")
    user_id = st.text_input("Enter User ID")
    
    if st.button("Get User"):
        if user_id:
            response = requests.get(f"{BASE_URL}/users/{user_id}")
            if response.status_code == 200:
                user = response.json()
                st.json(user)  # Display user info nicely
            else:
                st.error(f"User not found or error: {response.text}")
        else:
            st.warning("Please enter a User ID")


elif choice == "Delete User":
    st.subheader("Delete a User")
    user_id = st.text_input("Enter User ID to delete")
    
    if st.button("Delete User"):
        if user_id:
            response = requests.delete(f"{BASE_URL}/users/{user_id}")
            if response.status_code == 200:
                st.success("User deleted successfully")
            elif response.status_code == 404:
                st.error("User not found")
            else:
                st.error(f"Failed to delete user: {response.text}")
        else:
            st.warning("Please enter a User ID")

