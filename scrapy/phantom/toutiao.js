var page = require('webpage').create();
system = require('system');
page.open(system.args[1],function(status){
    // return document.body.outerHTML;
    console.log("-------------");
    console.log(document.body.outerHTML);
    return("-=====================");
    phantom.exit();
return("-=====================");
})