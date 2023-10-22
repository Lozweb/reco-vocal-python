import record
import voice_to_text

filename = "record.wav"

data = record.record_default_device()

record.write_to_file(data, filename)

text = voice_to_text.translate(filename)

if text == "comment tu t'appelles":
    print("je m'appelle Stitch")
    record.to_voice("je m'appelle Stitch")
else:
    print("Hum ... Je ne sais pas")
    record.to_voice("Hum ... Je ne sais pas")
