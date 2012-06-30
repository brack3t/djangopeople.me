var options = {
    valueNames: ["distance"]
};

var resultsList = new List("searchResults", options);

$(".sort-by li").click(function(e) {
    var value = $(this).attr("data-close");

    var asc = true;
    if (value === "false") {
        asc = false;
    }

    return resultsList.sort("distance", {asc: asc});
});

$(".filter-availability li").click(function(e) {
    var value = $(this).attr("data-value");

    if (value) {
        resultsList.filter(function(item) {
            if ($(item.elm).attr("data-availability") == value) {
                return true;
            } else {
                return false;
            }
        });
    } else {
       resultsList.filter();
    }
});