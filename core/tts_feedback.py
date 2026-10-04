import sys

class VoiceSynthesizer:
    """
    Offline Text-To-Speech engine providing spoken feedback.
    Falls back gracefully to console speech output when audio hardware is detached.
    """

    def __init__(self, voice_speed: int = 175):
        self.engine = None
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", voice_speed)
        except Exception:
            self.engine = None

    def speak(self, text: str):
        print(f"\n[JARVIS]: {text}")
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass
