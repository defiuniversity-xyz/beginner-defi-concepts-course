# Course Formatting Guide - Beginner DeFi Concepts

**Purpose:** This guide provides step-by-step instructions for replicating the formatting and structure of the Beginner DeFi Concepts course for other DeFi University courses.

---

## Overview

This guide documents the complete formatting standards, file organization, and integration patterns used in the Beginner DeFi Concepts course. Follow these patterns to ensure consistency across all courses.

---

## Course Structure Requirements

### Required Components Per Course

1. **12 Lessons** - Organized into 3 modules (4 lessons per module)
2. **12 Exercises** - One per lesson
3. **3 Quizzes** - One per module
4. **6 Interactive Tools** - Content-specific, embedded in relevant lessons
5. **Audio Files** - 12 podcast files (.m4a format)
6. **Video Files** - 12 overview videos (.mp4 format)
7. **Images** - ~3 images per lesson (36 total)

---

## Directory Structure

### Standard Course Directory Layout

```
{course-name}-ebook/
├── .gitbook.yaml                    # GitBook configuration
├── .gitignore                       # Git ignore rules
├── README.md                        # Course overview
├── content/
│   ├── README.md                    # Content index
│   ├── SUMMARY.md                   # GitBook table of contents
│   ├── lessons/                     # 12 lesson markdown files
│   ├── exercises/                   # 12 exercise markdown files
│   ├── quizzes/                     # 3 quiz markdown files
│   ├── interactives/                # 6 interactive HTML tools
│   ├── images/                      # Images organized by lesson
│   │   └── lessons/
│   │       └── lesson_{NN}/
│   ├── audio/                       # Audio files (local, uploaded to GCS)
│   └── video/                        # Video files (local, uploaded to GCS)
└── tools/                           # Python upload scripts
    ├── upload_images_to_gcs.py
    └── upload_media_to_gcs.py
```

---

## Lesson File Formatting

### 1. YAML Frontmatter

**Required at the top of every lesson file:**

```yaml
---
module: 1
lesson_number: 1
course: {course-key}
---
```

**Fields:**
- `module`: Module number (1, 2, or 3)
- `lesson_number`: Lesson number (1-12)
- `course`: Course identifier (e.g., `defi-concepts`, `investor-mindset`)

**Module Assignments:**
- Module 1: Lessons 1-4
- Module 2: Lessons 5-8
- Module 3: Lessons 9-12

### 2. Audio and Video Embeds

**Place immediately after YAML frontmatter, before lesson title:**

```markdown
{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-{NN}/audio/{url-encoded-filename}.m4a" %}

{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-{NN}/video/{url-encoded-filename}.mp4" %}
```

**Example:**
```markdown
{% embed url="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-01/audio/lesson1%20History_of_Blockchain_Before_Bitcoin.m4a" %}

{% embed url="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-01/video/lesson1%20The_History_of_Trust.mp4" %}
```

**Requirements:**
- Audio embed first, then video embed
- Empty line between embeds
- Empty line after video embed before lesson title
- **URL-encode filenames**: Spaces must be encoded as `%20`, commas as `%2C`, ampersands as `%26`, etc.
- Use GitBook's `{% embed url="..." %}` syntax (not HTML5 tags)
- Filenames should match exactly as uploaded to GCS, but URL-encoded in the embed

**URL Encoding Rules:**
- Space → `%20`
- Comma (`,`) → `%2C`
- Ampersand (`&`) → `%26`
- Underscore (`_`) → `_` (no encoding needed)
- Hyphen (`-`) → `-` (no encoding needed)

**Important:** GitBook requires URL-encoded filenames in embed URLs. The CORS configuration on the GCS bucket must allow GitBook domains for media playback to work.

### 3. Lesson Title

**Format:**
```markdown
# Lesson {N}: {Lesson Title}
```

**Example:**
```markdown
# Lesson 1: The Evolution of Money and Trust
```

### 4. Core Concept Section

**Required section after title:**

```markdown
## 🎯 Core Concept: {Concept Name}

{2-3 paragraph explanation of the core concept}
```

### 5. Content Sections

**Use H2 headings with emoji prefixes:**

```markdown
## 📚 {Section Title}

{Content...}

### {Subsection Title}

{Content...}
```

**Common section patterns:**
- `## 📚 The Historical Evolution: {Topic}`
- `## 📚 How It Works`
- `## 📚 {Concept} Fundamentals`
- `## 📚 Types of {Things}`

