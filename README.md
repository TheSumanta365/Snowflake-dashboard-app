# **Government Financial Support for Art - India Dashboard**

## **Overview**
This project is a Streamlit app that allows users to upload state-wise art funding data in CSV format. The app processes the data and visualizes the funding trends over the years for each state in India. It aims to help users analyze how financial support for arts is distributed across different states in India.

The app allows users to:
- Upload CSV data containing state-wise funding information.
- View a processed dataset preview.
- Visualize the funding trends over time for any selected state.
- Filter and analyze data based on state and funding amount.

## **Features**
- **Data Upload**: Users can upload a CSV file containing state-wise funding data.
- **Data Processing**: The app processes and cleans the uploaded data.
- **Interactive Visualizations**: Displays funding trends for the selected state.
- **State Selection**: Allows the user to choose a state to visualize its funding trends.
- **CSV Format**: The CSV should have columns for the state name and corresponding funding amounts for different years.



## **Technologies Used**
- **Streamlit**: For building the interactive web app.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib**: For visualizing the data.
- **Python**: For scripting the app.

## **Installation and Setup**

### **Prerequisites**
- Python 3.7 or higher
- Streamlit account (for deployment on Streamlit Cloud)

### **Local Setup**
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/project-name.git
   cd project-name
Create a virtual environment (optional but recommended)

python -m venv venv
Activate the virtual environment:

For Windows:

.\venv\Scripts\activate
For Mac/Linux:

source venv/bin/activate
Install the required dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
This will start a local server, and you can access the app in your browser at http://localhost:8501.

