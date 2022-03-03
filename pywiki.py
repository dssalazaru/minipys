import wikipedia
import tkinter as tk

result = ''

def search():
    wikiSearch = tk.Tk()
    l = tk.Label(wikiSearch, text = entlvar.get())
    l.pack()
    t = tk.Text(wikiSearch, height = 10, width = 52)
    t.pack()
    result = wikipedia.summary(entlvar.get(), sentences = 2)
    t.insert(tk.END, result)

wikiSearch = tk.Tk()

l = tk.Label(wikiSearch, text = 'Search').grid(row = 0)
entlvar = tk.StringVar()
enl = tk.Entry(wikiSearch, textvariable = entlvar)
enl.grid(row = 0, column = 1)

tk.Button(wikiSearch, text = 'Exit', command = wikiSearch.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
tk.Button(wikiSearch, text = 'Search', command = search).grid(row = 3, column = 1, sticky = tk.W, pady = 4)

tk.mainloop()
