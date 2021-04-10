/*
 * vim:sw=4 ts=4 et:
 * Copyright (c) 2015 Torchbox Ltd.
 * felicity@torchbox.com 2015-09-14
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely. This software is provided 'as-is', without any express or implied
 * warranty.
 */

/*
 * Used to initialize Simple MDE when Markdown blocks are used in StreamFields
 */
function simplemdeAttach(id) {
        var mde = new SimpleMDE({
            element: document.getElementById(id),
            autofocus: false,
            toolbar: ["bold", "italic", "heading-1",
        {
            name: "redText",
            action: drawRedText,
            className: "fa fa-bold", // Look for a suitable icon
            title: "Red text (Ctrl/Cmd-Alt-R)",
        }
    ]
        });
        mde.render();

        mde.codemirror.on("change", function(){
            $('#' + id).val(mde.value());
        });
}

function drawRedText(editor) {

    var cm = editor.codemirror;
    var output = '';
    var selectedText = cm.getSelection();
    var text = selectedText || 'placeholder';

    output = '!!' + text + '!!';
    cm.replaceSelection(output);

}

/*
 * Used to initialize Simple MDE when MarkdownFields are used on a page.
 */
$(document).ready(function() {
    $(".object.markdown textarea").each(function(index, elem) {
        simplemdeAttach(elem.id);
    });
});

/*
 * Used to initialize content when MarkdownFields are used in admin panels.
 */
$(document).on('shown.bs.tab', function(e) {
    $('.CodeMirror').each(function(i, el){
        setTimeout(
            function() {
                el.CodeMirror.refresh();
            }, 100
        );
    });
});