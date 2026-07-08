# SGS Academic Planner -- User Guide

## Running the Planner

1.  Open the project in VS Code.
2.  Open the integrated terminal.
3.  Run:

```{=html}
<!-- -->
```
    python main.py

## Knowledge Masters

Place all master Excel workbooks inside the `masters/` folder.

## Current Workflow

1.  Start the planner.
2.  Enter:
    -   Academic Year (coming soon)
    -   Division
    -   Level
    -   Term
3.  Generate timetable.
4.  Review the output.
5.  Commit changes to Git.
6.  Push to GitHub.

## Git Workflow

After making code changes:

    git add .
    git commit -m "Describe the feature"
    git push

## Folder Structure

-   config/ - Configuration
-   data/ - Loaders
-   models/ - Data models
-   scheduling/ - Scheduling logic
-   masters/ - Knowledge Masters
-   output/ - Generated timetables
-   docs/ - Project documentation
