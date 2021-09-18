from module.voiceAssistant import voiceAssistant;
from module.firefoxAutomating import firefoxAutomating

robot = voiceAssistant()
last_talk = robot.get_audio()

firefox = firefoxAutomating()

if 'Bonjour' in last_talk:
    robot.speak("Bonjour Léo, comment allez-vous aujourd'hui ?")
if 'youtube' in last_talk:
    firefox.open_url('https://www.youtube.com')



