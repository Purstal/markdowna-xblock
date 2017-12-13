/* Javascript for MarkdownXBlock. */
function MarkdownXBlock(runtime, element) {
  /*
  function updateCount(result) {
    $('.count', element).text(result.count);
  }
  */

  var mde;

  var updateMarkdownTextHandlerUrl =
      runtime.handlerUrl(element, 'save_markdown_text');

  var message_area = $('.error_message', element);

  $(element).find('.cancel-button').click(function() {
    runtime.notify('cancel', {});
  });

  $(element).find('.save-button').click(function(eventObject) {
    runtime.notify('save', {state: 'start'});

    // var target = $(eventObject.target);
    // var oldText = target.text();
    // target.text('saving...');

    $.ajax({
      type: 'POST',
      url: updateMarkdownTextHandlerUrl,
      data: JSON.stringify({markdown_text: mde.value()}),
      success: function(ret) {
        // alert('success!\n' + JSON.stringify(ret));
        // runtime.notify('save', {state: 'end'});
        // SyntaxError: Unexpected end of JSON input
        // whatever, I will just reload the whole page
        window.location.reload()

      },
      error: function(data) {
        alert('error!\n' + JSON.stringify(data));
        runtime.notify('error', {msg: data});
      }
    });
  });

  $(function($) {
    var data_unescaped = $('.initialized-data-area', element).text();
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
    //$('.display-area', element).html(md.render(data.markdown_text));

    mde = new window.SimpleMDE({
      autofocus: true,
      // autosave
      element: $('.editor-area', element)[0],
      forceSync: true,
      hideIcons: false,
      indentWithTabs: true,
      initialValue: data.markdown_text,
      // insertTexts
      lineWrapping: true,
      // parsingConfig
      // placeholder
      previewRender: function(text) {
        return md.render(text)
      },
      promptURLs: true,
      renderingConfig: {
        singleLineBreaks: false
        // codeSyntaxHighlighting
      },
      // shortcuts
      // showIcons
      spellChecker: false,
      status: true,
      styleSelectedText: true,
      tabSize: 2,
      // toolbar
      toolbarTips: true
    })

  });
}
