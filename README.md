# Nearfleet_Docs

The repository containing all documentation for usage of the Nearfleet apps

## Repository Structure

Nearfleet documentation in this repository follows this exact structure:

```
Docs_Help (Copy)/                    # Root documentation folder
├── index.json                      # Root directory index (REQUIRED)
├── Carousel/                       # Featured articles for home carousel
│   ├── index.json                  # Carousel directory index (REQUIRED)
│   ├── Getting Started/
│   │   ├── index.json              # Article directory index (REQUIRED)
│   │   ├── info.json               # Article metadata (REQUIRED)
│   │   ├── Article.md              # Article content (REQUIRED)
│   │   ├── iconSmall.png           # Small icon (optional)
│   │   ├── iconBig.png             # Large icon (optional)
│   │   └── randomImage.png         # Additional images (optional)
│   └── New Features/
│       ├── index.json
│       ├── info.json
│       ├── Article.md
│       └── [icons and images]
├── Category1/                      # Regular category
│   ├── index.json                  # Category directory index (REQUIRED)
│   ├── smallIcon.png               # Category icon (recommended)
│   ├── Article1/
│   │   ├── index.json              # Article directory index (REQUIRED)
│   │   ├── info.json               # Article metadata (REQUIRED)
│   │   ├── Article.md              # Article content (REQUIRED)
│   │   └── [icons and images]
│   └── Article2/
│       ├── index.json
│       ├── info.json
│       ├── Article.md
│       └── [icons and images]
└── Category2/                      # Another category
    ├── index.json
    ├── smallIcon.png
    └── Article1/
        ├── index.json
        ├── info.json
        ├── Article.md
        └── [icons and images]
```

> An additional README.md file may be present in each article in order to allow for internal review from the GitHub repository.

## Required Files

### 1. Index Files (index.json) - REQUIRED for GitHub Pages

Every directory must contain an `index.json` file that lists its contents:

#### Root Directory Index (`Docs_Help (Copy)/index.json`):
```json
{
  "directories": ["Carousel", "Category1", "Category2"],
  "files": []
}
```

#### Category Directory Index (`Category1/index.json`):
```json
{
  "directories": ["Article1", "Article2"],
  "files": ["smallIcon.png"]
}
```

index.json is used in order to dynamically traverse the GitHub Pages deployment.

#### Article Directory Index (`Category1/Article1/index.json`):
```json
{
  "directories": [],
  "files": ["info.json", "Article.md", "iconSmall.png", "iconBig.png"]
}
```

### 2. Article Metadata (info.json) - REQUIRED

Each article must have an `info.json` file with the following structure:

```json
{
  "title": "Your Article Title",
  "date": "2024-01-15",
  "ratingNumerator": 45,
  "ratingDenominator": 50,
  "views": 1234,
  "relatedArticles": [
    "Category1/Article2",
    "Category2/Article1"
  ]
}
```

**Field Descriptions:**
- `title`: Display title for the article
- `date`: Publication date (YYYY-MM-DD format)
- `ratingNumerator`: Number of positive ratings
- `ratingDenominator`: Total number of ratings
- `views`: View count 
- `relatedArticles`: Array of related article paths (relative to root)

The user is shown the articles with most views first,

we utilize rating and feedback to create better documentation.

## About Github Pages

This repository is deployed automatically on push using GitHub Pages to prevent hitting GitHub's API rate limits.

## Content Guidelines

### Writing Articles

1. **Organized and Methodical**: Structure content with proper markdown headings
2. **Be Visual**: Provide screenshots where helpful
3. **Keep It Concise**: Break long content into digestible sections
4. **Use Lists**: Bullet points and numbered lists improve readability

### Related Articles

Link related articles using their folder paths relative to the root:

```json
"relatedArticles": [
  "Category1/Article2",
  "Carousel/Getting Started",
  "Category2/Advanced Features"
]
```

### Images and Icons

- **Category Icons**: Add `smallIcon.png` to category folders (48x48px recommended)
- **Article Icons**: Add `iconSmall.png` and `iconBig.png` to article folders
- **Content Images**: Reference images in markdown using direct URLs

## Common Issues & Solutions

### 404 Errors
- ✅ Ensure GitHub Pages is enabled
- ✅ Check that all directories have `index.json` files
- ✅ Verify file paths match exactly (case-sensitive)
- ✅ Wait a few minutes for GitHub Pages to update after changes

### Empty Categories/Articles
- ✅ Check that `info.json` files exist and are valid JSON
- ✅ Ensure `Article.md` files exist
- ✅ Verify `index.json` files list the correct files

### Articles Not Loading
- ✅ Check article folder structure
- ✅ Ensure `info.json` contains required fields
- ✅ Verify markdown file exists and is accessible in pages

### Related Articles Not Working
- ✅ Use correct relative paths in `relatedArticles` array
- ✅ Ensure referenced articles exist
- ✅ Check for typos in article paths