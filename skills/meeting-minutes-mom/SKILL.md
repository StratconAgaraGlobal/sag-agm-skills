---
name: "meeting-minutes-mom"
description: "Turn a meeting source (Fireflies/Otter transcript, voice recording, or handwritten-note photos) into branded Minutes of Meeting (AGM or SAG brand). Use for any MoM, minutes, or meeting write-up request."
---

# Minutes of Meeting (MoM) → branded Word + PDF

The content structure comes from the SAG × Bitera minutes. The **look comes from a brand skill**: apply `agm-brand` for AGM meetings (default) or `sag-brand` for SAG meetings. Both brand skills are self-contained (fonts, logos, graphics and build code are bundled), so no design package has to be attached. Load the brand skill, then follow its "Set up" step (`python scripts/install_fonts.py`, which skips fonts already installed).

## 0. Inputs — handle each source type
- **Fireflies/Otter export (CSV/TXT/DOCX)**: the primary source. Speaker labels ("Speaker 1–5") are unreliable. Work out who is speaking from what people say ("This is Mr. Lu", "I'm from Surabaya"), and note wherever one label seems to cover two people.
- **Voice recording (m4a/mp3/wav)**: transcribe it if a speech model is available. If it isn't, say so and ask for the transcript. Always compare the audio's length with the transcript's length. If the transcript is much shorter, it starts mid-meeting, so flag the missing part.
- **Handwritten notes (photos/PDF scans)**: read the image directly. Mark illegible words as [illegible]. Never guess numbers.
- If several sources are given, use the transcript for content and the rest to fill gaps. Where they conflict, list both versions and flag them.

## 1. Ask before drafting (one AskUserQuestion, only what's unknown)
- Which brand/company is ours (AGM or SAG), and which side of the meeting is us. This decides the A vs B actions.
- Official names of counterparties, if the transcript garbles them.
- Output: Word + PDF (default), or PDF only.
If the user is away, assume AGM (Seafood edition) is our side, deliver Word + PDF, and list the assumptions in the Items to verify box.

## 2. Extraction pass (before writing)
Sort every substantive statement into one of these buckets:
- **Facts stated** — figures, fees, locations, with units exactly as said
- **Questions & answers** — who asked, the gist, and the position given
- **Our pitch / information we gave**
- **Commitments** — the source of the action items
- **Unanswered / deferred** items
- **Unclear items** — garbled names, numbers without units, conflicting figures
Skip small talk, audio checks, side chatter and private post-meeting talk unless it contains a commitment.

## 3. Structure, mapped to brand components (`BrandDoc` in the brand skill's `scripts/components.py`)
1. **Page 1:**
   - masthead (with the meeting date);
   - title block: eyebrow `MINUTES OF MEETING · <REF> · v0.9 DRAFT`, title, subtitle "… with **<counterparty>**";
   - 2 short intro paragraphs;
   - **tiles**: 5 headline figures;
   - **callout** "HEADLINE FOR MANAGEMENT" containing **Opportunity.** and **Immediate action.**
2. **Meeting details** band → **kv** (date, time, format, host, our attendees, minutes by, source) → **Participants** data_table (Organisation / Name / Role) + a note on speaker labels → **Meeting objective** bullets.
3. **Key discussion** band → one numbered **item** per question, with label "POSITION GIVEN" and the answer in the box. Unanswered questions start with **Not answered.** Close with a **callout** "KEY TAKEAWAY".
4. **Topic bands** (one per major subject) → data_table Parameter / Detail / Status (marks: TBC, TO DO) or kv. Add a callout "OBSERVATION" where there's an insight for us.
5. **Opportunity for <us>** → data_table Workstream / Provided / Relevance (HIGH / MEDIUM / LOW marks), plus a note that the ratings are a preliminary view.
6. **Considerations & risks** → data_table Consideration / Impact / Mitigation.
7. **Action items** band (subtitle "A = us · B = counterparty") → data_table No. / Action / Owner / Target / Status (OPEN / PENDING / DONE).
8. **Next steps** → immediate action, a numbered agenda for the next discussion, and a **roadmap** of 5 phases with phase 1 = this meeting (done).
9. **Review & approval** → corrections note + distribution → **sign_row** (Prepared / Reviewed / Approved) → callout "ITEMS TO VERIFY BEFORE ISSUE (v1.0)" → contact panel ("MINUTES PREPARED BY") → closing band.
Let sections flow. Force page breaks only after page 1, when a section would otherwise start in the last quarter of a page.

## 4. Rules (never break these)
- **Source-only.** Every fact must trace to the source. No outside facts, and no filling in names or numbers from general knowledge.
- **Flag rather than fix.** Garbled names, figures without units and conflicting numbers get marked "TBC" and listed in Items to verify. Explain caveated figures in a note.
- **Never print partial phone numbers, emails or IDs** heard in audio. Write "shared in chat" instead.
- Keep titles as used in the meeting (Bapak, Pak, Mr.) and Indonesian terms (akta, NIB) as they are.
- Only list actions that someone committed to or that clearly follow from the meeting. Use "TBC" for unknown owners and dates.
- Tone: neutral, third-person, management-ready, British spelling. Keep table cells to one or two short sentences.
- The first issue is **v0.9 Draft**, classified Internal. It becomes v1.0 after the user confirms the TBC items.
- Doc ref: `<AGM|SAG>-<COUNTERPARTY3>-MOM-<NNN>`. Files: `<AGM|SAG>_x_<Counterparty>_MoM_<DDMonYYYY>.docx/.pdf` in /mnt/user-data/outputs/.

## 5. Build and verify
- Build with the brand skill's `scripts/build_mom.py`, the worked example of exactly this structure (fictional sample content). Copy it, replace `CONTENT` with the real minutes, and run it from that skill's `scripts/` folder: `python build_mom.py --brand seafood --out minutes.docx` (`--brand seafood|marine` for AGM, `--brand sag` for SAG). Then `soffice --headless --convert-to pdf minutes.docx`. A rendered sample is in the brand skill's `assets/reference/`.
- Component helpers you will use: `masthead`, `title_block`, `intro`, `tiles`, `callout`, `band`, `kv`, `data_table` (status marks: TBC, TO DO, OPEN, PENDING, DONE, HIGH, MEDIUM, LOW), `item`, `bullets`, `numbered`, `roadmap`, `sign_row`, `contact_panel`, `closing`.
- Render all pages (`pdftoppm -r 40`) into a contact sheet and view it. Check for:
  - clipped callouts or tiles (shapes don't grow);
  - tiles wrapping to a second line;
  - bands orphaned at a page foot;
  - fonts other than Plus Jakarta Sans (`pdffonts`).
- Cross-check every number in the tiles and tables against the transcript.
- Reply in 1–2 lines, then list the TBC items the user must confirm.