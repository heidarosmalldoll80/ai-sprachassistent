import speech_recognition as sr
import pyttsx3

class Sprachassistent:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def sprich(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def höre(self):
        with sr.Microphone() as source:
            print('Höre...')
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='de-DE')
                print(f'Erkannt: {text}')
                return text
            except sr.UnknownValueError:
                print('Ich habe dich nicht verstanden.')
                return None
            except sr.RequestError:
                print('Fehler beim Anfrage an den Google Sprachdienst.')
                return None

    def beantworte(self, frage):
        antworten = {
            'Wie geht es dir?': 'Mir geht es gut, danke der Nachfrage!',
            'Hallo': 'Hallo! Wie kann ich Ihnen helfen?',
            'Was ist dein Name?': 'Ich bin ein Sprachassistent.',
        }
        return antworten.get(frage, 'Das habe ich nicht verstanden.')

    def starte(self):
        while True:
            frage = self.höre()
            if frage:
                antwort = self.beantworte(frage)
                self.sprich(antwort)

if __name__ == '__main__':
    assistent = Sprachassistent()
    assistent.starte()