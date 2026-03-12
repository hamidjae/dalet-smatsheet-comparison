from tkinter import *
from tkinter import ttk
from pathlib import Path
import csv

#Establishing the name of the file
CSV_FILE = Path("form.csv")

def store_entry(text):
    return text.get("1.0", "end-1c").strip()

def split_seo_keywords(text):
    keywords = []
    words = text.split(";")
    for word in words:
        cleaned_word = word.strip()
        if cleaned_word:
            keywords.append(cleaned_word)
    return keywords

def store_series_form():
    row={
        "form_type": "series",
        "title": store_entry(SeriesTitle_Titletext),
        "short_title": store_entry(SeriesShortTitle_text),
        "sort_title": store_entry(SeriesSortTitle_text),
        "long": store_entry(SeriesLong_text),
        "medium": store_entry(SeriesMedium_text),
        "short": store_entry(SeriesShort_text),
        "xshort": store_entry(SeriesXShort_text),
        "tiny": store_entry(SeriesTiny_text),
        "seo_keywords": store_entry(SeriesSEO_text),
        "expected_duration": store_entry(seriesTitle_Durationtext),
    }
    write_to_csv(row)
    print("Saved Series Form")

def store_season_form():
    row={
        "form_type": "season",
        "title/number": store_entry(seasonTitle_text),
        "long": store_entry(SeasonLong_text),
        "medium": store_entry(SeasonMedium_text),
        "short": store_entry(SeasonShort_text),
        "xshort": store_entry(SeasonXShort_text),
        "tiny": store_entry(SeasonTiny_text),
        "seo_keywords": store_entry(SeasonSEO_text),
    }
    write_to_csv(row)
    print("Saved Season Form")

def store_episode_form():
    row={
        "form_type": "episode",
        "title/number": store_entry(episodeTitle_text),
        "short title": store_entry(episodeShortTitle_text),
        "sort title": store_entry(episodeSortTitle_text),
        "long": store_entry(episodeLong_text),
        "medium": store_entry(episodeMedium_text),
        "short": store_entry(episodeShort_text),
        "xshort": store_entry(episodeXShort_text),
        "tiny": store_entry(episodeTiny_text),
        "seo_keywords": store_entry(episodeSEO_text),
        "expected_duration": store_entry(episodeDuration_text),
    }
    write_to_csv(row)
    print("Saved Season Form")

def store_extra_form():
    row={
        "form_type": "extra",
        "title/number": store_entry(extraTitle_text),
        "short title": store_entry(extraShortTitle_text),
        "sort title": store_entry(extraSortTitle_text),
        "long": store_entry(extraLong_text),
        "medium": store_entry(extraMedium_text),
        "short": store_entry(extraShort_text),
        "xshort": store_entry(extraXShort_text),
        "tiny": store_entry(extraTiny_text),
        "expected_duration": store_entry(extraDuration_text),
    }
    write_to_csv(row)
    print("Saved Season Form")

def write_to_csv(dictionary):
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for key, value in dictionary.items():
            if key == "seo_keywords":
                keywords = split_seo_keywords(value)
                # Write up the key, and then as separate column entries, each keyword.
                writer.writerow([key] + keywords)
            else:
                # Write up the key and then the value in the next column.
                writer.writerow([key, value])
        # Writing an empty row to account for multiple saves.
        writer.writerow([])

def add_save_button(tab_frame, row, save_cmd):
    btn = ttk.Button(tab_frame, text="Save Form", command=save_cmd)
    btn.grid(column=1, row=row, sticky="e", pady=(10, 0))
    return btn

#Establishing the TTK skeleton
root = Tk()
root.title("Dalet Series/Season Form to CSV")
#VERY IMPORTANT: Establish a notebook BEFORE adding the tabs.. otherwise it does not work
formFiller = ttk.Notebook(root)

#Adding tabs to the notebook
seriesView = ttk.Frame(root, padding=15)
seasonView = ttk.Frame(root, padding=15)
episodeView = ttk.Frame(root, padding=15)
extraView = ttk.Frame(root, padding=15)

formFiller.add(seriesView, text="Series Form")
formFiller.add(seasonView, text="Season Form")
formFiller.add(episodeView, text="Episode Form")
formFiller.add(extraView, text="Extra Form")
formFiller.pack(expand=True, fill="both")

#Series Form
ttk.Label(seriesView, text="Title").grid(column=0, row=0, sticky="w")
SeriesTitle_Titletext = Text(seriesView, height=2, width=60)
SeriesTitle_Titletext.grid(column=1, row=0, sticky="nsew")

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

ttk.Label(seriesView, text="Expected Duration").grid(column=0, row=9, sticky="w")
seriesTitle_Durationtext = Text(seriesView, height=2, width=60)
seriesTitle_Durationtext.grid(column=1, row=9, sticky="nsew")
seriesTitle_Durationtext.insert("1.0", "hh:mm:ss")
add_save_button(seriesView, 10, store_series_form)

