#! /usr/bin/env python3

import json
import os

import pandas as pd
from plotnine import (
    aes,
    after_stat,
    geom_histogram,
    ggplot,
    labs,
    save_as_pdf_pages,
    theme_minimal,
)

SCRIPT_DIR = os.path.dirname(__file__)
JSON_FILE = open(os.path.join(SCRIPT_DIR, "symbols-ubuntu.json"), "r")

# Load JSON data into a Python dictionary
data_dict = json.load(JSON_FILE)

# Convert to DataFrame
df = pd.DataFrame(list(data_dict.items()), columns=["File", "Symbols"])

# Create plot
plot = (
    ggplot(df, aes(x="Symbols", y=after_stat("ncount")))
    + geom_histogram(bins=100, fill="skyblue", color="black", alpha=0.7)
    + labs(title="", x="Number of Symbols", y="Normalized Count")
    + theme_minimal()
)

save_as_pdf_pages([plot])
