# Travel Planner

Explore the world with a custom itinerary tailored to your preferences using advanced natural language processing powered by Google's Gemini API. This Streamlit app dynamically creates travel plans based on user inputs such as destination, date, budget, and personal interests.

## Features

- **Dynamic Travel Planning:** Generate personalized travel plans with details on daily activities.
- **Interactive User Feedback:** Refine travel plans by providing feedback, leveraging the power of Chain of Thought prompting and Dynamic Interaction techniques.
- **User-Friendly Interface:** Simple and intuitive interface using Streamlit for seamless user experience.

## How It Works

1. Users input travel details including the number of people, destination, travel dates, budget, and interests.
2. The app uses the Gemini API to generate an initial travel plan based on these inputs.
3. Users can review the plan and provide feedback to refine the suggestions, which the app then uses to generate a revised itinerary.

## Advanced Prompting Techniques Used

### Enhanced Detail with Chain of Thought Prompting
This technique helps in generating detailed responses by guiding the AI with a series of logical steps, which is utilized to enhance the depth of the travel plan details.

### Dynamic Interaction
Allows the application to interact dynamically with the user's feedback to refine and improve the suggested travel itinerary, making the app more responsive and tailored to user preferences.

## Getting Started

To run this app locally:

1. Clone the GitHub repository:
    ```
    git clone <repository-url>
    ```
2. Install required packages:
    ```
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```
    streamlit run travel_planner.py
    ```
Or visit the Web App here: [View App](https://jingyi-new-travel-planner.streamlit.app/)


## Lessons Learned

- **Prompt Engineering:** How advanced prompting techniques can significantly enhance the AI's ability to generate useful and contextually appropriate content.
- **User Interaction:** The importance of user feedback in interactive applications for personalized experiences.

## Future Improvements

- **Multi-language Support:** To cater to a global audience by adding multiple language options.
- **Integration with Real-Time Data:** To provide updates on weather, local events, etc., enhancing the travel experience.
- **Mobile Optimization:** To ensure the app is fully responsive and functional on mobile devices.
