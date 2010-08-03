from pymongo.code import Code

map_tags = Code("""
function () {
    this.tags.forEach(function(z) {
        emit(z, 1);
    });
}
""")

reduce_tags = Code("""
function (key, values) {
    var total = 0;
    for (var i = 0; i < values.length; i++) {
        total += values[i];
    }
    return total;
}
""")