### 6. Image Integration

**Format:**
```markdown
![{Alt Text}](https://storage.googleapis.com/{bucket-name}/lessons/lesson_{NN}/{filename}.png)
```

**Requirements:**
- Empty line before and after image
- Descriptive alt text
- Use GCS URLs (not local paths)

**Image Naming Convention:**
- Format: `{course-prefix}{NN}_{##}_{description}.png`
- Example: `bdc01_01_money_evolution_timeline.png`
- Course prefix: `bdc` (Beginner DeFi Concepts), `im` (Investor Mindset), etc.

### 7. Interactive Tool Integration

**Place in relevant content sections:**

```markdown
### Interactive {Tool Name}

Use this interactive tool to {purpose}:

{% embed url="https://defi-university-app.web.app/interactives/{course-name}/{tool}.html?course={course-key}&id={tool-id}-lesson{number}&topic={Topic}" %}
```

**Requirements:**
- Use H3 heading (`###`)
- Include descriptive text before embed
- Use tracking parameters: `course`, `id`, `topic`
- Tool ID format: `{tool-id}-lesson{number}`

### 8. Key Takeaways Section

**Required at end of lesson:**

```markdown
## 🔑 Key Takeaways

1. **{Takeaway 1}**: {Explanation}
2. **{Takeaway 2}**: {Explanation}
3. **{Takeaway 3}**: {Explanation}
...
```

**Format:**
- Numbered list
- Bold key phrase followed by colon and explanation
- Typically 5-7 takeaways

### 9. Beginner's Corner (Optional)

**For complex concepts:**

```markdown
## 📖 Beginner's Corner

If you're new to these concepts:

- **Don't worry about**: {What to skip}
- **Focus on**: {What to understand}
- **Key insight**: {Main point}
```

### 10. Important Notes/Warnings

**Use when needed:**

```markdown
## ⚠️ Important Notes

- **{Note 1}**: {Explanation}
- **{Note 2}**: {Explanation}
```

**Or:**

```markdown
## ⚠️ Important Warnings

- **{Warning 1}**: {Explanation}
- **{Warning 2}**: {Explanation}
```

### 11. Next Lesson Reference

**At the very end:**

```markdown
---

**Next Lesson**: In Lesson {N}, we'll explore {topic}.
```

---

## Exercise File Formatting

### Standard Exercise Structure

```markdown
# Exercise {N}: {Exercise Title}

⏰ Time Investment: {X-Y} minutes
🎯 Goal: {Goal statement}

📚 Required Reading Integration
📖 Primary: Lesson {N}: {Lesson Title}

## 🔍 Phase 1: {Phase Name} ({X} minutes)

### {Section Title}

{Content...}

**{Question/Activity}:**
   - Your answer: _________________________________

## 🔍 Phase 2: {Phase Name} ({X} minutes)

{Content...}

## ✅ Completion Checklist

- [ ] {Task 1}
- [ ] {Task 2}
- [ ] {Task 3}
```

**Key Elements:**
- Time investment estimate
- Clear goal statement
- Reference to related lesson
- Phased structure (typically 2-3 phases)
- Completion checklist

---

## Quiz File Formatting

### Standard Quiz Structure

```markdown
# Module {N} Quiz: {Module Title}

Test your understanding of the core concepts from Module {N}, covering {topics}.

## Quiz Details

- **Questions**: {X} multiple choice
- **Passing Score**: 70%
- **Points**: 100 (+ 50 bonus for perfect score)
- **Topics Covered**: Lessons {X-Y}

## Instructions

1. Sign in to DeFi University to track your progress and earn points
2. Read each question carefully
3. Select the best answer from the options
4. Review your results and explanations

{% embed url="https://defi-university-app.web.app/quizzes/{course-key}/module-{NN}-quiz.html" %}
```

**Requirements:**
- Module number in title
- Clear quiz details
- Instructions for students
- GitBook embed to quiz HTML page

---

## Interactive Tool Integration

### Tool-to-Lesson Mapping

**Guidelines:**
- Embed tools in lessons where they're most relevant
- Typically 1-3 tools per lesson
- Tools should support lesson learning objectives
- Use descriptive section headings

**Example Integration:**

```markdown
## 📚 Understanding Gas Fees

Gas fees are the cost of executing transactions on the blockchain...

### Interactive Gas Fee Estimator

Use this interactive tool to estimate gas fees for different blockchain operations:

{% embed url="https://defi-university-app.web.app/interactives/beginner-defi-concepts/gas-fee-estimator.html?course=defi-concepts&id=gas-fee-estimator-lesson3&topic=Blockchain%20Infrastructure" %}
```

