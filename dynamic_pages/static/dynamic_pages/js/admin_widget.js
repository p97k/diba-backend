$(function($) {
    $(function() {
        let sequence = $('#id_sequence'), verified = $('.HiddenSequence');

        function toggleVerified(value, HiddenSeq) {
            if (value !== '') {
                HiddenSeq.show();
            } else {
                HiddenSeq.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(sequence.val(), verified);

        // show/hide on change
        sequence.change(function() {
            toggleVerified($(this).val(), verified);
        });
    });
});