from twilio.rest import Client
import pyaudio
import wave
import get_predictions
import classify

# putting these in plaintext because why not
account_sid = "AC7d4a590d36bee825f69931b3549953ff"
auth_token = "18ebd2f54e0d7c33eb047cccbfec13dd"

client = Client(account_sid, auth_token)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "input.wav"

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)


f = open("log.txt", "a")

while True:
    frames = [stream.read(CHUNK) for i in range(RATE//CHUNK*RECORD_SECONDS)]

    wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    prediction = get_predictions.get_prediction(WAVE_OUTPUT_FILENAME)

    dangers = [i for i in prediction if i not in classify.non_intrusive]

    if len(dangers) > 0:
        if len(dangers) == 1:
            text = "There is " + dangers[0].lower() + " at your house."
        else:
            text = "There is either "
            for i in range(len(dangers)):
                if i == 0:
                    text += dangers[i].lower()
                else:
                    text += " or " + dangers[i].lower()
            text += " at your house."

        message = client.messages.create(
            to="+16478343687",
            from_="+12892174631",
            body=text
        )

    f.write(str(prediction) + "\n")
    f.flush()
