from slang_detector import detect_slang
from detector import detect_word_ambiguity
from context_ambiguity import detect_contextual_ambiguity
from output_formatter import format_ambiguity_results

while True:
    sentence = input("Enter a sentence (or 'exit' to quit): ")
    if sentence.lower() == "exit":
        break

    slang_results = detect_slang(sentence)
    print("\n=== Slang Detection ===")
    if not slang_results:
        print("slang no detection")
    else:
        for word, meaning in slang_results.items():
            print(f"{word} : {meaning}")

    word_ambiguity_results = detect_word_ambiguity(sentence)
    print("\n=== Word-Level Ambiguity ===")
    print(format_ambiguity_results(word_ambiguity_results))
    
    is_ambiguous, ambiguous_words = detect_contextual_ambiguity(sentence)
    print(f"\nambiguity detected : {'yes' if is_ambiguous else 'no'}")
    
    if is_ambiguous:
        for word, meanings in ambiguous_words.items():
            print(f"ambigous word : {word}")
            for i, meaning in enumerate(meanings, 1):
                print(f"   {i}. {meaning}")