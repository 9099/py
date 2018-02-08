
// function scrollToBottom() {

//     var Height = document.body.clientHeight,  //文本高度
//         screenHeight = window.innerHeight,  //屏幕高度
//         INTERVAL = 100,  // 滚动动作之间的间隔时间
//         delta = 500,  //每次滚动距离
//         curScrollTop = 0;    //当前window.scrollTop 值

//     var scroll = function () {
//         curScrollTop = document.body.scrollTop;
//         window.scrollTo(0,curScrollTop + delta);
//     };

//     var timer = setInterval(function () {
//         var curHeight = curScrollTop + screenHeight;
//         if (curHeight >= Height){   //滚动到页面底部时，结束滚动
//             clearInterval(timer);
//         }
//         scroll();
//     }, INTERVAL)
// }



// function sleep(numberMillis) {
// var now = new Date();
// var exitTime = now.getTime() + numberMillis;
// while (true) {
// now = new Date();
// if (now.getTime() > exitTime)
// return;
// }
// }

// var page = require('webpage').create();
// page.open("http://www.toutiao.com", function (status) {
//     if(status==="success") {
//         // page.render('a.png');
//         page.includeJs("http://apps.bdimg.com/libs/jquery/2.1.1/jquery.js", function() {
//         page.evaluate(function() {
//          $("refresh-mode").click();
//         });

//         $(".refresh-mode").test("-=-=-=-=-=-=-=");
//         $(".refresh-mode").click();

//         var data = page.evaluate(function(){
//             return document.title;
//         });
//         // console.log(document.getElementsByClassName("refresh-mode").textContent);
//         console.log(data);

//         page.render('2.png');
//         phantom.exit()
//     }
// });
//
//
//
//



//jqurey滚动到底部
// function(){
// $('html, body, .content').animate({scrollTop: $(document).height()}, 300);
// return false;
// }


var page = require('webpage').create();
page.viewportSize = { width: 300, height: 300 };
//the clipRect is the portion of the page you are taking a screenshot of
// page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };

page.open('http://www.toutiao.com', function() {
//    var obj = document.getElementsByClassName("refresh-mode");
// var clickEvent = document.createEvent("HTMLEvents");

//        clickEvent.initEvent("click",false,true);

//        var a = document.getElementsByClassName("refresh-mode");

//        a.dispatchEvent(clickEvent);

  page.includeJs("http://apps.bdimg.com/libs/jquery/2.1.1/jquery.js", function() {
    //


    page.evaluate(function() {
      $(".refresh-mode").trigger('click');
      $(".refresh-mode").text("--22--------------");
      // $('html, body, .content').animate({scrollTop: $(document).height()}, 300);

    });

    // $(".refresh-mode").text('some text');
    // $(".refresh-mode").click();
    page.render('aa.jpg')
    phantom.exit()
  });
});