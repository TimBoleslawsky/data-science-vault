# Uni Vault AI Assistant Instructions

This is an Obsidian-based knowledge management system for university Data Science studies. Follow these patterns and conventions when working with this vault.

## Architecture Overview

- **Atlas/**: Maps of Content (MOCs) that serve as navigation hubs. `Data Science.md` is the primary MOC organizing all data science knowledge
- **Notes/**: Individual concept notes using bidirectional linking `[[Note Name]]` for knowledge graph connections
- **Projects/**: Practical implementations with code (Python scripts, Jupyter notebooks, R code, PDFs)
- **Literature/**: Academic sources and references
- **Images/**: Visual assets and diagrams

## Content Organization Patterns

### Note Structure
- Start with clear definition/purpose statement
- Use hierarchical headings (##, ###) for logical organization
- Employ bidirectional links `[[Topic Name]]` extensively to create knowledge graph connections
- Include practical examples and code snippets in triple backticks with language specification

### Linking Conventions
- Link related concepts bidirectionally: `[[Data Science, a Definition]]`, `[[Mathematical Modeling in Data Science]]`
- Reference specific sections using pipe syntax when needed: `[[Data Science#Theory behind Machine and Deep Learning|Machine Learning]]`
- Create topic clusters through consistent linking (e.g., all ML algorithms link back to parent concepts)

### Academic Focus Areas
- **Core Data Science**: From theory to implementation, emphasizing both mathematical foundations and practical applications
- **Machine Learning Pipeline**: Data preprocessing → model selection → evaluation → deployment patterns
- **Statistical Methods**: Bayesian approaches (following McElreath's Statistical Rethinking), hypothesis testing, inference
- **Programming Implementation**: Python-centric with pandas, scikit-learn, neural networks; some R for specialized analysis

## Project Integration

When working with `/Projects/` code:
- Python projects use standard data science stack (pandas, scikit-learn, matplotlib, spacy)
- Code includes both educational examples and practical implementations
- Documentation emphasizes learning objectives and conceptual understanding
- Link project work back to theoretical notes using Obsidian links

## Obsidian-Specific Features

- **Plugins enabled**: TOC, symbols-prettifier, language tool, table-to-csv, VSCode editor, Excalidraw, linter
- **Math notation**: Use LaTeX syntax `$formula$` for inline and `$$formula$$` for block equations
- **Visual diagrams**: Create using Excalidraw plugin for conceptual diagrams
- **Cross-references**: Leverage graph view connections - always consider how new content connects to existing knowledge

## Content Creation Guidelines

- Maintain academic rigor while ensuring practical applicability
- Include both theoretical foundations and implementation examples
- Reference course materials and academic sources appropriately
- Create comprehensive coverage from basic concepts to advanced applications
- Emphasize understanding over memorization through conceptual linking

When adding new content, always consider: How does this connect to existing knowledge? What practical applications demonstrate this concept? How does this fit into the broader Data Science learning journey?
