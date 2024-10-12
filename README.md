# Orbit Tracker - Satellite Tracker Project

This project allows users to track satellites currently orbiting above a specific city. By inputting a city, country, and an observation angle, the application will return information about visible satellites over that location. The project leverages various modules to retrieve city coordinates, city elevation, satellite data from an API, and display the results via a graphical user interface (GUI).

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [API Key Setup](#api-key-setup)
- [Contributing](#contributing)
- [License](#license)

## Features
- Retrieve city coordinates and elevation based on user input.
- Fetch real-time satellite data using the [N2YO Satellite API](https://www.n2yo.com/api/).
- Display a list of satellites currently passing over a specified city using a simple GUI.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Fritzalas/Orbit_Tracker.git
    cd Orbit_Tracker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a valid API key from the [N2YO Satellite API](https://www.n2yo.com/api/). See the [API Key Setup](#api-key-setup) section.

## Usage
1. Run the main script:
    ```bash
    python main.py
    ```

2. When prompted, enter:
   - **City**: The name of the city you want to track satellites over.
   - **Country**: The country the city is located in.
   - **Angle**: The observation angle in degrees to search for visible satellites (e.g., 10, 45, etc.).

3. The application will then:
   - Retrieve the city's coordinates.
   - Get the city's elevation.
   - Fetch a list of satellites currently passing over the city.
   - Display the satellites in a graphical user interface.

## Modules
This project uses the following modules:
- `City_Coordinates`: Retrieves latitude and longitude coordinates for the inputted city and country.
- `City_Elevation`: Gets the elevation of the city based on the coordinates.
- `Satellite_API_Call`: Makes an API call to N2YO to retrieve satellite data.
- `Submit`: Manages user input for city, country, and angle.
- `display_satellites`: Displays the satellite information in a GUI format.

## API Key Setup
1. Go to the [N2YO Satellite API](https://www.n2yo.com/api/) and sign up for an API key.
2. Add your API key to the `main.py` file, replacing the placeholder:
    ```python
    api_key = 'YOUR_API_KEY_HERE'
    ```
3. Adjust the `category_id` if needed:
    - **0**: Retrieves all satellites (default).
    - You can find other category IDs in the API manual [here](https://www.n2yo.com/api/).

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new feature branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add your feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Create a pull request describing your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information, visit the [Orbit Tracker GitHub Repository](https://github.com/Fritzalas/Orbit_Tracker).
