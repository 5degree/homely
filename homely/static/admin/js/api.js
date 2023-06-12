var base_url="http://127.0.0.1:8000/api/"

function callAPI(rel_url,method, data, successCallback,errorCallback) {
	$.ajax({
		type: method,
		url: base_url+rel_url,
		data: data,
		cache: false,
		beforeSend : function(){
			//enable loader
			$('.loader').fadeIn();
		},
		success: successCallback,
		error: errorCallback,
		complete : function(){
			//disable loader
			$('.loader').fadeOut();
		}
	});
};



