var cd = 30;
var buy,sell;
var buyhigh,buylow,sellhigh,selllow;
function reload(){
    location.reload();
}
function countdown(){
    $('#countdown').text(cd);
    cd--;
}
function post(){
    cd = 30;
    if ($("#buyhigh_chk").is(':checked')){
        if ($('#buyhigh').val()>0){
            buyhigh = $('#buyhigh').val();
        }else{
            //alert("勿输入非负数");
            return;
        }
        buylow = -1;
    }else{
        if ($('#buylow').val()>0){
            buylow = $('#buylow').val();
        }else{
            //alert("勿输入非负数");
            return;
        }
        buyhigh = -1;
    }
    if ($("#sellhigh_chk").is(':checked')){
        if ($('#sellhigh').val()>0){
            sellhigh = $('#sellhigh').val();
        }else{
            //alert("勿输入非负数");
            return;
        }
        selllow = -1;
    }else{
        if ($('#selllow').val()>0){
            selllow = $('#selllow').val();
        }else{
            //alert("勿输入非负数");
            return;
        }
        sellhigh = -1;
    }
    localStorage.setItem('isTTS_chk',$("#isTTS_chk").is(':checked'));
    localStorage.setItem('buyhigh_chk',$("#buyhigh_chk").is(':checked'));
    localStorage.setItem('buylow_chk',$("#buylow_chk").is(':checked'));
    localStorage.setItem('sellhigh_chk',$("#sellhigh_chk").is(':checked'));
    localStorage.setItem('selllow_chk',$("#selllow_chk").is(':checked'));
    localStorage.setItem('buyhigh',buyhigh);
    localStorage.setItem('buylow',buylow);
    localStorage.setItem('sellhigh',sellhigh);
    localStorage.setItem('selllow',selllow);
    //isTTS = $("#isTTS_chk").is(':checked');
    //,"isTTS":isTTS
    jsonquery = {"buyhigh":buyhigh,"buylow":buylow,"sellhigh":sellhigh,"selllow":selllow};
    /*
    $.ajax({
        type: 'POST',
        url: "\query",
        data: JSON.stringify(jsonquery),
        success: function(){return},
        dataType: 'json',
    });
    */
    $.getJSON('query', jsonquery, function (data) {
        buy = data.buy;
        sell = data.sell;
        $('#received').text("当前买" + buy + "当前卖" + sell);
        if (buyhigh > 0) {
            if (buyhigh < buy) {
                jsonisTTS = { "isTTS": true };
                $.getJSON('isTTS', jsonisTTS);
                audioready();
                // var audio_ = document.getElementById("audio");
                // audio_.load();
                // setTimeout("audio()",1000);
            }
        }
        if (buylow > 0) {
            if (buylow > buy) {
                jsonisTTS = { "isTTS": true };
                $.getJSON('isTTS', jsonisTTS);
                audioready();
                // var audio_ = document.getElementById("audio");
                // audio_.load();
                // setTimeout("audio()",1000);
            }
        }
        if (sellhigh > 0) {
            if (sellhigh < sell) {
                jsonisTTS = { "isTTS": true };
                $.getJSON('isTTS', jsonisTTS);
                audioready();
                // var audio_ = document.getElementById("audio");
                // audio_.load();
                // setTimeout("audio()",1000);
            }
        }
        if (selllow > 0) {
            if (selllow > sell) {
                jsonisTTS = { "isTTS": true };
                $.getJSON('isTTS', jsonisTTS);
                audioready();
                // var audio_ = document.getElementById("audio");
                // audio_.load();
                // setTimeout("audio()",1000);
            }
        }
    });
}
function onload(){
    if (localStorage.getItem('buyhigh_chk') != 'false'){
        $("#buyhigh_chk").attr("checked", true);
    }else{
        $("#buylow_chk").attr("checked", true);
    }
    if (localStorage.getItem('sellhigh_chk') != 'false'){
        $("#sellhigh_chk").attr("checked", true);
    }else{
        $("#selllow_chk").attr("checked", true);
    }
    if (localStorage.getItem('isTTS_chk') != 'false'){
        $("#isTTS_chk").attr("checked", true);
    }else{
        $("#notTTS_chk").attr("checked", true);
    }
    $('#buyhigh').attr("value",localStorage.getItem('buyhigh'));
    $('#buylow').attr("value",localStorage.getItem('buylow'));
    $('#sellhigh').attr("value",localStorage.getItem('sellhigh'));
    $('#selllow').attr("value",localStorage.getItem('selllow'));
    post();
}
function audio(){
    $("#isTTS_chk").attr("checked", true);
    $("#notTTS_chk").attr("checked", false);
    var audio_ = document.getElementById("audio");
    audio_.play();
    $("#isTTS_chk").attr("checked", false);
    $("#notTTS_chk").attr("checked", true);
    jsonisTTS = { "isTTS": false };
    $.getJSON('query', jsonisTTS);
}
function audioready(){
    var audio_ = document.getElementById("audio");
    audio_.src = 'out.mp3';
    audio_.load();
    audio_.play();
}
    //var t1 = window.setTimeout(post, cd * 1000);
    var t1 = window.setInterval(post, cd * 1000);
    var t2 = window.setInterval(countdown, 1000);