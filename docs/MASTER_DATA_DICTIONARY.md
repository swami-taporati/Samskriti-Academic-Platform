# SGS Academic Planner -- Master Data Dictionary

## Purpose

This document is the central reference for every Knowledge Master
workbook used by the Academic Planner.

------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------
  Workbook                             Purpose                 Status      Used By
  ------------------------------------ ------------------- --------------- -----------------
  SGS_Knowledge_Catalog                Index of all              ✅        Loader
                                       Knowledge Masters                   

  SGS_Master_LearningActivities        Defines all               ✅        Scheduler
                                       learning activities                 

  SGS_Master_CurriculumAllocation      Number of sessions        ✅        Scheduler
                                       required for each                   
                                       activity                            

  SGS_Master_GroupLearningProfiles     Group/division            ✅        Planner
                                       configuration                       

  SGS_Master_DailyEventStructure       Daily schedule            ✅        Planner
                                       templates and                       
                                       learning slots                      

  SGS_Master_GlobalSchedulingRules     Rules applicable          ✅        Validation
                                       across all groups                   

  SGS_Master_ActivitySchedulingRules   Activity-specific         ✅        Scheduler
                                       scheduling rules                    

  SGS_Master_People                    Teachers and staff        ✅        Teacher
                                                                           Allocation

  SGS_Master_PeopleCompetencies        Teacher                   ✅        Teacher
                                       competencies                        Allocation

  SGS_Master_PeopleResponsibilities    Teacher                   ✅        Teacher
                                       responsibilities                    Allocation

  SGS_Master_LearningSpaces            Rooms and learning        ✅        Space Allocation
                                       spaces                              

  SGS_Master_StudentSubjectChoices     Subject selections        ✅        Future
                                       for students                        

  SGS_Master_Lookups                   Common lookup             ✅        Application
                                       values                              

  SGS_Master_TimetableTemplate         Prototype only            ⚠️        Temporary
                                       (planned to be                      
                                       generated                           
                                       automatically)                      
  ------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Naming Convention

Every master workbook should follow:

    SGS_Master_<Name>_v<Version>.xlsx

Example:

    SGS_Master_CurriculumAllocation_v1.0.0.xlsx

------------------------------------------------------------------------

## Source of Truth

Each concept must have only one source of truth.

-   Activities → Learning Activities
-   Required Sessions → Curriculum Allocation
-   Daily Timetable Structure → Daily Event Structure
-   Teachers → People
-   Teacher Skills → People Competencies
-   Learning Spaces → Learning Spaces

------------------------------------------------------------------------

## Future Master Workbooks

Planned additions:

-   Assessment Framework
-   Student Profiles
-   Attendance
-   Academic Calendar
-   Events & Festivals
-   Examinations
-   Resource Library

------------------------------------------------------------------------

## Maintenance Rules

1.  Do not duplicate master data.
2.  Update this document whenever a master workbook is added, removed,
    renamed, or its purpose changes.
3.  Every planner module should reference this dictionary before
    introducing a new master workbook.
