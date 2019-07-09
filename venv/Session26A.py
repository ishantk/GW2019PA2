from gtts import gTTS

# Create Object for gTTS class
text = "How are you"
tts = gTTS(text, lang="en")
tts.save("hello.mp3")
print(">> File Saved")

# Explore More here !!
# https://gtts.readthedocs.io/en/latest/module.html#examples
# https://pypi.org/project/SpeechRecognition/