from pymongo.code import Code

map_tags = Code("""
function () {
    if (this.tags) {
        this.tags.forEach(function(z) {
            emit(z, 1);
        });
    }
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

def get_word_map(word):
    _map = Code("""
    function() {
        if (this.title) {
            if (this.title.indexOf('%s') >= 0) {
                emit(this._id, 2);
            }
        }
        if (this.text) {
            if (this.text.indexOf('%s') >= 0) {
                emit(this._id, 1);
            }
        }
    }""" % (word, word)
    )
    return _map

reduce_word = Code("""
function(key, values) {
    var total = 0;
    for (var i = 0; i < values.length; i++) {
        total += values[i];
    }
    return total;
}
""")
