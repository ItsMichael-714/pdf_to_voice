import PyPDF2
import pyttsx3

pdf_reader = PyPDF2.PdfReader(open("PDF document.pdf ", "rb"))
speaker = pyttsx3.init()
clean_text = ""
num_pages = len(pdf_reader.pages)

for page_Num in range(num_pages):
    text = pdf_reader.pages[page_Num].extract_text()
    clean_text += text.strip().replace("\n", " ")
    print(clean_text)
speaker.say(clean_text)
speaker.save_to_file(clean_text, "name.mp3")
speaker.runAndWait()

speaker.stop()
