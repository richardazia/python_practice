from textblob import TextBlob
import pyttsx3
engine = pyttsx3.init()
engine.say("Enter your thought of the day. ")
engine.runAndWait()

print("Enter your thought of the day: ")
phrase = input("> ")
assess = TextBlob(phrase)
print(assess.sentiment.polarity)
while assess.sentiment.polarity < 0.5:
    print("That response is not happy enough. Try again: ")
    engine.say(f"{phrase}That response is not happy enough. Try again: ")
    engine.runAndWait()
    phrase = input("> ")
    assess = TextBlob(phrase)
print("Finally, you are more positive. Our work here is done. ")

engine = pyttsx3.init()
engine.say("Finally, you are more positive. Our work here is done. ")
engine.runAndWait()

# blob = TextBlob("Good Morning World")
# print(blob.sentiment)

# blab = TextBlob("That was such a fantastic race. I can't wait to see how well you did. ")
# print(blab.sentiment)

# blib = TextBlob("You are a deeply confusing and frustrating person to deal with. ")
# print(blib.sentiment)