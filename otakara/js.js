function ChangeMainForm(stage) {
    var str = new Array(5);
    var link = new Array(5);
    var count, myid;
    var text = "";
    switch (stage) {
        case 1:
            str[0] = "“´ŒA"
            link[0] = 1;
            str[1] = "ã©"
            link[1] = 2;
            str[2] = "‰¤‚ÌÕ’d"
            link[2] = 3;
            str[3] = "’T‹†"
            link[3] = 4;
            count = 4;
            break;
        case 2:
            str[0] = "”’‹â‚Ì¢ŠE"
            link[0] = 5;
            str[1] = "‹ÉŠ¦"
            link[1] = 6;
            str[2] = "á‚Ì–é‚É"
            link[2] = 7;
            str[3] = "‹ÉŒÀ‚Ì¢ŠE"
            link[3] = 8;
            count = 4;
            break;
        case 3:
            str[0] = "…’ê"
            link[0] = 9;
            str[1] = "“ï”j‘D"
            link[1] = 10;
            str[2] = "—³‹{é"
            link[2] = 11;
            str[3] = "ŒQÂ‚Ì’n—‹Œ´"
            link[3] = 12;
            count = 4;
            break;
        case 4:
            str[0] = "”pšĞ"
            link[0] = 13;
            str[1] = "‹€‚¿‚½ŠZ"
            link[1] = 14;
            str[2] = "ƒGƒEƒŒƒCƒA‚ÌŒÃé"
            link[2] = 15;
            str[3] = "â‘Î•ïˆÍ"
            link[3] = 16;
            count = 4;
            break;
        case 5:
            str[0] = "Ü”M‚Ì’n"
            link[0] = 17;
            str[1] = "Œ‰Š"
            link[1] = 18;
            str[2] = "ŒÀŠE“Ë”j"
            link[2] = 19;
            count = 3;
            break;
        case 6:
            str[0] = "“V‹ó‚Ìé"
            link[0] = 20;
            count = 1;
            break;
    }
    myid = document.getElementById("mainform");
    text += "ƒXƒe[ƒW<ul>";
    for (i = 0; i < count; i++) {
        text += "<li>"+stage+"-"+(i+1)+"@<a href='http://www38.atpages.jp/hitsujimeeee/otakara/ranking.cgi?3&"+link[i]+"'>"+str[i]+"</a></li>";
    }
    text += "</ul><br>"
    myid.innerHTML = text;
}


function Test() {
    alert("test");
}