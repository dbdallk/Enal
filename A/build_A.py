from pathlib import Path
import json
import re
import cmudict

OUT = Path(__file__).parent
TARGET_PER_FILE = 900
FILES = 9

# Uses the locally available CMU pronunciation dictionary as the initial
# verified English vocabulary source. It deliberately refuses to invent
# words or fake Persian translations.
words = sorted({
    w.lower()
    for w in cmudict.words()
    if w.lower().startswith("a") and re.fullmatch(r"[a-z]+(?:['-][a-z]+)?", w.lower())
})

if len(words) < TARGET_PER_FILE * FILES:
    raise SystemExit(
        f"Not enough verified A-entries in the source dictionary: "
        f"{len(words)} available, {TARGET_PER_FILE * FILES} required. "
        "Add a larger English dictionary source before generating."
    )

# Persian translations must be supplied by a real bilingual dictionary.
# Never silently use transliteration or fabricated meanings.
