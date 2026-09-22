# PYTHON-EXPERENTIAL-LEARNING
Hindi to english translator with python
WORKFLOW:

┌─────────────────────────┐
│         START           │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Display Translator     │
│       Title             │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Enter English Text      │
└────────────┬────────────┘
             ↓
        ┌──────────────┐
        │ Is input     │
        │   "exit"?    │
        └──────┬───────┘
          YES  │  NO
           ↓   ↓
┌───────────────────┐  ┌─────────────────────────┐
│ Display Thank You │  │ Is input empty?         │
│     Message       │  └────────────┬────────────┘
└─────────┬─────────┘               │
          │                    YES   │   NO
          │                     ↓    ↓
          │          ┌──────────────┐ ┌─────────────────────┐
          │          │ Display      │ │ Normalize Text      │
          │          │ Error Message│ │ strip() + lower()   │
          │          └──────┬───────┘ └──────────┬──────────┘
          │                 │                    ↓
          │                 │          ┌─────────────────────┐
          │                 │          │ Is complete phrase  │
          │                 │          │ in dictionary?      │
          │                 │          └──────────┬──────────┘
          │                 │                YES  │  NO
          │                 │                 ↓   ↓
          │                 │      ┌─────────────┐ ┌─────────────────┐
          │                 │      │ Get Hindi   │ │ Split Text into │
          │                 │      │ Translation │ │     Words       │
          │                 │      └──────┬──────┘ └────────┬────────┘
          │                 │             │                 ↓
          │                 │             │       ┌─────────────────┐
          │                 │             │       │ Process Each    │
          │                 │             │       │ Word using Loop │
          │                 │             │       └────────┬────────┘
          │                 │             │                ↓
          │                 │             │       ┌─────────────────┐
          │                 │             │       │ Is Word in     │
          │                 │             │       │ Dictionary?    │
          │                 │             │       └───────┬─────────┘
          │                 │             │          YES  │  NO
          │                 │             │           ↓   ↓
          │                 │             │   ┌──────────┐ ┌─────────────┐
          │                 │             │   │ Translate│ │ Keep Word   │
          │                 │             │   │   Word   │ │ Unchanged   │
          │                 │             │   └─────┬────┘ └──────┬──────┘
          │                 │             │         │             │
          │                 │             └─────────┴──────┬──────┘
          │                 │                              ↓
          │                 │                    ┌───────────────────┐
          │                 │                    │ Combine Translated│
          │                 │                    │      Words        │
          │                 │                    └─────────┬─────────┘
          │                 │                              │
          │                 └──────────────────────────────┘
          │                                ↓
          │                    ┌─────────────────────────┐
          │                    │ Display English +      │
          │                    │ Hindi Translation      │
          │                    └────────────┬────────────┘
          │                                 ↓
          │                    ┌─────────────────────────┐
          │                    │ Ask for Next Input      │
          │                    └────────────┬────────────┘
          │                                 │
          │                                 └──────→ Repeat
          │
          ↓
┌─────────────────────────┐
│          END            │
└─────────────────────────┘

 
TO RUN THIS PROJECT ON YOUR DEVICE OPEN THIS FILES IN YOUR DEVICE:
1.phase2.py
2.translation_history.json
3.vocab_export.csv
4.vocab_study_notes.md