### Tool Naming Convention

**File names:** `{tool-name}.html` (kebab-case)

**Examples:**
- `defi-protocol-explorer.html`
- `wallet-security-checklist.html`
- `token-economics-calculator.html`

---

## Media Assets Setup

### Audio Files

**Requirements:**
- Format: `.m4a`
- Naming: `lesson{N} {Title}.m4a`
- Location: `content/audio/` (local)
- Upload to: GCS bucket `{course-name}-gitbook-media/lesson-{NN}/audio/`

**Upload Process:**
1. Place files in `content/audio/`
2. Run `tools/upload_media_to_gcs.py`
3. Files uploaded to: `lesson-{NN}/audio/{filename}.m4a`
4. Use generated URLs in lesson embeds with **URL encoding**

**Embed Format:**
```markdown
{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-{NN}/audio/{url-encoded-filename}.m4a" %}
```

**Important:** Filenames with spaces, commas, or special characters must be URL-encoded in the embed URL:
- Space → `%20`
- Comma (`,`) → `%2C`
- Ampersand (`&`) → `%26`

### Video Files

**Requirements:**
- Format: `.mp4`
- Naming: `lesson{N} {Title}.mp4`
- Location: `content/video/` (local)
- Upload to: GCS bucket `{course-name}-gitbook-media/lesson-{NN}/video/`

**Upload Process:**
1. Place files in `content/video/`
2. Run `tools/upload_media_to_gcs.py`
3. Files uploaded to: `lesson-{NN}/video/{filename}.mp4`
4. Use generated URLs in lesson embeds with **URL encoding**

**Embed Format:**
```markdown
{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-{NN}/video/{url-encoded-filename}.mp4" %}
```

**Important:** Filenames with spaces, commas, or special characters must be URL-encoded in the embed URL:
- Space → `%20`
- Comma (`,`) → `%2C`
- Ampersand (`&`) → `%26`

### CORS Configuration (Required for GitBook)

**Critical:** The GCS bucket must have CORS configured to allow GitBook domains to access media files.

**Configuration File:** `tools/cors_config.json`

**Apply CORS using gcloud CLI:**
```bash
gcloud storage buckets update gs://{bucket-name} --cors-file=tools/cors_config.json
```

**Or use the Python script:**
```bash
cd tools
python3 configure_cors.py
```

**CORS Configuration allows:**
- GitBook domains (`app.gitbook.com`, `*.gitbook.com`, `*.gitbook.io`)
- GET, HEAD, OPTIONS methods
- Required headers for media streaming

**Without CORS:** Audio and video files will not play in GitBook, even if URLs are correct.

### Images

**Requirements:**
- Format: `.png` (preferred) or `.jpg`
- Naming: `{prefix}{NN}_{##}_{description}.png`
- Location: `content/images/lessons/lesson_{NN}/`
- Upload to: GCS bucket `{course-name}-gitbook-images/lessons/lesson_{NN}/`

**Naming Convention:**
- Prefix: Course identifier (e.g., `bdc` for Beginner DeFi Concepts)
- Lesson number: `{NN}` (01-12)
- Sequence: `{##}` (01, 02, 03...)
- Description: Short descriptive name (kebab-case)

**Example:** `bdc07_02_constant_product_formula_visualization.png`

---

## Google Cloud Storage Setup

### Bucket Creation

**For each course, create two buckets:**

1. **Media Bucket** (audio/video):
   ```bash
   gcloud storage buckets create gs://{course-name}-gitbook-media \
     --project=defi-university \
     --location=US \
     --uniform-bucket-level-access
   
   gcloud storage buckets add-iam-policy-binding gs://{course-name}-gitbook-media \
     --member=allUsers \
     --role=roles/storage.objectViewer \
     --project=defi-university
   ```

2. **Images Bucket** (images):
   ```bash
   gcloud storage buckets create gs://{course-name}-gitbook-images \
     --project=defi-university \
     --location=US \
     --uniform-bucket-level-access
   
   gcloud storage buckets add-iam-policy-binding gs://{course-name}-gitbook-images \
     --member=allUsers \
     --role=roles/storage.objectViewer \
     --project=defi-university
   ```

### Service Account Permissions

**Grant service account access:**

