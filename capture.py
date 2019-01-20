from twilio.rest import Client
import pyaudio
import wave
import datetime
import get_predictions
import classify

lines = [line.strip().split("=") for line in open("key.txt")]
keys = dict()
for line in lines:
    keys[line[0]] = line[1]


def listen_for_intruders():
    # putting these in plaintext because why not
    account_sid = keys["account_sid"]
    auth_token = keys["auth_token"]

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

    #f = open("log.txt", "a")

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
            to=keys["to"],
            from_=keys["from"],
            body=text
        )

    #f.write("[" + str(datetime.datetime.now().time()) + "] " + str(prediction) + "\n")
    #f.flush()
