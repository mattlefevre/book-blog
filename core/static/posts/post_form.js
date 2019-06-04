var checkbox = document.querySelector("input[name=book_check]");
var book_form = document.getElementById("include_book")

checkbox.addEventListener( 'change', function() {
    if(this.checked) {
        book_form.className = "checked"
    } else {
        book_form.className = "form-group"
    }
});