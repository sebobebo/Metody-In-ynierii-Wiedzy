def funkcja(data_text):
    return {
        'length': len(data_text),
        'letters': set(list(data_text)),
        'big_letters': data_text.upper(),
        'small_letters': data_text.lower()
    }

print(funkcja('To jest fajny napis'))
