$(function() {
    var form = $("#message_form form"),
        errors = form.find(".error");

    if (errors.length === 0) {
        // if there are no errors, hide the form on page load.
        form.hide();
    }

    $("#message_me").click(function(e) {
        e.preventDefault();

        form.show();
    });
});