```bash
gcloud storage buckets add-iam-policy-binding gs://{bucket-name} \
  --member=serviceAccount:defi-university-automation@defi-university.iam.gserviceaccount.com \
  --role=roles/storage.objectAdmin \
  --project=defi-university

gcloud storage buckets add-iam-policy-binding gs://{bucket-name} \
  --member=serviceAccount:defi-university-automation@defi-university.iam.gserviceaccount.com \
  --role=roles/storage.legacyBucketWriter \
  --project=defi-university
```

### CORS Configuration (Required)

**After creating buckets, configure CORS to allow GitBook access:**

1. **Create CORS config file** (`tools/cors_config.json`):
```json
[
  {
    "origin": [
      "https://app.gitbook.com",
      "https://*.gitbook.com",
      "https://*.gitbook.io",
      "https://gitbook.com",
      "*"
    ],
    "method": ["GET", "HEAD", "OPTIONS"],
    "responseHeader": [
      "Content-Type",
      "Content-Length",
      "Content-Range",
      "Accept-Ranges",
      "Content-Disposition",
      "Access-Control-Allow-Origin",
      "Access-Control-Allow-Methods",
      "Access-Control-Allow-Headers",
      "Access-Control-Max-Age"
    ],
    "maxAgeSeconds": 3600
  }
]
```

2. **Apply CORS to media bucket:**
```bash
gcloud storage buckets update gs://{course-name}-gitbook-media --cors-file=tools/cors_config.json
```

**Note:** CORS is only needed for the media bucket (audio/video), not the images bucket.

**Verification:**
```bash
curl -I -H "Origin: https://app.gitbook.com" "https://storage.googleapis.com/{bucket-name}/lesson-01/audio/{file}.m4a" | grep -i "access-control"
```

Should return: `access-control-allow-origin: *`

---

## Upload Scripts

### Media Upload Script Template

**File:** `tools/upload_media_to_gcs.py`

**Key Configuration:**
```python
BUCKET_NAME = os.getenv('GCS_BUCKET_NAME', '{course-name}-gitbook-media')
PROJECT_ID = 'defi-university'
```

**Features:**
- Extracts lesson number from filename
- Organizes files: `lesson-{NN}/audio/` and `lesson-{NN}/video/`
- Sets correct MIME types (audio/mp4 for .m4a, video/mp4 for .mp4)
- Generates GitBook embed syntax
- Prints upload summary

### Image Upload Script Template

**File:** `tools/upload_images_to_gcs.py`

**Key Configuration:**
```python
BUCKET_NAME = os.getenv('GCS_BUCKET_NAME', '{course-name}-gitbook-images')
PROJECT_ID = 'defi-university'
```

**Features:**
- Uploads from `content/images/lessons/`
- Preserves directory structure
- Sets image MIME types
- Generates markdown image syntax

---

## GitBook Configuration

### .gitbook.yaml Template

```yaml
# GitBook Configuration
root: ./content

structure:
  readme: README.md
  summary: SUMMARY.md

# Redirects (add as needed)
redirects: {}

# GitBook metadata
metadata:
  title: "DeFi University - {Course Name}"
  description: "{Course description}"

# Variables for consistent branding
variables:
  university_name: "DeFi University"
  course_name: "{Course Name}"
```

---

## Account Hub Integration

### Backend API Requirements

**Required Endpoints:**

1. **POST /api/progress/exercise**
   - Tracks exercise completion
   - Awards 15 points
   - Checks module completion

2. **POST /api/progress/lesson**
   - Tracks lesson completion
   - Awards 50 points
   - Checks module completion

3. **POST /api/progress/quiz**
   - Tracks quiz completion
   - Awards 100 points (+50 for perfect score)
   - Checks module completion

4. **GET /api/progress/me**
   - Returns module-level progress
   - Includes `exercisesCompleted` array
   - Includes `modulesCompleted` array
   - Includes `moduleProgress` object

5. **GET /api/progress/points**
   - Returns exercise points
   - Returns lesson points
   - Returns module bonuses
   - Per-course breakdown

### Frontend Display Requirements

**Points Display:**
- Total Points
- Quiz Points
- Lesson Points
- Exercise Points
- Interaction Points
- Module Bonuses
- Bonus Points

**Module Progress:**
- Module completion badges (1, 2, 3)
- Lesson/exercise counts per module
- Module completion tooltips

---

## Naming Conventions

### File Naming

