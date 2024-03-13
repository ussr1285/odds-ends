from gtts import gTTS

# 텍스트 읽기
with open('./text/text.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

# TTS 설정 및 MP3 파일 생성
tts = gTTS(text, lang='ko')
tts.save('output.mp3')
