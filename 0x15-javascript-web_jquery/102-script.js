// JavaScript script that adds, removes and clears LI elements
// from a list when the user clicks

$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	});
});
