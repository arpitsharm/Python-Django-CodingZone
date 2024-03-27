var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/wf466pshnuteo5x9vuvr40z7uyhhbelihmyr1plasyzpiwbc/tinymce/6/tinymce.min.js"
document.head.appendChild(script)
document.write("<style>#id_contant{ height: 591px; }</style>")
script.onload = function () {
    tinymce.init({
        selector: 'textarea',
        plugins: 'code anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss',
        toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Author name',
        mergetags_list: [
          { value: 'First.Name', title: 'First Name' },
          { value: 'Email', title: 'Email' },
        ],
        // menu: {
        //   TextViewCode: { title: 'My Favorites', items: 'code' }
        // },
        // plugins: 'code',  // required by the code menu item
        // menubar: 'favs file edit view insert format tools table help'  // adds happy to the menu bar
        
      });
}