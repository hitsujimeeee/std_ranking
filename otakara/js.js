function ChangeMainForm(stage) {
    var str = new Array(5);
    var link = new Array(5);
    var count, myid;
    var text = "";
    switch (stage) {
        case 1:
            str[0] = "���A"
            link[0] = 1;
            str[1] = "�"
            link[1] = 2;
            str[2] = "���̍Ւd"
            link[2] = 3;
            str[3] = "�T��"
            link[3] = 4;
            count = 4;
            break;
        case 2:
            str[0] = "����̐��E"
            link[0] = 5;
            str[1] = "�Ɋ�"
            link[1] = 6;
            str[2] = "����̖��"
            link[2] = 7;
            str[3] = "�Ɍ��̐��E"
            link[3] = 8;
            count = 4;
            break;
        case 3:
            str[0] = "����"
            link[0] = 9;
            str[1] = "��j�D"
            link[1] = 10;
            str[2] = "���{��"
            link[2] = 11;
            str[3] = "�Q�̒n����"
            link[3] = 12;
            count = 4;
            break;
        case 4:
            str[0] = "�p��"
            link[0] = 13;
            str[1] = "�������Z"
            link[1] = 14;
            str[2] = "�G�E���C�A�̌Ï�"
            link[2] = 15;
            str[3] = "��Ε��"
            link[3] = 16;
            count = 4;
            break;
        case 5:
            str[0] = "�ܔM�̒n"
            link[0] = 17;
            str[1] = "����"
            link[1] = 18;
            str[2] = "���E�˔j"
            link[2] = 19;
            count = 3;
            break;
        case 6:
            str[0] = "�V��̏�"
            link[0] = 20;
            count = 1;
            break;
    }
    myid = document.getElementById("mainform");
    text += "�X�e�[�W<ul>";
    for (i = 0; i < count; i++) {
        text += "<li>"+stage+"-"+(i+1)+"�@<a href='http://www38.atpages.jp/hitsujimeeee/otakara/ranking.cgi?3&"+link[i]+"'>"+str[i]+"</a></li>";
    }
    text += "</ul><br>"
    myid.innerHTML = text;
}


function Test() {
    alert("test");
}