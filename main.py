from tkinter import *
from tkinter import ttk
from pathlib import Path
import csv

#Establishing the name of the file
CSV_FILE = Path("form.csv")

#Establishing the TTK skeleton
root = Tk()
root.title("Dalet Series/Season Form to CSV")
formFiller = ttk.Notebook(root)
seriesView = ttk.Frame(root, padding=15)
seasonView = ttk.Frame(root, padding=15)

formFiller.add(seriesView, text="Series Form")
formFiller.add(seasonView, text="Season Form")
formFiller.pack(expand=True, fill="both")

for i in range(8):
    seriesView.rowconfigure(i, weight=1)
seriesView.columnconfigure(1, weight=1)

#Series Form
ttk.Label(seriesView, text="Title").grid(column=0, row=0, sticky="w")
SeriesTitle_text = Text(seriesView, height=2, width=60)
SeriesTitle_text.grid(column=1, row=0, sticky="nsew")

ttk.Label(seriesView, text="Short Title (25 chars)").grid(column=0, row=1, sticky="w")
SeriesShortTitle_text = Text(seriesView, height=2, width=60, wrap="word")
SeriesShortTitle_text.grid(column=1, row=1)

ttk.Label(seriesView, text="Sort Title").grid(column=0, row=2, sticky="w")
SeriesSortTitle_text = Text(seriesView, height = 2, width=60)
SeriesSortTitle_text.grid(column = 1, row = 2)

ttk.Label(seriesView, text="Long (1000 chars)").grid(column=0, row=3, sticky="w")
SeriesLong_text = Text(seriesView, width=60, height=11, wrap="word")
SeriesLong_text.grid(column=1, row=3)

ttk.Label(seriesView, text="Medium (250 chars)").grid(column=0, row=4, sticky="w")
SeriesMedium_text = Text(seriesView, width=60, height=5, wrap="word")
SeriesMedium_text.grid(column=1, row=4)

ttk.Label(seriesView, text="Short (99 chars)").grid(column=0, row=5, sticky="w")
SeriesShort_text = Text(seriesView, width=60, height=4, wrap="word")
SeriesShort_text.grid(column=1, row=5)

ttk.Label(seriesView, text="XShort (60 chars)").grid(column=0, row=6, sticky="w")
SeriesXShort_text = Text(seriesView, width=60, height=3, wrap="word")
SeriesXShort_text.grid(column=1, row=6)

ttk.Label(seriesView, text="Tiny (40 chars)").grid(column=0, row=7, sticky="w")
SeriesTiny_text = Text(seriesView, width=60, height=2, wrap="word")
SeriesTiny_text.grid(column=1, row=7)

ttk.Label(seriesView, text="SEO Keywords").grid(column=0, row=8, sticky="w")
SeriesSEO_text = Text(seriesView, width=60, height=2, wrap="word")
SeriesSEO_text.grid(column=1, row=8)

#Season Form
ttk.Label(seasonView, text="Title").grid(column=0, row=0, sticky="w")
seasonTitle_text = Text(seasonView, height=2, width=60)
seasonTitle_text.grid(column=1, row=0, sticky="nsew")

ttk.Label(seasonView, text="Long (1000 chars)").grid(column=0, row=1, sticky="w")
SeasonLong_text = Text(seasonView, width=60, height=11, wrap="word")
SeasonLong_text.grid(column=1, row=1)

ttk.Label(seasonView, text="Medium (250 chars)").grid(column=0, row=2, sticky="w")
SeasonMedium_text = Text(seasonView, width=60, height=5, wrap="word")
SeasonMedium_text.grid(column=1, row=2)

ttk.Label(seasonView, text="Short (99 chars)").grid(column=0, row=3, sticky="w")
SeasonShort_text = Text(seasonView, width=60, height=4, wrap="word")
SeasonShort_text.grid(column=1, row=3)

ttk.Label(seasonView, text="XShort (60 chars)").grid(column=0, row=4, sticky="w")
SeasonXShort_text = Text(seasonView, width=60, height=3, wrap="word")
SeasonXShort_text.grid(column=1, row=4)

ttk.Label(seasonView, text="Tiny (40 chars)").grid(column=0, row=5, sticky="w")
SeasonTiny_text = Text(seasonView, width=60, height=2, wrap="word")
SeasonTiny_text.grid(column=1, row=5)

ttk.Label(seasonView, text="SEO Keywords").grid(column=0, row=6, sticky="w")
SeasonSEO_text = Text(seasonView, width=60, height=2, wrap="word")
SeasonSEO_text.grid(column=1, row=6)


root.mainloop()