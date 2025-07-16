import pandas as pd
from collections import Counter

# ====================================================
# STEP 1: Define configuration
# ====================================================
essential_cols = [
    "AUTHORS", "ARTICLE TITLE", "SOURCE TITLE", "PUBLICATION DATE",
    "PUBLICATION YEAR", "ABSTRACT", "DOI", "DOCUMENT TYPE"
]

keywords = [
    'laundry', 'washing machine', 'biodegradable', 'filter',
    'low-shedding', 'microfiber', 'microfibre', 'innovation', 'textile'
]

def extract_keywords(text, keyword_list):
    """Extract which keywords were found in the text"""
    text = str(text).lower()
    found = [kw for kw in keyword_list if kw in text]
    return found

# ====================================================
# STEP 2: Create data loading function
# ====================================================
def load_and_preview(filepath, name):
    """Load Excel file and preview sample data"""
    try:
        print(f"\n=== Loading {name} ===")
        df = pd.read_excel(filepath)

        # Standardize column names to UPPERCASE
        df.columns = df.columns.str.strip().str.upper()

        # Initialize missing essential columns
        for col in essential_cols:
            if col not in df.columns:
                df[col] = ""

        # Create combined text field for keyword extraction
        df['SEARCH_TEXT'] = df['ARTICLE TITLE'].fillna('') + " " + df['ABSTRACT'].fillna('')

        # Select only the essential columns plus our search text
        df = df[essential_cols + ['SEARCH_TEXT']]

        # Preview data
        print(f"\nColumns ({len(df.columns)}):\n{df.columns.tolist()}")
        print("\nSample data (first 2 rows):")
        print(df.head(2).to_string())

        return df
    except Exception as e:
        print(f"Error loading {name}: {str(e)}")
        return pd.DataFrame(columns=essential_cols + ['SEARCH_TEXT'])

# ====================================================
# STEP 3: Load and preview all files
# ====================================================
print("="*50)
print("BEGINNING DATA LOADING PROCESS")
print("="*50)

wos = load_and_preview('wos1.xls', "Web of Science 1")
wos2 = load_and_preview('wos2.xls', "Web of Science 2")
medline = load_and_preview('medline.xls', "Medline")
cscd = load_and_preview('chinesecsd.xls', "Chinese CSD")

# ====================================================
# STEP 4: Combine datasets
# ====================================================
print("\n" + "="*50)
print("COMBINING DATASETS")
print("="*50)

df = pd.concat([wos, wos2, medline, cscd], ignore_index=True)
print(f"\nCombined dataset shape: {df.shape}")

# ====================================================
# STEP 5: Clean and deduplicate
# ====================================================
print("\n" + "="*50)
print("DATA CLEANING AND DEDUPLICATION")
print("="*50)

df['DOI'] = df['DOI'].fillna('').astype(str).str.strip().str.lower()
df['ARTICLE TITLE'] = df['ARTICLE TITLE'].astype(str).str.strip().str.lower()

print("\nDuplicate removal strategy: DOI + Article Title")

df_cleaned = df.copy()

has_doi = df_cleaned['DOI'] != ''
df_with_doi = df_cleaned[has_doi].drop_duplicates(subset='DOI', keep='first')
df_without_doi = df_cleaned[~has_doi].drop_duplicates(subset='ARTICLE TITLE', keep='first')
df_cleaned = pd.concat([df_with_doi, df_without_doi], ignore_index=True)

print(f"\nShape after duplicate removal: {df_cleaned.shape}")
print(f"Duplicates removed: {len(df) - len(df_cleaned)}")

# ====================================================
# STEP 6: Keyword filtering
# ====================================================
print("\n" + "="*50)
print("KEYWORD FILTERING")
print("="*50)

df_screened = df_cleaned.copy()
df_screened['SEARCH_TEXT'] = df_screened['SEARCH_TEXT'].str.lower()

keyword_mask = df_screened['SEARCH_TEXT'].apply(lambda x: any(k in str(x) for k in keywords))
df_screened = df_screened[keyword_mask].copy()

df_screened['EXTRACTED_KEYWORDS'] = df_screened['SEARCH_TEXT'].apply(
    lambda x: extract_keywords(x, keywords)
)

print(f"\nShape after keyword filtering: {df_screened.shape}")
print(f"Records removed by keyword filter: {len(df_cleaned) - len(df_screened)}")

# ====================================================
# STEP 7: Save results
# ====================================================
print("\n" + "="*50)
print("SAVING RESULTS")
print("="*50)

# Restore title case for output
df_screened.columns = df_screened.columns.str.title()

output_csv = "screened_literature.csv"
output_excel = "screened_for_vosviewer.xlsx"

df_screened.to_csv(output_csv, index=False)
df_screened.to_excel(output_excel, index=False)

print(f"\nSaved files:")
print(f"- CSV: {output_csv}")
print(f"- Excel: {output_excel}")

# ====================================================
# STEP 8: Generate reports
# ====================================================
print("\n" + "="*50)
print("GENERATING REPORTS")
print("="*50)

print("\n=== DOI Usage Report ===")
doi_counts = (df_screened['Doi'] != '').value_counts()
print(f"Records with valid DOI: {doi_counts.get(True, 0)}")
print(f"Records without DOI: {doi_counts.get(False, 0)}")

print("\n=== Publication Year Distribution ===")
year_counts = df_screened['Publication Year'].value_counts().sort_index()
print(year_counts.to_string())

print("\n=== Keyword Analysis ===")
all_keywords = [kw for sublist in df_screened['Extracted_Keywords'] for kw in sublist]
keyword_counts = Counter(all_keywords)

print(f"Total keyword occurrences: {len(all_keywords)}")
print(f"Unique keywords found: {len(keyword_counts)}")
print("\nTop 20 keyword frequencies:")
for kw, count in keyword_counts.most_common(20):
    print(f"- {kw}: {count}")

print("\n" + "="*50)
print("PROCESSING COMPLETE!")
print("="*50)
