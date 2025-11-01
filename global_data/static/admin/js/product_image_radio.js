(function($) {
    'use strict';
    
    function updateRowHighlighting() {
        $('input.general-image-radio[type="radio"]').each(function() {
            var $radio = $(this);
            var $row = $radio.closest('tr');
            
            if ($radio.is(':checked')) {
                $row.addClass('selected-general').css('background-color', '#e8f5e8');
            } else {
                $row.removeClass('selected-general').css('background-color', '');
            }
        });
    }
    
    function initImageRadios() {
        var $radios = $('input.general-image-radio[type="radio"]');
        
        $radios.off('change').on('change', function() {
            var $clicked = $(this);
            
            if ($clicked.is(':checked')) {
                // Uncheck all other radios
                $radios.not($clicked).each(function() {
                    $(this).prop('checked', false);
                    
                    // Update hidden field for False value
                    var $hidden = $(this).siblings('input[type="hidden"]');
                    if ($hidden.length) {
                        $hidden.val('False');
                    }
                });
                
                // Ensure the clicked one is True
                var $hidden = $clicked.siblings('input[type="hidden"]');
                if ($hidden.length) {
                    $hidden.val('True');
                }
                
                // Update row highlighting
                updateRowHighlighting();
            }
        });
        
        // Initialize highlighting
        updateRowHighlighting();
        
        // If none is selected, select the first one
        if ($radios.filter(':checked').length === 0 && $radios.length > 0) {
            $radios.first().prop('checked', true).trigger('change');
        }
    }
    
    $(document).ready(function() {
        initImageRadios();
        
        // Reinitialize when new inlines are added
        $('.add-row a').on('click', function() {
            setTimeout(initImageRadios, 100);
        });
    });
    
    // Django formset events
    if (typeof(django) !== 'undefined' && django.jQuery) {
        django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
            if (formsetName.indexOf('productimage') !== -1) {
                setTimeout(initImageRadios, 100);
            }
        });
    }
    
})(django.jQuery || $);