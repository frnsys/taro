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
