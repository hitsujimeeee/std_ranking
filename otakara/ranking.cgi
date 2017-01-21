#!/usr/bin/perl


$max_count = 50;
$disp_count = 10;
$retry = 5;                                    # ���g���C�񐔃Z�b�g
$lockdir = "data/lock";
$lockdir2 = "data/lock2";
@strlist = split(/&/, $ENV{'QUERY_STRING'});
@stage_name = ("���A", "�", "���̍Ւd", "�T��", "����̐��E", "�Ɋ�", "����̖��", "�Ɍ��̐��E", "����", "��j�D", "���{��", "�Q�̒n����", "�p��", "�������Z", "�G�E���C�A�̌Ï�", "��Ε��", "�ܔM�̒n", "����", "���E�˔j", "�V��̏�");
$source = "data/@strlist[1].txt";
if(@strlist[0] == 5963){
	&filelock;
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	$serial = @strlist[2];
	$name = @strlist[3];
	$twitter = @strlist[4];
	$time = @strlist[5];
	if(!open(OUT, "$source")){
		print "�t�@�C����ǂݍ��߂܂���B\n";
		&freelock;
		exit();
	}
	@list = <OUT>;
	close(OUT);
	$count = 0;
	foreach (@list){
		$count++;
	}
	if($count != 0){
		$sorts = 0;	#�\�[�g���邩�t���O
		$p = 0;		#���݂�temp_ooo�̈ʒu
		for($i=0;$i<$count;$i++){
			@temp_line = split(/:/, @list[$i]);
			@t = split(/\n/, @temp_line[3]);
			if($sorts == 1){
				if(@temp_line[0] != $serial){
					@list_serial[$p] = @temp_line[0];
					@list_name[$p] = @temp_line[1];
					@list_twitter[$p] = @temp_line[2];
					@list_time[$p] = @t[0];
					$p++;
				}
			}elsif($sorts == 0 && $time <= @t[0]){
				if($serial == @temp_line[0]){
					@list_serial[$p] = $serial;
					@list_name[$p] = $name;
					@list_twitter[$p] = $twitter;
					@list_time[$p] = $time;
					$p++;
					$sorts = 1;
				}else{
					@list_serial[$p] = $serial;
					@list_name[$p] = $name;
					@list_twitter[$p] = $twitter;
					@list_time[$p] = $time;
					@list_serial[$p+1] = @temp_line[0];
					@list_name[$p+1] = @temp_line[1];
					@list_twitter[$p+1] = @temp_line[2];
					@list_time[$p+1] = @t[0];
					$sorts = 1;
					$p += 2;
				}
			}else{
				@list_serial[$p] = @temp_line[0];
				@list_name[$p] = @temp_line[1];
				@list_twitter[$p] = @temp_line[2];
				@list_time[$p] = @t[0];
				$p++;
			}
		}
		if($sorts == 0 && $count < $max_count){
			@list_serial[$count] = $serial;
			@list_name[$count] = $name;
			@list_twitter[$count] = $twitter;
			@list_time[$count] = $time;
		}
	}else{
		@list_serial[$count] = $serial;
		@list_name[$count] = $name;
		@list_twitter[$count] = $twitter;
		@list_time[$count] = $time;
	}
	$count = 0;
	foreach (@list_serial){
		$count++;
	}
	if (!open(FH, ">$source")){
		print "�t�@�C���ɏ������߂܂���B\n";
		&freelock;
		exit();
	}
	for($i=0;$i<$count;$i++){
		if($i >= $max_count){
			last;
		}
		print FH "@list_serial[$i]:@list_name[$i]:@list_twitter[$i]:@list_time[$i]\n";
	}
	close(FH);
	&freelock;
}elsif(@strlist[0] == 2){
	&filelock;
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	if(!open(FH, "$source")){
		print "�t�@�C����ǂݍ��߂܂���B\n";
		&freelock;
		exit();
	}
	print <FH>;
	close(FH);
	&freelock;
}elsif(@strlist[0] == 3){
	&filelock;
	print "Content-Type: text/html; charset=Shift_JIS\n\n";
	print "<html>\n";
	print "<meta http-equiv='Content-Type' content='text/html; charset=Shift_JIS'>\n";
	print "<head><title>�����L���O</title></head>\n";
	print "<body>\n";
	print "<br><br>\n\n";
	print "		<table border='1' align='center'>\n";
	print "			<tr align='center'>\n";
	for($i=0;$i<3;$i++){
		$temp = @strlist[1]-1+$i;
		if($temp <= 0 || $temp > 20){
			print "<td>�@</td>\n";
		}else{
			print "<td>@stage_name[(@strlist[1]-2+$i)]</td>\n";
		}
	}
	print "			</tr>\n";
	print "			<tr align='center'>\n";
	for($i=0;$i<3;$i++){
		$temp = @strlist[1]-1+$i;
		if($temp >= 1 && $temp <= 4){
			$graph = "001";
		}elsif($temp >= 5 && $temp <= 8){
			$graph = "002";
		}elsif($temp >= 9 && $temp <= 12){
			$graph = "003";
		}elsif($temp >= 13 && $temp <= 16){
			$graph = "004";
		}elsif($temp >= 17 && $temp <= 19){
			$graph ="005";
		}elsif($temp == 20){
			$graph = "006";
		}
		if($temp <= 0 || $temp > 20){
			print "<td width='200'>�@</td>\n";
		}else{
			print "<td width='200'><a href='http://www38.atpages.jp/hitsujimeeee/otakara/ranking.cgi?3&$temp'><img src=img/$graph.jpg></a></td>\n";
		}
	}
	print "			</tr>\n";
	print "		</table>\n";
	print "			<br><br>\n";

	if(open(FH, "$source")){
		@ranking = <FH>;
		close(FH);
		$count = 0;
		foreach (@ranking){
			$count++;
		}
		$temp = @stage_name[@strlist[1]-1];
		$an = ucfirst(@strlist[1]);
		print "<table border='0' align='center' 'cellspacing='0' cellpadding='0'><tr><td>\n";
		print "<table border='0'><tr><td><img src='img/icon.gif' width='32'></td><td valign='bottom'><font size='+3'>$temp</font></td></tr></table>\n";
		print "</td></tr>\n";
		print "<tr><td>\n";
		print "<table align='center' border='1'><tr><td>����</td><td width='160' align='center'>name</td><td width='120' align='center'>time</td></tr>\n";
		for($i=0;$i<$disp_count;$i++){
			print "<tr>";
			@bun = split(/:/, @ranking[$i]);
			$num = $i+1;
			print "<td align='center'>$num</td>\n";
			if($i >= $count){
				print "<td align='center'>-----------</td>\n";
			}else{
				if(@bun[2] eq ""){
					print "<td align='center'>@bun[1]</td>\n";
				}else{
					print "<td align='center'><a href='https://twitter.com/@bun[2]' target='_blank'>@bun[1]</a></td>\n";
				}
			}
			$minute = int(@bun[3]/(1000*60));
			$minute = sprintf("%02d",$minute);
			$second = int(@bun[3]%(1000*60)/1000);
			$second = sprintf("%02d",$second);
			$m_second = int(@bun[3]%1000/10);
			$m_second = sprintf("%02d",$m_second);
			if($i >= $count){
				print "<td align='center'>--:--:--</td>\n";
			}else{
				print "<td align='center'>$minute:$second:$m_second</td>\n";
			}
			print "</tr>\n";
		}
		print "</table>\n";
		close(FH);
	}else{
		print "�t�@�C����ǂݍ��߂܂���I<br>\n";
	}
	print "</td></tr></table>\n";
	print "<br><br>\n\n";
	$count = 0;
	if(open(FH, "counter.txt")){
		@temp = <FH>;
		$count = @temp[0];
		close(FH);
	}
	print "<center>���݂̃����L���O�Q���Ґ��@�@�@�@     $count�l</center>\n";
	print "<br><br>\n";
	print "<center><a href='index.html'>�ꗗ�ɖ߂�</a></center>\n";
	print "<br><br><br><br><br>\n";
	print "</body>\n";
	print "</html>\n";	
	&freelock;
}else{
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	print "Error!\n"
}





sub filelock{
	while (!mkdir($lockdir, 0755)) {               # �쐬�B�o���Ȃ���Α҂�
		if (--$retry <= 0) {                       # 5��_���Ȃ�
			if (mkdir($lockdir2, 0755)) {          # ���b�N���������߂̔r��
				if ((-M $lockdir) * 86400 > 600) { # �쐬���Ԃ�10���ȏ�O�Ȃ�
					# ���b�N����ւ�
					rename($lockdir2, $lockdir) or &error("LOCK ERROR"); 
					last;                          # ��A�̏�����
				}
					else { rmdir($lockdir2); }         # �������b�N�폜
			}
			print "Content-Type: text/plain; charset=Shift_JIS\n\n";
			print "BUSY";
			&error("BUSY");                        # ������߂�
			exit();
		}
		sleep(1);                                  # 1�b�҂�
	}
}


sub freelock{
	rmdir($lockdir);                               # �폜
}