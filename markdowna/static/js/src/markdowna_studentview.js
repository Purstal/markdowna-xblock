/* Javascript for MarkdownXBlock. */
function MarkdownXBlock(runtime, element) {
  // alert([runtime, element]);
  var markdown_text;

  $(function($) {
    var data_unescaped = $('.data-area', element).text();
    var data_text = data_unescaped.replace(/&(lt|gt|amp);/, function(old) {
      switch (old) {
        case '&lt;':
          return '<';
        case '&gt;':
          return '>';
        case '&amp;':
          return '&';
      }
    });
    var data = JSON.parse(data_text);
    var md = window.markdownit({linkify: true});
    md = md.use(window.front_matter_plugin);
    $('.display-area', element).html(md.render(data.markdown_text));
  });
}
