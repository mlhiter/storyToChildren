import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0")
engine.say("你好，世界！")
engine.save_to_file("你好，世界！", "test.mp3")
engine.runAndWait()
