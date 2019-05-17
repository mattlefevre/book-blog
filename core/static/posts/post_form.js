var checkbox = document.querySelector("input[name=no_book]");
var book_form = document.getElementById("book_form")

checkbox.addEventListener( 'change', function() {
    if(this.checked) {
        book_form.className = "checked"
    } else {
        book_form.className = "notChecked"
    }
});