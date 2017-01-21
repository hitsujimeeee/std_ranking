#!/usr/bin/perl


print "Content-Type: text/plain; charset=Shift_JIS\n\n";
$retry = 5;                                    # リトライ回数セット
$lockdir = "data/lock";
$lockdir2 = "data/lock2";
@data = split(/&/, $ENV{'QUERY_STRING'});
if(@data[0] == 5963){
	&filelock;
	if(open(FH, "people.txt")){
		@list = <FH>;
		close(FH);
		$flag = 0;
		$count = 0;
		foreach $check (@list){
			$count++;
			if(@data[1] == $check){
				$flag = 1;
			}
		}
		if($flag == 0){
			if(open(FH, ">>people.txt")){
				print FH "@data[1]\n";
				close(FH);
			}else{
				print "ファイルに書き込めません！\n";
			}
			if(open(FH, ">counter.txt")){
				$new_count = $count+1;
				print FH "$new_count";
				close(FH);
			}else{
				print "ファイルに書き込めません！\n";
			}
		}
	}else{
		print "ファイルを読み込めません！\n";
	}
	&freelock;
}elsif(@data[0] == 4353){
	&filelock;
	if(open(FH, "people.txt")){
		@list = <FH>;
		close(FH);
		$count = 0;
		foreach(@list){
			$count++;
		}
		print "$count";
	}
	&freelock;
}else{
	print "Error!";
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