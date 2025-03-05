from vosk import Model, KaldiRecognizer
import wave


def transcribe_audio(audio_path):
    model = Model("model")  # Placeholder for Vosk model
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    transcription = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            transcription += rec.Result()
    return transcription or "No transcription available"