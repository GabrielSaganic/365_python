let editor = document.querySelector("#editor");

ace.edit(editor, {
    theme: "ace/theme/tomorrow_night_blue",
    mode: "ace/mode/python",
    maxLines: 50,
    minLines: 50,
    hasCssTransforms: true,
    value: "print(\"Hello world\")",
});
