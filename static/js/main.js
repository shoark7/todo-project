$('.solve-button').click(function() { 
  let todo_id = $(this).attr("value");
  let button = $(this);
  $.ajax({
      url: todo_id + '/solve_toggle',
      type: "POST",
      success: function (result) {
        let card = $('#card' + result.pk);
        let icon = button.children();

        if (result.is_solved === true) {
          card.removeClass( "todo-expired todo-not-solved" ).addClass("todo-solved");
          icon.removeClass( "fa-check").addClass("fa-backspace");
        } else {
          card.removeClass("todo-solved")
            if (result.is_expired === true) {
              card.addClass("todo-expired");
            } else {
              card.addClass("todo-not-solved");
            }
          icon.removeClass("fa-backspace").addClass("fa-check");
        }
      }
  });  

});
