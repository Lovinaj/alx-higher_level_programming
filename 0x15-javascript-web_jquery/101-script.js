// A JavaScript script that adds, removes and clears LI elements
// from a list when the user clicks

$(document).ready(function(){
    $('div#add_item').click(function(){
        $('ul.my_list').append('<li>Item</li>');
    });
    $('div#remove_item').click(function(){
        $('li').last().remove();
    });
    $('div#clear_list').click(function(){
        $('ul.my_list').empty();
    });
});
