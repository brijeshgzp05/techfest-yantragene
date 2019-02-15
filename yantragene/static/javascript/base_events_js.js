$(document).ready(function(){
	var x=100;
	$('#desc_btn').click(function(){
		
		$('#desc_div').delay(x).fadeIn(x);
		$('#rules_div').fadeOut(x);
		$('#cord_div').fadeOut(x);
		$('#reg_div').fadeOut(x);
	});

	$('#rules_btn').click(function(){
		$('#desc_div').fadeOut(x);
		$('#rules_div').delay(x).fadeIn(x);
		$('#cord_div').fadeOut(x);
		$('#reg_div').fadeOut(x);
	});

	$('#cord_btn').click(function(){
		$('#desc_div').fadeOut(x);
		$('#rules_div').fadeOut(x);
		$('#cord_div').delay(x).fadeIn(x);
		$('#reg_div').fadeOut(x);
	});

	$('#reg_btn').click(function(){
		$('#desc_div').fadeOut(x);
		$('#rules_div').fadeOut(x);
		$('#cord_div').fadeOut(x);
		$('#reg_div').delay(x).fadeIn(x);
		$('#desc_div').fadeOut(100);
	});

	$('.cross').click(function(){
		$('#desc_div').fadeOut(100);
		$('#rules_div').fadeOut(100);
		$('#cord_div').fadeOut(100);
		$('#reg_div').fadeOut(100);
	});

});