# RetailIQ

**RetailIQ** is an AI-powered platform aimed at enhancing demand forecasting in the retail industry. By leveraging advanced machine learning techniques, it helps retailers optimize inventory management, streamline logistics, and improve customer satisfaction.

## Features
- **Accurate Demand Forecasting**: Use AI to predict retail demand trends and plan inventory accordingly.
- **Logistics Optimization**: Streamline warehouse operations, transport routes, and minimize delivery times.
- **Interactive Visualizations**: View forecasts and operational insights through a user-friendly interface.

## Technology Stack
- **Programming Language**: Python
- **Machine Learning Framework**: TensorFlow
- **API Framework**: FastAPI
- **UI Framework**: Streamlit
- **Database**: PostgreSQL

## Installation

### Prerequisites
- **Python 3.8+** installed.
- **PostgreSQL** installed and running.

### Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/RetailIQ.git
   cd RetailIQ
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database (PostgreSQL):
   - Create a database named `retailiq` and update connection settings in the config.

5. Run the application:
   - For the API: 
     ```sh
     uvicorn src.api.main:app --reload
     ```
   - For the UI:
     ```sh
     streamlit run src/ui/app.py
     ```

## Usage
- Use the **Streamlit UI** to input parameters and view demand forecasts.
- Access the **FastAPI REST API** to integrate with other systems for demand prediction.

## Contributing
We welcome contributions from the community! Please refer to the **ROADMAP.md** for the planned features and open issues.

## License
[MIT](https://choosealicense.com/licenses/mit/)
