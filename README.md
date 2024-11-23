
# Car AI Assistant

This project is an AI-powered assistant designed for infotainment systems, capable of answering questions related to location, playing music, providing weather updates, and suggesting nearby hotels. It can be deployed on embedded devices such as the i.MX8M Plus or in cloud environments like Azure.

## Features

- **Location-based responses**: Get the user's location and provide location-based responses.
- **Music playback**: Search for and play songs through Spotify.
- **Weather updates**: Fetch and provide weather information using OpenWeatherMap.
- **Hotel recommendations**: Suggest hotels nearby using the Booking.com API.

## Project Structure

```
car_ai_assistant/
├── .env              # Environment variables (not included in version control)
├── .gitignore        # Git ignore file for sensitive and unnecessary files
├── requirements.txt  # Dependencies
├── main.py           # Main CLI app entry
├── nodes.py          # Contains nodes for location, music, weather, and hotel tools
├── state.py          # Defines state structure
├── graph.py          # Defines the flow of the application
├── webapp.py         # Web server entry (Flask) for Azure and embedded deployment
└── startup.sh        # Startup script for cloud/embedded deployment
```

## Prerequisites

- **Python 3.8+**
- API keys:
  - **OpenWeatherMap** for weather updates
  - **Spotify** for music playback
  - **Booking.com** for hotel recommendations

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shelarsujit/CarAssistant.git
cd CarAssistant
```

### 2. Install Dependencies

Install required packages with `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
OPENWEATHER_API_KEY="openweather_api_key"
BOOKING_API_KEY="booking_api_key"
SPOTIFY_CLIENT_ID="spotify_client_id"
SPOTIFY_CLIENT_SECRET="spotify_client_secret"
```

### 4. Running the Application

- **CLI Mode**: Run the assistant as a command-line interface tool.

  ```bash
  python main.py
  ```

- **Web Server Mode**: Run the assistant as a web server using Flask.

  ```bash
  python webapp.py
  ```

  Then, make POST requests to `http://localhost:8000/assist` with JSON input:

  ```bash
  curl -X POST http://localhost:8000/assist -H "Content-Type: application/json" -d '{"query": "What's the weather?"}'
  ```

## Deployment

### Deployment on Azure

To deploy on Azure, follow these steps:

1. Create an App Service on Azure.
2. Set up environment variables in the App Service Configuration.
3. Push the repository to Azure for deployment.

### Deployment on Embedded Systems (e.g., i.MX8M Plus)

To deploy on i.MX8M Plus:

1. Install Python and dependencies on the device.
2. Run `webapp.py` as a systemd service or as a standalone script.
3. Adjust configurations as needed for resource constraints.

## Usage

You can interact with the assistant by sending queries. For example:

- **Get Weather**: `"What's the weather in New York?"`
- **Play Music**: `"Play some relaxing music"`
- **Find Hotels**: `"Show hotels near me"`

## API Integration

- **OpenWeatherMap**: Provides current weather data based on location.
- **Spotify**: Plays songs or retrieves song details based on user input.
- **Booking.com**: Fetches nearby hotels for the user’s location.

## Troubleshooting

- **Dependencies**: Ensure `requirements.txt` is installed, and Python 3.8+ is being used.
- **Environment Variables**: Double-check that `.env` is configured and loaded correctly.
- **Embedded Deployment**: For i.MX8M Plus, ensure limited threads and lightweight API calls to prevent system overload.

## Contributing

Contributions are welcome! Please create a new branch for each feature or bug fix.

1. Fork the project.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
