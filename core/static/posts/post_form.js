var checkbox = document.querySelector("input[name=book_check]");
var book_form = document.getElementById("include_book")
var book_lis = document.getElementById("include_book").getElementsByTagName("input")

checkbox.addEventListener( 'change', function() {
    if(this.checked) {
        book_form.className = "checked"
        // only looks at book's title and author, ignoring all other fields since they'll be deleted on submit.
        for (let index = 0; index < 2; index++) {
            book_lis[index].value = ""          
        }
    } else {
        book_form.className = "form-group"
    }
});
