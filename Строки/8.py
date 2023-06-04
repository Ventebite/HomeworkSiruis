stringa = input()
redact = stringa.replace('ический', '.')
end = redact.replace('ическая', '.')
print(end)