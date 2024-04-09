# Weather Application

This is a simple command-line weather application that retrieves weather information for a specified city using the OpenWeatherMap API.

## Functionality

The application allows users to retrieve weather information for a specific city. It provides the following details:

- City name
- Country
- Temperature
- Weather description

Additionally, the user can specify optional flags to retrieve additional information:

- `-p` or `--pressure`: Get the atmospheric pressure data for the entered city.
- `-h` or `--humidity`: Get the humidity data for the entered city.

## Setup

### Environment Variables

Before running the application, you need to set up an environment variable for the OpenWeatherMap API key. Follow these steps:

1. Sign up for an account on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Once logged in, navigate to the API keys section and copy your API key.
3. Set an environment variable named `OpenWeatherMapAPI` and paste your API key as the value.

#### Windows

```bash
setx OpenWeatherMapAPI "your-api-key"
