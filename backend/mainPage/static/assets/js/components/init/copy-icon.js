//
// Icon code copy/paste
//

'use strict';

var CopyIcon = (function() {

	// Variables

	var $element = '.btn-icon-clipboard',
		$btn = $($element);


	// Methods

	function init($this) {
		$this.tooltip().on('mouseleave', function() {
			// Explicitly hide tooltip, since after clicking it remains
			// focused (as it's a button), so tooltip would otherwise
			// remain visible until focus is moved away
			$this.tooltip('hide');
		});

		var clipboard = new ClipboardJS($element);

		clipboard.on('success', function(e) {
			$(e.trigger)
				.attr('title', '계측기가 저장되었습니다!')
				.tooltip('_fixTitle')
				.tooltip('show')
				.attr('title', '계측기 모델을 저장하시겠습니까?')
				.tooltip('_fixTitle')

			e.clearSelection()
		});
	}


	// Events
	if ($btn.length) {
		init($btn);
	}

})();
