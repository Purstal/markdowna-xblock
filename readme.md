# Markdowna XBlock

## How to use

1. Install this XBlock

   * either

     1. Clone this repo.
     2. `sudo -u edxapp /edx/bin/pip.edxapp install "path/to/this/xblock"`.

   * or

     `sudo -u edxapp /edx/bin/pip.edxapp install git+https://github.com/Purstal/markdowna-xblock.git`

2. Restart openedx service.

   ```
   sudo /edx/bin/supervisorctl restart edxapp:
   sudo /edx/bin/supervisorctl restart edxapp_worker:
   ```

3. Open your course from LMS, open `settings -> Advanced Settings` in the menu, then  add `"markdowna"` to the `Advanced Module List` .

4. You will find this xblock in Category "Advanced".

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


## Front Matter 

```
display-name: Hello World # The display name for this component.
```

## Known Issues

* The page will reload after saving modified content.


## Todo list

* Adding some plugins of markdown-it and support customization of that.


## Screenshots

![studio_view](screenshots/studio_view.png)

![author_view](screenshots/author_view.png)

![student_view](screenshots/student_view.png)

## Credits

projects used by this XBlock:

* SimpleMDE Markdown Editor
  * A simple, beautiful, and embeddable JavaScript Markdown editor. Delightful editing for beginners and experts alike. Features built-in autosaving and spell checking.
  * <https://simplemde.com>
  * The MIT License
* markdown-it
  * Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed
  * <https://markdown-it.github.io/>
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