#Season Form
ttk.Label(seasonView, text="Title/Number").grid(column=0, row=0, sticky="w")
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
add_save_button(seasonView, 7, store_season_form)

#Episode Form
ttk.Label(episodeView, text="Title").grid(column=0, row=0, sticky="w")
episodeTitle_text = Text(episodeView, height=2, width=60)
episodeTitle_text.grid(column=1, row=0, sticky="nsew")

ttk.Label(episodeView, text="Short Title (25 chars)").grid(column=0, row=1, sticky="w")
episodeShortTitle_text = Text(episodeView, height=2, width=60, wrap="word")
episodeShortTitle_text.grid(column=1, row=1)

ttk.Label(episodeView, text="Sort Title").grid(column=0, row=2, sticky="w")
episodeSortTitle_text = Text(episodeView, height = 2, width=60)
episodeSortTitle_text.grid(column = 1, row = 2)

ttk.Label(episodeView, text="Long (1000 chars)").grid(column=0, row=3, sticky="w")
episodeLong_text = Text(episodeView, width=60, height=11, wrap="word")
episodeLong_text.grid(column=1, row=3)

ttk.Label(episodeView, text="Medium (250 chars)").grid(column=0, row=4, sticky="w")
episodeMedium_text = Text(episodeView, width=60, height=5, wrap="word")
episodeMedium_text.grid(column=1, row=4)

ttk.Label(episodeView, text="Short (99 chars)").grid(column=0, row=5, sticky="w")
episodeShort_text = Text(episodeView, width=60, height=4, wrap="word")
episodeShort_text.grid(column=1, row=5)

ttk.Label(episodeView, text="XShort (60 chars)").grid(column=0, row=6, sticky="w")
episodeXShort_text = Text(episodeView, width=60, height=3, wrap="word")
episodeXShort_text.grid(column=1, row=6)

ttk.Label(episodeView, text="Tiny (40 chars)").grid(column=0, row=7, sticky="w")
episodeTiny_text = Text(episodeView, width=60, height=2, wrap="word")
episodeTiny_text.grid(column=1, row=7)

ttk.Label(episodeView, text="SEO Keywords").grid(column=0, row=8, sticky="w")
episodeSEO_text = Text(episodeView, width=60, height=2, wrap="word")
episodeSEO_text.grid(column=1, row=8)

ttk.Label(episodeView, text="Expected Duration").grid(column=0, row=9, sticky="w")
episodeDuration_text = Text(episodeView, height=2, width=60)
episodeDuration_text.grid(column=1, row=9, sticky="nsew")
add_save_button(episodeView, 10, store_episode_form)

#Extra Form
ttk.Label(extraView, text="Title").grid(column=0, row=0, sticky="w")
extraTitle_text = Text(extraView, height=2, width=60)
extraTitle_text.grid(column=1, row=0, sticky="nsew")

ttk.Label(extraView, text="Short Title (25 chars)").grid(column=0, row=1, sticky="w")
extraShortTitle_text = Text(extraView, height=2, width=60, wrap="word")
extraShortTitle_text.grid(column=1, row=1)

ttk.Label(extraView, text="Sort Title").grid(column=0, row=2, sticky="w")
extraSortTitle_text = Text(extraView, height = 2, width=60)
extraSortTitle_text.grid(column = 1, row = 2)

ttk.Label(extraView, text="Long (1000 chars)").grid(column=0, row=3, sticky="w")
extraLong_text = Text(extraView, width=60, height=11, wrap="word")
extraLong_text.grid(column=1, row=3)

ttk.Label(extraView, text="Medium (250 chars)").grid(column=0, row=4, sticky="w")
extraMedium_text = Text(extraView, width=60, height=5, wrap="word")
extraMedium_text.grid(column=1, row=4)

ttk.Label(extraView, text="Short (99 chars)").grid(column=0, row=5, sticky="w")
extraShort_text = Text(extraView, width=60, height=4, wrap="word")
extraShort_text.grid(column=1, row=5)

ttk.Label(extraView, text="XShort (60 chars)").grid(column=0, row=6, sticky="w")
extraXShort_text = Text(extraView, width=60, height=3, wrap="word")
extraXShort_text.grid(column=1, row=6)

ttk.Label(extraView, text="Tiny (40 chars)").grid(column=0, row=7, sticky="w")
extraTiny_text = Text(extraView, width=60, height=2, wrap="word")
extraTiny_text.grid(column=1, row=7)

ttk.Label(extraView, text="Expected Duration").grid(column=0, row=8, sticky="w")
extraDuration_text = Text(extraView, height=2, width=60)
extraDuration_text.grid(column=1, row=8, sticky="nsew")
add_save_button(extraView, 9, store_extra_form)

root.mainloop()