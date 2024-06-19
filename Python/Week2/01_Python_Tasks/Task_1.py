import webbrowser

URL_OPTIONS = {
"1.GOOGLE":"https://www.google.com",
"2.LINKEDON":"https://www.linkedin.com",
"3.GMAIL":"https://mail.google.com",
"4.YOUTUBE":"https://www.youtube.com",
}

print("Chosoe the Website Please :")
for key in URL_OPTIONS.keys():
    print(key)


selected_websit=int(input())
selected_websit = list(URL_OPTIONS.values())[selected_websit - 1]
webbrowser.get('firefox').open(selected_websit)