#!/usr/bin/perl


$max_count = 20;
$disp_count = 10;
$retry = 5;                                    # リトライ回数セット
$lockdir = "data/lock";
$lockdir2 = "data/lock2";
@strlist = split(/&/, $ENV{'QUERY_STRING'});
$source = "data/@strlist[1].txt";
if(@strlist[0] == 5963){
	&filelock;
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	$serial = @strlist[2]; 
	$name = @strlist[3];
	$time = @strlist[4];
	$rank = @strlist[5];
	if(open(OUT, "$source")){
		@list = <OUT>;
		close(OUT);
		$count = 0;
		foreach (@list){
			$count++;
		}
		if($count != 0){
			$sorts = 0;	#ソートするかフラグ
			$now_p = 0;		#現在のtemp_oooの位置
			for($i=0;$i<$count;$i++){
				@temp_line = split(/:/, @list[$i]);
				@ranker = split(/\n/, @temp_line[3]);
				if($sorts == 1){
					if(@temp_line[0] != $serial){
						@temp_serial[$now_p] = @temp_line[0];
						@temp_name[$now_p] = @temp_line[1];
						@temp_time[$now_p] = @temp_line[2];
						@temp_rank[$now_p] = @ranker[0];
						$now_p++;
					}
				}elsif($sorts == 0 && $time <= @temp_line[2]){
					if($serial == @temp_line[0]){
						@temp_serial[$now_p] = $serial;
						@temp_name[$now_p] = $name;
						@temp_time[$now_p] = $time;
						@temp_rank[$now_p] = $rank;
						$now_p++;
						$sorts = 1;
					}else{
						@temp_serial[$now_p] = $serial;
						@temp_name[$now_p] = $name;
						@temp_time[$now_p] = $time;
						@temp_rank[$now_p] = $rank;
						@temp_serial[$now_p+1] = @temp_line[0];
						@temp_name[$now_p+1] = @temp_line[1];
						@temp_time[$now_p+1] = @temp_line[2];
						@temp_rank[$now_p+1] = @ranker[0];
						$sorts = 1;
						$now_p += 2;
					}
				}else{
					@temp_serial[$now_p] = @temp_line[0];
					@temp_name[$now_p] = @temp_line[1];
					@temp_time[$now_p] = @temp_line[2];
					@temp_rank[$now_p] = @ranker[0];
					$now_p++;
				}
			}
			if($sorts == 0 && $count < $max_count){
				@temp_serial[$count] = $serial;
				@temp_name[$count] = $name;
				@temp_time[$count] = $time;
				@temp_rank[$count] = $rank;
			}
		}else{
			@temp_serial[$count] = $serial;
			@temp_name[$count] = $name;
			@temp_time[$count] = $time;
			@temp_rank[$count] = $rank;
		}
		$count = 0;
		foreach (@temp_serial){
			$count++;
		}
		if (open(FH, ">$source")){
			for($i=0;$i<$count;$i++){
				if($i >= $max_count){
					last;
				}
				print FH "@temp_serial[$i]:@temp_name[$i]:@temp_time[$i]:@temp_rank[$i]\n";
			}
			close(FH);
		} else {
			print "ファイルに書き込めません。\n";
		}
	}else{
		print "ファイルを読み込めません。\n";
	}
	&freelock;
}elsif(@strlist[0] == 2){
	&filelock;
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	if(open(FH, "$source")){
		print <FH>;
		close(FH);
	}else{
		print "ファイルを読み込めません。\n";
	}
	&freelock;
}elsif(@strlist[0] == 3){
	&filelock;
	print "Content-Type: text/html; charset=Shift_JIS\n\n";
	print "<html>\n";
	print "<meta http-equiv='Content-Type' content='text/html; charset=Shift_JIS'>\n";
	print "<head><title>ランキング</title></head>\n";
	print "<body>\n";
	print "<br><br>\n\n";
	print "			<table align='center' border='1'>\n";
	print "				<tr>\n";
	print "					<td width='48'><a href='ranking.cgi?3&nagisa&夏目　凪沙'><img src='img/nagisa.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&mei&久我原　芽衣'><img src='img/mei.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&rin&笹峰　燐'><img src='img/rin.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&nene&紅葉　音々'><img src='img/nene.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&ayame&春日野　菖蒲'><img src='img/ayame.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&hikari&神代　光'><img src='img/hikari.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&asuka&日比野　飛鳥'><img src='img/asuka.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&risa&本宮　理沙'><img src='img/risa.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&haku&東雲　白'><img src='img/haku.png' width='48' border='0'></a></td>\n";
	print "					<td width='48'><a href='ranking.cgi?3&kobayan&コバヤン'><img src='img/kobayan.png' width='48' border='0'></a></td>\n";
	print "				</tr>\n";
	print "			</table>\n";
	print "			<br><br>\n";

	if(open(FH, "$source")){
		@ranking = <FH>;
		close(FH);
		$count = 0;
		foreach (@ranking){
			$count++;
		}
		$cn = @strlist[2];
		$cn =~ tr/+/ /;
		$cn =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack("C", hex($1))/eg;
		$an = ucfirst(@strlist[1]);
		print "<table border='0' align='center' 'cellspacing='0' cellpadding='0'><tr><td>\n";
		print "<table border='0'><tr><td><img src='img/@strlist[1].png' width='48'></td><td valign='bottom'><font size='+3'>$cn</font>－$an－</td></tr></table>\n";
		print "</td></tr>\n";
		print "<tr><td>\n";
		print "<table align='center' border='1'><tr><td>順位</td><td width='160' align='center'>name</td><td width='120' align='center'>time</td><td width='50' align='center'>Rank</td></tr>\n";
		for($i=0;$i<10;$i++){
			print "<tr>";
			@bun = split(/:/, @ranking[$i]);
			$num = $i+1;
			print "<td align='center'>$num</td>\n";
			if($i >= $count){
				print "<td align='center'>-----------</td>\n";
			}else{
				print "<td align='center'>@bun[1]</td>\n";
			}
			$minute = int(@bun[2]/(1000*60));
			$minute = sprintf("%02d",$minute);
			$second = int(@bun[2]%(1000*60)/1000);
			$second = sprintf("%02d",$second);
			$m_second = int(@bun[2]%1000/10);
			$m_second = sprintf("%02d",$m_second);
			$rank = sprintf("%d", @bun[3]);
			if($rank == 0){
				$rank = "E";
			}elsif($rank == 1){
				$rank = "D";
			}elsif($rank == 2){
				$rank = "C";
			}elsif($rank == 3){
				$rank = "B";
			}elsif($rank == 4){
				$rank = "A";
			}elsif($rank == 5){
				$rank = "S";
			}elsif($rank == 6){
				$rank = "SS";
			}elsif($rank == 7){
				$rank = "SSS";
			}
			if($i >= $count){
				print "<td align='center'>--:--:--</td>\n";
			}else{
				print "<td align='center'>$minute:$second:$m_second</td>\n";
			}
			if($i >= $count){
				print "<td align='center'>--</td>\n";
			}else{
				print "<td align='center'>$rank</td>\n";
			}
			print "</tr>\n";
		}
		print "</table>\n";
		close(FH);
	}else{
		print "ファイルを読み込めません！<br>\n";
	}
	print "</td></tr></table>\n";
	print "<br><br>\n\n";
	$count = 0;
	if(open(FH, "counter.txt")){
		@temp = <FH>;
		$count = @temp[0];
		close(FH);
	}
	print "<center>現在のランキング参加者数　　　　     $count人</center>\n";
	print "<br><br>\n";
	print "<center><a href='index.html'>一覧に戻る</a></center>\n";
	print "<br><br><br><br><br>\n";
	print "</body>\n";
	print "</html>\n";	
	&freelock;
}else{
	print "Content-Type: text/plain; charset=Shift_JIS\n\n";
	print "Error!\n"
}





sub filelock{
	while (!mkdir($lockdir, 0755)) {               # 作成。出来なければ待つ
		if (--$retry <= 0) {                       # 5回ダメなら
			if (mkdir($lockdir2, 0755)) {          # ロックを消すための排他
				if ((-M $lockdir) * 86400 > 600) { # 作成時間が10分以上前なら
					# ロック入れ替え
					rename($lockdir2, $lockdir) or &error("LOCK ERROR"); 
					last;                          # 一連の処理へ
				}
					else { rmdir($lockdir2); }         # 部分ロック削除
			}
			print "Content-Type: text/plain; charset=Shift_JIS\n\n";
			print "BUSY";
			&error("BUSY");                        # あきらめる
			exit();
		}
		sleep(1);                                  # 1秒待つ
	}
}


sub freelock{
	rmdir($lockdir);                               # 削除
}