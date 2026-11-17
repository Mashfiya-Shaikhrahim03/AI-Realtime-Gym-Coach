# AI Realtime Gym Coach – Your Personal AI Fitness Assistant

## About the Project

Many people prefer working out at home, but not everyone has access to a personal trainer. Sometimes people know which exercises to perform but don't know whether they are performing them correctly.

That's what inspired me to build **AI Realtime Gym Coach**, an AI-powered fitness assistant designed to guide people during their home workouts.

I wanted to build something that works like a virtual gym trainer. Instead of only counting repetitions, the application analyzes body posture, understands exercise movements, and uses an LLM to provide suggestions when users perform an exercise incorrectly.

The main idea is to make exercise guidance more accessible through AI, computer vision, and voice interaction.

## Key Features

- **AI-Powered Exercise Guidance:** Uses an LLM through the Groq API to generate exercise-related suggestions based on the user's movements and posture analysis.
- **Real-Time Pose Detection:** Uses a pretrained MediaPipe Pose Landmarker model to detect body landmarks through the camera.
- **Exercise and Posture Analysis:** Processes detected body landmarks to understand exercise movements and identify posture-related issues.
- **Multiple Exercise Support:** Includes common exercises such as:
  - Squats
  - Bicep Curls
  - Lunges
  - Push-ups
  - Other supported exercises
- **Text-to-Speech:** Converts AI-generated exercise suggestions into voice feedback.
- **Voice Pipeline:** Connects text generation, speech conversion, and audio playback.
- **Automatic Audio Playback:** Allows users to hear exercise guidance without constantly checking the screen.
- **User Authentication:** Provides an authentication system for user access.
- **SQLite3 Database:** Stores user-related information and application data.
- **Interactive Interface:** Built using Streamlit for a simple and user-friendly experience.

## How It Works

The application combines computer vision, exercise analysis, and an LLM to provide interactive workout guidance.

1. **Camera Input:** The user starts the workout using the camera.
2. **Video Processing:** The video processor captures and processes incoming camera frames.
3. **Pose Detection:** MediaPipe Pose Landmarker detects important body landmarks.
4. **Exercise Analysis:** The application processes the detected landmarks to analyze posture and exercise movements.
5. **LLM Integration:** Exercise-related information is passed to the Groq-powered LLM using a custom prompt. The model generates suggestions based on the analysis.
6. **Text-to-Speech:** The generated feedback is converted into speech.
7. **Voice Feedback:** The voice pipeline handles audio playback so users can hear the suggestions during their workout.

### System Workflow

Camera Input → Video Processor → MediaPipe Pose Detection → Exercise Analysis → Groq LLM → Text-to-Speech → Voice Feedback

SQLite3 manages application data separately.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Streamlit | Web application and user interface |
| MediaPipe | Pretrained pose landmark detection |
| NumPy | Numerical operations and landmark calculations |
| Pandas | Data handling and processing |
| Groq API | LLM integration and AI-generated exercise guidance |
| gTTS | Text-to-speech conversion |
| Streamlit-WebRTC | Real-time camera and video streaming |
| SQLite3 | Database and data storage |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

## Voice Pipeline

One feature I wanted to add was voice-based interaction.

When the LLM generates exercise suggestions, the application can convert the text into speech using gTTS. The voice pipeline then handles the generated audio and automatic playback.

This makes the application more interactive because users can listen to exercise guidance while focusing on their movements.

## Deployment

The application is deployed using Streamlit Community Cloud.

**Live Application:**  
https://ai-realtime-gym-coach-personal-asistant.streamlit.app/

**Landing Page:**  

## What I Learned

Building this project helped me understand how different AI technologies can work together in a real-world application.

Some of the key areas I explored were:

- Real-time computer vision and video processing.
- Pose estimation using a pretrained model.
- Body landmark analysis for exercise movements.
- LLM integration using the Groq API.
- Prompt engineering for contextual exercise guidance.
- Text-to-speech and voice pipeline integration.
- User authentication and SQLite3 database management.
- Building and deploying an interactive application using Streamlit.

The most interesting part was connecting video processing with an LLM and a voice pipeline to create an interactive fitness assistant rather than just another exercise-tracking application.

---
