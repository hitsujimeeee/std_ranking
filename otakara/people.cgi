#!/usr/bin/perl


print "Content-Type: text/plain; charset=Shift_JIS\n\n";
$retry = 5;                                    # ���g���C�񐔃Z�b�g
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
				print "�t�@�C���ɏ������߂܂���I\n";
			}
			if(open(FH, ">counter.txt")){
				$new_count = $count+1;
				print FH "$new_count";
				close(FH);
			}else{
				print "�t�@�C���ɏ������߂܂���I\n";
			}
		}
	}else{
		print "�t�@�C����ǂݍ��߂܂���I\n";
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