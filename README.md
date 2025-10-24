# Text Generation Project (Primarily Rap)

# Text Generator Frontend

React-based frontend for the AI Text Generation project using SmolLM2-135M-Instruct model.

## Project Overview

This application provides a user-friendly interface for text generation using a pretrained language model. Users can input prompts and adjust generation parameters (temperature, max tokens) to create AI-generated text.

## Prerequisites

- Node.js (version 14.0.0 or higher)
- Running FastAPI backend at `http://localhost:8000`

## Installation

```bash
npm install
```

## Running the Application

### Development Mode

```bash
npm start
```

Runs the app in development mode at [http://localhost:3000](http://localhost:3000).

The page will reload when you make changes. You may also see any lint errors in the console.

### Production Build

```bash
npm run build
```

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.

## Backend Setup

Make sure the FastAPI backend is running before starting the frontend:

```bash
# In the project root directory
make init
make api
```

The backend should be available at `http://localhost:8000`.

## Features

- Text generation with customizable parameters
- Real-time API communication with FastAPI backend
- Modern, responsive UI
- Error handling and loading states
- Adjustable temperature and token limits

## API Integration

The frontend communicates with the backend via POST requests to `/generate` endpoint:

**Request:**
```json
{
  "prompt": "Your text prompt",
  "max_new_tokens": 50,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "prompt": "Your text prompt",
  "generated": "AI-generated text"
}
```

## Project Structure

```
frontend/
├── public/
├── src/
│   ├── App.js          # Main component with API integration
│   ├── App.css         # Styling
│   ├── index.js        # Entry point
│   └── ...
├── package.json
└── README.md
```

## Technologies Used

- React 18
- Fetch API for HTTP requests
- CSS3 for styling
- Create React App for project setup

## Testing

```bash
npm test
```

Launches the test runner in interactive watch mode.

See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

## Troubleshooting

### CORS Errors

If you encounter CORS errors, ensure the backend has CORS middleware configured:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Backend Not Running

Verify the backend is running at `http://localhost:8000/docs` - you should see the FastAPI interactive documentation.

### Port Already in Use

If port 3000 is already in use, you'll be prompted to use another port. Press `Y` to accept.

## Learn More

- [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started)
- [React documentation](https://reactjs.org/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)

## Available Scripts

### `npm start`

Runs the app in the development mode.
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.

### `npm run build`

Builds the app for production to the `build` folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

---

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
