# Markdowna XBlock

## Installation

1. Clone this repo.
2. `sudo -u edxapp /edx/bin/pip.edxapp install "path/to/this/xblock"`.
3. Open your course from LMS, open `settings -> Advanced Settings` in the menu, then  add `"markdowna"` to the `Advanced Module List` .



## Supported Markdown Features

Basically it is what markdown-it without any plugins supported:

* Headers (Setext-style)
* Horizontal
* Bold, italic and strikethrough
* Blockquote (nesting)
* Lists (ordered and unordered)
* Code fence and code span
* Github-style table
* Link
* Image (unresizable)



## YAML Front Matter

```
display-name: Markdown # The title of that Component
```



## Known Issues

* The page will reload after saving modified content.



## Todo list

* Adding some plugins of markdown-it and support customization of that.



## Credits

projects used by this XBlock:

* SimpleMDE Markdown Editor
  * A simple, beautiful, and embeddable JavaScript Markdown editor. Delightful editing for beginners and experts alike. Features built-in autosaving and spell checking.
  * <https://simplemde.com>
  * The MIT License
* markdown-it
  * Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed
  *  <https://markdown-it.github.io/>
  * The MIT License
* github-markdown-css
  * The minimal amount of CSS to replicate the GitHub Markdown style
  * <https://github.com/sindresorhus/github-markdown-css>
  * The MIT License
* markdown-it-front-matter
  * Plugin to process front matter container for markdown-it markdown parser
  * <https://github.com/craigdmckenna/markdown-it-front-matter>
  * The MIT License
* PyYAML
  * <http://pyyaml.org/>
  * The MIT License