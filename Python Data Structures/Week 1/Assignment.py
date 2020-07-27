text = "X-DSPAM-Confidence:    0.8475";
x = float(text[text.find('0.8475'):])
print(x)