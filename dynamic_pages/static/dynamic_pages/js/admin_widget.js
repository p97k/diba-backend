ItemAction = {
  init: function () {
    this.$initWidgetTypeHandler();
  },
  $initWidgetTypeHandler: function () {
    let object = $('.widget_type_select');

    $handleWidgetTypes(object.val());

    object.change(function () {
      $handleWidgetTypes(this.value)
    });

    function $handleWidgetTypes($current_widget_id) {
      $('.form-form_content').hide();
      let $postWidget = $('.post_widget');

      switch ($current_widget_id) {
        case 'post':
          $postWidget.show();
          break;
      }
    }
  }
}

$(function () {
  ItemAction.init();
});