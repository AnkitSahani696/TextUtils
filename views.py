from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', '')

    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    analyzed = text

    # 1️⃣ Remove punctuation
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp = ""
        for char in analyzed:
            if char not in punctuations:
                temp += char
        analyzed = temp

    # 2️⃣ Convert to uppercase
    if uppercase == 'on':
        analyzed = analyzed.upper()

    # 3️⃣ Remove new lines
    if newlineremover == 'on':
        temp = ""
        for char in analyzed:
            if char != '\n' and char != '\r':
                temp += char
        analyzed = temp

    # 4️⃣ Remove extra spaces
    if extraspaceremover == 'on':
        temp = ""
        for index, char in enumerate(analyzed):
            if not (analyzed[index] == " " and index + 1 < len(analyzed) and analyzed[index + 1] == " "):
                temp += char
        analyzed = temp

    # 5️⃣ Character Counter
    if charcount == 'on':
        count = len(analyzed)
        return HttpResponse(f"<h1>Character Count</h1><h2>Total Characters: {count}</h2><br><p>{analyzed}</p>")

    return HttpResponse(f"<h1>Analyzed Result</h1><br><p>{analyzed}</p>")
