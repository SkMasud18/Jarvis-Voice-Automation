import os
import sys
import webbrowser
import subprocess
import psutil
from datetime import datetime

class ActionDispatcher:
    """
    Executes operating system level commands based on classified intents.
    Supports cross-platform desktop hooks for macOS, Linux, and Windows.
    """

    def __init__(self):
        self.platform = sys.platform

    def open_whatsapp(self) -> str:
        """Launches WhatsApp desktop application or web portal."""
        try:
            if self.platform == "darwin":
                subprocess.run(["open", "-a", "WhatsApp"], check=True)
            elif self.platform.startswith("win"):
                os.system("start whatsapp:")
            else:
                webbrowser.open("https://web.whatsapp.com")
            return "Opening WhatsApp..."
        except Exception:
            webbrowser.open("https://web.whatsapp.com")
            return "Opening WhatsApp Web in your default browser..."

    def open_youtube(self, query: str = None) -> str:
        """Launches YouTube or directly executes search."""
        if query:
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Searching YouTube for '{query}'..."
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    def web_search(self, query: str) -> str:
        """Executes a Google search in the default web browser."""
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        return f"Executing web search for: {query}"

    def get_system_telemetry(self) -> str:
        """Gathers real-time CPU, RAM, and Battery statistics."""
        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory().percent
        battery = psutil.sensors_battery()
        bat_str = f"{battery.percent}%" if battery else "AC Powered"
        return f"System status: CPU at {cpu}%, RAM utilization at {ram}%, Battery: {bat_str}."

    def get_time(self) -> str:
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d')}."
