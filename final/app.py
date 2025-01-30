from openai import OpenAI
import os 
from bs4 import BeautifulSoup
import pandas as pd
import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)

# Web scraper URL for the menu
url = "https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=03&locationName=Glasgow&naFlag=1&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate=11%2F20%2F2023"

# Request the webpage and parse its content using BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

# Extract the date of the menu from the page
date_element = soup.find('div', class_='shortmenutitle')  # Find the title element with the menu date
date_string = date_element.text.split('Menus for ')[1].strip()  # Extract and clean up the date string

# Extract all menu items from the page
menu_items = soup.find_all('div', class_='shortmenurecipes')  # Find all recipe elements in the menu
menu_items = [item.text for item in menu_items]  # Extract and clean the text for each menu item

# Function to generate a personalized meal plan
def get_menu_items(weight, height, diet_plan):
    # Initialize OpenAI API client with the key stored in environment variables
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")  # Securely load API key from environment variables
    )
    food_list = menu_items  # Use the extracted menu items as input

    # Use OpenAI API to generate a personalized meal plan
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        temperature=0.8,        # Set the creativity level of the model
        max_tokens=500,         # Limit the number of tokens in the response

        # Input messages to guide the assistant
        messages=[
            # System role message: Defines the assistant's role and context
            {"role": "system", "content": 'You are a concise health assistant helping the user maintain a healthy diet.'},
            
            # User's request: Provide weight, height, diet plan, and menu items for customization
            {"role": "user", "content": f"Display a short list containing a personalized menu for the date: {date_string}. Write in a bulleted list format, a personalized meal plan for the user for each meal given the breakfast menu: {food_list[:13]}, the lunch menu: {food_list[14:43]}, and the dinner menu: {food_list[44:-1]}. Consider the user's weight (pounds):{weight} and height (inches): {height}, and diet plan: {diet_plan}. It should include the date. It should include calories, protein, and fat for each food item and meal. Limit to up to three items per meal. Keep it concise and simple. No extra information is needed."},
        ]
    )

    # Return the generated meal plan
    return completion.choices[0].message.content

# Define the main route for the website
@app.route('/')
def home():
    # Render the main HTML page (index.html)
    return render_template('index.html')

# Define the endpoint to generate a meal plan
@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    # Extract user data from the POST request
    user_data = request.json  # Get JSON payload from the client-side request
    weight = user_data['weight']  # Extract user's weight
    height = user_data['height']  # Extract user's height
    diet_plan = user_data['dietPlan']  # Extract user's dietary preferences

    # Call the function to generate the meal plan
    meal_plan = get_menu_items(weight, height, diet_plan)

    # Return the generated meal plan as a JSON response
    return jsonify(meal_plan)

# Entry point of the application
if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True, port=5000, use_reloader=False)  # Enable debugging and set port
