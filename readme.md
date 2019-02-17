# Taro

(work in progress)

For managing research (epubs, web articles, and papers).

Basic usage is that you drop in web article urls, paper PDFs, and/or epubs into a queue.

For PDFs, Taro will check if they are scanned or typeset. If scanned, OCR will be used to apply a searchable layer over the scan. If typeset, Taro will try to extract what metadata it can from the document.

For web articles, Taro will try to fetch the relevant content from the page as well as basic metadata (title, author) and save the page to an epub.

For epubs, Taro will load highlights and annotations from an e-reader (this is Kobo-focused for now).

A client web app will allow people to:

- browse/search the collection
- add missing or adjust metadata (where possible, metadata updates are saved as part of the file's metadata, rather than separately in a database)
- add notes (which are saved as markdown files)

---

Notes:

- use `whoosh` for full-text search, store index in `~/.config/taro/`
- also store taro main config there (describe epub/pdf library dirs and what not)
    - where to store pdfs
    - where to store epubs
    - where to store notes
- client views:
    - list readings
        - unread (default)
        - by author
        - by tag
        - search results
    - list tags
    - single reading (pdf/epub reader)
    - edit notes
    - edit metadata
- when a reading is added it should be marked as unread
- pdf reader w/ annotation and highlights (<https://agentcooper.github.io/react-pdf-highlighter/>)
- epub reader (<https://github.com/gerhardsletten/react-reader>, doesn't support highlights or annotations though by default)
    - maybe? <https://github.com/gerhardsletten/react-reader/issues/10>

- app api
    - get by tag/author/query/unread, paginated
    - get all tags
    - get single reading
        - get/update notes
        - get/update metadata
    - add reading
    - delete reading?