**Lessons:**
- Format: `lesson-{NN}-{kebab-case-title}.md`
- Example: `lesson-01-the-evolution-of-money-and-trust.md`

**Exercises:**
- Format: `exercise-{NN}-{kebab-case-title}.md`
- Example: `exercise-01-historical-foundations-assessment.md`

**Quizzes:**
- Format: `quiz-module-{NN}.md`
- Example: `quiz-module-01.md`

**Interactive Tools:**
- Format: `{tool-name}.html` (kebab-case)
- Example: `defi-protocol-explorer.html`

**Images:**
- Format: `{prefix}{NN}_{##}_{description}.png`
- Example: `bdc07_02_constant_product_formula_visualization.png`

**Audio:**
- Format: `lesson{N} {Title}.m4a`
- Example: `lesson1 History_of_Blockchain_Before_Bitcoin.m4a`

**Video:**
- Format: `lesson{N} {Title}.mp4`
- Example: `lesson1 The_History_of_Trust.mp4`

---

## Content Standards

### Writing Style

- **Clear and accessible:** Write for beginners but don't oversimplify
- **Structured:** Use consistent section headings and formatting
- **Visual:** Include images, diagrams, and interactive elements
- **Actionable:** Provide exercises and practical applications

### Section Headings

**Standard hierarchy:**
- H1: Lesson title (only one per lesson)
- H2: Major sections (🎯 Core Concept, 📚 Content, 🔑 Key Takeaways)
- H3: Subsections and interactive tool sections
- H4: Sub-subsections (rarely used)

### Emoji Usage

**Standard emojis for sections:**
- 🎯 Core Concept
- 📚 Content sections
- 🔑 Key Takeaways
- 📖 Beginner's Corner
- ⚠️ Important Notes/Warnings
- 🎮 Interactive sections

---

## Step-by-Step Course Setup

### Phase 1: Content Creation

1. **Create directory structure**
   ```bash
   mkdir -p {course-name}-ebook/content/{lessons,exercises,quizzes,interactives,images/lessons,audio,video}
   mkdir -p {course-name}-ebook/tools
   ```

2. **Create .gitbook.yaml** (use template above)

3. **Write 12 lessons** (follow lesson formatting guide)

4. **Write 12 exercises** (follow exercise formatting guide)

5. **Write 3 quizzes** (follow quiz formatting guide)

### Phase 2: Media Assets

1. **Prepare audio files**
   - Record/create 12 podcast files
   - Name: `lesson{N} {Title}.m4a`
   - Place in `content/audio/`

2. **Prepare video files**
   - Create 12 overview videos
   - Name: `lesson{N} {Title}.mp4`
   - Place in `content/video/`

3. **Prepare images**
   - Create ~3 images per lesson (36 total)
   - Name: `{prefix}{NN}_{##}_{description}.png`
   - Place in `content/images/lessons/lesson_{NN}/`

### Phase 3: Interactive Tools

1. **Create 6 interactive tools**
   - HTML files with functionality
   - Place in `content/interactives/`

2. **Embed tools in lessons**
   - Identify relevant lessons
   - Add tool embeds with tracking parameters

### Phase 4: Module Organization

1. **Add YAML frontmatter to all lessons**
   - Module number (1, 2, or 3)
   - Lesson number (1-12)
   - Course identifier

2. **Verify module structure**
   - Module 1: Lessons 1-4
   - Module 2: Lessons 5-8
   - Module 3: Lessons 9-12

### Phase 5: Google Cloud Storage

1. **Create GCS buckets**
   - Media bucket: `{course-name}-gitbook-media`
   - Images bucket: `{course-name}-gitbook-images`

2. **Create upload scripts**
   - Copy and customize `upload_media_to_gcs.py`
   - Copy and customize `upload_images_to_gcs.py`

3. **Upload all media**
   - Run media upload script
   - Run images upload script
   - Verify all URLs accessible

4. **Update lesson files**
   - Replace local paths with GCS URLs
   - Add audio/video embeds to all lessons

### Phase 6: Account Hub Integration

1. **Backend API**
   - Exercise endpoint already implemented (works for all courses)
   - Module tracking already implemented (works for all courses)
   - Points API already updated (works for all courses)

2. **Frontend Display**
   - Already updated to show all point categories
   - Already shows module progress indicators

**Note:** Account Hub integration is course-agnostic and works automatically for all courses.

---

## Quality Checklist

Before pushing to GitHub, verify:

