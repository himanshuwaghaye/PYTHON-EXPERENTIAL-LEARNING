"""
English to Hindi Translator
Project Assessment-I
Python Programming Language (N-PCCCM304P)

Name: HIMANSHU SHRIDHAR WAGHAYE
USN: CM25019

This is a simple classroom/demo implementation using a predefined
English-to-Hindi dictionary. It also includes the structure needed
to extend the project with a translation API.
"""

# Predefined English-to-Hindi dictionary
translations = {
    "hello": "नमस्ते",
    "hi": "नमस्ते",
    "good morning": "सुप्रभात",
    "good afternoon": "शुभ दोपहर",
    "good evening": "शुभ संध्या",
    "good night": "शुभ रात्रि",
    "how are you": "आप कैसे हैं",
    "i am fine": "मैं ठीक हूँ",
    "thank you": "धन्यवाद",
    "thanks": "धन्यवाद",
    "welcome": "स्वागत है",
    "please": "कृपया",
    "sorry": "माफ़ कीजिए",
    "yes": "हाँ",
    "no": "नहीं",
    "friend": "दोस्त",
    "student": "विद्यार्थी",
    "teacher": "शिक्षक",
    "school": "विद्यालय",
    "college": "महाविद्यालय",
    "book": "किताब",
    "water": "पानी",
    "food": "भोजन",
    "house": "घर",
    "computer": "कंप्यूटर",
    "python": "पायथन",
    "program": "कार्यक्रम",
    "language": "भाषा",
    "india": "भारत",
    "good": "अच्छा",
    "bad": "बुरा",
    "day": "दिन",
    "night": "रात",
    "today": "आज",
    "tomorrow": "कल",
    "help": "मदद",
}


def translate_with_dictionary(text):
    """
    Translate a word or complete phrase using the predefined dictionary.

    Exact phrase matching is checked first.
    If the complete phrase is not found, each word is translated
    individually when a dictionary entry exists.
    """

    text = text.strip().lower()

    if not text:
        return ""

    # First try the complete sentence/phrase
    if text in translations:
        return translations[text]

    # Otherwise translate word by word
    words = text.split()
    translated_words = []

    for word in words:
        # Remove common punctuation for dictionary lookup
        clean_word = word.strip(".,!?;:")

        if clean_word in translations:
            translated = translations[clean_word]

            # Preserve basic punctuation
            if word and word[-1] in ".,!?;:":
                translated += word[-1]

            translated_words.append(translated)
        else:
            # Keep unknown words unchanged
            translated_words.append(word)

    return " ".join(translated_words)


def translate_text(text):
    """
    Main translation function.

    This version uses the predefined dictionary.
    A translation API can be connected here later for
    larger vocabulary and sentence-level translation.
    """
    return translate_with_dictionary(text)


def main():
    print("=" * 55)
    print("        ENGLISH TO HINDI TRANSLATOR")
    print("=" * 55)

    print("\nType 'exit' to close the program.")
    print("You can enter a word, sentence or short paragraph.")

    while True:
        english_text = input("\nEnter English text: ").strip()

        # Exit option
        if english_text.lower() == "exit":
            print("\nThank you for using the English to Hindi Translator!")
            break

        # Input validation
        if not english_text:
            print("Please enter some English text.")
            continue

        try:
            hindi_text = translate_text(english_text)

            if not hindi_text:
                print("Translation could not be generated.")
            else:
                print("\nEnglish :", english_text)
                print("Hindi   :", hindi_text)

        except Exception as error:
            # Exception handling prevents the application from crashing
            print("An error occurred while translating the text.")
            print("Error:", error)


if __name__ == "__main__":
    main()
