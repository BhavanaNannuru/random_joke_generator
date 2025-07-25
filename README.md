# Joke Generator App

A simple yet engaging Joke Generator built with Python and Tkinter, leveraging a public joke API. The app provides users with a clean, dark-themed interface and fetches random jokes on demand, displaying them clearly and responsively.

## Features Implemented

- **Live Joke Fetching:** Retrieves jokes in real-time using the [Official Joke API](https://github.com/15Dkatz/official_joke_api).
- **Dark Mode UI:** Built with `ttkbootstrap` using the `darkly` theme for modern aesthetics.
- **Responsive Text Display:** Automatically adjusts the label height to accommodate jokes of varying lengths.
- **Cross-platform Compatibility:** Runs smoothly on Windows, Linux, and macOS with Python installed.

## Requirements

- Python 3.7+
- `requests`
- `tkinter` (usually comes pre-installed with Python)
- `ttkbootstrap`

Install required dependencies using:

```bash
pip install requests ttkbootstrap
```

## Planned Enhancements

### 1. Category & Language Filters
Introduce dropdown menus or buttons to allow users to select joke categories (e.g., programming, general, knock-knock) and preferred languages, provided the API supports such filtering.

### 2. Text-to-Speech (TTS) Integration
Enable text-to-speech functionality so jokes can be read aloud to users using libraries such as:
- `pyttsx3` for offline TTS
- `gTTS` for Google-based online TTS

### 3. Joke Sharing Capabilities
Add multiple sharing options:
- Copy joke text to clipboard
- Share via email using `smtplib`
- Post to Twitter using the `tweepy` library or Twitter API

### 4. Daily Joke Scheduler
Implement a feature that delivers a random joke to users once a day via:
- Tkinter popup notifications
- Desktop notifications using `plyer` or `notify2`

### 5. Custom Theming Options
Allow users to personalize the app appearance:
- Toggle between light and dark modes
- Select preferred fonts and sizes
- Save UI preferences between sessions

### 6. Optional Features (Time-Permitting)
- **Keyboard Shortcuts:** Add hotkeys for common actions (e.g., spacebar to fetch a joke)
- **Fun Animations:** Use fade-in/fade-out or slide effects to make joke transitions more engaging
- **Android Port:** Build a mobile version using frameworks such as:
  - `Kivy` or `KivyMD`
  - `BeeWare`
  - Converting to a web app and wrapping via tools like `WebView`



## Credits

This project was inspired by the video tutorial:

**"How to Make a Joke Generator App in Python with Tkinter"**  
by **Tech With Tim**  
Watch the video here: [https://youtu.be/n6EcLv7ICtI](https://youtu.be/n6EcLv7ICtI)




## Disclaimer

This application is developed purely for educational and entertainment purposes. The jokes fetched and displayed by the app are sourced from a public API ([Official Joke API](https://official-joke-api.appspot.com)), and the developer holds no responsibility for the content served through it. 

Use of this application signifies that you understand and accept that:

- The humor and language of jokes are not curated or moderated by the developer.
- Any inappropriate or offensive content retrieved from the API is unintended and should be reported to the API provider.
- No data is collected, stored, or shared by this application.

The project is open-source and distributed without any warranty. Use at your own discretion.