### Content
- [ ] All 12 lessons have YAML frontmatter
- [ ] All 12 lessons have audio embeds
- [ ] All 12 lessons have video embeds
- [ ] All 12 exercises exist and are formatted
- [ ] All 3 quizzes exist and are formatted
- [ ] All 6 interactive tools present
- [ ] Tools embedded in relevant lessons

### Media
- [ ] All audio files uploaded to GCS
- [ ] All video files uploaded to GCS
- [ ] All images uploaded to GCS
- [ ] All GCS URLs accessible
- [ ] All embeds use correct URLs

### Structure
- [ ] Directory structure follows standard
- [ ] Naming conventions consistent
- [ ] GitBook configuration present
- [ ] Module organization correct (3 modules, 4 lessons each)

### Integration
- [ ] Account Hub tracking works (automatic)
- [ ] Points system configured correctly
- [ ] Module progress tracking works (automatic)

---

## Example: Complete Lesson Template

```markdown
---
module: 1
lesson_number: 1
course: {course-key}
---

{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-01/audio/lesson1%20{Title}.m4a" %}

{% embed url="https://storage.googleapis.com/{bucket-name}/lesson-01/video/lesson1%20{Title}.mp4" %}

# Lesson 1: {Lesson Title}

## 🎯 Core Concept: {Core Concept Name}

{2-3 paragraph explanation of the core concept that students must understand.}

## 📚 {Main Content Section}

{Detailed content explaining the concept...}

![{Image Alt Text}](https://storage.googleapis.com/{bucket-name}/lessons/lesson_01/{image-filename}.png)

### {Subsection Title}

{More detailed content...}

### Interactive {Tool Name}

Use this interactive tool to {purpose}:

{% embed url="https://defi-university-app.web.app/interactives/{course-name}/{tool}.html?course={course-key}&id={tool-id}-lesson1&topic={Topic}" %}

## 🔑 Key Takeaways

1. **{Takeaway 1}**: {Explanation}
2. **{Takeaway 2}**: {Explanation}
3. **{Takeaway 3}**: {Explanation}
4. **{Takeaway 4}**: {Explanation}
5. **{Takeaway 5}**: {Explanation}

## 📖 Beginner's Corner

If you're new to these concepts:

- **Don't worry about**: {What to skip}
- **Focus on**: {What to understand}
- **Key insight**: {Main point}

## ⚠️ Important Notes

- **{Note 1}**: {Explanation}
- **{Note 2}**: {Explanation}

---

**Next Lesson**: In Lesson 2, we'll explore {next topic}.
```

---

## Quick Reference

### GitBook Embed Syntax

**Audio:**
```markdown
{% embed url="https://storage.googleapis.com/{bucket}/lesson-{NN}/audio/{filename}.m4a" %}
```

**Video:**
```markdown
{% embed url="https://storage.googleapis.com/{bucket}/lesson-{NN}/video/{filename}.mp4" %}
```

**Interactive Tool:**
```markdown
{% embed url="https://defi-university-app.web.app/interactives/{course}/{tool}.html?course={key}&id={id}&topic={Topic}" %}
```

**Image:**
```markdown
![{Alt Text}](https://storage.googleapis.com/{bucket}/lessons/lesson_{NN}/{filename}.png)
```

### Module Assignments

- **Module 1:** Lessons 1-4 + Exercise 1-4 + Quiz Module 1
- **Module 2:** Lessons 5-8 + Exercise 5-8 + Quiz Module 2
- **Module 3:** Lessons 9-12 + Exercise 9-12 + Quiz Module 3

### Points Allocation

- Lesson: 50 points
- Exercise: 15 points
- Quiz: 100 points (+50 for perfect)
- Interactive Tool: 25 points
- Module Completion: 50 bonus points
- Course Completion: 500 bonus points

---

## Support Files

### .gitignore Template

```
# Media files (stored in Google Cloud Storage)
content/audio/
content/video/

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~

# Python (if tools are added later)
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
```

---

## Summary

This guide provides complete formatting standards for DeFi University courses. Follow these patterns to ensure:

- Consistent structure across all courses
- Proper Account Hub tracking integration
- Standardized media asset management
- Professional presentation in GitBook
- Easy maintenance and updates

**Key Principles:**
1. Always use YAML frontmatter with module metadata
2. Always include audio and video embeds at lesson top
3. Always organize content into clear sections with emoji prefixes
4. Always embed interactive tools where relevant
5. Always upload media to GCS before adding embeds
6. Always follow naming conventions consistently
