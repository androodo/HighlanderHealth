# Highlander Health

Highlander Health is a dynamic web application designed to empower college students to achieve their nutritional goals. Tailored to the busy lifestyles of campus life, our app delivers a personalized daily meal plan based on individual health metrics and the latest Glasgow dining hall menu.

---

## Table of Contents

- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges](#challenges)
- [Accomplishments](#accomplishments)
- [What We Learned](#what-we-learned)
- [What's Next](#whats-next)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Inspiration

Everyone is familiar with the infamous "Freshman 15." Balancing academics, extracurricular activities, and a healthy diet is a constant challenge for college students. Inspired by this struggle, we developed Highlander Health—an app specifically designed for dining hall users. Our goal is to foster a healthy lifestyle by making nutrition accessible and personalized.

---

## What It Does

Highlander Health optimizes your nutrition journey by:
- **Personalized Meal Plans:** Input your weight, height, and dietary goals (whether bulking, cutting, or maintaining) to receive a tailored daily meal plan.
- **Dynamic Integration:** Our system pulls data directly from the current Glasgow menu, ensuring your meal plans are both relevant and adaptable.
- **Precision in Personalization:** We leverage advanced algorithms and the GPT-3.5 Turbo API to analyze user inputs and create meal plans that align with your health and fitness objectives.

---

## How We Built It

Highlander Health is a full-stack web application that combines modern frontend development with robust backend integration:
- **Frontend:** Developed using HTML, CSS, and JavaScript to create an intuitive and responsive user interface.
- **Backend:** Powered by Python and Flask, our backend seamlessly handles user requests, integrates with external APIs, and processes data.
- **API Integration:** The GPT-3.5 Turbo API analyzes user input to generate personalized meal recommendations.
- **Data Scraping & Processing:** Using libraries like BeautifulSoup (`bs4`) and Pandas, we scrape the Glasgow dining hall menu to ensure up-to-date meal information.
  
---

## Challenges

During development, our team encountered several hurdles:
- **API Response Times:** Managing and optimizing the response times for the GPT-3.5 Turbo API was critical to ensure a smooth user experience.
- **Fetch Request Implementation:** Integrating fetch requests within Flask required innovative solutions to seamlessly connect the frontend with the backend.
- **Data Integration:** Scraping and synchronizing data from the Glasgow menu in real-time posed unique challenges in data handling and consistency.

---

## Accomplishments

We are proud to have:
- Developed a fully functional, personalized meal planning app within a short timeframe.
- Created a tool that empowers students to make healthier dietary choices effortlessly.
- Fostered a collaborative environment that not only led to technical success but also built lasting connections and teamwork skills.

---

## What We Learned

This project was a deep dive into full-stack development and provided several key insights:
- **Enhanced Web Development Skills:** We significantly improved our skills in both frontend and backend technologies.
- **Effective Team Collaboration:** Working under pressure in a small team honed our ability to collaborate efficiently.
- **Time Management:** Balancing different aspects of the project taught us the importance of time management and agile methodologies.

---

## What's Next

Highlander Health is just getting started! Our future plans include:
- **Improved Accuracy & Speed:** Refining the algorithms for faster and more precise meal recommendations.
- **User Interface Enhancements:** Further polishing the UI to enhance user experience and accessibility.
- **Expansion:** Extending the app’s reach to include other dining halls like Lothian and expanding to more college campuses.

---

## Built With

- **[Python](https://www.python.org/)** - The primary programming language for our backend.
- **[Flask](https://flask.palletsprojects.com/)** - The web framework used to build our server and API endpoints.
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)** - The markup language for structuring the web pages.
- **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)** - The style sheet language used to design the frontend.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - The programming language for dynamic client-side interactions.
- **[GPT-3.5 Turbo API](https://openai.com/api/)** - The AI service used for personalized meal plan generation.
- **[BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** - For web scraping the Glasgow menu.
- **[Pandas](https://pandas.pydata.org/)** - For data manipulation and processing.
- **[OpenAI](https://openai.com/)** - For integrating cutting-edge AI technology into our application.

---

## Getting Started

To get a local copy up and running, follow these simple steps:

### Prerequisites

- **Python 3.7+**
- **Node.js and npm (for frontend dependencies, if applicable)**

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/highlander-health.git
   cd highlander-health

2. **Set Up a Virtual Environment:

   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
