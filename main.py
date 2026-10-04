#!/usr/bin/env python3
"""
Jarvis: Deterministic Voice Automation & Desktop OS Assistant
Author: Sk Masud Rahaman (@SkMasud18) - Falcon Intelligence
Project 1 of the Nox Intelligence Evolution
"""

import sys
import time
from core.intent_parser import IntentParser
from core.action_dispatcher import ActionDispatcher
from core.tts_feedback import VoiceSynthesizer

def print_banner():
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                 PROJECT JARVIS : GENESIS                  ║
    ║       Deterministic Voice & Desktop Operating Assistant   ║
    ║             Architect: Sk Masud Rahaman                   ║
    ╚═══════════════════════════════════════════════════════════╝
    Commands to try:
      - "open whatsapp"
      - "search on youtube lofi beats"
      - "google quantum computing breakthroughs"
      - "system status"
      - "what time is it"
      - "exit"
    """
    print(banner)

def main():
    print_banner()
    parser = IntentParser()
    dispatcher = ActionDispatcher()
    voice = VoiceSynthesizer()

    voice.speak("Jarvis online. Awaiting directive.")

    while True:
        try:
            user_input = input("\n[USER Directive] > ").strip()
            if not user_input:
                continue

            parsed = parser.parse(user_input)
            intent = parsed["intent"]
            slot = parsed["slot"]

            if intent == "whatsapp":
                res = dispatcher.open_whatsapp()
                voice.speak(res)

            elif intent == "youtube":
                res = dispatcher.open_youtube(slot)
                voice.speak(res)

            elif intent == "search":
                res = dispatcher.web_search(slot or user_input)
                voice.speak(res)

            elif intent == "telemetry":
                res = dispatcher.get_system_telemetry()
                voice.speak(res)

            elif intent == "time":
                res = dispatcher.get_time()
                voice.speak(res)

            elif intent == "exit":
                voice.speak("Shutting down Jarvis systems. Goodbye, sir.")
                break

            else:
                voice.speak(f"Directive '{user_input}' not recognized in deterministic register. Forwarding to search...")
                dispatcher.web_search(user_input)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting Jarvis...")
            break

if __name__ == "__main__":
    main()
