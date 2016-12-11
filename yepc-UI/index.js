/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * | Author:        Iman Tabrizian (tabrizian@outlook.com)
 * |
 * | Creation Date: 09-09-2016
 * |
 * | File Name:     index.js
 * +===============================================
 */

/* global Vue : Vue.js */
/* global $   : JQuery */

var lexer = new Vue({
  el: '#lexer',
  data: {
    tokens: []
  },
  methods: {
    tokenize: function () {
      var form = $("#source").serialize()
      $.post('lex', form, function (data, status) {
        lexer.tokens = JSON.parse(data)
      })
    }
  }
})

var parser = new Vue({
  el: '#parser',
  data: {
    quadruples: []
  },
  methods: {
    parse: function () {
      var form = $("#source").serialize()
      $.post('yacc', form, function (data, status) {
        parser.quadruples = JSON.parse(data)
      })
    }
  }
})

new Vue({
  el: '#source',
  methods: {
    fromFile: function () {
      var file = document.getElementById("file").files[0];
      var reader = new FileReader();
      reader.onload = function (e) {
            var textArea = document.getElementsByName("text")[0];
            textArea.value = e.target.result;
      };
      if (file) {
        reader.readAsText(file);
      }
    }
  }
})

$('document').ready(function () {
})
