var page = require('webpage').create();
page.open('http://www.toutiao.com',function(status){
    if(status==='success'){
		page.render('toutiao.png')
	}
          
        });
    console.log("title is :"+status);

    phantom.exit();
});