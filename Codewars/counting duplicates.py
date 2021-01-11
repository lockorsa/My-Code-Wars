def duplicate_count(text):
    return len([i for i in set(text.lower) if text.lower().count(i) > 1])


print(duplicate_count(""), 0)
print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdeaa"), 1)
print(duplicate_count("abcdeaB"), 2)
print(duplicate_count("Indivisibilities"), 2)
